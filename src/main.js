// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue';
import vuex from 'vuex';
import store from './stores';
import App from './App';
import axios from 'axios';
import router from './router';
import VueAxios from 'vue-axios';
import { Urls } from './common/script/config';
import QS from 'qs';
import './common/sass/app.scss';


//引用iview库
import ViewUI from 'view-design';
import 'view-design/dist/styles/iview.css';
Vue.use(ViewUI);

//使用vuex管理状态
Vue.use(vuex);

//初始化富文本编辑器
import VueQuillEditor from 'vue-quill-editor';

// require styles
import 'quill/dist/quill.core.css'
import 'quill/dist/quill.snow.css'
import 'quill/dist/quill.bubble.css'

Vue.use(VueQuillEditor, {
    modules: {
        toolbar: [
            ['bold', 'italic', 'underline', 'strike'],
            ['blockquote', 'code-block'],
            [{ 'list': 'ordered' }, { 'list': 'bullet' }],
            [{ 'indent': '-1' }, { 'indent': '+1' }],
            [{ 'direction': 'rtl' }],
            [{ 'size': ['small', false, 'large', 'huge'] }],
            [{ 'header': [1, 2, 3, 4, 5, 6, false] }],
            [{ 'color': [] }, { 'background': [] }],
            [{ 'align': [] }],
            ['clean'],
            ['image']
        ]
    },
    placeholder: '请输入内容...'
});
//
axios.defaults.headers.post['Content-Type'] = 'application/x-www-form-urlencoded;charset=UTF-8';
//全局引用script
global.axios = axios;
global.REQUEST_URL = Urls;



axios.interceptors.response.use(response=>{

    if(response.data.status) return response;
    return Promise.reject(response.data.err);
},error=>{
    return Promise.reject(error);
});

const objectCopy = obj => {
   return JSON.parse(JSON.stringify(obj));
};
global.objectCopy = objectCopy;
//Qs处理axios Post请求
REQUEST_URL.handleParams = (params) => {
	if (params) params.PostContent = params.PostContent ? JSON.stringify(params.PostContent) : {};
	let now = new Date().getTime();
	let result = {
        RequestStamp: now
        ,PostTime: now
        ,Platform: 'PC Admin(Web)'
        ,CustomApp: 'PC Admin(Web)'
        ,Mac: 'unknown'
    };
    return params ? QS.stringify(Object.assign(result, objectCopy(params))) : QS.stringify(result);
}




Date.prototype.Format = function(format, timeCheck) {
    if(timeCheck !== false && this.getTime() < 1) return '';
    var o = {
        'M+': this.getMonth() + 1,
        'd+': this.getDate(),
        'h+': this.getHours(),
        'm+': this.getMinutes(),
        's+': this.getSeconds(),
        'q+': Math.floor((this.getMonth() + 3) / 3),
        'ms': this.getMilliseconds()
    };
    if(/(y+)/.test(format)) format = format.replace(RegExp.$1, (this.getFullYear() + '').substr(4 - RegExp.$1.length));
    for(var k in o)
        if(new RegExp('(' + k + ')').test(format)) format = format.replace(RegExp.$1, (RegExp.$1.length == 1) ? (o[k]) : (('00' + o[k]).substr(('' + o[k]).length)));
    return format;
}


/* eslint-disable no-new */
let vm = {};
ready();
function ready(){
    vm = new Vue({
        el: '#app'
        ,router
        ,store
        ,template: '<App/>'
        ,components:{App}
        ,data: {}
    });

    //设置REM
    document.body.onresize = function(){
        /**
            支持自适应式设置
            document.getElementsByTagName('html')[0].style.fontSize = (document.body.clientWidth / 100) * 6.25 + 'px';
        */
        document.getElementsByTagName('html')[0].style.fontSize = '20px';
    }
    document.body.onresize();
}


Vue.config.productionTip = false;
router.beforeEach((to, from, next) => {
    if (to.path.search('adminDetailPage') != -1) {
        if (store.state.UserInfo && !store.state.UserInfo[0].Jurisdiction.find(item => item == '01')){
            vm.$Modal.error({
                title: '警告',
                content: '用户无后台管理权限！！！',
                okText: '关闭'
            })
            return next({
                path: '/admin',
                query: {redirect: to.fullPath}
            })
        }
        store.commit('showAdminMenu', true);
        store.commit('showMenu', true);
    } else {
        store.commit('showAdminMenu', false);
        store.commit('showMenu', true);
    }
    next();
})