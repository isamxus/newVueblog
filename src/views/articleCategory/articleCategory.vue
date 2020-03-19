<style lang="scss">
    @import './sass/articleCategory';
</style>

<template>
    <SubNavigationFrame :title="$route.meta.title" :breadcrumb="breadcrumbs">
        <div class="article-category-page-container" slot="content">
            <Row :style="{margin: '.7rem 0'}" type="flex" justify="space-around" v-for="(item, index) in articleListData" :key="index">
                <Col span="15">
                    <Card :style="{height: '220px', cursor: 'pointer', display: 'flex', justifyContent: 'center'}" >
                        <h1 :style="{textAlign: 'center'}">{{ item.articleTitle }}</h1>
                        <span>分类：{{ item.articleCagetoryName }}</span>
                        <span>标签：{{ item.articleTagsName }}</span>
                        <span>{{ item.CreateTime }}</span>
                        <p :style="{textIndent: '.7rem', marginTop: '.7rem'}">{{ item.articleAbstract }}...</p>
                        <Button long :style="{marginTop: '1.2rem'}" @click="$router.push({
                            name: 'articleDetail',
                            query: {
                                id: item.id
                            }
                        })">进入阅读</Button>
                    </Card>
                </Col>
            </Row>
            <!-- 分页 -->
            <Page
                :style="{paddingTop: '1rem',textAlign: 'center'}"
                :total="PageCount"
                :current="PageNumber"
                :page-size="PageSize"
                placement="top"
                @on-change="e => {PageNumber=e, getAricleListHandler()}" 
                @on-page-size-change="(size) => { PageSize = size, getAricleListHandler() }"
                show-elevator
                show-total
                show-sizer />
            </Page>
        </div>
        
    </SubNavigationFrame>
</template>

<script>
import SubNavigationFrame from '../../components/SubNavigationFrame/SubNavigationFrame';
import Action from './action/articleCategory';
export default {
    data () {
        return {
            articleListData: [],
            breadcrumbs:[
                {title: '文章分类'},
                {title: this.$route.meta.title}
            ],
            data: [
                {
                    articleTitle: '模拟数据1',
                    articleAuthor: '模拟数据1',
                    articleAbstract: '模拟数据1',
                    articleCreateTime: '2019-08-11',
                }
            ],
            PageCount: 0,
            PageNumber: 1,
            PageSize: 10
        }
    },
    components: {
        SubNavigationFrame
    },
    watch: {
        '$route' : 'getAricleListHandler'
    },
    mounted () {
        this.getAricleListHandler();
    },
    methods: {
        //获取文章列表
        getAricleListHandler(){
            Action.articleGetPageList({
                PostContent: {
                    filter: {
                        articleCagetoryID: this.$route.query.id
                    },
                    _OrderBy: '-CreateTime',
                    PageSize: this.PageSize,
                    PageNumber: this.PageNumber
                }
            })
            .then(res => {
                this.articleListData = res.Items.map(item => {
                    item.CreateTime = new Date(item.CreateTime).Format('yyyy-MM-dd');
                    return item;
                });
                this.PageCount = res.TotalItems;
            })
            .catch(err => {
                this.$Message.error(err);
            })
        },
    }
}
</script>
