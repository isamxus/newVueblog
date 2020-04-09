<style lang="scss">
    @import './sass/articleDetail';
</style>

<template>
    <SubNavigationFrame :title="$route.meta.title" :breadcrumb="breadcrumbs">
        <div  slot="navigation" :style="{textAlign:'right',marginTop:'-2.5rem'}">
            <Button @click="$router.go(-1)">返回</Button>
        </div>
        <div class="article-detail-page-container" slot="content">
            <div class="article-content-part">
                <div :style="{borderBottom: '1px solid #f8f8f9', padding: '.7rem'}">
                    <h2 :style="{textAlign: 'center'}">{{ articleDetailData.articleTitle }}</h2>
                    <div :style="{display: 'flex', justifyContent: 'center', margin: '.7rem'}">
                        <span><Icon type="md-browsers" />分类：{{ articleDetailData.articleCagetoryName }}</span>
                        <span><Icon type="ios-pricetags" />标签：{{ articleDetailData.articleTagsName || '无' }}</span>
                        <span><Icon type="md-time" />{{ articleDetailData.CreateTime }}</span>
                        <span><Icon type="md-eye" />浏览{{ articleDetailData.articleViews }}</span>
                    </div>
                    <p v-html="articleDetailData.articleContent"></p>
                </div>
                
                <div class="titlebox" :style="{marginTop: '.7rem'}">
                    <h3>发表评论</h3>
                </div>
                <div >
                    <Input v-model="commentContent"  type="textarea"  :autosize="{minRows: 5,maxRows: 5}"></Input>
                </div>
                <div :style="{textAlign:'right', margin:'1.5rem 0rem'}">
                    <Button type="primary"  @click="createCommentHandler">发布评论</Button>
                </div>       
            </div>
            <div class="comment-content-part">
                <div class="titlebox">
                    <h3>评论列表</h3>
                </div>
                <div class="comment-container">
                    <Row class="comment-item" v-for="(item, index) in commentListData" :key="item.id">
                        <Col span="4">
                            <Avatar icon="ios-person"  />
                        </Col>
                        <Col span="20">
                            <Row>{{ item.commentAuthor }}</Row>
                            <span :style="{fontSize: '10px'}">{{item.CreateTime}}</span>
                        </Col>
                        <Col span="24">
                            <p :style="{wordBreak: 'break-all', padding: '.7rem 0'}">{{ item.commentContent }}</p>
                        </Col>
                    </Row>
                </div>
                <!-- 分页 -->
                <Page
                    size="small"
                    :style="{paddingTop: '1rem',textAlign: 'center'}"
                    :total="PageCount"
                    :current="PageNumber"
                    :page-size="PageSize"
                    placement="top"
                    @on-change="e => {PageNumber=e, getCommentListHandler()}" 
                    @on-page-size-change="(size) => { PageSize = size, getCommentListHandler() }"
                    show-elevator
                    show-total/>
                </Page>
            </div>
        </div>
        
    </SubNavigationFrame>
</template>

<script>
import SubNavigationFrame from '../../components/SubNavigationFrame/SubNavigationFrame';
import Action from './action/articleDetail';
export default {
    data () {
        return {
            articleDetailData: {

            },
            breadcrumbs:[
                {title: this.$route.meta.title}
            ],
            commentContent: '',
            PageCount: 0,
            PageNumber: 1,
            PageSize: 5,
            commentListData: []
        }
    },
    components: {
        SubNavigationFrame
    },
    mounted () {
        this.getAricleDetailHandler();
        this.getCommentListHandler();
    },
    methods: {
        //根据ID获取文章
        getAricleDetailHandler(){
            Action.articleGetSingle({
                PostContent: {
                    article_id: this.$route.query.id
                }
            })
            .then(res => {
                this.articleDetailData = res;
                res.CreateTime = new Date(res.CreateTime).Format('yyyy-MM-dd');
            })
            .catch(err => {
                this.$Message.error(err);
            })
        },
        //创建一条评论
        createCommentHandler(){
            if (!this.$store.state.IsLogin) return this.$Message.warning('请登录后发表评论！！！');
            let UserName = JSON.parse(localStorage.getItem('UserInfo')).UserName;
            Action.commentCreate({
                PostContent: {
                    parentArticleID: this.$route.query.id,
                    parentArticleTitle: this.articleDetailData.articleTitle,
                    commentContent: this.commentContent,
                    commentHeadImg: '',
                    commentAuthor: UserName
                }
            })
            .then(res => {
                this.commentContent = '';
                this.getCommentListHandler();
                this.$Message.success('创建评论成功！！！')
            })
            .catch(err => {
                if(err.type === 'local') return this.$Message.warning(err.Msg);
                this.$Message.error(err);
            })
        },
        //获取评论列表
        getCommentListHandler(){
            Action.commentGetPageList({
                PostContent: {
                    filter: {
                        parentArticleID: this.$route.query.id
                    },
                    _OrderBy: '-CreateTime',
                    PageSize: this.PageSize,
                    PageNumber: this.PageNumber
                }
            })
            .then(res => {
                this.commentListData = res.Items.map(item => {
                    item.CreateTime = new Date(item.CreateTime).Format('yyyy-MM-dd hh:mm');
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
