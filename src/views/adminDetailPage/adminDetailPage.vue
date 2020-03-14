<style lang="scss">
    @import './sass/adminDetailPage';
</style>

<template>
  	<SubNavigationFrame  :hiddenBreadAndTitle="true" >
  		  <div class="admin-detail-page-container" slot="content">
  	        <Card class="Card">
              <p slot="title">首页轮播图设置</p>
              
            </Card>
            <Card class="Card">
              <p slot="title">首页右侧滚动标签设置</p>
            </Card>
            <Card class="Card">
              <p slot="title">首页留言板管理</p>
            </Card>
            <Card class="Card">
              <p slot="title">首页网站信息设置</p>
            </Card>
            <Card class="Card">
              <p slot="title">首页友情链接设置</p>
            </Card>
  		  </div>
	  </SubNavigationFrame>
</template>

<script>
import SubNavigationFrame from '../../components/SubNavigationFrame/SubNavigationFrame';
import Action from './action/adminDetailPage';

export default {
    data () {
        return {

        }
    },
    components: {
        SubNavigationFrame
    },
    mounted () {
        //this.$store.state.showAdminMenu = true;
        //this.$store.commit('showMenu', false);
    }
}
</script>