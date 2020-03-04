<style lang="scss">
    @import './sass/blogIndex';
</style>

<template>
  	<SubNavigationFrame title="工作日报" :breadcrumb="breadcrumbs" :hiddenBreadAndTitle="true" >
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
  			<Row :style="{marginTop:'.7rem'}">
  				<Col span="15">
  					<Card>
  						<p slot="title">留言板</p>
                		<Input type="textarea" :rows="5" :autosize="{minRows: 5,maxRows: 5}"></Input>
                		<Button type="primary" @click="test" :style="{margin: '.7rem 0'}" long>留言</Button>
                		<h4>留言列表</h4>
  					</Card>
  				</Col>
  				<Col span="8" offset="1">
  					<Card>
  						<p slot="title">网站信息</p>
                		<p>Content of card</p>
                		<p>Content of card</p>
                		<p>Content of card</p>
  					</Card>
  					<Card :style="{margin: '.7rem 0'}">
  						<p slot="title">友情链接</p>
                		<p>Content of card</p>
                		<p>Content of card</p>
                		<p>Content of card</p>
  					</Card>
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
			breadcrumbs: [
  	      		{title: '工作日报'}
  	  		],
  	  		//
  	  		CarouselIndex: 0,
  	  		//
  	  		CarouselData: [0, 1, 2, 3]
		}
	},
	components: {
		SubNavigationFrame
	},
	mounted () {
        this.$store.commit('showMenu', true);
	},
	methods: {
		test () {
			Action.testAxios()
			.then(res => {
				console.log(res);
			})
			.catch(err => {
				console.log(err);
			})
		}
	}
}
</script>