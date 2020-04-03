<style lang="scss">
    @import './sass/blogIndex';
</style>

<template>
  	<SubNavigationFrame :hiddenBreadAndTitle="true" >
  		<div class="blog-index-container" slot="content">
  			<Row :style="{background: '#fff'}">
  				<Col span="15">
  					<Carousel autoplay v-model="CarouselIndex" loop>
        				<CarouselItem v-for="(item, key) in CarouselData" :key="key">
            				<div class="carousel-image"></div>
        				</CarouselItem>
    				</Carousel>
  				</Col>
  				<Col span="9" :style="{padding: '.7rem'}"> 
  					<Tabs value="name1">
        				<TabPane label="最新文章" name="name1">标签一的内容</TabPane>
        				<TabPane label="归档" name="name2">标签二的内容</TabPane>
        				<TabPane label="公告" name="name3">标签三的内容</TabPane>
    				</Tabs>
  				</Col>
  			</Row>
  		</div>
	</SubNavigationFrame>
</template>

<script>
import SubNavigationFrame from '../../components/SubNavigationFrame/SubNavigationFrame';
import Action from './action/blogIndex';

export default {
	  data () {
		    return {
			      breadcrumbs: [],
  	        CarouselIndex: 0,
  	        CarouselData: [0, 1, 2, 3]
		    }
	  },
	  components: {
		    SubNavigationFrame
	  },
	  mounted () {
        this.$store.commit('showMenu', true);
        this.$store.commit('showAdminMenu', false);
        this.checkLoginStatusHandler();
	  },
	  methods: {
        checkLoginStatusHandler(){
            Action.getStatusInfo()
            .then(res => {
              
            })
            .catch(err => {
                this.$Message.error(err);
            })
        }
	  }
}
</script>