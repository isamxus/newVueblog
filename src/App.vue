<template>
    <div id="app">
        <div class="page-container" :style="{left: !showMenu ? '0' : pageNavShrink ? '3.5rem' : '12rem'}">
            <keep-alive :include="$store.state.keepAliveViews" :max="5">
                <router-view />
            </keep-alive>
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

//左侧菜单
const pageArray = [
    {title: '首页',icon:'ios-navigate',name:'Index',path:'/'},
    {
        title: '文章分类'
        ,icon:'ios-navigate'
        ,name:'article_category'
        ,children:[
            {title: '技术文章',icon:'ios-navigate',name:'technology',path:'/'},
        ]
    },
    {
        title: '关于作者'
        ,icon:'ios-navigate'
        ,name:'about_author'
        ,children:[
            {title: '技术文章',icon:'ios-navigate',name:'technology',path:'/'},
        ]
    }
]

export default {
    name: 'App',
    data () {
        return {
            pages: [],
            openNames:['sys_settiger']
        }
    },
    components: {
        SidebarMenu,
        SidebarMenuShrink
    },
    mounted () {
        this.pages = pageArray;
    },
    computed: {
        pageNavShrink(){
            return this.$store.state.pageNavShrink;
        },
        showMenu(){
            return this.$store.state.showMenu;
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


