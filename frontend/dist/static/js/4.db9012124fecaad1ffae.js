webpackJsonp([4],{"5q/2":function(e,t,o){"use strict";Object.defineProperty(t,"__esModule",{value:!0});var s=o("rVsN"),r=o.n(s),n={userCreate:function(e){var t=e.PostContent;return t.UserName?t.PassWord?t.PassWordConfirm?t.PassWordConfirm!=t.PassWord?r.a.reject({Msg:"两次输入的密码不一致",type:"local"}):axios.post(REQUEST_URL.userCreate,REQUEST_URL.handleParams(e)).then(function(e){return r.a.resolve(e.data.PostContent)}):r.a.reject({Msg:"请再次输入密码",type:"local"}):r.a.reject({Msg:"请输入密码",type:"local"}):r.a.reject({Msg:"请输入用户名",type:"local"})}},a={data:function(){return{loginForm:{UserName:"",PassWord:"",PassWordConfirm:""}}},mounted:function(){this.$store.commit("showMenu",!1)},methods:{createUserHandler:function(){var e=this;console.log(this.loginForm),n.userCreate({PostContent:this.loginForm}).then(function(t){e.$Message.success("注册成功，即将跳转至登录页面"),setTimeout(function(){e.$router.push({name:"login"})},2e3)}).catch(function(t){if("local"===t.type)return e.$Message.warning(t.Msg);e.$Message.error(t)})}}},l={render:function(){var e=this,t=e.$createElement,o=e._self._c||t;return o("div",{staticClass:"login-container"},[o("div",{staticClass:"login-form-contain"},[o("Row",[o("Col",{attrs:{span:"24"}},[o("h1",[e._v("用户注册")])])],1),e._v(" "),o("Form",{staticClass:"login-form"},[o("Row",[o("Col",{attrs:{span:"20",offset:"2"}},[o("FormItem",{attrs:{prop:"User"}},[o("Input",{attrs:{type:"text",placeholder:"请输入用户名称",size:"large"},model:{value:e.loginForm.UserName,callback:function(t){e.$set(e.loginForm,"UserName",t)},expression:"loginForm.UserName"}},[o("Icon",{attrs:{slot:"prepend",size:"24",type:"ios-person-outline"},slot:"prepend"})],1)],1)],1),e._v(" "),o("Col",{attrs:{span:"20",offset:"2"}},[o("FormItem",{attrs:{prop:"Password"}},[o("Input",{attrs:{type:"text",placeholder:"请输入你的密码",size:"large"},model:{value:e.loginForm.PassWord,callback:function(t){e.$set(e.loginForm,"PassWord",t)},expression:"loginForm.PassWord"}},[o("Icon",{attrs:{slot:"prepend",size:"24",type:"ios-lock-outline"},slot:"prepend"})],1)],1)],1),e._v(" "),o("Col",{attrs:{span:"20",offset:"2"}},[o("FormItem",{attrs:{prop:"Password"}},[o("Input",{attrs:{type:"text",placeholder:"请再次输入密码",size:"large"},model:{value:e.loginForm.PassWordConfirm,callback:function(t){e.$set(e.loginForm,"PassWordConfirm",t)},expression:"loginForm.PassWordConfirm"}},[o("Icon",{attrs:{slot:"prepend",size:"24",type:"ios-lock-outline"},slot:"prepend"})],1)],1)],1),e._v(" "),o("Col",{attrs:{span:"8",offset:"8"}},[o("FormItem",{attrs:{prop:"User"}},[o("Button",{attrs:{type:"primary",size:"large",long:""},on:{click:e.createUserHandler}},[e._v("确定")])],1)],1)],1),e._v(" "),o("Row",[o("Col",{attrs:{span:"8"}},[o("span",{style:{cursor:"pointer"},on:{click:function(t){return e.$router.push({name:"login"})}}},[e._v("<<<返回登陆页面")])])],1)],1)],1)])},staticRenderFns:[]};var i=o("C7Lr")(a,l,!1,function(e){o("H1/c")},"data-v-e797db10",null);t.default=i.exports},"H1/c":function(e,t){}});
//# sourceMappingURL=4.db9012124fecaad1ffae.js.map