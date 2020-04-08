<style lang="scss">
    @import './sass/blogIndex';
</style>

<template>
  	<SubNavigationFrame :hiddenBreadAndTitle="true" >
  		<div class="blog-index-container" slot="content">
  			<Row :style="{background: '#fff'}">
  				<Col span="15">
  					<Carousel autoplay v-model="CarouselIndex" loop>
        				<CarouselItem v-for="(item, key) in IndexImageData" :key="key">
            				<div @click="$router.push({
                                name: 'articleDetail',
                                query: {
                                    id: item.ConnectArticleID
                                }
                            })" class="carousel-image" :style="{backgroundImage: `url('${item.IndexImageUrl}')`}">
                                      
                            </div>
        				</CarouselItem>
    				</Carousel>
  				</Col>
  				<Col span="9" :style="{padding: '.7rem'}"> 
  					 <Tabs :value="recentArtShow ? 'RecentlyArticle' : CustomTabList.length > 0 ? CustomTabList[0].IndexTabID : 'noTab'">
                <TabPane label="无" name="noTab" v-if="!recentArtShow && CustomTabList.length==0">
                    无
                </TabPane>
        				<TabPane v-if="recentArtShow" label="最新文章" name="RecentlyArticle" :style="{padding: '0 .2rem'}">
                    <Row v-for="(item, index) in articleListData" :key="item.article_id" class="recent-article-tab">
                        <Col span="18" class="title"><span  @click="linkToDetailHandler(item.article_id)">{{ item.articleTitle }}</span></Col>
                        <Col span="6" :style="{fontSize: '.5rem', color: '#dcdee2'}">{{ item.CreateTime }}</Col>
                    </Row>
                </TabPane>
                <TabPane v-for="(item, index) in CustomTabList" :label="item.IndexTabName" :name="item.IndexTabID" :key="item.IndexTabID" :style="{padding: '0 .2rem'}">
                    <div v-html="item.IndexTabContent"></div>
                </TabPane>
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
  	        CarouselData: [0, 1, 2, 3],
            articleListData: [],
            tabListData: [],
            IndexImageData: []
		}
	},
	components: {
		SubNavigationFrame
	},
    computed: {
        recentArtShow(){
            return this.tabListData.find(item => item.IndexTabCode == '000601') && this.tabListData.find(item => item.IndexTabCode == '000601').IsShowTab;
        },
        CustomTabList(){
            return this.tabListData.filter(item => item.IndexTabCode != '000601' && item.IsShowTab );
        }
    },
	mounted () {
        this.$store.commit('showMenu', true);
        this.$store.commit('showAdminMenu', false);
        this.checkLoginStatusHandler();
        this.getAricleListHandler();
        this.getTabListHandler();
        this.getImageListHandler();
	},
	methods: {
        checkLoginStatusHandler(){
            Action.getStatusInfo()
            .then(res => {
              
            })
            .catch(err => {
                this.$Message.error(err);
            })
        },
        //获取文章列表
        getAricleListHandler(){
            Action.articleGetList()
            .then(res => {
                this.articleListData = res.map(item => {
                    item.CreateTime = new Date(item.CreateTime).Format('yyyy-MM-dd');
                    return item;
                }).slice(0, 5);
            })
            .catch(err => {
                this.$Message.error(err);
            })
        },
        //跳转至文章详情页
        linkToDetailHandler(id){
            this.$router.push({
                name: 'articleDetail',
                query: {
                    id: id
                }
            })
        },
        //获取Tab页
        getTabListHandler(){
            Action.tabGetlist()
            .then(res => {
                this.tabListData = res;
            })
            .catch(err => {
                this.$Message.error(err);
            })
        },
        //获取轮播图集合
        getImageListHandler(){
            Action.IndexImageGetList()
            .then(res => {
                this.IndexImageData = res.map(item => {
                    item.IndexImageUrl = `${REQUEST_URL.IndexImageDownload}${item.IndexImageUrl}`;
                    return item;
                }).filter(e => e.ShowOnIndex);
            })
            .catch(err => {
                this.$Message.error(err);
            })
        }
	}
}
</script>