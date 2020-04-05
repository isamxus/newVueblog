<style lang="scss">
    @import './sass/SubNavigationFrame';
</style>

<template>
    <ContentFrame not-padding :hidden-footer="hiddenFooter" :hidden-navigation="hiddentNavigation">
        <div slot="content">
            <div class="sub-navigation-container" v-show="!hiddenBreadAndTitle">
                <Breadcrumb v-show="!hiddenBreadcrumb">
                    <BreadcrumbItem :to="$store.state.showAdminMenu ? '/adminDetailPage/paramsSettings' : '/'">首页</BreadcrumbItem>
                    <BreadcrumbItem :to="item.path" v-for="(item,index) in breadcrumb" :key="index">{{item.title}}</BreadcrumbItem>
                </Breadcrumb>
                <h2 v-show="!showTitle" class="sub-navigation-title">{{ title }}</h2>
                <slot name="navigation"></slot>
            </div>
            <div class="sub-navigation-content">
                <slot name="content"></slot>
            </div>
        </div>
    </ContentFrame>
</template>

<script>
import ContentFrame from '../ContentFrame/ContentFrame';
export default {
    props:{
        //地址路径
        breadcrumb:{
            type: Array
            ,default: () => {return []}
        }
        //标题
        ,title: String
        //隐藏脚部
        ,hiddenFooter:{
            type: Boolean
            ,default: false
        }
        //隐藏地址栏
        ,hiddenBreadcrumb:{
            type: Boolean
            ,default: false
        }
        //隐藏导航
        ,hiddentNavigation: {
            type: Boolean
            ,default: false
        },
        hiddenBreadAndTitle: {
        	type: Boolean
        	,default: false
        },
        showTitle: {
        	type: Boolean
        	,default: false
        }
    }
    ,components:{
        ContentFrame
    }
}
</script>