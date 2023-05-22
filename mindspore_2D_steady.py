import os
import time
import numpy as np
import argparse

os.system('pip install https://ms-release.obs.cn-north-4.myhuaweicloud.com/2.0.0rc1/MindScience/ascend/aarch64/mindflow_ascend-0.1.0rc1-py3-none-any.whl -i https://pypi.tuna.tsinghua.edu.cn/simple')

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


args = parser.parse_args()

context.set_context(mode=context.GRAPH_MODE,
                    save_graphs=False,
                    device_target=args.device_target,
                    device_id=0)
use_ascend = context.get_context("device_target") == "Ascend"

root_path = os.path.abspath(__file__)
config = load_yaml_config(os.path.join(root_path,args.yaml_file))
data_params = config["data"]
model_params = config["model"]
optimizer_params = config["optimizer"]
ckpt_params = config["ckpt"]
eval_params = config["eval"]
epoch_params = config["optimizer"]

mindrecord_name = "flowfield_000_050.mind"   

if args.use_zhisuan or args.use_qizhi:
    data_dir = '/cache/data'  
    train_dir = '/cache/train'
    mindrecord_name = args.mindrecord_name

# download dataset
if args.use_zhisuan:
    import moxing as mox
    import json


    if not os.path.exists(data_dir):
        os.makedirs(data_dir)
    if not os.path.exists(train_dir):
        os.makedirs(train_dir)

    ### Copy multiple datasets from obs to training image and unzip###  
    def C2netMultiObsToEnv(multi_data_url, data_dir):
        #--multi_data_url is json data, need to do json parsing for multi_data_url
        multi_data_json = json.loads(multi_data_url)  
        for i in range(len(multi_data_json)):
            zipfile_path = data_dir + "/" + multi_data_json[i]["dataset_name"]
            try:
                mox.file.copy(multi_data_json[i]["dataset_url"], zipfile_path) 
                print("Successfully Download {} to {}".format(multi_data_json[i]["dataset_url"],zipfile_path))
                #get filename and unzip the dataset
                filename = os.path.splitext(multi_data_json[i]["dataset_name"])[0]
                filePath = data_dir + "/" + filename
                if not os.path.exists(filePath):
                    os.makedirs(filePath)
                os.system("unzip {} -d {}".format(zipfile_path, filePath))

            except Exception as e:
                print('moxing download {} to {} failed: '.format(
                    multi_data_json[i]["dataset_url"], zipfile_path) + str(e))
        #Set a cache file to determine whether the data has been copied to obs. 
        #If this file exists during multi-card training, there is no need to copy the dataset multiple times.
        f = open("/cache/download_input.txt", 'w')    
        f.close()
        try:
            if os.path.exists("/cache/download_input.txt"):
                print("download_input succeed")
        except Exception as e:
            print("download_input failed")
        return 
    ### Copy the output model to obs ###  
    def EnvToObs(train_dir, obs_train_url):
        try:
            mox.file.copy_parallel(train_dir, obs_train_url)
            print("Successfully Upload {} to {}".format(train_dir,
                                                        obs_train_url))
        except Exception as e:
            print('moxing upload {} to {} failed: '.format(train_dir,
                                                        obs_train_url) + str(e))
        return                                                       
    def DownloadFromQizhi(multi_data_url, data_dir):
        device_num = int(os.getenv('RANK_SIZE'))
        if device_num == 1:
            C2netMultiObsToEnv(multi_data_url,data_dir)
            context.set_context(mode=context.GRAPH_MODE,device_target=args.device_target)
        if device_num > 1:
            # set device_id and init for multi-card training
            context.set_context(mode=context.GRAPH_MODE, device_target=args.device_target, device_id=int(os.getenv('ASCEND_DEVICE_ID')))
            context.reset_auto_parallel_context()
            context.set_auto_parallel_context(device_num = device_num, parallel_mode=ParallelMode.DATA_PARALLEL, gradients_mean=True, parameter_broadcast=True)
            init()
            #Copying obs data does not need to be executed multiple times, just let the 0th card copy the data
            local_rank=int(os.getenv('RANK_ID'))
            if local_rank%8==0:
                C2netMultiObsToEnv(multi_data_url,data_dir)
            #If the cache file does not exist, it means that the copy data has not been completed,
            #and Wait for 0th card to finish copying data
            while not os.path.exists("/cache/download_input.txt"):
                time.sleep(1)  
        return
    def UploadToQizhi(train_dir, obs_train_url):
        device_num = int(os.getenv('RANK_SIZE'))
        local_rank=int(os.getenv('RANK_ID'))
        if device_num == 1:
            EnvToObs(train_dir, obs_train_url)
        if device_num > 1:
            if local_rank%8==0:
                EnvToObs(train_dir, obs_train_url)
        return

    ###Initialize and copy data to training image
    DownloadFromQizhi(args.multi_data_url, data_dir)
    ###The dataset path is used here:data_dir + "/MNIST_Data" +"/train"  
