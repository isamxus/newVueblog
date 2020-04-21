import Vue from 'vue'
import Router from 'vue-router'
//首页
const Index = () => import('../views/blogIndex/index');

//文章分类详情页
const articleCategory = () => import('../views/articleCategory/articleCategory');
const articleDetail = () => import('../views/articleCategory/articleDetail');

//用户设置页面
const userSettings = () => import('../views/blogAdmin/userSettings');


//后台管理登录页面
const blogAdmin = () => import('../views/blogAdmin/blogAdmin');
const blogRegister = () => import('../views/blogAdmin/blogRegister');

//后台管理页面
const paramsSettings = () => import('../views/adminDetailPage/paramsSettings');
const paramsDetailPage = () => import('../views/adminDetailPage/paramsDetailPage');
const articleListPage = () => import('../views/adminDetailPage/articleListPage');
const addArticle = () => import('../views/adminDetailPage/addArticle');
const commentManagement = () => import('../views/adminDetailPage/commentManagement');
const usersManagement = () => import('../views/adminDetailPage/usersManagement');
const blogIndexTab = () => import('../views/adminDetailPage/blogIndexTab');
const blogIndexImage = () => import('../views/adminDetailPage/blogIndexImage');


Vue.use(Router)

const originalPush = Router.prototype.push;
Router.prototype.push = function push(location) {
  return originalPush.call(this, location).catch(err => err)
};



export default new Router({
  	routes: [
        {path:'/',name: 'Index',component: Index,meta:{title:'首页'}},
        {path:'/login',name: 'login',component: blogAdmin,meta:{title:'用户登录'}},
      	{path:'/register',name: 'register',component: blogRegister,meta:{title:'用户注册'}},
        {path:'/admin',name: 'blogAdmin',component: blogAdmin,meta:{title:'博客后台管理系统'}},
        {path:'/blogAdmin/userSettings',name: 'userSettings',component: userSettings,meta:{title:'修改用户信息'}},
      	{path:'/adminDetailPage/paramsSettings',name: 'paramsSettings',component: paramsSettings,meta:{title:'参数设置'}},
      	{path:'/adminDetailPage/paramsDetailPage',name: 'paramsDetailPage',component: paramsDetailPage,meta:{title:''}},
      	{path:'/adminDetailPage/articleListPage',name: 'articleListPage',component: articleListPage,meta:{title:''}},
      	{path:'/adminDetailPage/commentManagement',name: 'commentManagement',component: commentManagement,meta:{title:''}},
      	{path:'/adminDetailPage/usersManagement',name: 'usersManagement',component: usersManagement,meta:{title:''}},
      	{path:'/adminDetailPage/addArticle',name: 'addArticle',component: addArticle,meta:{title:''}},
        {path:'/adminDetailPage/blogIndexTab',name: 'blogIndexTab',component: blogIndexTab,meta:{title:'首页Tab'}},
        {path:'/adminDetailPage/blogIndexImage',name: 'blogIndexImage',component: blogIndexImage,meta:{title:'首页轮播图'}},

      	{path:'/article/simplePage',name: 'articleCategory',component: articleCategory,meta:{title:'文章列表'}},
      	{path:'/article/detailPage',name: 'articleDetail',component: articleDetail,meta:{title:'文章详情'}},
    ]
})
