<!DOCTYPE html>
<html lang='zh-CN'>
<head>
<title>MindFlow/applications/data_driven/airfoil/2D_steady/src/utils.py · MindSpore/mindscience - Gitee.com</title>
<meta content='on' http-equiv='x-dns-prefetch-control'>
<link href='//e.gitee.com' rel='dns-prefetch'>
<link href='//files.gitee.com' rel='dns-prefetch'>
<link href='//toscode.gitee.com' rel='dns-prefetch'>
<link href='https://cn-assets.gitee.com' rel='dns-prefetch'>
<link href='https://portrait.gitee.com' rel='dns-prefetch'>
<link rel="shortcut icon" type="image/vnd.microsoft.icon" href="https://cn-assets.gitee.com/assets/favicon-9007bd527d8a7851c8330e783151df58.ico" />
<link rel="canonical" href="https://gitee.com/mindspore/mindscience" />
<meta content='gitee.com/mindspore/mindscience git https://gitee.com/mindspore/mindscience.git' name='go-import'>
<meta charset='utf-8'>
<meta content='always' name='referrer'>
<meta content='Gitee' property='og:site_name'>
<meta content='Object' property='og:type'>
<meta content='https://gitee.com/mindspore/mindscience/blob/master/MindFlow/applications/data_driven/airfoil/2D_steady/src/utils.py' property='og:url'>
<meta content='https://gitee.com/static/images/logo_themecolor.png' itemprop='image' property='og:image'>
<meta content='MindFlow/applications/data_driven/airfoil/2D_steady/src/utils.py · MindSpore/mindscience - Gitee.com' itemprop='name' property='og:title'>
<meta content='MindScience is scientific computing kits for various industries based on the converged MindSpore framework.' property='og:description'>
<meta content='码云,Gitee,代码托管,Git,Git@OSC,Gitee.com,开源,内源,项目管理,版本控制,开源代码,代码分享,项目协作,开源项目托管,免费代码托管,Git代码托管,Git托管服务' name='Keywords'>
<meta content='MindScience is scientific computing kits for various industries based on the converged MindSpore framework.' itemprop='description' name='Description'>
<meta content='pc,mobile' name='applicable-device'>

<meta content="IE=edge" http-equiv="X-UA-Compatible" />
<meta name="csrf-param" content="authenticity_token" />
<meta name="csrf-token" content="fBok3ZrfOJ4UrIL+vQk59JRdoT8/mZtGNe970VaRP+CkEZ7n1mdimeRxRjKCSLEsycl6NEKuMEErwPOHCfo0Pg==" />

<link rel="stylesheet" media="all" href="https://cn-assets.gitee.com/assets/application-306e08aaee04876ddced6a25ca15f720.css" />
<script>
//<![CDATA[
window.gon = {};gon.locale="zh-CN";gon.sentry_dsn=null;gon.baidu_register_hm_push=null;gon.sensor={"server_url":"https://haveaniceday.gitee.com:3443/sa?project=production","sdk_url":"https://cn-assets.gitee.com/assets/static/sensors-sdk-2f850fa5b654ad55ac0993fda2f37ba5.js","page_type":"其他"};gon.info={"controller_path":"blob","action_name":"show","current_user":false};gon.tour_env={"current_user":null,"action_name":"show","original_url":"https://gitee.com/mindspore/mindscience/blob/master/MindFlow/applications/data_driven/airfoil/2D_steady/src/utils.py","controller_path":"blob"};gon.http_clone="https://gitee.com/mindspore/mindscience.git";gon.user_project="mindspore/mindscience";gon.manage_branch="管理分支";gon.manage_tag="管理标签";gon.enterprise_id=5439905;gon.create_reaction_path="/mindspore/mindscience/reactions";gon.ipipe_base_url="https://go-api.gitee.com";gon.artifact_base_url="https://go-repo.gitee.com";gon.gitee_go_remote_url="https://go.gitee.com/assets";gon.gitee_go_active=false;gon.current_project_is_mirror=false;gon.show_repo_comment=false;gon.diagram_viewer_path="https://diagram-viewer.giteeusercontent.com";gon.ref="master";
//]]>
</script>
<script src="https://cn-assets.gitee.com/assets/static/sensor-6269b9ad61bbcdaff20078e5dcff62d5.js"></script>
<script src="https://cn-assets.gitee.com/assets/static/sentry-5.1.0-a823fb0be1b61c5d7ca4a89f0536cb0a.js"></script>
<script src="https://cn-assets.gitee.com/assets/application-7169872a7f3a9d6f6ae1a1ff8733a480.js"></script>
<script src="https://cn-assets.gitee.com/assets/lib/jquery.timeago.zh-CN-4a4818e98c1978d2419ab19fabcba740.js"></script>

<link rel="stylesheet" media="all" href="https://cn-assets.gitee.com/assets/projects/application-46b94c31ba11ae8c37eacce2bdb5603e.css" />
<script src="https://cn-assets.gitee.com/assets/projects/app-13ffdf2374f7ce2bbf54408e0c6116e4.js"></script>

<script src="//res.wx.qq.com/open/js/jweixin-1.2.0.js"></script>
<script>
  var title = document.title.replace(/( - Gitee| - 码云)$/, '')
      imgUrl = '';
  
  document.addEventListener('DOMContentLoaded', function(event) {
    var imgUrlEl = document.querySelector('.readme-box .markdown-body > img, .readme-box .markdown-body :not(a) > img');
    imgUrl = imgUrlEl && imgUrlEl.getAttribute('src');
  
    if (!imgUrl) {
      imgUrlEl = document.querySelector('meta[itemprop=image]');
      imgUrl = imgUrlEl && imgUrlEl.getAttribute('content');
      imgUrl = imgUrl || "https://gitee.com/static/images/logo_themecolor.png";
    }
  
    wx.config({
      debug: false,
      appId: "wxff219d611a159737",
      timestamp: "1685068204",
      nonceStr: "8588c18739033864d8e9b78448bdf1f3",
      signature: "b2eeff42560e8b216ee59a8b7c5e56dae2d42753",
      jsApiList: [
        'onMenuShareTimeline',
        'onMenuShareAppMessage'
      ]
    });
  
    wx.ready(function () {
      wx.onMenuShareTimeline({
        title: title, // 分享标题
        link: "https://gitee.com/mindspore/mindscience/blob/master/MindFlow/applications/data_driven/airfoil/2D_steady/src/utils.py", // 分享链接，该链接域名或路径必须与当前页面对应的公众号JS安全域名一致
        imgUrl: imgUrl // 分享图标
      });
      wx.onMenuShareAppMessage({
        title: title, // 分享标题
        link: "https://gitee.com/mindspore/mindscience/blob/master/MindFlow/applications/data_driven/airfoil/2D_steady/src/utils.py", // 分享链接，该链接域名或路径必须与当前页面对应的公众号JS安全域名一致
        desc: document.querySelector('meta[name=Description]').getAttribute('content'),
        imgUrl: imgUrl // 分享图标
      });
    });
    wx.error(function(res){
      console.error('err', res)
    });
  })
</script>

<script type='text/x-mathjax-config'>
MathJax.Hub.Config({
  tex2jax: {
    inlineMath: [['$','$'], ['\\(','\\)']],
    displayMath: [["$$","$$"],["\\[","\\]"]],
    processEscapes: true,
    skipTags: ['script', 'noscript', 'style', 'textarea', 'pre', 'code'],
    ignoreClass: "container|files",
    processClass: "markdown-body"
  }
});
</script>
<script src="https://cn-assets.gitee.com/uploads/resources/MathJax-2.7.2/MathJax.js?config=TeX-AMS-MML_HTMLorMML"></script>

<script>
  (function () {
    var messages = {
      'zh-CN': {
        addResult: '增加 <b>{term}</b>',
        count: '已选择 {count}',
        maxSelections: '最多 {maxCount} 个选择',
        noResults: '未找到结果',
        serverError: '连接服务器时发生错误'
      },
      'zh-TW': {
        addResult: '增加 <b>{term}</b>',
        count: '已選擇 {count}',
        maxSelections: '最多 {maxCount} 個選擇',
        noResults: '未找到結果',
        serverError: '連接服務器時發生錯誤'
      }
    }
  
    if (messages[gon.locale]) {
      $.fn.dropdown.settings.message = messages[gon.locale]
    }
  }());
</script>

<script>
  var userAgent = navigator.userAgent;
  var isLessIE11 = userAgent.indexOf('compatible') > -1 && userAgent.indexOf('MSIE') > -1;
  if(isLessIE11){
    var can_access = ""
    if (can_access != "true"){
      window.location.href = "/incompatible.html";
    }
  }
  document.addEventListener("error", function (ev) {
    var elem = ev.target;
    if (elem.tagName.toLowerCase() === 'img') {
      elem.src = "data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAMgAAADICAAAAACIM/FCAAACh0lEQVR4Ae3ch5W0OgyG4dt/mQJ2xgQPzJoM1m3AbALrxzrf28FzsoP0HykJEEAAAUQTBBBAAAEEEEAAAQQQQAABBBBAAAEEEEAAAQQQQAABBBBAAAEEkKK0789+GK/I2ezfQB522PnS1qc8pGgXvr4tE4aY0XOUWlGImThWgyCk6DleixzE7qwBkg/MGiDPlVVAyp1VQGrPKiACDhFI6VkF5LmzCki+sg7IwDoglnVAil0IMkeG9CyUiwsxLFUVFzJJOQaKCjFCDN9RXMjIX7W6ztZXZDKKCyn8sWJvH+nca7WHDN9lROlAliPH9iRKCPI4cswFJQWxB46toLQgQ9jhn5QYZA9DOkoMUoQde5YapAxDWkoNYsOQR3KQd9CxUnIQF4S49CB9ENKlBxmDEKsFUgMCCCCAAHIrSF61f6153Ajy8nyiPr8L5MXnmm4CyT2fzN4DUvHZ+ntA2tOQBRBAAAEEEEAAAQQQ7ZBaC6TwSiDUaYHQ2yuB0MN+ft+43whyrs4rgVCjBUKTFshLC6TUAjGA3AxSaYFYLZBOC2RUAsk8h5qTg9QcbEoOsoQhQ2qQhsO5xCD5dgB5JQaZ+KBKGtKecvR81Ic0ZDjByKdDx0rSEDZ/djQbH+bkIdvfJFm98BfV8hD2zprfVdlu9PxVeyYAkciREohRAplJCaRSAplJCcQogTjSAdlyHRBvSAekJR0QRzogA+mADJkOiCPSAPEtqYBshlRAXC43hxix2QiOuEZkVERykGyNo9idIZKE0HO7XrG6OiMShlDWjstVzdPgXtUH9v0CEidAAAEEEEAAAQQQQAABBBBAAAEEEEAAAQQQQAABBBBAAAEEEEAAAQQQQP4HgjZxTpdEii0AAAAASUVORK5CYII=";
    }
  }, true);
</script>
</head>

<body class='git-project lang-zh-CN'>
<header class='common-header fixed noborder' id='git-header-nav'>
<div class='ui container'>
<div class='ui menu header-menu header-container'>
<div class='git-nav-expand-bar'>
<i class='iconfont icon-mode-table'></i>
</div>
<div class='gitee-nav__sidebar'>
<div class='gitee-nav__sidebar-container'>
<div class='gitee-nav__sidebar-top'>
<div class='gitee-nav__avatar-box'></div>
<div class='gitee-nav__buttons-box'>
<a class="ui button small fluid orange" href="/login">登录</a>
<a class="ui button small fluid basic is-register" href="/signup">注册</a>
</div>
</div>
<div class='gitee-nav__sidebar-middle'>
<div class='gitee-nav__sidebar-list'>
<ul>
<li class='gitee-nav__sidebar-item'>
<a href="/explore"><i class='iconfont icon-ic-discover'></i>
<span class='gitee-nav__sidebar-name'>开源软件</span>
</a></li>
<li class='gitee-nav__sidebar-item'>
<a href="/enterprises"><i class='iconfont icon-ic-enterprise'></i>
<span class='gitee-nav__sidebar-name'>企业版</span>
</a></li>
<li class='gitee-nav__sidebar-item'>
<a href="/education"><i class='iconfont icon-ic-education'></i>
<span class='gitee-nav__sidebar-name'>高校版</span>
</a></li>
<li class='gitee-nav__sidebar-item split-line'></li>
<li class='gitee-nav__sidebar-item'>
<a href="/search"><i class='iconfont icon-ic-search'></i>
<span class='gitee-nav__sidebar-name'>搜索</span>
</a></li>
<li class='gitee-nav__sidebar-item'>
<a href="/help"><i class='iconfont icon-help-circle'></i>
<span class='gitee-nav__sidebar-name'>帮助中心</span>
</a></li>
<li class='gitee-nav__sidebar-item'>
<a href="/terms"><i class='iconfont icon-file'></i>
<span class='gitee-nav__sidebar-name'>使用条款</span>
</a></li>
<li class='gitee-nav__sidebar-item'>
<a href="/about_us"><i class='iconfont icon-issuepx'></i>
<span class='gitee-nav__sidebar-name'>关于我们</span>
</a></li>
</ul>
</div>
</div>
<div class='gitee-nav__sidebar-bottom'>
<div class='gitee-nav__sidebar-close-button'>
<i class='fa fa-angle-double-left'></i>
</div>
</div>
</div>
</div>

