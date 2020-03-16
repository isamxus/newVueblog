<template>
    <div id="app">
        <div class="page-container" :style="{left: !showMenu ? '0' : pageNavShrink ? '3.5rem' : '12rem'}">
            <!--<keep-alive :include="$store.state.keepAliveViews" :max="5">-->
                <router-view />
            <!--</keep-alive>-->
        </div>
        <div class="page-navigation" v-if="showMenu" :style="{width: pageNavShrink ? '3.5rem' : '12rem'}">
              <!--
                <div class="page-logo" :style="{display: 'flex',alignItems: 'center'}">
                    <img v-show="!pageNavShrink" class="nav-logo" :style="{height: '70%'}" src="./assets/logo.png">
                    <img v-show="pageNavShrink" class="nav-logo" src="./assets/logo.png">
                </div> -->  
        

            <!-- 左侧菜单栏目 -->
            <SidebarMenu 
                v-show="!pageNavShrink" 
                class="navigation" 
                theme="dark" 
                width="12rem" 
                :items="pages" 
                @item-click="menuItemClick"  />

            <!-- 左侧菜单栏目（收缩时） -->
            <SidebarMenuShrink  
                v-show="pageNavShrink" 
                class="navigation" 
                theme="dark" 
                width="3.5rem" 
                :items="pages" 
                @item-click="menuItemClick" />
        </div>
    </div>
</template>

<script>
//载入样式
import './common/sass/frame.scss';
//载入组件
import SidebarMenu from './components/SidebarMenu/SidebarMenu';
import SidebarMenuShrink from './components/SidebarMenu/SidebarMenuShrink';
import Action from './common/script/baseAction';

export default {
    name: 'App',
    data () {
        return {
            openNames:['sys_settiger'],
            //左侧菜单(博客前端页面)
            pageArray: [
                {title: '首页',icon:'ios-navigate',name:'Index',path:'/'},
                {
                    title: '文章分类'
                    ,icon:'ios-navigate'
                    ,name:'article_category'
                    ,children:[]
                },
                {
                    title: '关于作者'
                    ,icon:'ios-navigate'
                    ,name:'about_author'
                    ,children:[
                        {title: '技术文章',icon:'ios-navigate',name:'technology',path:'/'},
                    ]
                }
            ],

            //左侧菜单(博客管理页面)
            adminPageArray: [
                {title: '首页视图管理',icon:'ios-navigate',name:'adminDetailPage',path:'/adminDetailPage'},
                {title: '参数设置',icon:'ios-navigate',name:'paramsSettings',path:'/adminDetailPage/paramsSettings'},
            ]
        }
    },
    components: {
        SidebarMenu,
        SidebarMenuShrink
    },
    mounted () {
        //获取分类导航列表
        Action.paramsDetailGetList({
            PostContent: {
                filter: {
                    detailParentParamID: 4,
                    detailParentParamCode: '0001'
                }
            }
        })
        .then(res => {
            res.map((item, index) => {
                this.$set(this.pageArray[1].children, index, {
                    title: item.detailName,
                    icon: 'ios-navigate',
                    name: item.detailName,
                    path: `/article/technology?id=${item.id}`
                })
            })
            console.log(this.pageArray)
        })
        .catch(err => {
            this.$Message.error(err);
        })
    },
    computed: {
        pageNavShrink(){
            return this.$store.state.pageNavShrink;
        },
        showMenu(){
            return this.$store.state.showMenu;
        },
        pages () {
            return this.$store.state.showAdminMenu ? this.adminPageArray : this.pageArray;
        }
    },
    methods: {
        //左侧导航item被点击时处理函数
        menuItemClick(item, itemName){
            this.$router.push(item.path);
        }
    }
}
</script>


