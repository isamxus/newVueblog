<style lang="scss">
    @import './sass/ContentFrame';
</style>

<template>
	<div  :class="['frame-container', hiddenFooter && 'hidden-footer',notPadding && 'not-padding']"
        :style="{paddingTop: hiddentNavigation ? 0 : null}">
		<!-- 页导航 -->
		<ContentNavigationBar v-show="!hiddentNavigation">
            <slot name="title" slot="title" />
            <slot name="navigation" slot="navigation" />
        </ContentNavigationBar>

        <!--页面内容-->
        <slot name="content" />
        
        <!-- 页脚 -->
        <template v-if="!hiddenFooter">
            <slot name="footer">
                <div class="frame-container-footer">
                    <p class="label">Copyright © 2014-2018 天联数创网络科技有限公司技术支持</p>
                    <p class="label">粤ICP备16018901号</p>
                </div>
            </slot>
        </template>
	</div>
</template>

<script>

//引用组件
import ContentNavigationBar from './ContentNavigationBar'; 

export default {
    props:{
        title: String
        ,hiddenFooter:{
            type: Boolean
            ,default: false
        }
        ,notPadding:{
            type: Boolean
            ,default: false
        }
        ,hiddentNavigation: {
            type: Boolean
            ,default: false
        }
    }
    ,components:{
        ContentNavigationBar
    }
}
</script>
