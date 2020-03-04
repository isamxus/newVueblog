import Vue from 'vue'
import Router from 'vue-router'
//首页
const Index = () => import('../views/blogIndex/index');

//后台管理登录页面
const blogAdmin = () => import('../views/blogAdmin/blogAdmin');

//后台管理页面
const adminDetailPage = () => import('../views/adminDetailPage/adminDetailPage');

Vue.use(Router)

export default new Router({
  	routes: [
      	{path:'/',name: 'Index',component: Index,meta:{title:'首页'}},
      	{path:'/admin',name: 'blogAdmin',component: blogAdmin,meta:{title:'后台管理登录'}},
      	{path:'/adminDetailPage',name: 'adminDetailPage',component: adminDetailPage,meta:{title:'后台管理登录'}}
  	]
})
