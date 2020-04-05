import Vue from 'vue'
import Router from 'vue-router'
//首页
const Index = () => import('../views/blogIndex/index');

//文章分类详情页
const articleCategory = () => import('../views/articleCategory/articleCategory');
const articleDetail = () => import('../views/articleCategory/articleDetail');

//后台管理登录页面
const blogAdmin = () => import('../views/blogAdmin/blogAdmin');
const blogRegister = () => import('../views/blogAdmin/blogRegister');

//后台管理页面
const adminDetailPage = () => import('../views/adminDetailPage/adminDetailPage');
const paramsSettings = () => import('../views/adminDetailPage/paramsSettings');
const paramsDetailPage = () => import('../views/adminDetailPage/paramsDetailPage');
const articleListPage = () => import('../views/adminDetailPage/articleListPage');
const addArticle = () => import('../views/adminDetailPage/addArticle');
const commentManagement = () => import('../views/adminDetailPage/commentManagement');
const usersManagement = () => import('../views/adminDetailPage/usersManagement');
const blogIndexTab = () => import('../views/adminDetailPage/blogIndexTab');


Vue.use(Router)

export default new Router({
  	routes: [
        {path:'/',name: 'Index',component: Index,meta:{title:'首页'}},
        {path:'/login',name: 'login',component: blogAdmin,meta:{title:'用户登录'}},
      	{path:'/register',name: 'register',component: blogRegister,meta:{title:'用户注册'}},
        {path:'/admin',name: 'blogAdmin',component: blogAdmin,meta:{title:'博客后台管理系统'}},
      	//{path:'/adminDetailPage',name: 'adminDetailPage',component: adminDetailPage,meta:{title:'首页视图管理'}},
      	{path:'/adminDetailPage/paramsSettings',name: 'paramsSettings',component: paramsSettings,meta:{title:'参数设置'}},
      	{path:'/adminDetailPage/paramsDetailPage',name: 'paramsDetailPage',component: paramsDetailPage,meta:{title:''}},
      	{path:'/adminDetailPage/articleListPage',name: 'articleListPage',component: articleListPage,meta:{title:''}},
      	{path:'/adminDetailPage/commentManagement',name: 'commentManagement',component: commentManagement,meta:{title:''}},
      	{path:'/adminDetailPage/usersManagement',name: 'usersManagement',component: usersManagement,meta:{title:''}},
      	{path:'/adminDetailPage/addArticle',name: 'addArticle',component: addArticle,meta:{title:''}},
      	{path:'/article/simplePage',name: 'articleCategory',component: articleCategory,meta:{title:'文章列表'}},
      	{path:'/article/detailPage',name: 'articleDetail',component: articleDetail,meta:{title:'文章详情'}},
        {path:'/article/blogIndexTab',name: 'blogIndexTab',component: blogIndexTab,meta:{title:'首页Tab'}},
    ]
})