<!-- /todo 10周年活动结束后 恢复 -->
<div class='item gitosc-logo gitee-birthday-logo-box'>
<div class='gitee-birthday-logo-container'>
<a href="https://gitee.com"><div class='gitee-birthday-logo'>
<img alt='Gitee — 基于 Git 的代码托管和研发协作平台' class='ui inline image logo-birthday logo-birthday-white' height='28' src='/static/images/logo-birthday-white.png?t=158106664' title='Gitee — 基于 Git 的代码托管和研发协作平台' width='95'>
<img alt='Gitee — 基于 Git 的代码托管和研发协作平台' class='ui inline black image logo-birthday' height='28' src='/static/images/logo-birthday-black.png?t=158106664' title='Gitee — 基于 Git 的代码托管和研发协作平台' width='95'>
</div>
<div class='gitee-birthday-logo-ani hide' id='lottie'></div>
</a></div>
<div class='birthday-logo-popup'>
<div class='popup-bg'>
<div class='popup-content'>
<div class='happy-birthday'>
<span>
Gitee 十周年生日快乐！
</span>
</div>
<div class='activity'>
快来 get 同款生日帽吧，还有 iPhone 14 等你来抽～
</div>
</div>
<div class='btn-box'>
<a title="立即查看" class="button" target="_blank" href="/activity/10th">立即查看
</a></div>
</div>
</div>
<style>
  .gitee-birthday-logo-box .birthday-logo-popup {
    position: absolute;
    top: 100%;
    left: -5px;
    padding-top: 7px;
    opacity: 0;
    pointer-events: none;
    -webkit-transition: opacity 0.2s ease-in-out;
    transition: opacity 0.2s ease-in-out; }
    .gitee-birthday-logo-box .birthday-logo-popup .popup-bg {
      height: 197px;
      width: 310px;
      background-image: url("/static/images/logo-birthday-popup.png");
      background-repeat: no-repeat;
      background-size: contain; }
    .gitee-birthday-logo-box .birthday-logo-popup .popup-content {
      padding: 28px 24px 0 90px; }
    .gitee-birthday-logo-box .birthday-logo-popup .happy-birthday {
      margin-bottom: 16px;
      font-size: 18px;
      font-weight: 600;
      background: linear-gradient(238deg, white 0%, #7f88c7 100%);
      -webkit-background-clip: text;
      color: transparent; }
    .gitee-birthday-logo-box .birthday-logo-popup .activity {
      font-size: 14px;
      color: #FCFCFD;
      font-weight: 400;
      line-height: 20px; }
    .gitee-birthday-logo-box .birthday-logo-popup .btn-box {
      margin-top: 24px;
      text-align: center; }
    .gitee-birthday-logo-box .birthday-logo-popup .button {
      font-size: 14px;
      padding: 6px 22px;
      border-radius: 20px;
      font-weight: 500;
      color: #FFFFFF;
      background: -webkit-gradient(linear, right top, left top, from(#6e83f1), to(#b182e9));
      background: linear-gradient(270deg, #6e83f1 0%, #b182e9 100%); }
      .gitee-birthday-logo-box .birthday-logo-popup .button:hover {
        background: -webkit-gradient(linear, right top, left top, from(rgba(110, 131, 241, 0.8)), to(rgba(177, 130, 233, 0.8)));
        background: linear-gradient(270deg, rgba(110, 131, 241, 0.8) 0%, rgba(177, 130, 233, 0.8) 100%); }
  .gitee-birthday-logo-box:hover .birthday-logo-popup {
    opacity: 1;
    pointer-events: auto;
    -webkit-animation: gitee_birthday_fadeIn 0.2s ease-in-out forwards;
            animation: gitee_birthday_fadeIn 0.2s ease-in-out forwards; }
  
  @-webkit-keyframes gitee_birthday_fadeIn {
    0% {
      -webkit-transform: translateY(-10px);
              transform: translateY(-10px); }
  
    100% {
      -webkit-transform: translateY(0);
              transform: translateY(0); } }
  
  @keyframes gitee_birthday_fadeIn {
    0% {
      -webkit-transform: translateY(-10px);
              transform: translateY(-10px); }
  
    100% {
      -webkit-transform: translateY(0);
              transform: translateY(0); } }
</style>

</div>
<a title="开源软件" class="item " href="/explore">开源软件
</a><a title="企业版" class="item " sa_evt="click_GiteeCommunity_tab_En" href="/enterprises">企业版
<sup class='ui red label'>
特惠
</sup>
</a><a title="高校版" class="item " href="/education">高校版
</a><a title="私有云" class="item" target="_blank" href="https://gitee.cn?utm_source=giteecom">私有云
</a><a title="博客" class="item" id="gitee-blog" target="_blank" href="https://blog.gitee.com/?utm_sources=site_nav">博客
</a><div class='center responsive-logo'>
<a href="https://gitee.com"><img alt='Gitee — 基于 Git 的代码托管和研发协作平台' class='ui inline image' height='24' src='/static/images/logo.svg?t=158106664' title='Gitee — 基于 Git 的代码托管和研发协作平台' width='85'>
<img alt='Gitee — 基于 Git 的代码托管和研发协作平台' class='ui inline black image' height='24' src='/static/images/logo-black.svg?t=158106664' title='Gitee — 基于 Git 的代码托管和研发协作平台' width='85'>
</a></div>
<div class='right menu userbar right-header' id='git-nav-user-bar'>
<form class="ui item" id="navbar-search-form" data-text-require="搜索关键字不能少于1个" data-text-filter="搜索格式不正确" action="/search" accept-charset="UTF-8" method="get"><input name="utf8" type="hidden" value="&#x2713;" />
<input type="hidden" name="type" id="navbar-search-type" />
<input type="hidden" name="fork_filter" id="fork_filter" value="on" />
<div class='ui search header-search'>
<input type="text" name="q" id="navbar-search-input" value="" class="prompt" placeholder="搜开源" />
</div>
</form>

<script>
  var can_search_in_repo = 1,
      repo = "VFZSak1rMXFRWGhPVkZKb1RucFplbHBuUFQxaE56WXpaZz09YTc2M2Y=",
      reponame = "mindspore/mindscience";
  
  $(function() {
    var $search = $('#navbar-search-form .ui.search');
    $search.search({
      apiSettings: {
        url: '/search/relative_project?q={query}',
        onResponse: function (res) {
          if (res && res.status === 200 && res.data) {
            var query = htmlSafe($search.search('get value'));
  
            res.data.map(function (item) {
              item.path_ns = '/' + item.path_ns;
              item.icon = 'iconfont icon-project-public';
            });
            res.data.unshift({
              name_ns: "在全站搜索 <b class='hl'>" + query +"</b> 相关项目",
              path_ns: '/search?fork_filter=on&q=' + query,
              icon: 'iconfont icon-search'
            });
            return res;
          } else {
            return { data: [] };
          }
        }
      },
      fields: {
        results: 'data',
        description: 'name_ns',
        url: 'path_ns',
        icon: 'icon'
      },
      minCharacters: 1,
      maxResults: 10,
      searchDelay: 250,
      showNoResults: false,
      transition: 'fade'
    });
  });
</script>

<div class='ui item' id='feature-update-notice'>
<div class='notice-update-icon'>
<a class="notice-update-popup click-knowed" title="" href="javascript:void(0)"><img alt="功能更新" title="" class="bubl_icon bubl-off-icon" src="https://cn-assets.gitee.com/assets/bulb_off-24ee940be20998aace89a3f040cbc704.svg" />
<img alt="功能更新" title="" class="bubl_icon bubl-on-icon" src="https://cn-assets.gitee.com/assets/bulb_on-3986b1dc417285398e3d15671bd8f261.svg" />
</a></div>
<div class='feature-update-notice-panel menu'>
<div class='notice-img'>
<img alt="" title="" class="notice-img-show" src="" />
</div>
<div class='notice-update-title'></div>
<div class='notice-update-des'></div>
<div class='notice-btn-list d-flex-between'>
<button name="button" type="button" class="ui basic orange button btn-notice btn-knowed click-knowed" style="margin-right: 0">我知道了</button>
<a class="ui button orange btn-notice btn-details click-knowed" target="_blank" href="">查看详情</a>
</div>
</div>
</div>

<a class="item git-nav-user__login-item" sa_evt="login_show" sa_referrer_url="" sa_referrer_action="站导航右上角-登录按钮" sa_referrer_type="其他" href="/login">登录
</a><a class="item git-nav-user__register-item" sa_evt="register_show" sa_referrer_url="" sa_referrer_action="站导航右上角-注册按钮" sa_referrer_type="其他" href="/signup">注册
</a><script>
  $('.destroy-user-session').on('click', function() {
    $.cookie('access_token', null, { path: '/' });
  })
</script>

</div>
</div>
</div>
</header>
<script src="/static/javascripts/lottie.min.js"></script>
<script src="/static/javascripts/logo-birthday-black.js"></script>
<script src="/static/javascripts/logo-birthday-white.js"></script>
<script>
  Gitee.initNavbar()
  Gitee.initRepoRemoteWay()
  $.cookie('user_locale',null)
  //10th 生日帽动画
  let $birthdayLogoBox = $('.gitee-birthday-logo-box')
  let $logoBirthday = $('.gitee-birthday-logo')
  let $logoBirthdayAni = $('.gitee-birthday-logo-ani')
  let isWhite = $(".black.logo-birthday").css("opacity") == "0"
  
  const animation = lottie.loadAnimation({
    container: document.getElementById('lottie'),
    renderer: 'svg',//渲染方式：svg：支持交互、不会失帧；canvas、html：支持3D，支持交互
    loop: false,//循环播放：默认为true
    autoplay: false,//自动播放：默认为true
    animationData: isWhite? logoWhite:logoBlack//变量名（js文件）
  })
  animation.addEventListener('complete', () => {
    $logoBirthdayAni.addClass('hide')
    $logoBirthday.removeClass('hide')
  });
  
  const handleMouseEnter = () => {
    if (animation?.isPaused) {
      $logoBirthday.addClass('hide')
      $logoBirthdayAni.removeClass('hide')
      animation.resetSegments(true);
      animation.play();
    }
  };
  $birthdayLogoBox.mouseenter(handleMouseEnter);
</script>

<script>
  var userAgent = navigator.userAgent;
  var isLessIE11 = userAgent.indexOf('compatible') > -1 && userAgent.indexOf('MSIE') > -1;
  if(isLessIE11){
    var can_access = ""
    if (can_access != "true"){
      window.location.href = "/incompatible.html";
    }
  }
</script>

<div class='fixed-notice-infos'>
<div class='all-messages'>
</div>
<div class='ui container'>
<div class='flash-messages' id='messages-container'></div>
</div>
<script>
  (function() {
    $(function() {
      var $error_box, alertTip, notify_content, notify_options, template;
      template = '<div data-notify="container" class="ui {0} message" role="alert">' + '<i data-notify="dismiss" class="close icon"></i>' + '<span data-notify="message">{2}</span>' + '</div>';
      notify_content = null;
      notify_options = {};
      alertTip = '';
      $error_box = $(".flash_error.flash_error_box");
      if (notify_options.type === 'error' && $error_box.length > 0 && !$.isEmptyObject(notify_content.message)) {
        if (notify_content.message === 'captcha_fail') {
          alertTip = "验证码不正确";
        } else if (notify_content.message === 'captcha_expired') {
          alertTip = "验证码已过期，请点击刷新";
        } else if (notify_content.message === 'not_found_in_database') {
          alertTip = "帐号或者密码错误";
        } else if (notify_content.message === 'not_found_and_show_captcha') {
          alertTip = "帐号或者密码错误";
        } else if (notify_content.message === 'phone_captcha_fail') {
          alertTip = "手机验证码不通过";
        } else {
          alertTip = notify_content.message;
        }
        return $error_box.html(alertTip).show();
      } else if (notify_content) {
        if ("show" === 'third_party_binding') {
          return $('#third_party_binding-message').html(notify_content.message).addClass('ui message red');
        }
        notify_options.delay = 3000;
        notify_options.template = template;
        notify_options.offset = {
          x: 10,
          y: 30
        };
        notify_options.element = '#messages-container';
        return $.notify(notify_content, notify_options);
      }
    });
  
  }).call(this);
</script>

</div>
<script>
  (function() {
    $(function() {
      var setCookie;
      setCookie = function(name, value) {
        $.cookie(name, value, {
          path: '/',
          expires: 365
        });
      };
      $('#remove-bulletin, #remove-bulletin-dashboard').on('click', function() {
        setCookie('remove_bulletin', "gitee-maintain-1684743204");
        $('#git-bulletin').hide();
      });
      $('#remove-member-bulletin').on('click', function() {
        setCookie('remove_member_bulletin', "gitee_member_bulletin");
        $(this).parent().hide();
      });
      return $('#remove-gift-bulletin').on('click', function() {
        setCookie('remove_gift_bulletin', "gitee-gift-bulletin");
        $(this).parent().hide();
      });
    });
  
  }).call(this);
</script>
<script>
  function closeMessageBanner(pthis, type, val) {
    var json = {}
  
    val = typeof val === 'undefined' ? null : val
    $(pthis).parent().remove()
    if (type === 'out_of_enterprise_member') {
      json = {type: type, data: val}
    } else if (type === 'enterprise_overdue') {
      json = {type: type, data: val}
    }
    $.post('/profile/close_flash_tip', json)
  }
</script>

<div class='site-content'>
<div class='git-project-header'>
<div class='fixed-notice-infos'>
<div class='ui info icon floating message green' id='fetch-ok' style='display: none'>
<div class='content'>
<div class='header status-title'>
<i class='info icon status-icon'></i>
代码拉取完成，页面将自动刷新
</div>
</div>
</div>
<div class='ui info icon floating message error' id='fetch-error' style='display: none'>
<div class='content'>
<div class='header status-title'>
<i class='info icon status-icon'></i>
<span class='error_msg'></span>
</div>
</div>
</div>
</div>
<div class='ui container'>
<div class='git-project-categories'>
<a href="/explore">开源项目</a>
<span class='symbol'>></span>
<a href="/explore/Artificial-Intelligence">人工智能</a>
<span class='symbol'>&gt;</span>
<a href="/explore/ai">AI-人工智能</a>
<span class='symbol and-symbol'>&&</span>
</div>

<div class='git-project-header-details'>
<div class='git-project-header-container'>
<div class='git-project-header-actions'>
<div class='ui tiny modal project-donate-modal' id='project-donate-modal'>
<i class='iconfont icon-close close'></i>
<div class='header'>捐赠</div>
<div class='content'>
捐赠前请先登录
</div>
<div class='actions'>
<a class='ui blank button cancel'>取消</a>
<a class='ui orange ok button' href='/login'>前往登录</a>
</div>
</div>
<div class='ui small modal wepay-qrcode'>
<i class='iconfont icon-close close'></i>
<div class='header'>
扫描微信二维码支付
<span class='wepay-cash'></span>
</div>
<div class='content weqcode-center'>
<img id='wepay-qrcode' src=''>
</div>
<div class='actions'>
<div class='ui cancel blank button'>取消</div>
<div class='ui ok orange button'>支付完成</div>
</div>
</div>
<div class='ui mini modal' id='confirm-alipay-modal'>
<div class='header'>支付提示</div>
<div class='content'>
将跳转至支付宝完成支付
</div>
<div class='actions'>
<div class='ui approve orange button'>确定</div>
<div class='ui blank cancel button'>取消</div>
</div>
</div>

<span class='ui buttons basic watch-container'>
<div class='ui dropdown button js-project-watch' data-watch-type='unwatch'>
<input type='hidden' value=''>
<i class='iconfont icon-watch'></i>
<div class='text'>
Watch
</div>
<i class='dropdown icon'></i>
<div class='menu'>
<a data-value="unwatch" class="item" sa_evt="loginInform_show" sa_referrer_url="" sa_referrer_action="Watch" sa_referrer_type="其他" rel="nofollow" data-method="post" href="/mindspore/mindscience/unwatch"><i class='iconfont icon-msg-read'></i>
不关注
</a><a data-value="watching" class="item" sa_evt="loginInform_show" sa_referrer_url="" sa_referrer_action="Watch" sa_referrer_type="其他" rel="nofollow" data-method="post" href="/mindspore/mindscience/watch"><i class='iconfont icon-msg-read'></i>
关注所有动态
</a><a data-value="releases_only" class="disabled item" sa_evt="loginInform_show" sa_referrer_url="" sa_referrer_action="Watch" sa_referrer_type="其他" rel="nofollow" data-method="post" href="/mindspore/mindscience/release_only_watch"><i class='iconfont icon-msg-read'></i>
仅关注版本发行动态
</a><a data-value="ignoring" class="item" sa_evt="loginInform_show" sa_referrer_url="" sa_referrer_action="Watch" sa_referrer_type="其他" rel="nofollow" data-method="post" href="/mindspore/mindscience/ignoring_watch"><i class='iconfont icon-msg-read'></i>
关注但不提醒动态
</a></div>
</div>
<style>
  .js-project-watch .text .iconfont {
    display: none; }
  .js-project-watch a, .js-project-watch a:hover {
    color: #000; }
  .js-project-watch .item > .iconfont {
    visibility: hidden;
    margin-left: -10px; }
  .js-project-watch .selected .iconfont {
    visibility: visible; }
  .js-project-watch .menu {
    margin-top: 4px !important; }
</style>
<script>
  $('.js-project-watch').dropdown({
    action: 'select',
    onChange: function(value, text, $selectedItem) {
      var type = value === 'unwatch' ? 'Watch' : 'Watching';
      $(this).children('.text').text(type);
      $(this).dropdown('set selected', value)
    }
  });
</script>

<a class="ui button action-social-count" title="93" href="/mindspore/mindscience/watchers">93
</a></span>
<span class='basic buttons star-container ui'>
<a class="ui button star" sa_evt="loginInform_show" sa_referrer_url="" sa_referrer_action="Star" sa_referrer_type="其他" href="/login"><i class='iconfont icon-star'></i>
Star
</a><a class="ui button action-social-count " title="632" href="/mindspore/mindscience/stargazers">632
</a></span>
<span class='ui basic buttons fork-container' title='无权 Fork 此仓库'>
<a class="ui button fork" title="你必须登录后才可以fork一个仓库" sa_evt="loginInform_show" sa_referrer_url="" sa_referrer_action="Fork" sa_referrer_type="其他" href="/login"><i class='iconfont icon-fork'></i>
Fork
</a><a class="ui button action-social-count disabled-style" title="347" href="/mindspore/mindscience/members">347
</a></span>
</div>
<h2 class='git-project-title mt-0 mb-0'>
<a title="GVP - Gitee 最有价值开源项目" class="ui small label git-project-gvp-badge" target="_blank" href="/gvp">GVP</a><a title="MindSpore" class="author" href="/mindspore">MindSpore</a> / <a title="mindscience" class="repository" target="" style="padding-bottom: 0px; margin-right: 4px" sa_evt="repoClick" sa_location="其他" sa_url="" sa_repo_id="17620154" href="/mindspore/mindscience">mindscience</a>
<input type="hidden" name="recomm_at" id="recomm_at" value="2021-11-09 01:28" />
<input type="hidden" name="project_title" id="project_title" value="MindSpore/mindscience" />
</h2>
</div>
</div>
</div>
<script>
  var title_import_url = "false";
  var title_post_url = "/mindspore/mindscience/update_import";
  var title_fork_url = "/mindspore/mindscience/sync_fork";
  var title_project_path = "mindscience";
  var title_p_name = "mindscience";
  var title_p_id= "17620154";
  var title_description = "MindScience is scientific computing kits for various industries based on the converged MindSpore framework.";
  var title_form_authenticity_token = "CyzB5Zs47ugHnlKrCJBmGugyzEyap3BaHrTFCNkWgBzTJ3vf14C07/dDlmc30e7CtaYXR+eQ210Am01ehn2Lwg==";
  var watch_type = "unwatch";
  var checkFirst = false;
  
  $('.js-project-watch').dropdown('set selected', watch_type);
  $('.checkbox.sync-wiki').checkbox();
  $('.checkbox.team-member-checkbox').checkbox();
</script>
<style>
  i.loading, .icon-sync.loading {
    -webkit-animation: icon-loading 1.2s linear infinite;
    animation: icon-loading 1.2s linear infinite;
  }
  .qrcode_cs {
    float: left;
  }
  .check-sync-wiki {
    float: left;
    height: 28px;
    line-height: 28px;
  }
  .sync-wiki-warn {
    color: #e28560;
  }
</style>

<div class='git-project-nav'>
<div class='ui container'>
<div class='ui secondary pointing menu'>
<a class="item active" href="/mindspore/mindscience"><i class='iconfont icon-code'></i>
代码
</a><a class="item " href="/mindspore/mindscience/issues"><i class='iconfont icon-task'></i>
Issues
<span class='ui mini circular label'>
13
</span>
</a><a class="item " href="/mindspore/mindscience/pulls"><i class='iconfont icon-pull-request'></i>
Pull Requests
<span class='ui mini circular label'>
19
</span>
</a><a class="item " href="/mindspore/mindscience/wikis"><i class='iconfont icon-wiki'></i>
Wiki
</a><a class="item  " href="/mindspore/mindscience/graph/master"><i class='iconfont icon-statistics'></i>
统计
</a><a class="item " href="/mindspore/mindscience/gitee_go"><i class='iconfont icon-workflow'></i>
流水线
</a><div class='item'>
<div class='ui pointing top right dropdown git-project-service'>
<div>
<i class='iconfont icon-service'></i>
服务
<i class='dropdown icon'></i>
</div>
<div class='menu' style='display:none'>
<a class="item" href="/mindspore/mindscience/pages"><img src="/static/images/logo-en.svg" alt="Logo en" />
<div class='item-title'>
Gitee Pages
</div>
</a><a class="item" href="/mindspore/mindscience/javadoc"><img src="https://cn-assets.gitee.com/assets/maven-bd58aee84f266d64d4b8ce5b006a9fcf.png" alt="Maven" />
<div class='item-title'>
JavaDoc
</div>
</a><a class="item" href="/mindspore/mindscience/phpdoc"><img src="https://cn-assets.gitee.com/assets/phpdoc-a99f87c2feaa2fd99e5065377a39487e.png" alt="Phpdoc" />
<div class='item-title'>
PHPDoc
</div>
</a><a class="item" href="/mindspore/mindscience/quality_analyses?platform=sonar_qube"><img src="https://cn-assets.gitee.com/assets/sonar_mini-5e1b54bb9f6c951d97fb778ef623afea.png" alt="Sonar mini" />
<div class='item-title'>
质量分析
</div>
</a><a class="item" target="_blank" href="https://gitee.com/help/articles/4193"><img src="https://cn-assets.gitee.com/assets/jenkins_for_gitee-554ec65c490d0f1f18de632c48acc4e7.png" alt="Jenkins for gitee" />
<div class='item-title'>
Jenkins for Gitee
</div>
</a><a class="item" target="_blank" href="https://gitee.com/help/articles/4285"><img src="https://cn-assets.gitee.com/assets/baidu_efficiency_cloud-81a98c2eb67fac83b1453ca3d2feb326.svg" alt="Baidu efficiency cloud" />
<div class='item-title'>
百度效率云
</div>
</a><a class="item" target="_blank" href="https://gitee.com/help/articles/4318"><img src="https://cn-assets.gitee.com/assets/cloudbase-1197b95ea3398aff1df7fe17c65a6d42.png?20200925" alt="Cloudbase" />
<div class='item-title'>
腾讯云托管
</div>
</a><a class="item" target="_blank" href="https://gitee.com/help/articles/4330"><img src="https://cn-assets.gitee.com/assets/cloud_serverless-686cf926ced5d6d2f1d6e606d270b81e.png" alt="Cloud serverless" />
<div class='item-title'>
腾讯云 Serverless
</div>
</a><a class="item" href="/mindspore/mindscience/open_sca"><img src="https://cn-assets.gitee.com/assets/open_sca/logo-9049ced662b2f9936b8001e6f9cc4952.png" alt="Logo" />
<div class='item-title'>
悬镜安全
</div>
</a><button class='ui orange basic button quit-button' id='quiting-button'>
我知道了，不再自动展开
</button>
</div>
</div>
</div>
</div>
</div>
</div>
<script>
  $('.git-project-nav .ui.dropdown').dropdown({ action: 'nothing' });
  var gitee_reward_config = JSON.parse(localStorage.getItem('gitee_reward_config') || null) || false
  var $settingText = $('.setting-text')
  // 如果没有访问过
  if(!gitee_reward_config) $settingText.addClass('red-dot')
</script>
<style>
  .git-project-nav i.checkmark.icon {
    color: green;
  }
  #quiting-button {
    display: none;
  }
  
  .git-project-nav .dropdown .menu.hidden:after {
    visibility: hidden !important;
  }
</style>
<script>
  isSignIn = false
  isClickGuide = false
  $('#git-versions.dropdown').dropdown();
  $.ajax({
    url:"/mindspore/mindscience/access/add_access_log",
    type:"GET"
  });
  $('#quiting-button').on('click',function() {
    $('.git-project-service').click();
    if (isSignIn) {
      $.post("/projects/set_service_guide")
    }
    $.cookie("Serve_State", true, { expires: 3650, path: '/'})
    $('#quiting-button').hide();
  });
  if (!(isClickGuide || $.cookie("Serve_State") == 'true')) {
    $('.git-project-service').click()
    $('#quiting-button').show()
  }
</script>

</div>
<div class='ui container'>
<div class='register-guide'>
<div class='register-container'>
<div class='regist'>
加入 Gitee
</div>
<div class='description'>
与超过 1000 万 开发者一起发现、参与优秀开源项目，私有仓库也完全免费 ：）
</div>
<a class="ui orange button free-registion" sa_evt="register_show" sa_referrer_url="" sa_referrer_action="免费加入" sa_referrer_type="其他" href="/signup?from=project-guide">免费加入</a>
<div class='login'>
已有帐号？
<a href="/login?from=project-guide">立即登录</a>
</div>
</div>
</div>

<div class='git-project-content-wrapper'>

<div class='ui grid' id='project-wrapper'>
<div class='sixteen wide column'>
<div class='git-project-content' id='git-project-content'>
<div class='row'>
<div class='git-project-desc-wrapper'>
<script>
  $('.git-project-desc-wrapper .ui.dropdown').dropdown();
  if (false) {
    gon.project_new_blob_path = "/mindspore/mindscience/new/master/MindFlow/applications/data_driven/airfoil/2D_steady/src/utils.py"
    bindShowModal({
      el: $('.no-license .project-license__create'),
      complete: function(data, modal) {
        if (!data.haveNoChoice && !data.data) {
          Flash.show('请选择一项开源许可证')
        } else {
          location.href = gon.project_new_blob_path + '?license=' + data.data
        }
      },
      skip: function () {
        location.href = gon.project_new_blob_path + '?license'
      }
    });
  }
  
  $(".project-admin-action-box .reject").click(function() {
    var reason = $('[name=review-reject-reason]').val();
    if (!reason) {
      Flash.error('请选择不通过理由')
      return
    }
    $.ajax({
      type: 'POST',
      url: "/admin/shumei_content/shumei_check/reject_project_public",
      data: {
        reason: reason,
        status: 'rejected',
        project_id: 17620154
      },
      success: function(result){
        if(result.status == 'success'){
          window.location.reload();
        }else{
          Flash.error(result.message)
        }
      }
    })
  })
  
  $(".project-admin-action-box .approve").click(function(){
  
    $.ajax({
      type: 'POST',
      url: "/admin/shumei_content/shumei_check/reject_project_public",
      data: {
        status: 'approved',
        project_id: 17620154
      },
      success: function(result){
        if(result.status == 'success'){
          window.location.reload();
        }else{
          Flash.error(result.message)
        }
      }
    })
  })
  
  $(".project-admin-action-box .waiting").click(function(){
  
    $.ajax({
      type: 'POST',
      url: "/admin/shumei_content/shumei_check/reject_project_public",
      data: {
        status: 'waiting',
        project_id: 17620154
      },
      success: function(result){
        if(result.status == 'success'){
          window.location.reload();
        }else{
          Flash.error(result.message)
        }
      }
    })
  })
  
  $('i.help.circle.icon').popup({
    popup: '.no-license .ui.popup',
    position: 'right center'
  });
  
  $('#remove-no-license-message').on('click', function() {
    $.cookie("skip_repo_no_license_message_17620154", 'hide', { expires: 365 });
    $('#user-no-license-message').hide();
    return;
  });
</script>
</div>

</div>
<div class='git-project-bread' id='git-project-bread'>
<div class='ui horizontal list mr-1'>
<div class='item git-project-branch-item'>
<input type="hidden" name="path" id="path" value="MindFlow/applications/data_driven/airfoil/2D_steady/src/utils.py" />
<div class='ui top left pointing dropdown gradient button dropdown-has-tabs' id='git-project-branch'>
<input type="hidden" name="ref" id="ref" value="master" />
<div class='default text'>
master
</div>
<i class='dropdown icon'></i>
<div class='menu'>
<div class='ui left icon search input'>
<i class='iconfont icon-search'></i>
<input class='search-branch' placeholder='搜索分支' type='text'>
</div>
<div class='tab-menu'>
<div class='tab-menu-action' data-tab='branches'>
<a class="ui link button" href="/mindspore/mindscience/branches">管理</a>
</div>
<div class='tab-menu-action' data-tab='tags'>
<a class="ui link button" href="/mindspore/mindscience/tags">管理</a>
</div>
<div class='tab-menu-item' data-placeholder='搜索分支' data-tab='branches'>
分支 (7)
</div>
<div class='tab-menu-item' data-placeholder='搜索标签' data-tab='tags'>
标签 (3)
</div>
</div>
<div class='tab scrolling menu' data-tab='branches' id='branches_panel'>
<div data-value="r0.2.0" class="item"><span>r0.2.0</span></div>
<div data-value="master" class="item"><span>master</span></div>
<div data-value="dev-md" class="item"><span>dev-md</span></div>
<div data-value="r0.2.0-alpha" class="item"><span>r0.2.0-alpha</span></div>
<div data-value="r0.2" class="item"><span>r0.2</span></div>
<div data-value="dev" class="item"><span>dev</span></div>
<div data-value="r0.1" class="item"><span>r0.1</span> <i class="iconfont icon-shieldlock protected-branch-popup" data-title="受保护分支" data-content="保护规则： r0.1"></i></div>
</div>
<div class='tab scrolling menu' data-tab='tags'>
<div class='item' data-value='v0.2.0-rc1'>v0.2.0-rc1</div>
<div class='item' data-value='v0.1.0'>v0.1.0</div>
<div class='item' data-value='v0.1.0-rc1'>v0.1.0-rc1</div>
</div>
</div>
</div>
<style>
  .iconfont.icon-shieldlock {
    color: #8c92a4;
  }
</style>
<script>
  var $branchesDropdown = $('#branches_panel');
  var $searchNameInput = $('.search-branch');
  var concurrentRequestLock = false;
  var filterXSS = window.filterXSS;
  $branchesDropdown.scroll(function() {
    var branchesPanel = document.getElementById('branches_panel');
    var numOfBranches = $branchesDropdown.children().length;
    var pageToken = $branchesDropdown.children().last().text().trim();
    if (branchesPanel.clientHeight + branchesPanel.scrollTop + 37 > branchesPanel.scrollHeight && numOfBranches < 7) {
      loadData({ page_token: pageToken });
    }
  });
  
  $searchNameInput.on('input', window.globalUtils.debouce(function (e) {
    var $currentTab = $('.tab-menu-action.active');
    var numOfBranches = $branchesDropdown.children().length;
    if($currentTab.data('tab') === 'branches' && numOfBranches < 7) {
    var searchWord = $searchNameInput.val().trim();
      if (searchWord !== "") {
        loadData({ search: searchWord });
      } else {
        loadData({});
      }
    }
  }, 500));
  
  function loadData(data) {
    if (concurrentRequestLock) { return; }
      concurrentRequestLock = true;
      $.ajax({
        url: "/mindspore/mindscience/branches/load_more",
        type: 'GET',
        data: data,
        dataType: 'json',
        success: function (branches) {
          var html = '';
          var protectRule = '';
          if (data.search || !data.page_token) {
            $branchesDropdown.empty();
          }
          branches.forEach(function (branch) {
            var branchName = filterXSS(branch.name);
            if(branch.branch_type.value === 1) {
              var rule = filterXSS(branch.protection_rule.wildcard);
              protectRule = `<i
                 class="iconfont icon-shieldlock protected-branch-popup"
                 data-title="受保护分支"
                 data-content='保护规则： ${rule}'
                >
                </i>`
            }
            html += `<div data-value='${branchName}' class="item">
                      <span>${branchName}</span> ${protectRule}
                     </div>`
          });
          $branchesDropdown.append(html);
          $('.protected-branch-popup').popup()
        },
        complete: function () {
          concurrentRequestLock = false;
        }
    });
  }
</script>

<script>
  $(function () {
    Gitee.initTabsInDropdown($('#git-project-branch').dropdown({
      fullTextSearch: true,
      selectOnKeydown: true,
      action: function (text,value,el) {
        var oItemOrInitObject = el[0] || el
        var isNotSelect = oItemOrInitObject.dataset.tab && oItemOrInitObject.dataset.tab === 'branches'
        if(isNotSelect){
          console.warn("You didn't choose a branch")
          return
        } 
        var path = $('#path').val();
        var href = ['/mindspore/mindscience/tree', encodeURIComponent(value), path].join('/');
        window.location.href = href;
        return true
      },
      onNoResults: function (searchTerm) {
        //未找到结果
        return true
      },
    }));
    $('.protected-branch-popup').popup()
  })
</script>

</div>
</div>
<div class='git-project-right-actions pull-right'>
<div class='ui orange button' id='btn-dl-or-clone'>
克隆/下载
<i class='dropdown icon'></i>
</div>
<div class='git-project-download-panel for-project ui bottom right popup'>
<div class='ui small secondary pointing menu'>
<a class='item active' data-text='' data-type='http' data-url='https://gitee.com/mindspore/mindscience.git'>HTTPS</a>
<a class='item' data-text='' data-type='ssh' data-url='git@gitee.com:mindspore/mindscience.git'>SSH</a>
<a class='item' data-text="该仓库未启用SVN访问，请仓库管理员前往【&lt;a target='_blank' href=/mindspore/mindscience/settings&gt;仓库设置&lt;/a&gt;】开启。" data-type='svn' data-url=''>SVN</a>
<a class='item' data-text="该仓库未启用SVN访问，请仓库管理员前往【&lt;a target='_blank' href=/mindspore/mindscience/settings&gt;仓库设置&lt;/a&gt;】开启。" data-type='svn_ssh' data-url=''>SVN+SSH</a>
</div>
<div class='ui fluid right labeled small input download-url-panel'>
<input type="text" name="project_clone_url" id="project_clone_url" value="https://gitee.com/mindspore/mindscience.git" onclick="focus();select()" readonly="readonly" />
<div class='ui basic label'>
<div class='ui small basic orange button' data-clipboard-target='#project_clone_url' id='btn-copy-clone-url'>
复制
</div>
</div>
</div>
<div class='ui fluid right labeled warning-text forbid-warning-text'>

</div>

<hr>
<a class="ui fluid download link button" sa_evt="loginInform_show" sa_referrer_url="" sa_referrer_action="克隆/下载" sa_referrer_type="其他" href="javascript:void(0);"><i class='icon download'></i>
下载ZIP
</a><div class='download_repository_zip form modal tiny ui' id='unlanding-complaint-modal'>
<i class='iconfont icon-close close'></i>
<div class='header'>
登录提示
</div>
<div class='container actions'>
<div class='content'>
该操作需登录 Gitee 帐号，请先登录后再操作。
</div>
<div class='ui orange icon large button ok'>
立即登录
</div>
<div class='ui button blank cancel'>
没有帐号，去注册
</div>
</div>
</div>
<script>
  var $elm = $('.download');
  
  $elm.on('click', function() {
    var modals = $("#unlanding-complaint-modal.download_repository_zip");
    if (modals.length > 1) {
      modals.eq(0).modal('show');
    } else {
      modals.modal('show');
    }
  })
  $("#unlanding-complaint-modal.download_repository_zip").modal({
    onDeny: function() {
      window.location.href = "/signup?from=download_repository_zip";
    },
    onApprove: function() {
      window.location.href = "/login?from=download_repository_zip";
    }
  })
</script>

</div>
<script>
  (function() {
    var $btnClone, $btnCopy, $input, $panel;
  
    $btnClone = $('#btn-dl-or-clone');
  
    $panel = $('.git-project-download-panel');
  
    $input = $('#project_clone_url');
  
    $btnCopy = $('#btn-copy-clone-url');
  
    $btnClone.popup({
      on: 'click',
      hoverable: true,
      position: 'bottom center'
    });
  
    $panel.find('.menu > .item').on('click', function(e) {
      var $item, dataUrl;
      $item = $(this).addClass('active');
      $item.siblings().removeClass('active');
      dataUrl = $item.attr('data-url');
      if (dataUrl) {
        $panel.find('.download-url-panel').show();
        $input.val(dataUrl);
        $panel.find('.forbid-warning-text').html('');
      } else {
        $panel.find('.download-url-panel').hide();
        $panel.find('.forbid-warning-text').html($item.attr('data-text') || '');
      }
      return $.cookie('remote_way', $item.attr('data-type'), {
        expires: 365,
        path: '/'
      });
    }).filter('[data-type="' + ($.cookie('remote_way') || 'http') + '"]').trigger('click');
  
    new Clipboard($btnCopy[0]).on('success', function() {
      $btnCopy.popup({
        content: '已复制',
        position: 'right center',
        onHidden: function() {
          return $btnCopy.popup('destroy');
        }
      });
      return $btnCopy.popup('show');
    });
  
  }).call(this);
</script>

</div>
<div class='d-inline pull-right' id='git-project-root-actions'>
<script>
  $('.disabled-upload-readonly').popup({
    content: "只读目录不允许上传文件",
    className: {
      popup: 'ui popup',
    },
    position: 'bottom center',
  })
  $('.disabled-create-folder').popup({
    content: "只读目录不允许创建目录",
    className: {
      popup: 'ui popup',
    },
    position: 'bottom center',
  })
  $('.disabled-create-file').popup({
    content: "只读目录不允许创建文件",
    className: {
      popup: 'ui popup',
    },
    position: 'bottom center',
  })
  $('.disabled-create-submodule').popup({
    content: "只读目录不允许创建子模块",
    className: {
      popup: 'ui popup',
    },
    position: 'bottom center',
  })
  $('.disabled-upload-readonly, .disabled-create-folder, .disabled-create-file, .disabled-create-submodule').click(function() {
    return false
  })
</script>
<style>
  .disabled-upload-readonly, .disabled-create-file, .disabled-create-folder, .disabled-create-submodule {
    background-color: #dcddde !important;
    color: rgba(0, 0, 0, 0.4) !important;
    opacity: 0.3 !important;
    background-image: none !important;
    -webkit-box-shadow: none !important;
            box-shadow: none !important; }
</style>


</div>
<div class='breadcrumb_path path-breadcrumb-contrainer' id='git-project-breadcrumb'>
<div class='ui breadcrumb path project-path-breadcrumb' id='path-breadcrumb'>
<a data-direction="back" class="section repo-name" style="font-weight: bold" href="/mindspore/mindscience/tree/master">mindscience
</a><div class='divider'>
/
</div>
<strong>
<a data-direction="back" class="section" href="/mindspore/mindscience/tree/master/MindFlow"><span class='cblue'>
MindFlow
</span>
</a></strong>
<div class='divider'>
/
</div>
<strong>
<a data-direction="back" class="section" href="/mindspore/mindscience/tree/master/MindFlow/applications"><span class='cblue'>
applications
</span>
</a></strong>
<div class='divider'>
/
</div>
<strong>
<a data-direction="back" class="section" href="/mindspore/mindscience/tree/master/MindFlow/applications/data_driven"><span class='cblue'>
data_driven
</span>
</a></strong>
<div class='divider'>
/
</div>
<strong>
<a data-direction="back" class="section" href="/mindspore/mindscience/tree/master/MindFlow/applications/data_driven/airfoil"><span class='cblue'>
airfoil
</span>
</a></strong>
<div class='divider'>
/
</div>
<strong>
<a data-direction="back" class="section" href="/mindspore/mindscience/tree/master/MindFlow/applications/data_driven/airfoil/2D_steady"><span class='cblue'>
2D_steady
</span>
</a></strong>
<div class='divider'>
/
</div>
<strong>
<a data-direction="back" class="section" href="/mindspore/mindscience/tree/master/MindFlow/applications/data_driven/airfoil/2D_steady/src"><span class='cblue'>
src
</span>
</a></strong>
<div class='divider'>
/
</div>
<strong>
utils.py
</strong>
<i class='iconfont icon-clone' data-clipboard-text='MindFlow/applications/data_driven/airfoil/2D_steady/src/utils.py' id='btn-copy-file-path'></i>
</div>
<style>
  #btn-copy-file-path {
    vertical-align: middle;
    cursor: pointer;
  }
</style>
<script>
  $btnCopy = $('#btn-copy-file-path')
  $btnCopy.popup({
    content: '复制路径'
  })
  
  if ($btnCopy[0]) {
    new Clipboard($btnCopy[0]).on('success', function() {
      $btnCopy.popup('destroy').popup({
        content: '已复制',
        on: 'manual'
      }).popup('show');
      setTimeout(function () {
        $btnCopy.popup('destroy').popup({
          content: '复制路径'
        });
      }, 2000)
    });
  }
</script>


</div>
<div class='ui horizontal list repo-action-list branches-tags' style='display: none;'>
<div class='item'>
<a class="ui blank button" href="/mindspore/mindscience/branches"><i class='iconfont icon-branches'></i>
分支 7
</a></div>
<div class='item mr-3'>
<a class="ui blank button" href="/mindspore/mindscience/tags"><i class='iconfont icon-tag'></i>
标签 3
</a></div>
</div>
</div>
<script src="https://cn-assets.gitee.com/webpacks/parse_blob_form_scheme-1a26a108dcc63124de75.bundle.js"></script>
<script>
  if(window.gon.locale == 'en')
    $('.branches-tags').css('margin-top', '12px')
   // 仓库页面切换路径时: 刷新 yaml 错误检查
  $(window).on('pjax-complete:file-show', function () {
    window.parseBlobFormScheme && window.parseBlobFormScheme($('.js-blob-data').data('blob'));
  });
</script>

<style>
  .ui.dropdown .menu > .header {
    text-transform: none; }
</style>
<script>
  $(function () {
    var $tip = $('#apk-download-tip');
    if (!$tip.length) {
      return;
    }
    $tip.find('.btn-close').on('click', function () {
      $tip.hide();
    });
  });
  (function(){
    function pathAutoRender() {
      var $parent = $('#git-project-bread'),
          $child = $('#git-project-bread').children('.ui.horizontal.list'),
          mainWidth = 0;
      $child.each(function (i,item) {
        mainWidth += $(item).width()
      });
      $('.breadcrumb.path.fork-path').remove();
      if (mainWidth > 995) {
        $('#path-breadcrumb').hide();
        $parent.append('<div class="ui breadcrumb path fork-path">' + $('#path-breadcrumb').html() + '<div/>')
      } else {
        $('#path-breadcrumb').show();
      }
    }
    window.pathAutoRender = pathAutoRender;
    pathAutoRender();
  })();
</script>

<div class='row column tree-holder' id='tree-holder'>
<div class='tree-content-holder' id='tree-content-holder'>
<div class='file_holder'>
<div class='file_title'>
<div class='blob-header-title'>
<div class='blob-description'>
<i class="iconfont icon-file"></i>
<span class='file_name' title='utils.py'>
utils.py
</span>
<small>6.52 KB</small>
</div>
<div class='options'><div class='ui mini buttons basic'>
<textarea name="blob_raw" id="blob_raw" style="display:none;">
# Copyright 2023 Huawei Technologies Co., Ltd&#x000A;#&#x000A;# Licensed under the Apache License, Version 2.0 (the &quot;License&quot;);&#x000A;# you may not use this file except in compliance with the License.&#x000A;# You may obtain a copy of the License at&#x000A;#&#x000A;# http://www.apache.org/licenses/LICENSE-2.0&#x000A;#&#x000A;# Unless required by applicable law or agreed to in writing, software&#x000A;# distributed under the License is distributed on an &quot;AS IS&quot; BASIS,&#x000A;# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.&#x000A;# See the License for the specific language governing permissions and&#x000A;# limitations under the License.&#x000A;# ==============================================================================&#x000A;&quot;&quot;&quot;&#x000A;utils&#x000A;&quot;&quot;&quot;&#x000A;import os&#x000A;import numpy as np&#x000A;&#x000A;from mindspore import ops&#x000A;&#x000A;&#x000A;def check_file_path(path):&#x000A;    &quot;&quot;&quot;check file dir&quot;&quot;&quot;&#x000A;    if not os.path.exists(path):&#x000A;        os.makedirs(path)&#x000A;&#x000A;&#x000A;def unpatchify(labels, img_size=(192, 384), patch_size=16, nchw=False):&#x000A;    &quot;&quot;&quot;unpatchify&quot;&quot;&quot;&#x000A;    label_shape = labels.shape&#x000A;    output_dim = label_shape[-1] // (patch_size * patch_size)&#x000A;    labels = ops.Reshape()(labels, (label_shape[0],&#x000A;                                    img_size[0] // patch_size,&#x000A;                                    img_size[1] // patch_size,&#x000A;                                    patch_size,&#x000A;                                    patch_size,&#x000A;                                    output_dim))&#x000A;&#x000A;    labels = ops.Transpose()(labels, (0, 1, 3, 2, 4, 5))&#x000A;    labels = ops.Reshape()(labels, (label_shape[0],&#x000A;                                    img_size[0],&#x000A;                                    img_size[1],&#x000A;                                    output_dim))&#x000A;    if nchw:&#x000A;        labels = ops.Transpose()(labels, (0, 3, 1, 2))&#x000A;    return labels&#x000A;&#x000A;&#x000A;def get_ckpt_summ_dir(callback_params, model_name, method):&#x000A;    &quot;&quot;&quot;get ckpt and summary dir&quot;&quot;&quot;&#x000A;    summary_dir = os.path.join(f&quot;{callback_params[&#39;summary_dir&#39;]}/summary_{method}&quot;, model_name)&#x000A;    ckpt_dir = os.path.join(summary_dir, &quot;ckpt_dir&quot;)&#x000A;    check_file_path(ckpt_dir)&#x000A;    print(f&#39;model_name: {model_name}&#39;)&#x000A;    print(f&#39;summary_dir: {summary_dir}&#39;)&#x000A;    print(f&#39;ckpt_dir: {ckpt_dir}&#39;)&#x000A;    return ckpt_dir, summary_dir&#x000A;&#x000A;&#x000A;def display_error(error_name, error, error_list):&#x000A;    &quot;&quot;&quot;display error&quot;&quot;&quot;&#x000A;    print(f&#39;mean {error_name} : {error}, max {error_name} : {max(error_list)},&#39;&#x000A;          f&#39; average {error_name} : {np.mean(error_list)},&#39;&#x000A;          f&#39; min {error_name} : {min(error_list)}, median {error_name} : {np.median(error_list)}&#39;&#x000A;          )&#x000A;&#x000A;&#x000A;def calculate_eval_error(dataset, model, save_error=False, post_dir=None):&#x000A;    &quot;&quot;&quot;calculate evaluation error&quot;&quot;&quot;&#x000A;    print(&quot;================================Start Evaluation================================&quot;)&#x000A;    length = dataset.get_dataset_size()&#x000A;    l1_error, l1_error_u, l1_error_v, l1_error_p, l1_error_cp = 0.0, 0.0, 0.0, 0.0, 0.0&#x000A;    l1_error_list, l1_error_u_list, l1_error_v_list, l1_error_p_list, l1_error_cp_list, l1_avg_list = \&#x000A;        [], [], [], [], [], []&#x000A;    for data in dataset.create_dict_iterator(output_numpy=False):&#x000A;        label, pred = get_label_and_pred(data, model)&#x000A;        l1_max_step, l1_max_u_step, l1_max_v_step, l1_max_p_step, cp_max_step = calculate_max_error(label, pred)&#x000A;&#x000A;        l1_avg = np.mean(np.mean(np.mean(np.abs(label - pred), axis=1), axis=1), axis=1).tolist()&#x000A;        l1_error_list.extend(l1_max_step)&#x000A;        l1_error_u_list.extend(l1_max_u_step)&#x000A;        l1_error_v_list.extend(l1_max_v_step)&#x000A;        l1_error_p_list.extend(l1_max_p_step)&#x000A;        l1_error_cp_list.extend(cp_max_step)&#x000A;        l1_avg_list.extend(l1_avg)&#x000A;&#x000A;        l1_error_step, l1_error_u_step, l1_error_v_step, l1_error_p_step, cp_error_step = \&#x000A;            calculate_mean_error(label, pred)&#x000A;        l1_error += l1_error_step&#x000A;        l1_error_u += l1_error_u_step&#x000A;        l1_error_v += l1_error_v_step&#x000A;        l1_error_p += l1_error_p_step&#x000A;        l1_error_cp += cp_error_step&#x000A;    l1_error /= length&#x000A;    l1_error_u /= length&#x000A;    l1_error_v /= length&#x000A;    l1_error_p /= length&#x000A;    l1_error_cp /= length&#x000A;    display_error(&#39;l1_error&#39;, l1_error, l1_error_list)&#x000A;    display_error(&#39;u_error&#39;, l1_error_u, l1_error_u_list)&#x000A;    display_error(&#39;v_error&#39;, l1_error_v, l1_error_v_list)&#x000A;    display_error(&#39;p_error&#39;, l1_error_p, l1_error_p_list)&#x000A;    display_error(&#39;cp_error&#39;, l1_error_cp, l1_error_cp_list)&#x000A;    if save_error:&#x000A;        save_dir = os.path.join(post_dir, &quot;ViT&quot;)&#x000A;        check_file_path(save_dir)&#x000A;        print(f&quot;eval error save dir: {save_dir}&quot;)&#x000A;        np.save(os.path.join(save_dir, &#39;l1_error_list&#39;), l1_error_list)&#x000A;        np.save(os.path.join(save_dir, &#39;l1_error_u_list&#39;), l1_error_u_list)&#x000A;        np.save(os.path.join(save_dir, &#39;l1_error_v_list&#39;), l1_error_v_list)&#x000A;        np.save(os.path.join(save_dir, &#39;l1_error_p_list&#39;), l1_error_p_list)&#x000A;        np.save(os.path.join(save_dir, &#39;l1_error_cp_list&#39;), l1_error_cp_list)&#x000A;        np.save(os.path.join(save_dir, &#39;l1_error_avg_list&#39;), l1_avg_list)&#x000A;    print(&quot;=================================End Evaluation=================================&quot;)&#x000A;&#x000A;&#x000A;def calculate_mean_error(label, pred):&#x000A;    &quot;&quot;&quot;calculate mean l1 error&quot;&quot;&quot;&#x000A;    l1_error = np.mean(np.abs(label - pred))&#x000A;    l1_error_u = np.mean(np.abs(label[..., 0] - pred[..., 0]))&#x000A;    l1_error_v = np.mean(np.abs(label[..., 1] - pred[..., 1]))&#x000A;    l1_error_p = np.mean(np.abs(label[..., 2] - pred[..., 2]))&#x000A;    cp_error = np.mean(np.abs(label[..., 2][0, 0, :] - pred[..., 2][0, 0, :]))&#x000A;    return l1_error, l1_error_u, l1_error_v, l1_error_p, cp_error&#x000A;&#x000A;&#x000A;def calculate_max_error(label, pred):&#x000A;    &quot;&quot;&quot;calculate max l1 error&quot;&quot;&quot;&#x000A;    l1_error = np.max(np.max(np.abs(label - pred), axis=1), axis=1)&#x000A;    l1_error_avg = np.mean(l1_error, axis=1).tolist()&#x000A;    l1_error_u = l1_error[:, 0].tolist()&#x000A;    l1_error_v = l1_error[:, 1].tolist()&#x000A;    l1_error_p = l1_error[:, 2].tolist()&#x000A;    cp_error = np.max(np.abs(label[..., 2][:, 0, :] - pred[..., 2][:, 0, :]), axis=1).tolist()&#x000A;    return l1_error_avg, l1_error_u, l1_error_v, l1_error_p, cp_error&#x000A;&#x000A;&#x000A;def save_label_and_pred(label, pred, save_img_dir):&#x000A;    &quot;&quot;&quot;save abel and pred&quot;&quot;&quot;&#x000A;    save_dir = os.path.join(save_img_dir, &#39;label_pred&#39;)&#x000A;    print(f&#39;label_and_pred: {save_dir}&#39;)&#x000A;    check_file_path(save_dir)&#x000A;    label = unpatchify(label)&#x000A;    pred = unpatchify(pred)&#x000A;    np.save(os.path.join(save_dir, &#39;label_list&#39;), label.asnumpy())&#x000A;    np.save(os.path.join(save_dir, &#39;ViT&#39;), pred.asnumpy())&#x000A;&#x000A;&#x000A;def get_label_and_pred(data, model):&#x000A;    &quot;&quot;&quot;get abel and pred&quot;&quot;&quot;&#x000A;    labels = data[&quot;labels&quot;]&#x000A;    pred = model(data[&#39;inputs&#39;])&#x000A;    pred = unpatchify(pred)&#x000A;    label = unpatchify(labels)&#x000A;    return label.asnumpy(), pred.asnumpy()&#x000A;</textarea>
<a class="ui button" id="copy-text" href="#">一键复制</a>
<a class="ui button edit-blob" title="只有登陆后才可以编辑" href="/mindspore/mindscience/edit/master/MindFlow/applications/data_driven/airfoil/2D_steady/src/utils.py">编辑</a>
<a class="ui button web-ide" target="_blank" href="/-/ide/project/mindspore/mindscience/edit/master/-/MindFlow/applications/data_driven/airfoil/2D_steady/src/utils.py">Web IDE</a>
<a class="ui button edit-raw" target="_blank" href="/mindspore/mindscience/raw/master/MindFlow/applications/data_driven/airfoil/2D_steady/src/utils.py">原始数据</a>
<a class="ui button edit-blame" href="/mindspore/mindscience/blame/master/MindFlow/applications/data_driven/airfoil/2D_steady/src/utils.py">按行查看</a>
<a class="ui button edit-history" href="/mindspore/mindscience/commits/master/MindFlow/applications/data_driven/airfoil/2D_steady/src/utils.py">历史</a>
</div>
<script>
  "use strict";
  try {
    if((gon.wait_fork!=undefined && gon.wait_fork==true) || (gon.wait_fetch!=undefined && gon.wait_fetch==true)){
      $('.edit-blob').popup({content:"当前仓库正在后台处理中,暂时无法编辑", on: 'hover', delay: { show: 200, hide: 200 }});
      $('.edit-blob').click(function(e){
        e.preventDefault();
      })
    }
  
    var setUrl = function() {
      var params = window.location.search
      if (params==undefined || $.trim(params).length==0) return;
      $('span.options').children('.basic').find('a').each(function(index,ele){
        var origin_href = $(ele).attr('href');
        if (origin_href!="#" && origin_href.indexOf('?') == -1){
          $(ele).attr('href',origin_href+params);
        }
      });
    }
  
    setUrl();
  
    var clipboard = null,
        $btncopy  = $("#copy-text");
  
    clipboard = new Clipboard("#copy-text", {
      text: function(trigger) {
        return $("#blob_raw").val();
      }
    })
  
    clipboard.on('success', function(e) {
      $btncopy.popup('hide');
      $btncopy.popup('destroy');
      $btncopy.popup({content: '已复制', position: 'bottom center'});
      $btncopy.popup('show');
    })
  
    clipboard.on('error', function(e) {
      var giteeModal = new GiteeModalHelper({okText: '确定'});
      giteeModal.alert("一键复制", '复制失败，请手动复制');
    })
  
    $(function() {
      $btncopy.popup({
        content: '点击复制',
        position: 'bottom center'
      })
    })
  
  } catch (error) {
    console.log('blob/action error:' + error);
  }
  
  $('.disabled-edit-readonly').popup({
    content: "只读文件不可编辑",
    className: {
      popup: 'ui popup',
    },
    position: 'bottom center',
  })
  $('.disabled-edit-readonly, .disabled-edit-status').click(function() {
    return false
  })
  $('.has_tooltip').popup({
    position: 'top center'
  });
</script>
<style>
  .disabled-edit-readonly, .disabled-edit-status {
    background-color: #dcddde !important;
    color: rgba(0, 0, 0, 0.4) !important;
    opacity: 0.3 !important;
    background-image: none !important;
    -webkit-box-shadow: none !important;
            box-shadow: none !important;
    cursor: default !important; }
  
  .drawio-iframe-code-card {
    position: relative; }
    .drawio-iframe-code-card textarea {
      width: 100%;
      height: 140px;
      resize: none; }
    .drawio-iframe-code-card .icon-clone {
      position: absolute;
      right: 32px;
      bottom: 32px; }
    .drawio-iframe-code-card iframe {
      border-radius: 2px;
      border: 1px solid #DEDEDF; }
</style>
</div>
</div>
<div class='blob-header-title mt-1 ubblock_tip'>
</div>
<div class='contributor-description'><span class='recent-commit' style='margin-top: 0.7rem'>
<a class="commit-author-link  js-popover-card " data-username="b_rookie" href="/b_rookie">Brian-K</a>
<span>提交于</span>
<span class='timeago commit-date' title='2023-03-23 19:19:33 +0800'>
2023-03-23 19:19
</span>
.
<a href="/mindspore/mindscience/commit/685390c2f6b6e8bbcb3df4dc80741934c023c38a">[add]: 2D_steady case code</a>
</span>
</div>
</div>
<div class='clearfix'></div>
<div class='file_content code'>
<div class='lines white'>
<div class='line-numbers'><a href='#L1' id='L1'>1</a><a href='#L2' id='L2'>2</a><a href='#L3' id='L3'>3</a><a href='#L4' id='L4'>4</a><a href='#L5' id='L5'>5</a><a href='#L6' id='L6'>6</a><a href='#L7' id='L7'>7</a><a href='#L8' id='L8'>8</a><a href='#L9' id='L9'>9</a><a href='#L10' id='L10'>10</a><a href='#L11' id='L11'>11</a><a href='#L12' id='L12'>12</a><a href='#L13' id='L13'>13</a><a href='#L14' id='L14'>14</a><a href='#L15' id='L15'>15</a><a href='#L16' id='L16'>16</a><a href='#L17' id='L17'>17</a><a href='#L18' id='L18'>18</a><a href='#L19' id='L19'>19</a><a href='#L20' id='L20'>20</a><a href='#L21' id='L21'>21</a><a href='#L22' id='L22'>22</a><a href='#L23' id='L23'>23</a><a href='#L24' id='L24'>24</a><a href='#L25' id='L25'>25</a><a href='#L26' id='L26'>26</a><a href='#L27' id='L27'>27</a><a href='#L28' id='L28'>28</a><a href='#L29' id='L29'>29</a><a href='#L30' id='L30'>30</a><a href='#L31' id='L31'>31</a><a href='#L32' id='L32'>32</a><a href='#L33' id='L33'>33</a><a href='#L34' id='L34'>34</a><a href='#L35' id='L35'>35</a><a href='#L36' id='L36'>36</a><a href='#L37' id='L37'>37</a><a href='#L38' id='L38'>38</a><a href='#L39' id='L39'>39</a><a href='#L40' id='L40'>40</a><a href='#L41' id='L41'>41</a><a href='#L42' id='L42'>42</a><a href='#L43' id='L43'>43</a><a href='#L44' id='L44'>44</a><a href='#L45' id='L45'>45</a><a href='#L46' id='L46'>46</a><a href='#L47' id='L47'>47</a><a href='#L48' id='L48'>48</a><a href='#L49' id='L49'>49</a><a href='#L50' id='L50'>50</a><a href='#L51' id='L51'>51</a><a href='#L52' id='L52'>52</a><a href='#L53' id='L53'>53</a><a href='#L54' id='L54'>54</a><a href='#L55' id='L55'>55</a><a href='#L56' id='L56'>56</a><a href='#L57' id='L57'>57</a><a href='#L58' id='L58'>58</a><a href='#L59' id='L59'>59</a><a href='#L60' id='L60'>60</a><a href='#L61' id='L61'>61</a><a href='#L62' id='L62'>62</a><a href='#L63' id='L63'>63</a><a href='#L64' id='L64'>64</a><a href='#L65' id='L65'>65</a><a href='#L66' id='L66'>66</a><a href='#L67' id='L67'>67</a><a href='#L68' id='L68'>68</a><a href='#L69' id='L69'>69</a><a href='#L70' id='L70'>70</a><a href='#L71' id='L71'>71</a><a href='#L72' id='L72'>72</a><a href='#L73' id='L73'>73</a><a href='#L74' id='L74'>74</a><a href='#L75' id='L75'>75</a><a href='#L76' id='L76'>76</a><a href='#L77' id='L77'>77</a><a href='#L78' id='L78'>78</a><a href='#L79' id='L79'>79</a><a href='#L80' id='L80'>80</a><a href='#L81' id='L81'>81</a><a href='#L82' id='L82'>82</a><a href='#L83' id='L83'>83</a><a href='#L84' id='L84'>84</a><a href='#L85' id='L85'>85</a><a href='#L86' id='L86'>86</a><a href='#L87' id='L87'>87</a><a href='#L88' id='L88'>88</a><a href='#L89' id='L89'>89</a><a href='#L90' id='L90'>90</a><a href='#L91' id='L91'>91</a><a href='#L92' id='L92'>92</a><a href='#L93' id='L93'>93</a><a href='#L94' id='L94'>94</a><a href='#L95' id='L95'>95</a><a href='#L96' id='L96'>96</a><a href='#L97' id='L97'>97</a><a href='#L98' id='L98'>98</a><a href='#L99' id='L99'>99</a><a href='#L100' id='L100'>100</a><a href='#L101' id='L101'>101</a><a href='#L102' id='L102'>102</a><a href='#L103' id='L103'>103</a><a href='#L104' id='L104'>104</a><a href='#L105' id='L105'>105</a><a href='#L106' id='L106'>106</a><a href='#L107' id='L107'>107</a><a href='#L108' id='L108'>108</a><a href='#L109' id='L109'>109</a><a href='#L110' id='L110'>110</a><a href='#L111' id='L111'>111</a><a href='#L112' id='L112'>112</a><a href='#L113' id='L113'>113</a><a href='#L114' id='L114'>114</a><a href='#L115' id='L115'>115</a><a href='#L116' id='L116'>116</a><a href='#L117' id='L117'>117</a><a href='#L118' id='L118'>118</a><a href='#L119' id='L119'>119</a><a href='#L120' id='L120'>120</a><a href='#L121' id='L121'>121</a><a href='#L122' id='L122'>122</a><a href='#L123' id='L123'>123</a><a href='#L124' id='L124'>124</a><a href='#L125' id='L125'>125</a><a href='#L126' id='L126'>126</a><a href='#L127' id='L127'>127</a><a href='#L128' id='L128'>128</a><a href='#L129' id='L129'>129</a><a href='#L130' id='L130'>130</a><a href='#L131' id='L131'>131</a><a href='#L132' id='L132'>132</a><a href='#L133' id='L133'>133</a><a href='#L134' id='L134'>134</a><a href='#L135' id='L135'>135</a><a href='#L136' id='L136'>136</a><a href='#L137' id='L137'>137</a><a href='#L138' id='L138'>138</a><a href='#L139' id='L139'>139</a><a href='#L140' id='L140'>140</a><a href='#L141' id='L141'>141</a><a href='#L142' id='L142'>142</a><a href='#L143' id='L143'>143</a><a href='#L144' id='L144'>144</a><a href='#L145' id='L145'>145</a><a href='#L146' id='L146'>146</a><a href='#L147' id='L147'>147</a><a href='#L148' id='L148'>148</a><a href='#L149' id='L149'>149</a><a href='#L150' id='L150'>150</a><a href='#L151' id='L151'>151</a><a href='#L152' id='L152'>152</a><a href='#L153' id='L153'>153</a><a href='#L154' id='L154'>154</a><a href='#L155' id='L155'>155</a><a href='#L156' id='L156'>156</a><a href='#L157' id='L157'>157</a></div><div class="highlight markdown-code-block"><pre class=""><div class='line' id='LC1'><span class="c1"># Copyright 2023 Huawei Technologies Co., Ltd</span>&#x000A;</div><div class='line' id='LC2'><span class="c1">#</span>&#x000A;</div><div class='line' id='LC3'><span class="c1"># Licensed under the Apache License, Version 2.0 (the "License");</span>&#x000A;</div><div class='line' id='LC4'><span class="c1"># you may not use this file except in compliance with the License.</span>&#x000A;</div><div class='line' id='LC5'><span class="c1"># You may obtain a copy of the License at</span>&#x000A;</div><div class='line' id='LC6'><span class="c1">#</span>&#x000A;</div><div class='line' id='LC7'><span class="c1"># http://www.apache.org/licenses/LICENSE-2.0</span>&#x000A;</div><div class='line' id='LC8'><span class="c1">#</span>&#x000A;</div><div class='line' id='LC9'><span class="c1"># Unless required by applicable law or agreed to in writing, software</span>&#x000A;</div><div class='line' id='LC10'><span class="c1"># distributed under the License is distributed on an "AS IS" BASIS,</span>&#x000A;</div><div class='line' id='LC11'><span class="c1"># WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.</span>&#x000A;</div><div class='line' id='LC12'><span class="c1"># See the License for the specific language governing permissions and</span>&#x000A;</div><div class='line' id='LC13'><span class="c1"># limitations under the License.</span>&#x000A;</div><div class='line' id='LC14'><span class="c1"># ==============================================================================</span>&#x000A;</div><div class='line' id='LC15'><span class="s">"""</span>&#x000A;</div><div class='line' id='LC16'><span class="s">utils</span>&#x000A;</div><div class='line' id='LC17'><span class="s">"""</span>&#x000A;</div><div class='line' id='LC18'><span class="kn">import</span> <span class="nn">os</span>&#x000A;</div><div class='line' id='LC19'><span class="kn">import</span> <span class="nn">numpy</span> <span class="k">as</span> <span class="n">np</span>&#x000A;</div><div class='line' id='LC20'>&#x000A;</div><div class='line' id='LC21'><span class="kn">from</span> <span class="nn">mindspore</span> <span class="kn">import</span> <span class="n">ops</span>&#x000A;</div><div class='line' id='LC22'>&#x000A;</div><div class='line' id='LC23'>&#x000A;</div><div class='line' id='LC24'><span class="k">def</span> <span class="nf">check_file_path</span><span class="p">(</span><span class="n">path</span><span class="p">):</span>&#x000A;</div><div class='line' id='LC25'>    <span class="s">"""check file dir"""</span>&#x000A;</div><div class='line' id='LC26'>    <span class="k">if</span> <span class="ow">not</span> <span class="n">os</span><span class="p">.</span><span class="n">path</span><span class="p">.</span><span class="n">exists</span><span class="p">(</span><span class="n">path</span><span class="p">):</span>&#x000A;</div><div class='line' id='LC27'>        <span class="n">os</span><span class="p">.</span><span class="n">makedirs</span><span class="p">(</span><span class="n">path</span><span class="p">)</span>&#x000A;</div><div class='line' id='LC28'>&#x000A;</div><div class='line' id='LC29'>&#x000A;</div><div class='line' id='LC30'><span class="k">def</span> <span class="nf">unpatchify</span><span class="p">(</span><span class="n">labels</span><span class="p">,</span> <span class="n">img_size</span><span class="o">=</span><span class="p">(</span><span class="mi">192</span><span class="p">,</span> <span class="mi">384</span><span class="p">),</span> <span class="n">patch_size</span><span class="o">=</span><span class="mi">16</span><span class="p">,</span> <span class="n">nchw</span><span class="o">=</span><span class="bp">False</span><span class="p">):</span>&#x000A;</div><div class='line' id='LC31'>    <span class="s">"""unpatchify"""</span>&#x000A;</div><div class='line' id='LC32'>    <span class="n">label_shape</span> <span class="o">=</span> <span class="n">labels</span><span class="p">.</span><span class="n">shape</span>&#x000A;</div><div class='line' id='LC33'>    <span class="n">output_dim</span> <span class="o">=</span> <span class="n">label_shape</span><span class="p">[</span><span class="o">-</span><span class="mi">1</span><span class="p">]</span> <span class="o">//</span> <span class="p">(</span><span class="n">patch_size</span> <span class="o">*</span> <span class="n">patch_size</span><span class="p">)</span>&#x000A;</div><div class='line' id='LC34'>    <span class="n">labels</span> <span class="o">=</span> <span class="n">ops</span><span class="p">.</span><span class="n">Reshape</span><span class="p">()(</span><span class="n">labels</span><span class="p">,</span> <span class="p">(</span><span class="n">label_shape</span><span class="p">[</span><span class="mi">0</span><span class="p">],</span>&#x000A;</div><div class='line' id='LC35'>                                    <span class="n">img_size</span><span class="p">[</span><span class="mi">0</span><span class="p">]</span> <span class="o">//</span> <span class="n">patch_size</span><span class="p">,</span>&#x000A;</div><div class='line' id='LC36'>                                    <span class="n">img_size</span><span class="p">[</span><span class="mi">1</span><span class="p">]</span> <span class="o">//</span> <span class="n">patch_size</span><span class="p">,</span>&#x000A;</div><div class='line' id='LC37'>                                    <span class="n">patch_size</span><span class="p">,</span>&#x000A;</div><div class='line' id='LC38'>                                    <span class="n">patch_size</span><span class="p">,</span>&#x000A;</div><div class='line' id='LC39'>                                    <span class="n">output_dim</span><span class="p">))</span>&#x000A;</div><div class='line' id='LC40'>&#x000A;</div><div class='line' id='LC41'>    <span class="n">labels</span> <span class="o">=</span> <span class="n">ops</span><span class="p">.</span><span class="n">Transpose</span><span class="p">()(</span><span class="n">labels</span><span class="p">,</span> <span class="p">(</span><span class="mi">0</span><span class="p">,</span> <span class="mi">1</span><span class="p">,</span> <span class="mi">3</span><span class="p">,</span> <span class="mi">2</span><span class="p">,</span> <span class="mi">4</span><span class="p">,</span> <span class="mi">5</span><span class="p">))</span>&#x000A;</div><div class='line' id='LC42'>    <span class="n">labels</span> <span class="o">=</span> <span class="n">ops</span><span class="p">.</span><span class="n">Reshape</span><span class="p">()(</span><span class="n">labels</span><span class="p">,</span> <span class="p">(</span><span class="n">label_shape</span><span class="p">[</span><span class="mi">0</span><span class="p">],</span>&#x000A;</div><div class='line' id='LC43'>                                    <span class="n">img_size</span><span class="p">[</span><span class="mi">0</span><span class="p">],</span>&#x000A;</div><div class='line' id='LC44'>                                    <span class="n">img_size</span><span class="p">[</span><span class="mi">1</span><span class="p">],</span>&#x000A;</div><div class='line' id='LC45'>                                    <span class="n">output_dim</span><span class="p">))</span>&#x000A;</div><div class='line' id='LC46'>    <span class="k">if</span> <span class="n">nchw</span><span class="p">:</span>&#x000A;</div><div class='line' id='LC47'>        <span class="n">labels</span> <span class="o">=</span> <span class="n">ops</span><span class="p">.</span><span class="n">Transpose</span><span class="p">()(</span><span class="n">labels</span><span class="p">,</span> <span class="p">(</span><span class="mi">0</span><span class="p">,</span> <span class="mi">3</span><span class="p">,</span> <span class="mi">1</span><span class="p">,</span> <span class="mi">2</span><span class="p">))</span>&#x000A;</div><div class='line' id='LC48'>    <span class="k">return</span> <span class="n">labels</span>&#x000A;</div><div class='line' id='LC49'>&#x000A;</div><div class='line' id='LC50'>&#x000A;</div><div class='line' id='LC51'><span class="k">def</span> <span class="nf">get_ckpt_summ_dir</span><span class="p">(</span><span class="n">callback_params</span><span class="p">,</span> <span class="n">model_name</span><span class="p">,</span> <span class="n">method</span><span class="p">):</span>&#x000A;</div><div class='line' id='LC52'>    <span class="s">"""get ckpt and summary dir"""</span>&#x000A;</div><div class='line' id='LC53'>    <span class="n">summary_dir</span> <span class="o">=</span> <span class="n">os</span><span class="p">.</span><span class="n">path</span><span class="p">.</span><span class="n">join</span><span class="p">(</span><span class="sa">f</span><span class="s">"</span><span class="si">{</span><span class="n">callback_params</span><span class="p">[</span><span class="s">'summary_dir'</span><span class="p">]</span><span class="si">}</span><span class="s">/summary_</span><span class="si">{</span><span class="n">method</span><span class="si">}</span><span class="s">"</span><span class="p">,</span> <span class="n">model_name</span><span class="p">)</span>&#x000A;</div><div class='line' id='LC54'>    <span class="n">ckpt_dir</span> <span class="o">=</span> <span class="n">os</span><span class="p">.</span><span class="n">path</span><span class="p">.</span><span class="n">join</span><span class="p">(</span><span class="n">summary_dir</span><span class="p">,</span> <span class="s">"ckpt_dir"</span><span class="p">)</span>&#x000A;</div><div class='line' id='LC55'>    <span class="n">check_file_path</span><span class="p">(</span><span class="n">ckpt_dir</span><span class="p">)</span>&#x000A;</div><div class='line' id='LC56'>    <span class="k">print</span><span class="p">(</span><span class="sa">f</span><span class="s">'model_name: </span><span class="si">{</span><span class="n">model_name</span><span class="si">}</span><span class="s">'</span><span class="p">)</span>&#x000A;</div><div class='line' id='LC57'>    <span class="k">print</span><span class="p">(</span><span class="sa">f</span><span class="s">'summary_dir: </span><span class="si">{</span><span class="n">summary_dir</span><span class="si">}</span><span class="s">'</span><span class="p">)</span>&#x000A;</div><div class='line' id='LC58'>    <span class="k">print</span><span class="p">(</span><span class="sa">f</span><span class="s">'ckpt_dir: </span><span class="si">{</span><span class="n">ckpt_dir</span><span class="si">}</span><span class="s">'</span><span class="p">)</span>&#x000A;</div><div class='line' id='LC59'>    <span class="k">return</span> <span class="n">ckpt_dir</span><span class="p">,</span> <span class="n">summary_dir</span>&#x000A;</div><div class='line' id='LC60'>&#x000A;</div><div class='line' id='LC61'>&#x000A;</div><div class='line' id='LC62'><span class="k">def</span> <span class="nf">display_error</span><span class="p">(</span><span class="n">error_name</span><span class="p">,</span> <span class="n">error</span><span class="p">,</span> <span class="n">error_list</span><span class="p">):</span>&#x000A;</div><div class='line' id='LC63'>    <span class="s">"""display error"""</span>&#x000A;</div><div class='line' id='LC64'>    <span class="k">print</span><span class="p">(</span><span class="sa">f</span><span class="s">'mean </span><span class="si">{</span><span class="n">error_name</span><span class="si">}</span><span class="s"> : </span><span class="si">{</span><span class="n">error</span><span class="si">}</span><span class="s">, max </span><span class="si">{</span><span class="n">error_name</span><span class="si">}</span><span class="s"> : </span><span class="si">{</span><span class="nb">max</span><span class="p">(</span><span class="n">error_list</span><span class="p">)</span><span class="si">}</span><span class="s">,'</span>&#x000A;</div><div class='line' id='LC65'>          <span class="sa">f</span><span class="s">' average </span><span class="si">{</span><span class="n">error_name</span><span class="si">}</span><span class="s"> : </span><span class="si">{</span><span class="n">np</span><span class="p">.</span><span class="n">mean</span><span class="p">(</span><span class="n">error_list</span><span class="p">)</span><span class="si">}</span><span class="s">,'</span>&#x000A;</div><div class='line' id='LC66'>          <span class="sa">f</span><span class="s">' min </span><span class="si">{</span><span class="n">error_name</span><span class="si">}</span><span class="s"> : </span><span class="si">{</span><span class="nb">min</span><span class="p">(</span><span class="n">error_list</span><span class="p">)</span><span class="si">}</span><span class="s">, median </span><span class="si">{</span><span class="n">error_name</span><span class="si">}</span><span class="s"> : </span><span class="si">{</span><span class="n">np</span><span class="p">.</span><span class="n">median</span><span class="p">(</span><span class="n">error_list</span><span class="p">)</span><span class="si">}</span><span class="s">'</span>&#x000A;</div><div class='line' id='LC67'>          <span class="p">)</span>&#x000A;</div><div class='line' id='LC68'>&#x000A;</div><div class='line' id='LC69'>&#x000A;</div><div class='line' id='LC70'><span class="k">def</span> <span class="nf">calculate_eval_error</span><span class="p">(</span><span class="n">dataset</span><span class="p">,</span> <span class="n">model</span><span class="p">,</span> <span class="n">save_error</span><span class="o">=</span><span class="bp">False</span><span class="p">,</span> <span class="n">post_dir</span><span class="o">=</span><span class="bp">None</span><span class="p">):</span>&#x000A;</div><div class='line' id='LC71'>    <span class="s">"""calculate evaluation error"""</span>&#x000A;</div><div class='line' id='LC72'>    <span class="k">print</span><span class="p">(</span><span class="s">"================================Start Evaluation================================"</span><span class="p">)</span>&#x000A;</div><div class='line' id='LC73'>    <span class="n">length</span> <span class="o">=</span> <span class="n">dataset</span><span class="p">.</span><span class="n">get_dataset_size</span><span class="p">()</span>&#x000A;</div><div class='line' id='LC74'>    <span class="n">l1_error</span><span class="p">,</span> <span class="n">l1_error_u</span><span class="p">,</span> <span class="n">l1_error_v</span><span class="p">,</span> <span class="n">l1_error_p</span><span class="p">,</span> <span class="n">l1_error_cp</span> <span class="o">=</span> <span class="mf">0.0</span><span class="p">,</span> <span class="mf">0.0</span><span class="p">,</span> <span class="mf">0.0</span><span class="p">,</span> <span class="mf">0.0</span><span class="p">,</span> <span class="mf">0.0</span>&#x000A;</div><div class='line' id='LC75'>    <span class="n">l1_error_list</span><span class="p">,</span> <span class="n">l1_error_u_list</span><span class="p">,</span> <span class="n">l1_error_v_list</span><span class="p">,</span> <span class="n">l1_error_p_list</span><span class="p">,</span> <span class="n">l1_error_cp_list</span><span class="p">,</span> <span class="n">l1_avg_list</span> <span class="o">=</span> \&#x000A;</div><div class='line' id='LC76'>        <span class="p">[],</span> <span class="p">[],</span> <span class="p">[],</span> <span class="p">[],</span> <span class="p">[],</span> <span class="p">[]</span>&#x000A;</div><div class='line' id='LC77'>    <span class="k">for</span> <span class="n">data</span> <span class="ow">in</span> <span class="n">dataset</span><span class="p">.</span><span class="n">create_dict_iterator</span><span class="p">(</span><span class="n">output_numpy</span><span class="o">=</span><span class="bp">False</span><span class="p">):</span>&#x000A;</div><div class='line' id='LC78'>        <span class="n">label</span><span class="p">,</span> <span class="n">pred</span> <span class="o">=</span> <span class="n">get_label_and_pred</span><span class="p">(</span><span class="n">data</span><span class="p">,</span> <span class="n">model</span><span class="p">)</span>&#x000A;</div><div class='line' id='LC79'>        <span class="n">l1_max_step</span><span class="p">,</span> <span class="n">l1_max_u_step</span><span class="p">,</span> <span class="n">l1_max_v_step</span><span class="p">,</span> <span class="n">l1_max_p_step</span><span class="p">,</span> <span class="n">cp_max_step</span> <span class="o">=</span> <span class="n">calculate_max_error</span><span class="p">(</span><span class="n">label</span><span class="p">,</span> <span class="n">pred</span><span class="p">)</span>&#x000A;</div><div class='line' id='LC80'>&#x000A;</div><div class='line' id='LC81'>        <span class="n">l1_avg</span> <span class="o">=</span> <span class="n">np</span><span class="p">.</span><span class="n">mean</span><span class="p">(</span><span class="n">np</span><span class="p">.</span><span class="n">mean</span><span class="p">(</span><span class="n">np</span><span class="p">.</span><span class="n">mean</span><span class="p">(</span><span class="n">np</span><span class="p">.</span><span class="nb">abs</span><span class="p">(</span><span class="n">label</span> <span class="o">-</span> <span class="n">pred</span><span class="p">),</span> <span class="n">axis</span><span class="o">=</span><span class="mi">1</span><span class="p">),</span> <span class="n">axis</span><span class="o">=</span><span class="mi">1</span><span class="p">),</span> <span class="n">axis</span><span class="o">=</span><span class="mi">1</span><span class="p">).</span><span class="n">tolist</span><span class="p">()</span>&#x000A;</div><div class='line' id='LC82'>        <span class="n">l1_error_list</span><span class="p">.</span><span class="n">extend</span><span class="p">(</span><span class="n">l1_max_step</span><span class="p">)</span>&#x000A;</div><div class='line' id='LC83'>        <span class="n">l1_error_u_list</span><span class="p">.</span><span class="n">extend</span><span class="p">(</span><span class="n">l1_max_u_step</span><span class="p">)</span>&#x000A;</div><div class='line' id='LC84'>        <span class="n">l1_error_v_list</span><span class="p">.</span><span class="n">extend</span><span class="p">(</span><span class="n">l1_max_v_step</span><span class="p">)</span>&#x000A;</div><div class='line' id='LC85'>        <span class="n">l1_error_p_list</span><span class="p">.</span><span class="n">extend</span><span class="p">(</span><span class="n">l1_max_p_step</span><span class="p">)</span>&#x000A;</div><div class='line' id='LC86'>        <span class="n">l1_error_cp_list</span><span class="p">.</span><span class="n">extend</span><span class="p">(</span><span class="n">cp_max_step</span><span class="p">)</span>&#x000A;</div><div class='line' id='LC87'>        <span class="n">l1_avg_list</span><span class="p">.</span><span class="n">extend</span><span class="p">(</span><span class="n">l1_avg</span><span class="p">)</span>&#x000A;</div><div class='line' id='LC88'>&#x000A;</div><div class='line' id='LC89'>        <span class="n">l1_error_step</span><span class="p">,</span> <span class="n">l1_error_u_step</span><span class="p">,</span> <span class="n">l1_error_v_step</span><span class="p">,</span> <span class="n">l1_error_p_step</span><span class="p">,</span> <span class="n">cp_error_step</span> <span class="o">=</span> \&#x000A;</div><div class='line' id='LC90'>            <span class="n">calculate_mean_error</span><span class="p">(</span><span class="n">label</span><span class="p">,</span> <span class="n">pred</span><span class="p">)</span>&#x000A;</div><div class='line' id='LC91'>        <span class="n">l1_error</span> <span class="o">+=</span> <span class="n">l1_error_step</span>&#x000A;</div><div class='line' id='LC92'>        <span class="n">l1_error_u</span> <span class="o">+=</span> <span class="n">l1_error_u_step</span>&#x000A;</div><div class='line' id='LC93'>        <span class="n">l1_error_v</span> <span class="o">+=</span> <span class="n">l1_error_v_step</span>&#x000A;</div><div class='line' id='LC94'>        <span class="n">l1_error_p</span> <span class="o">+=</span> <span class="n">l1_error_p_step</span>&#x000A;</div><div class='line' id='LC95'>        <span class="n">l1_error_cp</span> <span class="o">+=</span> <span class="n">cp_error_step</span>&#x000A;</div><div class='line' id='LC96'>    <span class="n">l1_error</span> <span class="o">/=</span> <span class="n">length</span>&#x000A;</div><div class='line' id='LC97'>    <span class="n">l1_error_u</span> <span class="o">/=</span> <span class="n">length</span>&#x000A;</div><div class='line' id='LC98'>    <span class="n">l1_error_v</span> <span class="o">/=</span> <span class="n">length</span>&#x000A;</div><div class='line' id='LC99'>    <span class="n">l1_error_p</span> <span class="o">/=</span> <span class="n">length</span>&#x000A;</div><div class='line' id='LC100'>    <span class="n">l1_error_cp</span> <span class="o">/=</span> <span class="n">length</span>&#x000A;</div><div class='line' id='LC101'>    <span class="n">display_error</span><span class="p">(</span><span class="s">'l1_error'</span><span class="p">,</span> <span class="n">l1_error</span><span class="p">,</span> <span class="n">l1_error_list</span><span class="p">)</span>&#x000A;</div><div class='line' id='LC102'>    <span class="n">display_error</span><span class="p">(</span><span class="s">'u_error'</span><span class="p">,</span> <span class="n">l1_error_u</span><span class="p">,</span> <span class="n">l1_error_u_list</span><span class="p">)</span>&#x000A;</div><div class='line' id='LC103'>    <span class="n">display_error</span><span class="p">(</span><span class="s">'v_error'</span><span class="p">,</span> <span class="n">l1_error_v</span><span class="p">,</span> <span class="n">l1_error_v_list</span><span class="p">)</span>&#x000A;</div><div class='line' id='LC104'>    <span class="n">display_error</span><span class="p">(</span><span class="s">'p_error'</span><span class="p">,</span> <span class="n">l1_error_p</span><span class="p">,</span> <span class="n">l1_error_p_list</span><span class="p">)</span>&#x000A;</div><div class='line' id='LC105'>    <span class="n">display_error</span><span class="p">(</span><span class="s">'cp_error'</span><span class="p">,</span> <span class="n">l1_error_cp</span><span class="p">,</span> <span class="n">l1_error_cp_list</span><span class="p">)</span>&#x000A;</div><div class='line' id='LC106'>    <span class="k">if</span> <span class="n">save_error</span><span class="p">:</span>&#x000A;</div><div class='line' id='LC107'>        <span class="n">save_dir</span> <span class="o">=</span> <span class="n">os</span><span class="p">.</span><span class="n">path</span><span class="p">.</span><span class="n">join</span><span class="p">(</span><span class="n">post_dir</span><span class="p">,</span> <span class="s">"ViT"</span><span class="p">)</span>&#x000A;</div><div class='line' id='LC108'>        <span class="n">check_file_path</span><span class="p">(</span><span class="n">save_dir</span><span class="p">)</span>&#x000A;</div><div class='line' id='LC109'>        <span class="k">print</span><span class="p">(</span><span class="sa">f</span><span class="s">"eval error save dir: </span><span class="si">{</span><span class="n">save_dir</span><span class="si">}</span><span class="s">"</span><span class="p">)</span>&#x000A;</div><div class='line' id='LC110'>        <span class="n">np</span><span class="p">.</span><span class="n">save</span><span class="p">(</span><span class="n">os</span><span class="p">.</span><span class="n">path</span><span class="p">.</span><span class="n">join</span><span class="p">(</span><span class="n">save_dir</span><span class="p">,</span> <span class="s">'l1_error_list'</span><span class="p">),</span> <span class="n">l1_error_list</span><span class="p">)</span>&#x000A;</div><div class='line' id='LC111'>        <span class="n">np</span><span class="p">.</span><span class="n">save</span><span class="p">(</span><span class="n">os</span><span class="p">.</span><span class="n">path</span><span class="p">.</span><span class="n">join</span><span class="p">(</span><span class="n">save_dir</span><span class="p">,</span> <span class="s">'l1_error_u_list'</span><span class="p">),</span> <span class="n">l1_error_u_list</span><span class="p">)</span>&#x000A;</div><div class='line' id='LC112'>        <span class="n">np</span><span class="p">.</span><span class="n">save</span><span class="p">(</span><span class="n">os</span><span class="p">.</span><span class="n">path</span><span class="p">.</span><span class="n">join</span><span class="p">(</span><span class="n">save_dir</span><span class="p">,</span> <span class="s">'l1_error_v_list'</span><span class="p">),</span> <span class="n">l1_error_v_list</span><span class="p">)</span>&#x000A;</div><div class='line' id='LC113'>        <span class="n">np</span><span class="p">.</span><span class="n">save</span><span class="p">(</span><span class="n">os</span><span class="p">.</span><span class="n">path</span><span class="p">.</span><span class="n">join</span><span class="p">(</span><span class="n">save_dir</span><span class="p">,</span> <span class="s">'l1_error_p_list'</span><span class="p">),</span> <span class="n">l1_error_p_list</span><span class="p">)</span>&#x000A;</div><div class='line' id='LC114'>        <span class="n">np</span><span class="p">.</span><span class="n">save</span><span class="p">(</span><span class="n">os</span><span class="p">.</span><span class="n">path</span><span class="p">.</span><span class="n">join</span><span class="p">(</span><span class="n">save_dir</span><span class="p">,</span> <span class="s">'l1_error_cp_list'</span><span class="p">),</span> <span class="n">l1_error_cp_list</span><span class="p">)</span>&#x000A;</div><div class='line' id='LC115'>        <span class="n">np</span><span class="p">.</span><span class="n">save</span><span class="p">(</span><span class="n">os</span><span class="p">.</span><span class="n">path</span><span class="p">.</span><span class="n">join</span><span class="p">(</span><span class="n">save_dir</span><span class="p">,</span> <span class="s">'l1_error_avg_list'</span><span class="p">),</span> <span class="n">l1_avg_list</span><span class="p">)</span>&#x000A;</div><div class='line' id='LC116'>    <span class="k">print</span><span class="p">(</span><span class="s">"=================================End Evaluation================================="</span><span class="p">)</span>&#x000A;</div><div class='line' id='LC117'>&#x000A;</div><div class='line' id='LC118'>&#x000A;</div><div class='line' id='LC119'><span class="k">def</span> <span class="nf">calculate_mean_error</span><span class="p">(</span><span class="n">label</span><span class="p">,</span> <span class="n">pred</span><span class="p">):</span>&#x000A;</div><div class='line' id='LC120'>    <span class="s">"""calculate mean l1 error"""</span>&#x000A;</div><div class='line' id='LC121'>    <span class="n">l1_error</span> <span class="o">=</span> <span class="n">np</span><span class="p">.</span><span class="n">mean</span><span class="p">(</span><span class="n">np</span><span class="p">.</span><span class="nb">abs</span><span class="p">(</span><span class="n">label</span> <span class="o">-</span> <span class="n">pred</span><span class="p">))</span>&#x000A;</div><div class='line' id='LC122'>    <span class="n">l1_error_u</span> <span class="o">=</span> <span class="n">np</span><span class="p">.</span><span class="n">mean</span><span class="p">(</span><span class="n">np</span><span class="p">.</span><span class="nb">abs</span><span class="p">(</span><span class="n">label</span><span class="p">[...,</span> <span class="mi">0</span><span class="p">]</span> <span class="o">-</span> <span class="n">pred</span><span class="p">[...,</span> <span class="mi">0</span><span class="p">]))</span>&#x000A;</div><div class='line' id='LC123'>    <span class="n">l1_error_v</span> <span class="o">=</span> <span class="n">np</span><span class="p">.</span><span class="n">mean</span><span class="p">(</span><span class="n">np</span><span class="p">.</span><span class="nb">abs</span><span class="p">(</span><span class="n">label</span><span class="p">[...,</span> <span class="mi">1</span><span class="p">]</span> <span class="o">-</span> <span class="n">pred</span><span class="p">[...,</span> <span class="mi">1</span><span class="p">]))</span>&#x000A;</div><div class='line' id='LC124'>    <span class="n">l1_error_p</span> <span class="o">=</span> <span class="n">np</span><span class="p">.</span><span class="n">mean</span><span class="p">(</span><span class="n">np</span><span class="p">.</span><span class="nb">abs</span><span class="p">(</span><span class="n">label</span><span class="p">[...,</span> <span class="mi">2</span><span class="p">]</span> <span class="o">-</span> <span class="n">pred</span><span class="p">[...,</span> <span class="mi">2</span><span class="p">]))</span>&#x000A;</div><div class='line' id='LC125'>    <span class="n">cp_error</span> <span class="o">=</span> <span class="n">np</span><span class="p">.</span><span class="n">mean</span><span class="p">(</span><span class="n">np</span><span class="p">.</span><span class="nb">abs</span><span class="p">(</span><span class="n">label</span><span class="p">[...,</span> <span class="mi">2</span><span class="p">][</span><span class="mi">0</span><span class="p">,</span> <span class="mi">0</span><span class="p">,</span> <span class="p">:]</span> <span class="o">-</span> <span class="n">pred</span><span class="p">[...,</span> <span class="mi">2</span><span class="p">][</span><span class="mi">0</span><span class="p">,</span> <span class="mi">0</span><span class="p">,</span> <span class="p">:]))</span>&#x000A;</div><div class='line' id='LC126'>    <span class="k">return</span> <span class="n">l1_error</span><span class="p">,</span> <span class="n">l1_error_u</span><span class="p">,</span> <span class="n">l1_error_v</span><span class="p">,</span> <span class="n">l1_error_p</span><span class="p">,</span> <span class="n">cp_error</span>&#x000A;</div><div class='line' id='LC127'>&#x000A;</div><div class='line' id='LC128'>&#x000A;</div><div class='line' id='LC129'><span class="k">def</span> <span class="nf">calculate_max_error</span><span class="p">(</span><span class="n">label</span><span class="p">,</span> <span class="n">pred</span><span class="p">):</span>&#x000A;</div><div class='line' id='LC130'>    <span class="s">"""calculate max l1 error"""</span>&#x000A;</div><div class='line' id='LC131'>    <span class="n">l1_error</span> <span class="o">=</span> <span class="n">np</span><span class="p">.</span><span class="nb">max</span><span class="p">(</span><span class="n">np</span><span class="p">.</span><span class="nb">max</span><span class="p">(</span><span class="n">np</span><span class="p">.</span><span class="nb">abs</span><span class="p">(</span><span class="n">label</span> <span class="o">-</span> <span class="n">pred</span><span class="p">),</span> <span class="n">axis</span><span class="o">=</span><span class="mi">1</span><span class="p">),</span> <span class="n">axis</span><span class="o">=</span><span class="mi">1</span><span class="p">)</span>&#x000A;</div><div class='line' id='LC132'>    <span class="n">l1_error_avg</span> <span class="o">=</span> <span class="n">np</span><span class="p">.</span><span class="n">mean</span><span class="p">(</span><span class="n">l1_error</span><span class="p">,</span> <span class="n">axis</span><span class="o">=</span><span class="mi">1</span><span class="p">).</span><span class="n">tolist</span><span class="p">()</span>&#x000A;</div><div class='line' id='LC133'>    <span class="n">l1_error_u</span> <span class="o">=</span> <span class="n">l1_error</span><span class="p">[:,</span> <span class="mi">0</span><span class="p">].</span><span class="n">tolist</span><span class="p">()</span>&#x000A;</div><div class='line' id='LC134'>    <span class="n">l1_error_v</span> <span class="o">=</span> <span class="n">l1_error</span><span class="p">[:,</span> <span class="mi">1</span><span class="p">].</span><span class="n">tolist</span><span class="p">()</span>&#x000A;</div><div class='line' id='LC135'>    <span class="n">l1_error_p</span> <span class="o">=</span> <span class="n">l1_error</span><span class="p">[:,</span> <span class="mi">2</span><span class="p">].</span><span class="n">tolist</span><span class="p">()</span>&#x000A;</div><div class='line' id='LC136'>    <span class="n">cp_error</span> <span class="o">=</span> <span class="n">np</span><span class="p">.</span><span class="nb">max</span><span class="p">(</span><span class="n">np</span><span class="p">.</span><span class="nb">abs</span><span class="p">(</span><span class="n">label</span><span class="p">[...,</span> <span class="mi">2</span><span class="p">][:,</span> <span class="mi">0</span><span class="p">,</span> <span class="p">:]</span> <span class="o">-</span> <span class="n">pred</span><span class="p">[...,</span> <span class="mi">2</span><span class="p">][:,</span> <span class="mi">0</span><span class="p">,</span> <span class="p">:]),</span> <span class="n">axis</span><span class="o">=</span><span class="mi">1</span><span class="p">).</span><span class="n">tolist</span><span class="p">()</span>&#x000A;</div><div class='line' id='LC137'>    <span class="k">return</span> <span class="n">l1_error_avg</span><span class="p">,</span> <span class="n">l1_error_u</span><span class="p">,</span> <span class="n">l1_error_v</span><span class="p">,</span> <span class="n">l1_error_p</span><span class="p">,</span> <span class="n">cp_error</span>&#x000A;</div><div class='line' id='LC138'>&#x000A;</div><div class='line' id='LC139'>&#x000A;</div><div class='line' id='LC140'><span class="k">def</span> <span class="nf">save_label_and_pred</span><span class="p">(</span><span class="n">label</span><span class="p">,</span> <span class="n">pred</span><span class="p">,</span> <span class="n">save_img_dir</span><span class="p">):</span>&#x000A;</div><div class='line' id='LC141'>    <span class="s">"""save abel and pred"""</span>&#x000A;</div><div class='line' id='LC142'>    <span class="n">save_dir</span> <span class="o">=</span> <span class="n">os</span><span class="p">.</span><span class="n">path</span><span class="p">.</span><span class="n">join</span><span class="p">(</span><span class="n">save_img_dir</span><span class="p">,</span> <span class="s">'label_pred'</span><span class="p">)</span>&#x000A;</div><div class='line' id='LC143'>    <span class="k">print</span><span class="p">(</span><span class="sa">f</span><span class="s">'label_and_pred: </span><span class="si">{</span><span class="n">save_dir</span><span class="si">}</span><span class="s">'</span><span class="p">)</span>&#x000A;</div><div class='line' id='LC144'>    <span class="n">check_file_path</span><span class="p">(</span><span class="n">save_dir</span><span class="p">)</span>&#x000A;</div><div class='line' id='LC145'>    <span class="n">label</span> <span class="o">=</span> <span class="n">unpatchify</span><span class="p">(</span><span class="n">label</span><span class="p">)</span>&#x000A;</div><div class='line' id='LC146'>    <span class="n">pred</span> <span class="o">=</span> <span class="n">unpatchify</span><span class="p">(</span><span class="n">pred</span><span class="p">)</span>&#x000A;</div><div class='line' id='LC147'>    <span class="n">np</span><span class="p">.</span><span class="n">save</span><span class="p">(</span><span class="n">os</span><span class="p">.</span><span class="n">path</span><span class="p">.</span><span class="n">join</span><span class="p">(</span><span class="n">save_dir</span><span class="p">,</span> <span class="s">'label_list'</span><span class="p">),</span> <span class="n">label</span><span class="p">.</span><span class="n">asnumpy</span><span class="p">())</span>&#x000A;</div><div class='line' id='LC148'>    <span class="n">np</span><span class="p">.</span><span class="n">save</span><span class="p">(</span><span class="n">os</span><span class="p">.</span><span class="n">path</span><span class="p">.</span><span class="n">join</span><span class="p">(</span><span class="n">save_dir</span><span class="p">,</span> <span class="s">'ViT'</span><span class="p">),</span> <span class="n">pred</span><span class="p">.</span><span class="n">asnumpy</span><span class="p">())</span>&#x000A;</div><div class='line' id='LC149'>&#x000A;</div><div class='line' id='LC150'>&#x000A;</div><div class='line' id='LC151'><span class="k">def</span> <span class="nf">get_label_and_pred</span><span class="p">(</span><span class="n">data</span><span class="p">,</span> <span class="n">model</span><span class="p">):</span>&#x000A;</div><div class='line' id='LC152'>    <span class="s">"""get abel and pred"""</span>&#x000A;</div><div class='line' id='LC153'>    <span class="n">labels</span> <span class="o">=</span> <span class="n">data</span><span class="p">[</span><span class="s">"labels"</span><span class="p">]</span>&#x000A;</div><div class='line' id='LC154'>    <span class="n">pred</span> <span class="o">=</span> <span class="n">model</span><span class="p">(</span><span class="n">data</span><span class="p">[</span><span class="s">'inputs'</span><span class="p">])</span>&#x000A;</div><div class='line' id='LC155'>    <span class="n">pred</span> <span class="o">=</span> <span class="n">unpatchify</span><span class="p">(</span><span class="n">pred</span><span class="p">)</span>&#x000A;</div><div class='line' id='LC156'>    <span class="n">label</span> <span class="o">=</span> <span class="n">unpatchify</span><span class="p">(</span><span class="n">labels</span><span class="p">)</span>&#x000A;</div><div class='line' id='LC157'>    <span class="k">return</span> <span class="n">label</span><span class="p">.</span><span class="n">asnumpy</span><span class="p">(),</span> <span class="n">pred</span><span class="p">.</span><span class="n">asnumpy</span><span class="p">()</span>&#x000A;</div></pre><div class="markdown-code-block-copy-btn"></div></div></div>
</div>
<script>
  window.Gitee.initReadmeCatalog();
  toMathMlCode('','markdown-body');
  $('.file_content a, .catalog-li a.anchor').click(function () {
    var anchor = $(this).attr('href')
    window.location.hash = anchor
  })
</script>

</div>
</div>
<div class='tree_progress'></div>
<div class='ui small modal' id='modal-linejump'>
<div class='ui custom form content'>
<div class='field'>
<div class='ui right action input'>
<input placeholder='跳转至某一行...' type='number'>
<div class='ui orange button'>
跳转
</div>
</div>
</div>
</div>
</div>

<div class='complaint'>
<div class='ui modal small form' id='landing-comments-complaint-modal'>
<i class='iconfont icon-close close'></i>
<div class='header'>
举报
</div>
<div class='content'>
<div class='appeal-success-tip hide'>
<i class='iconfont icon-ic_msg_success'></i>
<div class='appeal-success-text'>
举报成功
</div>
<span>
我们将于2个工作日内通过站内信反馈结果给你！
</span>
</div>
<div class='appeal-tip'>
请认真填写举报原因，尽可能描述详细。
</div>
<div class='ui form appeal-form'>
<div class='inline field'>
<label class='left-part appeal-type-wrap'>
举报类型
</label>
<div class='ui dropdown selection' id='appeal-comments-types'>
<div class='text default'>
请选择举报类型
</div>
<i class='dropdown icon'></i>
<div class='menu'></div>
</div>
</div>
<div class='inline field'>
<label class='left-part'>
举报原因
</label>
<textarea class='appeal-reason' id='appeal-comment-reason' name='msg' placeholder='请说明举报原因' rows='3'></textarea>
</div>
<div class='ui message callback-msg hide'></div>
<div class='ui small error text message exceeded-size-tip'></div>
</div>
</div>
<div class='actions'>
<div class='ui button blank cancel'>
取消
</div>
<div class='ui orange icon button disabled ok' id='complaint-comment-confirm'>
发送
</div>
</div>
</div>
<script>
  var $complaintCommentsModal = $('#landing-comments-complaint-modal'),
      $complainCommentType = $complaintCommentsModal.find('#appeal-comments-types'),
      $complaintModalTip = $complaintCommentsModal.find('.callback-msg'),
      $complaintCommentsContent = $complaintCommentsModal.find('.appeal-reason'),
      $complaintCommentBtn = $complaintCommentsModal.find('#complaint-comment-confirm'),
      complaintSending = false,
      initedCommentsType = false;
  
  function initCommentsTypeList() {
    if (!initedCommentsType) {
      $.ajax({
        url: "/appeals/fetch_types",
        method: 'get',
        data: {'type': 'comment'},
        success: function (data) {
          var result = '';
          for (var i = 0; i < data.length; i++) {
            result = result + "<div class='item' data-value='" + data[i].id + "'>" + data[i].name + "</div>";
          }
          $complainCommentType.find('.menu').html(result);
        }
      });
      $complainCommentType.dropdown({showOnFocus: false});
      initedCommentsType = true;
    }
  }
  $complainCommentType.on('click', function() {
    $complaintCommentsModal.modal({
      autofocus: false,
      onApprove: function() {
        return false;
      },
      onHidden: function() {
        restoreCommonentDefault();
      }
    }).modal('show');
  });
  
  $complaintCommentsContent.on('change keyup', function(e) {
    var content = $(this).val();
    if ($.trim(content).length > 0 && $complainCommentType.dropdown('get value').length > 0 ) {
      $complaintCommentBtn.removeClass('disabled');
      return;
    }
    $complaintCommentBtn.addClass('disabled');
  });
  
  
  $complainCommentType.dropdown({
    showOnFocus: false,
    onChange: function(value, text, $selectedItem) {
      if (value.length > 0 && $.trim($complaintCommentsContent.val()).length > 0) {
        $complaintCommentBtn.removeClass('disabled');
        return
      }
      $complaintCommentBtn.addClass('disabled');
    }
  });
  
  function restoreCommonentDefault() {
    $complainCommentType.dropdown('restore defaults');
    $complaintCommentsContent.val('');
    $('.exceeded-size-tip').text('').hide();
    $complaintModalTip.text('').hide();
    setTimeout(function() {
      setCommentSendTip(false);
    }, 1500);
  }
  
  $complaintCommentBtn.on('click',function(e){
    var reason = $complaintCommentsContent.val();
    var appealableId = $('#landing-comments-complaint-modal').attr('data-id');
    if (complaintSending) {
      return;
    }
    var appealType = $complainCommentType.dropdown('get value');
    var formData = new FormData();
    formData.append('appeal_type_id', appealType);
    formData.append('reason', reason);
    formData.append('appeal_type','Note');
    formData.append('target_id',appealableId);
    $.ajax({
      type: 'POST',
      url: "/appeals",
      cache: false,
      contentType: false,
      processData: false,
      data: formData,
      beforeSend: function() {
        setCommentSendStatus(true);
      },
      success: function(res) {
        if (res.status == 200) {
          setCommentSendTip(true);
          setTimeout(function() {
            $complaintCommentsModal.modal('hide');
            restoreCommonentDefault();
          }, 3000);
        }
        setCommentSendStatus(false);
      },
      error: function(err) {
        showCommonTips(err.responseJSON.message, 'error');
        setCommentSendStatus(false);
      }
    })
  });
  
  function showCommonTips(text, type) {
    $complaintModalTip.text(text).show();
    if (type == 'error') {
      $complaintModalTip.removeClass('success').addClass('error');
    } else {
      $complaintModalTip.removeClass('error').addClass('success');
    }
  }
  
  function setCommentSendStatus(value) {
    complaintSending = value;
    if (complaintSending) {
      $complaintCommentBtn.addClass('loading');
      $complaintCommentsContent.attr('readonly', true);
      $complainCommentType.attr('readonly', true);
    } else {
      $complaintCommentBtn.removeClass('loading');
      $complaintCommentsContent.attr('readonly', false);
      $complainCommentType.attr('readonly', false);
    }
  }
  
  function setCommentSendTip(value) {
    if (value) {
      $('.appeal-success-tip').removeClass('hide');
      $('.appeal-tip').addClass('hide');
      $('.appeal-form').addClass('hide');
      $('#landing-comments-complaint-modal .actions').addClass('hide');
    } else {
      $('.appeal-success-tip').addClass('hide');
      $('.appeal-tip').removeClass('hide');
      $('.appeal-form').removeClass('hide');
      $('#landing-comments-complaint-modal .actions').removeClass('hide');
    }
  }
</script>

<div class='ui small modal' id='misjudgment_appeal_modal'>
<i class='close icon'></i>
<div class='header dividing ui'>
误判申诉
</div>
<div class='content'>
<p>此处可能存在不合适展示的内容，页面不予展示。您可通过相关编辑功能自查并修改。</p>
<p>如您确认内容无涉及 不当用语 / 纯广告导流 / 暴力 / 低俗色情 / 侵权 / 盗版 / 虚假 / 无价值内容或违法国家有关法律法规的内容，可点击提交进行申诉，我们将尽快为您处理。</p>
<div class='buttons'>
<div class='ui button blank cancel'>取消</div>
<div class='ui button orange submit'>提交</div>
</div>
</div>
</div>
<style>
  #misjudgment_appeal_modal .buttons {
    float: right;
    margin-top: 30px;
    margin-bottom: 20px; }
    #misjudgment_appeal_modal .buttons .cancel {
      margin-right: 20px; }
</style>
<script>
  var $misjudgmentAppealModal = $('#misjudgment_appeal_modal');
  $('.cancel').on('click',function(){
    $misjudgmentAppealModal.modal('hide');
  });
  var $jsSubmitAppeal = $misjudgmentAppealModal.find('.submit')
  $jsSubmitAppeal.on('click', function(e) {
    e.preventDefault();
    $(this).addClass('loading').addClass('disabled');
    var type = $(this).attr('data-type');
    var id = $(this).attr('data-id');
    var projectId = $(this).attr('data-project-id');
    var appealType = $(this).attr('data-appeal-type');
    $.ajax({
      type: "PUT",
      url: "/misjudgment_appeal",
      data: {
        type: type,
        id: id,
        project_id: projectId,
        appeal_type: appealType
      },
      success: function(data) {
        Flash.info('提交成功');
        $jsSubmitAppeal.removeClass('loading');
        $misjudgmentAppealModal.modal('hide');
        location.reload()
      },
      error: function(e) {
        Flash.error('提交失败:'+e.responseText);
        $jsSubmitAppeal.removeClass('loading').removeClass('disabled');
        location.reload()
      }
    });
  })
</script>

</div>
<script>
  "use strict";
  $('.js-check-star').checkbox('set unchecked')
</script>

</div>
</div>
</div>
<div class='four wide column' style='display: none;'>
<div class='project__right-side'>
<div class='side-item intro'>
<div class='header'>
<h4>简介</h4>
</div>
<div class='content'>
<span class='git-project-desc-text'>MindScience is scientific computing kits for various industries based on the converged MindSpore framework.</span>
<a class='hide spread' href='javascript:void(0);'>
展开
<i class='caret down icon'></i>
</a>
<a class='retract hide' href='javascript:void(0);'>
收起
<i class='caret up icon'></i>
</a>
<div class='intro-list'>
<div class='blank d-flex d-flex-between dropdown item js-project-label_show label-list-line-feed project-label-list ui' data-labels='[]' data-url='/mindspore/mindscience/update_description'>
<div class='mixed-label'>
</div>

<div class='default'>暂无标签</div>
</div>
<div class='item'>
<i class='iconfont icon-link'></i>
<span class='git-project-homepage'>
<a rel="nofollow" id="homepage" target="_blank" href="https://www.mindspore.cn/mindscience">https://www.mindspore.cn/mindscience</a>
</span>
</div>
<div class='item'>
<i class='iconfont icon-tag-program'></i>
<span class='summary-languages'>
Jupyter Notebook
<span class='text-muted'>
等 6 种语言
<i class='icon dropdown'></i>
</span>
</span>
<div class='ui popup summary-languages-popup'>
<div class='row'>
<div class='lang'>
<a href="/explore/all?lang=Jupyter+Notebook">Jupyter Notebook</a>
</div>
<div class='lang-bar'>
<div class='bar' style='width: 46.7%;'></div>
</div>
<a class="percentage" href="/explore/all?lang=Jupyter+Notebook">46.7%</a>
</div>
<div class='row'>
<div class='lang'>
<a href="/explore/all?lang=Python">Python</a>
</div>
<div class='lang-bar'>
<div class='bar' style='width: 46.6%;'></div>
</div>
<a class="percentage" href="/explore/all?lang=Python">46.6%</a>
</div>
<div class='row'>
<div class='lang'>
<a href="/explore/all?lang=Cuda">Cuda</a>
</div>
<div class='lang-bar'>
<div class='bar' style='width: 5.2%;'></div>
</div>
<a class="percentage" href="/explore/all?lang=Cuda">5.2%</a>
</div>
<div class='row'>
<div class='lang'>
<a href="/explore/all?lang=C%2B%2B">C++</a>
</div>
<div class='lang-bar'>
<div class='bar' style='width: 0.7%;'></div>
</div>
<a class="percentage" href="/explore/all?lang=C%2B%2B">0.7%</a>
</div>
<div class='row'>
<div class='lang'>
<a href="/explore/all?lang=Shell">Shell</a>
</div>
<div class='lang-bar'>
<div class='bar' style='width: 0.4%;'></div>
</div>
<a class="percentage" href="/explore/all?lang=Shell">0.4%</a>
</div>
<div class='row'>
<div class='lang'>
<a href="/explore/all?lang=Other">Other</a>
</div>
<div class='lang-bar'>
<div class='bar' style='width: 0.4%;'></div>
</div>
<a class="percentage" href="/explore/all?lang=Other">0.4%</a>
</div>
</div>
</div>

<div class='item'>
<i class='iconfont icon-licence'></i>
<a target="_blank" id="license-popup" href="/mindspore/mindscience/blob/master/LICENSE">Apache-2.0</a>
<div class='ui popup dark'>使用 Apache-2.0 开源许可协议</div>
</div>
</div>
</div>
<div class='content intro-form'>
<div class='ui small input'>
<textarea name='project[description]' placeholder='描述' rows='5'></textarea>
</div>
<div class='ui small input'>
<input data-regex-value='(^$)|(^(http|https):\/\/(([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.){3}([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5]).*)|(^(http|https):\/\/[a-zA-Z0-9]+([_\-\.]{1}[a-zA-Z0-9]+)*\.[a-zA-Z]{2,10}(:[0-9]{1,10})?(\?.*)?(\/.*)?$)' name='project[homepage]' placeholder='主页(eg: https://gitee.com)' type='text'>
</div>
<button class='ui orange button mt-1 btn-save'>
保存更改
</button>
<div class='ui blank button btn-cancel-edit'>
取消
</div>
</div>
</div>
<div class='side-item release'>
<div class='header'>
<h4>
发行版
<span class='text-muted'>
(1)
</span>
</h4>
<a class="ui link button pull-right" href="/mindspore/mindscience/releases">全部</a>
</div>
<div class='content ml-3'>
<i class='iconfont icon-release'></i>
<div class='desc'>
<a href="/mindspore/mindscience/releases/tag/v0.1.0-rc1">Release 0.1.0-rc1</a>
</div>
<span class='timeago' datetime='2021-09-26 09:21' title='2021-09-26 09:21:29 +0800'></span>
</div>
</div>
<div class='side-item radar'>
<div class='header mb-1'>
<h4 class='limit-length'>mindscience</h4>
<a class="ui link button radar-qa" href="javascript:void(0);"><i class='iconfont icon-help-circle'></i>
</a></div>
<div class='content'>
<div data-url='/mindspore/mindscience/project_radars' id='metrics-radar'>
<div class='wrap skeleton'>
<div class='total-score hide'>
<div class='text'></div>
<div class='score'></div>
</div>
</div>
<div class='ui popup radar-popup'>
<h4 class='title'>Gitee 指数包含如下维度</h4>
<div class='project-radar-list'>
<div class='descript-contianer'>
<div class='descript-title'>
<p>代码活跃度</p>
<p>社区活跃度</p>
<p>团队健康</p>
<p>流行趋势</p>
<p>影响力</p>
</div>
<div class='descript'>
<p>：与代码提交频次相关</p>
<p>：与项目和用户的issue、pr互动相关</p>
<p>：与团队成员人数和稳定度相关</p>
<p>：与项目近期受关注度相关</p>
<p>：与项目的star、下载量等社交指标相关</p>
</div>
</div>
</div>
<div class='finaltime'></div>
</div>
</div>
<script src="https://cn-assets.gitee.com/assets/skill_radar/rep_app-145010700aea13172f33e6c1c7df08c2.js"></script>

</div>
</div>
<div class='side-item contrib' data-url='/mindspore/mindscience/contributors_count?ref=master' id='contributor'>
<div class='header'>
<h4>
贡献者
<span class='text-muted' id='contributor-count'></span>
</h4>
<a class="ui link button pull-right" href="/mindspore/mindscience/contributors?ref=master">全部</a>
</div>
<div class='content' id='contributor-list'></div>
<div class='ui active centered inline loader' id='contributor-loader'></div>
</div>
<div class='side-item events' data-url='/mindspore/mindscience/events.json' id='proj-events'>
<div class='header'>
<h4>近期动态</h4>
</div>
<div class='content'>
<div class='ui comments' id='event-list'></div>
<a class="loadmore hide" href="javascript:void(0);">加载更多
<i class='icon dropdown'></i>
</a><center>
<div class='text-muted nomore hide'>不能加载更多了</div>
<div class='ui inline loader active'></div>
</center>
</div>
</div>
</div>
<div class='ui modal tiny' id='edit-project-description'>
<i class='iconfont icon-close close'></i>
<div class='header'>编辑仓库简介</div>
<div class='content'>
<div class='item mb-2'>
<div class='title label'>简介内容</div>
<div class='ui small input'>
<textarea maxlength='200' name='project[description]' placeholder='描述' rows='5'>MindScience is scientific computing kits for various industries based on the converged MindSpore framework.</textarea>
</div>
</div>
<div class='item mb-2'>
<div class='title label'>主页</div>
<div class='ui small input'>
<input data-regex-value='(^$)|(^(http|https):\/\/(([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.){3}([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5]).*)|(^(http|https):\/\/[a-zA-Z0-9]+([_\-\.]{1}[a-zA-Z0-9]+)*\.[a-zA-Z]{2,10}(:[0-9]{1,10})?(\?.*)?(\/.*)?$)' name='project[homepage]' placeholder='主页(eg: https://gitee.com)' type='text' value='https://www.mindspore.cn/mindscience'>
</div>
</div>
</div>
<div class='actions'>
<button class='ui button blank cancel'>取消</button>
<button class='ui button orange btn-save'>保存更改</button>
</div>
</div>

<script>
  window.gon.projectRightSide = {
    homepage: "https://www.mindspore.cn/mindscience",
    description: "MindScience is scientific computing kits for various industries based on the converged MindSpore framework.",
    url: '/mindspore/mindscience/update_description',
    i18n: {
      invalidHomepage: '不是有效的 http 地址',
      descriptionLimitExceeded: '简介长度不得超过%{limit}个字符',
      noDescription: '暂无描述',
      noPermission: '无权限操作！',
      requestError: '修改发生错误，请稍后重试！'
    }
  }
  window.gon.cloneArrSelectedLabel = [] || []
  $(function () {
    var $editModal = $('#edit-project-description')
    $editModal.modal({
      onShow: function () {
        window.globalUtils.getFocus($editModal.find('textarea'))
      }
    })
    $('.project__right-side').on('click', '.header .btn-edit', function () {
      $editModal.modal('show')
    })
    $('#license-popup').popup({ position: 'bottom center', lastResort: 'bottom center' })
  
    $('.js-project-label_show').projectLabel({
      i18n: {
        empty: "标签名不能为空",
        verify: "标签名只允许包含中文、字母、数字或者中划线(-)，不能以中划线开头，且长度少于35个字符",
        max: "最多选择 5 个标签"
      }
    })
  })
</script>

</div>
</div>
</div>
<script>
  (function() {
    $(function() {
      Tree.init();
      return TreeCommentActions.init();
    });
  
  }).call(this);
</script>

</div>
<script>
  (function() {
    var donateModal;
  
    Gitee.modalHelper = new GiteeModalHelper({
      alertText: '提示',
      okText: '确定'
    });
  
    donateModal = new ProjectDonateModal({
      el: '#project-donate-modal',
      alipayUrl: '/mindspore/mindscience/alipay',
      wepayUrl: '/mindspore/mindscience/wepay',
      nameIsBlank: '名称不能为空',
      nameTooLong: '名称过长（最多为 36 个字符）',
      modalHelper: Gitee.modalHelper
    });
  
    if (null === 'true') {
      donateModal.show();
    }
  
    $('#project-donate').on('click', function() {
      return donateModal.show();
    });
  
  }).call(this);
</script>
<script>
  Tree.initHighlightTheme('white')
</script>


</div>
<div class='gitee-project-extension'>
<div class='extension public'>1</div>
<div class='extension https'>https://gitee.com/mindspore/mindscience.git</div>
<div class='extension ssh'>git@gitee.com:mindspore/mindscience.git</div>
<div class='extension namespace'>mindspore</div>
<div class='extension repo'>mindscience</div>
<div class='extension name'>mindscience</div>
<div class='extension branch'>master</div>
</div>

<script>
  $(function() {
    GitLab.GfmAutoComplete.dataSource = "/mindspore/mindscience/autocomplete_sources"
    GitLab.GfmAutoComplete.Emoji.assetBase = '/assets/emoji'
    GitLab.GfmAutoComplete.setup();
  });
</script>

<footer id='git-footer-main'>
<div class='ui container'>
<div class='logo-row'>
<a href="https://gitee.com"><img alt='Gitee — 基于 Git 的代码托管和研发协作平台' class='logo-img' src='/static/images/logo-black.svg?t=158106666'>
</a></div>
<div class='name-important'>
深圳市奥思网络科技有限公司版权所有
</div>
<div class='ui two column grid d-flex-center'>
<div class='nine wide column git-footer-left'>
<div class='ui four column grid' id='footer-left'>
<div class='column'>
<div class='ui link list'>
<div class='item'>
<a class="item" href="/all-about-git">Git 大全</a>
</div>
<div class='item'>
<a class="item" rel="nofollow" href="https://oschina.gitee.io/learn-git-branching/">Git 命令学习</a>
</div>
<div class='item'>
<a class="item" rel="nofollow" href="https://copycat.gitee.com/">CopyCat 代码克隆检测</a>
</div>
<div class='item'>
<a class="item" href="/appclient">APP与插件下载</a>
</div>
</div>
</div>
<div class='column'>
<div class='ui link list'>
<div class='item'>
<a class="item" href="/gitee_reward">Gitee Reward</a>
</div>
<div class='item'>
<a class="item" href="/gitee-stars">Gitee 封面人物</a>
</div>
<div class='item'>
<a class="item" href="/gvp">GVP 项目</a>
</div>
<div class='item'>
<a class="item" rel="nofollow" href="https://blog.gitee.com/">Gitee 博客</a>
</div>
<div class='item'>
<a class="item" href="/enterprises#nonprofit-plan">Gitee 公益计划</a>
</div>
<div class='item'>
<a class="item" href="https://gitee.com/features/gitee-go">Gitee 持续集成</a>
</div>
</div>
</div>
<div class='column'>
<div class='ui link list'>
<div class='item'>
<a class="item" href="/api/v5/swagger">OpenAPI</a>
</div>
<div class='item'>
<a class="item" href="https://help.gitee.com">帮助文档</a>
</div>
<div class='item'>
<a class="item" href="/self_services">在线自助服务</a>
</div>
<div class='item'>
<a class="item" href="/help/articles/4378">更新日志</a>
</div>
</div>
</div>
<div class='column'>
<div class='ui link list'>
<div class='item'>
<a class="item" href="/about_us">关于我们</a>
</div>
<div class='item'>
<a class="item" rel="nofollow" href="https://www.oschina.net/news/131099/oschina-hiring">加入我们</a>
</div>
<div class='item'>
<a class="item" href="/terms">使用条款</a>
</div>
<div class='item'>
<a class="item" href="/oschina/git-osc/issues">意见建议</a>
</div>
<div class='item'>
<a class="item" href="/links.html">合作伙伴</a>
</div>
</div>
</div>
</div>
</div>
<div class='seven wide column right aligned followus git-footer-right'>
<div class='qrcode mini_app'>
<img alt="微信小程序" src="https://cn-assets.gitee.com/assets/mini_app-e5eee5a21c552b69ae6bf2cf87406b59.jpg" />
<p class='mini_app-text'>微信小程序</p>
</div>
<div class='qrcode weixin'>
<img alt="微信服务号" src="https://cn-assets.gitee.com/assets/qrcode-weixin-9e7cfb27165143d2b8e8b268a52ea822.jpg" />
<p class='weixin-text'>微信服务号</p>
</div>
<div class='phone-and-qq column'>
<div class='ui list official-support-container'>
<div class='item'>
<a class="icon-popup" title="点击加入 Gitee 官方群" rel="nofollow" href="//qm.qq.com/cgi-bin/qm/qr?k=FOdoYurYb10aXeAiViAgsqWX0fsgykNZ"><i class='iconfont icon-logo-qq'></i>
<span>官方技术交流QQ群：777320883</span>
</a></div>
<div class='item mail-and-zhihu'>
<a rel="nofollow" href="mailto: git@oschina.cn"><i class='iconfont icon-msg-mail'></i>
<span id='git-footer-email'>git#oschina.cn</span>
</a></div>
<div class='item mail-and-zhihu'>
<a target="_blank" rel="nofollow" href="https://www.zhihu.com/org/ma-yun-osc/"><i class='iconfont icon-zhihu'></i>
<span>Gitee</span>
</a></div>
<div class='item tel'>
<a>
<i class='iconfont icon-tel'></i>
<span>售前及售后使用咨询：400-606-0201</span>
</a>
</div>
</div>
</div>
</div>
</div>
</div>
<div class='bottombar'>
<div class='ui container'>
<div class='ui d-flex d-flex-between'>
<div class='seven wide column partner d-flex'>
<div class='open-atom d-flex-center'>
<img class="logo-openatom mr-1" alt="开放原子开源基金会" src="https://cn-assets.gitee.com/assets/logo-openatom-d083391cc8a54e283529f3fc11cc38ca.svg" />
<a target="_blank" rel="nofollow" href="https://www.openatom.org/">开放原子开源基金会</a>
<div class='sub-title ml-1'>合作代码托管平台</div>
</div>
<div class='report-12377 d-flex-center ml-3'>
<img class="report-12377__logo mr-1" alt="违法和不良信息举报中心" src="https://cn-assets.gitee.com/assets/12377@2x-1aa42ed2d2256f82a61ecf57be1ec244.png" />
<a target="_blank" rel="nofollow" href="https://12377.cn">违法和不良信息举报中心</a>
</div>
<div class='copyright ml-3'>
<a rel="nofollow" href="http://beian.miit.gov.cn/">粤ICP备12009483号</a>
</div>
</div>
<div class='nine wide column right aligned'>
<i class='icon world'></i>
<a href="/language/zh-CN">简 体</a>
/
<a href="/language/zh-TW">繁 體</a>
/
<a href="/language/en">English</a>
</div>
</div>
</div>
</div>
</footer>

<script>
  var officialEmail = $('#git-footer-email').text()
  $('#git-footer-main .icon-popup').popup({ position: 'bottom center' })
  $('#git-footer-email').text(officialEmail.replace('#', '@'))
  window.gon.popover_card_locale = {
    follow:"关注",
    unfollow:"已关注",
    gvp_title: "GVP - Gitee 最有价值开源项目",
    project: "项目",
    org: "开源组织",
    member: "",
    author: "作者",
    user_blocked: "该用户已被屏蔽或已注销",
    net_error: "网络错误",
    unknown_exception: "未知异常"
  }
  window.gon.select_message = {
    placeholder: "请输入个人空间地址或完整的邮箱地址"
  }
</script>
<script src="https://cn-assets.gitee.com/webpacks/popover_card-19f60a4dedc0294c145c.bundle.js"></script>
<link rel="stylesheet" media="all" href="https://cn-assets.gitee.com/webpacks/css/gitee_nps-69491f94919350b0258c.css" />
<script src="https://cn-assets.gitee.com/webpacks/gitee_nps-548cf00696f895086765.bundle.js"></script>
<script src="https://cn-assets.gitee.com/webpacks/gitee_icons-3cce3cb0d49977ab50c9.bundle.js"></script>


<div class='side-toolbar'>
<div class='button toolbar-help'>
<i class='iconfont icon-help'></i>
</div>
<div class='ui popup left center dark'>点此查找更多帮助</div>
<div class='toolbar-help-dialog'>
<div class='toolbar-dialog-header'>
<h3 class='toolbar-dialog-title'>搜索帮助</h3>
<form class="toolbar-help-search-form" action="/help/load_keywords_data" accept-charset="UTF-8" method="get"><input name="utf8" type="hidden" value="&#x2713;" />
<div class='ui icon input fluid toolbar-help-search'>
<input name='keywords' placeholder='请输入产品名称或问题' type='text'>
<i class='icon search'></i>
</div>
</form>

<i class='iconfont icon-close toolbar-dialog-close-icon'></i>
</div>
<div class='toolbar-dialog-content'>
<div class='toolbar-help-hot-search'>
<div class='toolbar-roll'>
<a class="init active" title="Git 命令在线学习" href="https://oschina.gitee.io/learn-git-branching/?utm_source==gitee-help-widget"><i class='Blue icon icon-command iconfont'></i>
<span>Git 命令在线学习</span>
</a><a class="init " title="如何在 Gitee 导入 GitHub 仓库" href="https://gitee.com/help/articles/4261?utm_source==gitee-help-widget"><i class='icon icon-clipboard iconfont orange'></i>
<span>如何在 Gitee 导入 GitHub 仓库</span>
</a></div>
<div class='toolbar-list'>
<div class='toolbar-list-item'>
<a href="/help/articles/4114">Git 仓库基础操作</a>
</div>
<div class='toolbar-list-item'>
<a href="/help/articles/4166">企业版和社区版功能对比</a>
</div>
<div class='toolbar-list-item'>
<a href="/help/articles/4191">SSH 公钥设置</a>
</div>
<div class='toolbar-list-item'>
<a href="/help/articles/4194">如何处理代码冲突</a>
</div>
<div class='toolbar-list-item'>
<a href="/help/articles/4232">仓库体积过大，如何减小？</a>
</div>
<div class='toolbar-list-item'>
<a href="/help/articles/4279">如何找回被删除的仓库数据</a>
</div>
<div class='toolbar-list-item'>
<a href="/help/articles/4283">Gitee 产品配额说明</a>
</div>
<div class='toolbar-list-item'>
<a href="/help/articles/4284">GitHub仓库快速导入Gitee及同步更新</a>
</div>
<div class='toolbar-list-item'>
<a href="/help/articles/4328">什么是 Release（发行版）</a>
</div>
<div class='toolbar-list-item'>
<a href="/help/articles/4354">将 PHP 项目自动发布到 packagist.org</a>
</div>
</div>
</div>
<div class='toolbar-help-search-reseult'></div>
</div>
</div>
<script>
  var opt = { position: 'left center'};
  var $helpSideToolbar = $('.button.toolbar-help');
  var $toolbarRoll = $('.toolbar-roll');
  
  $(function() {
    if (false) {
      $helpSideToolbar.popup(opt).popup({lastResort:'left center'})
    } else {
      $helpSideToolbar.popup({lastResort:'left center'}).popup('show', opt);
      setTimeout(function() {
        $helpSideToolbar.popup('hide', opt);
      }, 3000);
    }
  
    if ($toolbarRoll.length) {
      setInterval(function() {
        var $nextActiveLink = $toolbarRoll.find('a.active').next();
        if (!$nextActiveLink.length) {
          $nextActiveLink = $toolbarRoll.find('a:first-child');
        }
        $nextActiveLink.attr('class', 'active').siblings().removeClass('active init');
      }, 5000);
    }
  })
</script>

<div class='toolbar-appeal popup button'>
<i class='iconfont icon-report'></i>
</div>
<div class='ui popup dark'>
仓库举报
</div>
<script>
  $('.toolbar-appeal').popup({ position: 'left center' });
</script>

<div class='button gotop popup' id='gotop'>
<i class='iconfont icon-top'></i>
</div>
<div class='ui popup dark'>回到顶部</div>
</div>
<div class='form modal normal-modal tiny ui' id='unlanding-complaint-modal'>
<i class='iconfont icon-close close'></i>
<div class='header'>
登录提示
</div>
<div class='container actions'>
<div class='content'>
该操作需登录 Gitee 帐号，请先登录后再操作。
</div>
<div class='ui orange icon large button ok'>
立即登录
</div>
<div class='ui button blank cancel'>
没有帐号，去注册
</div>
</div>
</div>
<script>
  var $elm = $('.toolbar-appeal');
  
  $elm.on('click', function() {
    var modals = $("#unlanding-complaint-modal.normal-modal");
    if (modals.length > 1) {
      modals.eq(0).modal('show');
    } else {
      modals.modal('show');
    }
  })
  $("#unlanding-complaint-modal.normal-modal").modal({
    onDeny: function() {
      window.location.href = "/signup?from=";
    },
    onApprove: function() {
      window.location.href = "/login?from=";
    }
  })
</script>

<style>
  .side-toolbar .bdsharebuttonbox a {
    font-size: 24px;
    color: white !important;
    opacity: 0.9;
    margin: 6px 6px 0px 6px;
    background-image: none;
    text-indent: 0;
    height: auto;
    width: auto;
  }
</style>
<style>
  #udesk_btn a {
    margin: 0px 20px 167px 0px !important;
  }
</style>
<script>
  (function() {
    $('#project-user-message').popup({
      position: 'left center'
    });
  
  }).call(this);
</script>
<script>
  Gitee.initSideToolbar({})
</script>



<style>
  .gitee-stars-main-widget {
    display: none;
    position: fixed;
    left: 0;
    bottom: 0;
    z-index: 106; }
    .gitee-stars-main-widget .close-icon {
      width: 20px;
      right: 10px;
      position: absolute;
      top: 0px;
      cursor: pointer; }
    .gitee-stars-main-widget .people-image {
      width: 200px;
      margin: 0 10px; }
  
  .gitee-stars-main-widget.gitee-stars-widget .close-icon {
    left: 20px; }
</style>
<div class='gitee-stars-main-widget pendan-widget'>
<a target="_blank" href="https://gitee.com/activity/10th"><img class="people-image" src="https://foruda.gitee.com/images/1685018924243196209/10d9f8b4_4838521.png" alt="10d9f8b4 4838521" />
<img class="close-icon" src="https://foruda.gitee.com/images/1685018118186144692/8bde8327_4838521.png" alt="8bde8327 4838521" />
</a></div>
<script>
  $(function () {
    var $giteeStarsWidget = $('.gitee-stars-main-widget')
    var cookieKey = "visit-gitee--2023-05-25"
  
    if ($.cookie(cookieKey) == 1) {
      $giteeStarsWidget.hide()
    } else {
      $giteeStarsWidget.show()
    }
  
    $giteeStarsWidget.on('click', '.close-icon', function (e) {
      e.preventDefault()
      $.cookie(cookieKey, 1, {path: '/', expires: 60})
      $giteeStarsWidget.hide()
    })
  })
</script>


<script>
  (function() {
    this.__gac = {
      domain: 'www.oschina.net'
    };
  
  }).call(this);
</script>

<script src="https://cn-assets.gitee.com/assets/bdstatic/app-070a9e339ac82bf2bf7ef20375cd4121.js"></script>
<script src="https://cn-assets.gitee.com/webpacks/build_status-a3ee4cc8489b2defc1a8.bundle.js"></script>
<script src="https://cn-assets.gitee.com/webpacks/scan_status-ec5f3b73a17207658c98.bundle.js"></script>
<script src="https://cn-assets.gitee.com/webpacks/mermaid_render-80437a0d645e9044f9e8.bundle.js"></script>
</body>
</html>
