webpackJsonp([14],{o8HC:function(e,t){},rv5y:function(e,t,n){"use strict";Object.defineProperty(t,"__esModule",{value:!0});var o=n("rVsN"),r=n.n(o),s={userGetPageList:function(e){return axios.post(REQUEST_URL.userGetPageList,REQUEST_URL.handleParams(e)).then(function(e){return r.a.resolve(e.data.PostContent)})},userUpdate:function(e){return axios.post(REQUEST_URL.userUpdate,REQUEST_URL.handleParams(e)).then(function(e){return r.a.resolve(e.data.PostContent)})},userDelete:function(e){return axios.post(REQUEST_URL.userDelete,REQUEST_URL.handleParams(e)).then(function(e){return r.a.resolve(e.data.PostContent)})}},a={name:"commentManagement",data:function(){return{breadcrumbs:[{title:this.$route.query.paramsName}],columns:[{title:"序号",type:"index",width:120},{title:"用户名",key:"UserName",width:120},{title:"创建时间",key:"CreateTime",width:220,render:this.TimeRender},{title:"操作",align:"center",render:this.toolColumnRender}],usersListData:[],PageCount:0,PageNumber:1,PageSize:10,popModal:!1,checkAllGroup:[],AuthList:[{title:"页面权限",children:[{Name:"博客首页",Code:"00",IsSelected:!1},{Name:"后台管理",Code:"01",IsSelected:!1}]},{title:"参数权限",children:[{Name:"文章分类",Code:"0001",IsSelected:!1},{Name:"文章设置",Code:"0002",IsSelected:!1},{Name:"文章标签",Code:"0003",IsSelected:!1},{Name:"文章评论",Code:"0004",IsSelected:!1},{Name:"用户管理",Code:"0005",IsSelected:!1},{Name:"首页Tab页",Code:"0006",IsSelected:!1}]}],allSelected:[],user_id:""}},components:{SubNavigationFrame:n("C7Kb").a},mounted:function(){this.$store.commit("showAdminMenu",!0),this.getUsersListHandler()},methods:{TimeRender:function(e,t){return e("span",{domProps:{innerText:new Date(t.row.CreateTime).Format("yyyy-MM-dd hh:mm")}})},getUsersListHandler:function(){var e=this;s.userGetPageList({PostContent:{_OrderBy:"-CreateTime",PageSize:this.PageSize,PageNumber:this.PageNumber}}).then(function(t){e.usersListData=t.Items.map(function(e){return e.CreateTime=new Date(e.CreateTime).Format("yyyy-MM-dd hh:mm"),e}),e.PageCount=t.TotalItems}).catch(function(t){e.$Message.error(t)})},toolColumnRender:function(e,t){var n=this;return e("div",[e("Button",{props:{type:"text"},domProps:{innerText:"编辑"},on:{click:function(e){n.popModal=!0,n.user_id=t.row.user_id;var o=t.row.Jurisdiction.split(",");n.AuthList=[{title:"页面权限",children:[{Name:"博客首页",Code:"00",IsSelected:!1},{Name:"后台管理",Code:"01",IsSelected:!1}]},{title:"参数权限",children:[{Name:"文章分类",Code:"0001",IsSelected:!1},{Name:"文章设置",Code:"0002",IsSelected:!1},{Name:"文章标签",Code:"0003",IsSelected:!1},{Name:"文章评论",Code:"0004",IsSelected:!1},{Name:"用户管理",Code:"0005",IsSelected:!1},{Name:"首页Tab页",Code:"0006",IsSelected:!1}]}];!function e(t){for(var n=function(n){if(t[n].children&&t[n].children.length>0)return e(t[n].children),"continue";-1!=o.findIndex(function(e){return e==t[n].Code})&&(t[n].IsSelected=!0)},r=0;r<t.length;r++)n(r)}(n.AuthList),e.stopPropagation()}}}),e("Button",{props:{type:"text"},domProps:{innerText:"删除"},on:{click:function(e){if(t.row.IsSuperUser)return n.$Message.warning("无法删除超级用户！！！");n.deleteUserHandler(t.row.user_id),e.stopPropagation()}}})])},deleteUserHandler:function(e){var t=this;if(!e)return this.$Message.warning("参数ID为空，无法删除！！！");this.$Modal.confirm({title:"操作确认",icon:"warning",content:"是否删除此用户",okText:"确定",showCancel:!0,loading:!0,onOk:function(){s.userDelete({PostContent:{user_id:e}}).then(function(e){t.$Message.success("成功删除用户！！！"),t.$Modal.remove(),t.getUsersListHandler()}).catch(function(e){t.$Modal.remove(),t.$Message.error(e)})}})},checkBoxselHandler:function(){var e=this,t=[];!function e(n){for(var o=0;o<n.length;o++)n[o].children&&n[o].children.length>0?e(n[o].children):n[o].IsSelected&&t.push(n[o].Code)}(this.AuthList),s.userUpdate({PostContent:{user_id:this.user_id,Jurisdiction:t.join(",")}}).then(function(t){e.getUsersListHandler(),e.popModal=!1}).catch(function(t){e.$Message.error(t)})}}},i={render:function(){var e=this,t=e.$createElement,n=e._self._c||t;return n("SubNavigationFrame",{attrs:{title:e.$route.query.paramsName,breadcrumb:e.breadcrumbs}},[n("div",{style:{textAlign:"right",marginTop:"-2.5rem"},attrs:{slot:"navigation"},slot:"navigation"},[n("Button",{on:{click:function(t){return e.$router.push({name:"Index"})}}},[e._v("返回主站")]),e._v(" "),n("Button",{on:{click:function(t){return e.$router.go(-1)}}},[e._v("返回")])],1),e._v(" "),n("div",{staticClass:"sub-page-container",style:{"margin-top":".5rem","padding-top":"1rem"},attrs:{slot:"content"},slot:"content"},[n("div",{style:{overflow:"auto"}},[n("Table",{attrs:{columns:e.columns,data:e.usersListData}})],1),e._v(" "),n("Page",{style:{paddingTop:"1rem",textAlign:"center"},attrs:{total:e.PageCount,current:e.PageNumber,"page-size":e.PageSize,placement:"top","show-elevator":"","show-total":"","show-sizer":""},on:{"on-change":function(t){e.PageNumber=t,e.getUsersListHandler()},"on-page-size-change":function(t){e.PageSize=t,e.getUsersListHandler()}}}),e._v(" "),n("Modal",{attrs:{title:"设置用户权限",width:"600"},model:{value:e.popModal,callback:function(t){e.popModal=t},expression:"popModal"}},[e._l(e.AuthList,function(t,o){return n("div",{key:o},[n("h4",[e._v(e._s(t.title))]),e._v(" "),n("div",{style:{padding:".7rem"}},e._l(t.children,function(t,o){return n("Checkbox",{key:o,model:{value:t.IsSelected,callback:function(n){e.$set(t,"IsSelected",n)},expression:"value.IsSelected"}},[e._v(e._s(t.Name))])}),1)])}),e._v(" "),n("div",{attrs:{slot:"footer"},slot:"footer"},[n("Button",{attrs:{type:"primary"},on:{click:e.checkBoxselHandler}},[e._v("确定")]),e._v(" "),n("Button",{on:{click:function(t){e.popModal=!1}}},[e._v("取消")])],1)],2)],1)])},staticRenderFns:[]};var l=n("C7Lr")(a,i,!1,function(e){n("o8HC")},null,null);t.default=l.exports}});
//# sourceMappingURL=14.93e44a3cf8817c926d12.js.map