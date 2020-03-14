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

//
axios.defaults.headers.post['Content-Type'] = 'application/x-www-form-urlencoded;charset=UTF-8';
//全局引用script
global.axios = axios;
global.REQUEST_URL = Urls;


const objectCopy = obj => {
   return JSON.parse(JSON.stringify(obj));
};

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


Vue.config.productionTip = false;
router.beforeEach((to, from, next) => {
	if (to.path.search('adminDetailPage') != -1) {
 		store.commit('showAdminMenu', true);
	} else {
		store.commit('showAdminMenu', false);
	}
	next();
})

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
