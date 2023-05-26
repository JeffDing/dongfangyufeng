import os
import time
import numpy as np
import argparse

os.system('pip install https://ms-release.obs.cn-north-4.myhuaweicloud.com/2.0.0rc1/MindScience/ascend/aarch64/mindflow_ascend-0.1.0rc1-py3-none-any.whl -i https://mirror.sjtu.edu.cn/pypi/web/simple')

import mindspore
import mindspore.nn as nn
import mindspore.ops as ops
import mindspore.dataset as ds
from mindspore import context
from mindspore import dtype as mstype
from mindspore import Tensor

from mindspore import save_checkpoint, jit, data_sink
from mindspore import set_seed

from mindflow.common import get_warmup_cosine_annealing_lr
from mindflow.pde import SteadyFlowWithLoss
from mindflow.loss import WaveletTransformLoss
from mindflow.cell import ViT
from mindflow.utils import load_yaml_config

from swin import swin_tiny_patch4_window7_224

from src import AirfoilDataset, calculate_eval_error, plot_u_and_cp, get_ckpt_summ_dir
set_seed(0)
np.random.seed(0)


parser = argparse.ArgumentParser(description='Cycle GAN')
parser.add_argument("--train_url", type=str, default='/cache/output/', help="train url")
parser.add_argument("--data_url", type=str, default='/cache/data/', help="dataset url")
parser.add_argument("--ckpt_url", type=str, help="ckpt url")
parser.add_argument("--use_qizhi", type=bool, default=False, help="use openi")
parser.add_argument("--use_zhisuan", type=bool, default=False, help="use modelarts")
parser.add_argument("--multi_data_url", default= '/cache/data/', help="path to multi dataset")
parser.add_argument("--data_path", default= '/cache/data/', help="path to dataset")
parser.add_argument("--mindrecord_name", default= '/cache/data/', help="path to mindrecord")
parser.add_argument("--grid_path", default= '/cache/data/', help="path to grid path")
parser.add_argument("--pretrain_url", default= '/cache/data/', help="pretrain_url")
parser.add_argument("--yaml_file", default= 'config.yaml', help="pretrain_url")
parser.add_argument("--device_target", default= 'Ascend', help="device_target")
parser.add_argument("--epochs", type=int, default= '3000', help="epochs")


args = parser.parse_args()

context.set_context(mode=context.GRAPH_MODE,
                    save_graphs=False,
                    device_target=args.device_target,
                    device_id=0)
use_ascend = context.get_context("device_target") == "Ascend"

root_path = os.path.dirname(__file__)

if args.use_qizhi or args.use_zhisuan:
    config = load_yaml_config(os.path.join(root_path,args.yaml_file))
else:
    config = load_yaml_config("config_swin.yaml")
data_params = config["data"]
model_params = config["model"]
optimizer_params = config["optimizer"]
ckpt_params = config["ckpt"]
eval_params = config["eval"]

mindrecord_name = "flowfield_000_050.mind"   


if args.use_qizhi:
    from openi import openi_multidataset_to_env as DatasetToEnv  
    from openi import pretrain_to_env as PretrainToEnv
    from openi import env_to_openi as EnvToOpeni
    data_dir = '/cache/data/'  
    train_dir = '/cache/output/'
    mindrecord_name = args.mindrecord_name
    if not os.path.exists(data_dir):
        os.makedirs(data_dir)      
    if not os.path.exists(train_dir):
        os.makedirs(train_dir)
    DatasetToEnv(args.multi_data_url,data_dir)

if args.use_zhisuan:
    from openi import c2net_multidataset_to_env as DatasetToEnv  
    from openi import pretrain_to_env as PretrainToEnv
    from openi import env_to_openi as EnvToOpeni
    data_dir = '/cache/data/'  
    train_dir = '/cache/output/'
    mindrecord_name = args.mindrecord_name
    if not os.path.exists(data_dir):
        os.makedirs(data_dir)      
    if not os.path.exists(train_dir):
        os.makedirs(train_dir)
    DatasetToEnv(args.multi_data_url,data_dir)
    
dataset = ds.MindDataset(dataset_files=mindrecord_name, shuffle=False)
dataset = dataset.project(["inputs", "labels"])
print("samples:", dataset.get_dataset_size())
for data in dataset.create_dict_iterator(num_epochs=1, output_numpy=False):
    input = data["inputs"]
    label = data["labels"]
    print(input.shape)
    print(label.shape)
    break
    
method = model_params['method']
batch_size = data_params['batch_size']
model_name = "_".join([model_params['name'], method, "bs", str(batch_size)])
ckpt_dir, summary_dir = get_ckpt_summ_dir(ckpt_params, model_name, method)
max_value_list = data_params['max_value_list']
min_value_list = data_params['min_value_list']
data_group_size = data_params['data_group_size']
dataset = AirfoilDataset(max_value_list, min_value_list, data_group_size)

train_list, eval_list = data_params['train_num_list'], data_params['eval_num_list']

if args.use_qizhi or args.use_zhisuan:
    train_dataset, eval_dataset = dataset.create_dataset(args.data_path,
                                                     train_list,
                                                     eval_list,
                                                     batch_size=batch_size,
                                                     shuffle=False,
                                                     mode="train",
                                                     train_size=data_params['train_size'],
                                                     finetune_size=data_params['finetune_size'],
                                                     drop_remainder=True)
