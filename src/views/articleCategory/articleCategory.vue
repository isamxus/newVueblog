<style lang="scss">
    @import './sass/articleCategory';
</style>

<template>
    <SubNavigationFrame :title="$route.meta.title" :breadcrumb="breadcrumbs">
        <div class="article-category-page-container" slot="content">
            <Row :style="{margin: '.7rem 0'}" type="flex" justify="space-around" v-for="(item, index) in articleListData">
                <Col span="15">
                    <Card :style="{height: '220px', cursor: 'pointer', display: 'flex', justifyContent: 'center'}">
                        <h1>ewfwe</h1>
                    </Card>
                </Col>
            </Row>
            <!-- 分页 -->
            <Page
                :style="{paddingTop: '1rem',textAlign: 'center'}"
                :total="100"
                :current="1"
                :page-size="10"
                placement="top"
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
            ]
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
            Action.articleGetList({
                PostContent: {
                    filter: {
                        articleCagetoryID: this.$route.query.id
                    },
                    _OrderBy: '-CreateTime'
                }
            })
            .then(res => {
                this.articleListData = res;
            })
            .catch(err => {
                this.$Message.error(err);
            })
        },
    }
}
</script>
