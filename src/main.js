// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue';
import vuex from 'vuex';
import store from './stores';
import App from './App';
import axios from 'axios';
import router from './router';
import VueAxios from 'vue-axios';

//引用iview库
import ViewUI from 'view-design';
import 'view-design/dist/styles/iview.css';
Vue.use(ViewUI);

//使用vuex管理状态
Vue.use(vuex);

//全局引用script
global.axios = axios;

Vue.config.productionTip = false;


/* eslint-disable no-new */
new Vue({
  el: '#app',
  router,
  store,
  components: { App },
  template: '<App/>'
})