elif args.use_qizhi:
    import moxing as mox
    import json
    import os

    if not os.path.exists(data_dir):
        os.makedirs(data_dir)
    if not os.path.exists(train_dir):
        os.makedirs(train_dir)

    ### Copy single dataset from obs to training image###
    def ObsToEnv(obs_data_url, data_dir):
        try:     
            mox.file.copy_parallel(obs_data_url, data_dir)
            print("Successfully Download {} to {}".format(obs_data_url, data_dir))
        except Exception as e:
            print('moxing download {} to {} failed: '.format(obs_data_url, data_dir) + str(e))
        #Set a cache file to determine whether the data has been copied to obs. 
        #If this file exists during multi-card training, there is no need to copy the dataset multiple times.
        f = open("/cache/download_input.txt", 'w')    
        f.close()
        try:
            if os.path.exists("/cache/download_input.txt"):
                print("download_input succeed")
        except Exception as e:
            print("download_input failed")
        return 
    ### Copy the output to obs###
    def EnvToObs(train_dir, obs_train_url):
        try:
            mox.file.copy_parallel(train_dir, obs_train_url)
            print("Successfully Upload {} to {}".format(train_dir,obs_train_url))
        except Exception as e:
            print('moxing upload {} to {} failed: '.format(train_dir,obs_train_url) + str(e))
        return      
    def DownloadFromQizhi(obs_data_url, data_dir):
        device_num = int(os.getenv('RANK_SIZE'))
        if device_num == 1:
            ObsToEnv(obs_data_url,data_dir)
            context.set_context(mode=context.GRAPH_MODE,device_target=args.device_target)
        if device_num > 1:
            # set device_id and init for multi-card training
            context.set_context(mode=context.GRAPH_MODE, device_target=args.device_target, device_id=int(os.getenv('ASCEND_DEVICE_ID')))
            context.reset_auto_parallel_context()
            context.set_auto_parallel_context(device_num = device_num, parallel_mode=ParallelMode.DATA_PARALLEL, gradients_mean=True, parameter_broadcast=True)
            init()
            #Copying obs data does not need to be executed multiple times, just let the 0th card copy the data
            local_rank=int(os.getenv('RANK_ID'))
            if local_rank%8==0:
                ObsToEnv(obs_data_url,data_dir)
            #If the cache file does not exist, it means that the copy data has not been completed,
            #and Wait for 0th card to finish copying data
            while not os.path.exists("/cache/download_input.txt"):
                time.sleep(1)  
        return
    def UploadToQizhi(train_dir, obs_train_url):
        device_num = int(os.getenv('RANK_SIZE'))
        local_rank=int(os.getenv('RANK_ID'))
        if device_num == 1:
            EnvToObs(train_dir, obs_train_url)
        if device_num > 1:
            if local_rank%8==0:
                EnvToObs(train_dir, obs_train_url)
        return
    DownloadFromQizhi(args.data_url, data_dir)

 
    
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
epochs = epoch_params["epochs"]
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
        
if args.use_zhisuan or use_qizhi:
    UploadToQizhi(ckpt_dir,args.train_url)
    UploadToQizhi(summary_dir,args.train_url)