else:
    train_dataset, eval_dataset = dataset.create_dataset(data_params['data_path'],
                                                        train_list,
                                                        eval_list,
                                                        batch_size=batch_size,
                                                        shuffle=False,
                                                        mode="train",
                                                        train_size=data_params['train_size'],
                                                        finetune_size=data_params['finetune_size'],
                                                        drop_remainder=True)

if use_ascend:
    compute_dtype = mstype.float16
else:
    compute_dtype = mstype.float32
    
class ARGS():
    def init(self):
        super(self).__init__()

    # image_size = args.image_size
    # patch_size = args.patch_size
    # in_chans = args.in_channel
    # embed_dim = args.embed_dim
    # depths = args.depths
    # num_heads = args.num_heads
    # window_size = args.window_size
    # drop_path_rate = args.drop_path_rate
    # mlp_ratio = args.mlp_ratio
    # qkv_bias = True
    # qk_scale = None
    # ape = args.ape
    # patch_norm = args.patch_norm
    # image_size= (224, 224)  #  (192, 384)
    image_size= (192, 192)
    patch_size=4 
    in_channel=6 
    num_classes=1000
    embed_dim=192 
    # depths=[ 2, 2, 6, 2 ] 
    depths=[ 2, 6, ] 
    num_heads=[ 4, 4, ]
    window_size=4  # 7
    mlp_ratio=4. 
    qkv_bias=True 
    qk_scale=None
    drop_rate=0.1  # 0 
    attn_drop_rate=0.1 # 0
    drop_path_rate=0.1  # 0.1
    norm_layer=nn.LayerNorm 
    ape=False 
    patch_norm=True
args = ARGS()
# x = mindspore.numpy.randn([2, 3, 192, 384])
# x = x.reshape([2, 6, 192, 192])
model = swin_tiny_patch4_window7_224(args)
model = mindspore.amp.auto_mixed_precision(model, amp_level="O2")

'''
model = ViT(in_channels=model_params[method]['input_dims'],
            out_channels=model_params['output_dims'],
            encoder_depths=model_params['encoder_depth'],
            encoder_embed_dim=model_params['encoder_embed_dim'],
            encoder_num_heads=model_params['encoder_num_heads'],
            decoder_depths=model_params['decoder_depth'],
            decoder_embed_dim=model_params['decoder_embed_dim'],
            decoder_num_heads=model_params['decoder_num_heads'],
            compute_dtype=compute_dtype
            )
'''

# prepare loss scaler
if use_ascend:
    from mindspore.amp import DynamicLossScaler, all_finite, init_status
    loss_scaler = DynamicLossScaler(1024, 2, 100)
else:
    loss_scaler = None
steps_per_epoch = train_dataset.get_dataset_size()
wave_loss = WaveletTransformLoss(wave_level=optimizer_params['wave_level'])
problem = SteadyFlowWithLoss(model, loss_fn=wave_loss)
# prepare optimizer
epochs = args.epochs
lr = get_warmup_cosine_annealing_lr(lr_init=optimizer_params["lr"],
                                    last_epoch=epochs,
                                    steps_per_epoch=steps_per_epoch,
                                    warmup_epochs=1)
optimizer = nn.Adam(model.trainable_params() + wave_loss.trainable_params(), learning_rate=Tensor(lr))

def forward_fn(x, y):
    loss = problem.get_loss(x, y)
    if use_ascend:
        loss = loss_scaler.scale(loss)
    return loss

grad_fn = ops.value_and_grad(forward_fn, None, optimizer.parameters, has_aux=False)

@jit
def train_step(x, y):
    loss, grads = grad_fn(x, y)
    if use_ascend:
        status = init_status()
        loss = loss_scaler.unscale(loss)
        if all_finite(grads, status):
            grads = loss_scaler.unscale(grads)
    loss = ops.depend(loss, optimizer(grads))
    return loss

train_sink_process = data_sink(train_step, train_dataset, sink_size=1)

print(f'pid: {os.getpid()}')
print(f'use_ascend : {use_ascend}')
print(f'device_id: {context.get_context("device_id")}')

eval_interval = eval_params['eval_interval']
plot_interval = eval_params['plot_interval']
save_ckt_interval = ckpt_params['save_ckpt_interval']
# train process
for epoch in range(1, 1+epochs):
    # train
    time_beg = time.time()
    model.set_train(True)
    for step in range(steps_per_epoch):
        step_train_loss = train_sink_process()
    print(f"epoch: {epoch} train loss: {step_train_loss} epoch time: {time.time() - time_beg:.2f}s")
    # eval
    model.set_train(False)
    if epoch % eval_interval == 0:
        calculate_eval_error(eval_dataset, model)
    if epoch % plot_interval == 0:
        if args.use_qizhi or args.use_zhisuan:
            plot_u_and_cp(eval_dataset=eval_dataset, model=model,
                      grid_path=args.grid_path, save_dir=summary_dir)
        else:
            plot_u_and_cp(eval_dataset=eval_dataset, model=model,
                        grid_path=data_params['grid_path'], save_dir=summary_dir)
    if epoch % save_ckt_interval == 0:
        ckpt_name = f"epoch_{epoch}.ckpt"
        save_checkpoint(model, os.path.join(ckpt_dir, ckpt_name))
        print(f'{ckpt_name} save success')
        
if args.use_zhisuan or args.use_qizhi:
    EnvToOpeni(ckpt_dir,args.train_url)
    EnvToOpeni(summary_dir,args.train_url)