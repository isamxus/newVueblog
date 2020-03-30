<style lang="scss">
    @import './sass/addArticle';
</style>

<template>
  	<SubNavigationFrame  :title="$route.query.id ? '编辑博客文章' : '新增博客文章'" :breadcrumb="breadcrumbs">
        <div  slot="navigation" :style="{textAlign:'right',marginTop:'-2.5rem'}">
            <Button @click="$router.push({name: 'Index'})">返回主站</Button>
            <Button @click="$router.go(-1)">返回</Button>
        </div>
  		  <div class="sub-page-container" slot="content">
            <Form ref="formRefs" :label-width="100" :style="{height: '100%', paddingBottom: '2rem'}"  :model="createArticleForm" :rules="createArticleRules">
                <Row>
                    <Col span="12">
                        <FormItem  label="文章标题：" prop="articleTitle">
                            <Input type="text" v-model="createArticleForm.articleTitle"  placeholder="请输入文章标题" />
                        </FormItem>
                    </Col>
                </Row>
                <Row>
                    <Col span="12">
                        <FormItem  label="文章作者：" prop="articleAuthor">
                            <Input type="text" v-model="createArticleForm.articleAuthor"  placeholder="请输入文章作者" />
                        </FormItem>
                    </Col>
                </Row>
                <Row>
                    <Col span="12">
                        <FormItem  label="文章摘要：" prop="articleAbstract">
                            <Input type="text" v-model="createArticleForm.articleAbstract" placeholder="请输入文章摘要：" />
                        </FormItem>
                    </Col>
                </Row>
                <Row>
                    <Col span="8">
                        <FormItem class="sub-page-input-container min-input-container" label="文章标签：" prop="">
                            <Select
                                transfer 
                                filterable
                                multiple
                                clearable
                                label-in-value
                                v-model="createArticleForm.articleTagsID" 
                                :label="createArticleForm.articleTagsName"
                                @on-change="e => {
                                    if(e.length === 0) return;
                                    createArticleForm.articleTagsName = e.map(item => item.label)
                                }">
                                <Option 
                                    v-for="(item,key) in TagListData" 
                                    :value="item.id" 
                                    :key="key">{{ item.detailName }}</Option>
                            </Select>
                        </FormItem>
                    </Col>
                </Row>
                <Row>
                    <Col span="8">
                        <FormItem class="sub-page-input-container min-input-container" label="文章分类：" prop="articleCagetoryID">
                            <Select
                                transfer 
                                clearable
                                label-in-value
                                v-model="createArticleForm.articleCagetoryID" 
                                @on-change="e => {
                                    createArticleForm.articleCagetoryName = e.label
                                }">
                                <Option 
                                    v-for="(item,key) in CategoryListData" 
                                    :value="item.detail_params_id" 
                                    :key="key">{{ item.detailName }}</Option>
                            </Select>
                        </FormItem>
                    </Col>
                </Row>
                <!--
                <Row>
                    <Col class="material-item" span="8">
                        <FormItem class="sub-page-input-container min-input-container" label="创建日期：" >
                            <DatePicker 
                                format="yyyy-MM-dd HH:mm" 
                                placeholder="请选择创建时间"
                                type="datetime" 
                                transfer
                                :style="{width: '100%'}" 
                                @on-change="e => {}" />   
                        </FormItem>
                    </Col>
                </Row>-->
                <Row>
                    <Col span="22">
                        <FormItem  label="文章正文：" prop="articleContent">
                            <quill-editor  v-model="createArticleForm.articleContent" style="height: 20rem" />
                        </FormItem>
                    </Col>
                </Row>
            </Form>
            <Row>
                <Col span="22">
                    <div :style="{textAlign:'right', margin:'1.5rem 0rem'}">
                        <Button  @click="$router.go(-1)">取消</Button>
                        <Button type="primary" @click="submitArticleHandler">确认</Button>
                    </div>
                </Col>
            </Row>
            
  		  </div>
	  </SubNavigationFrame>
</template>

<script>
import SubNavigationFrame from '../../components/SubNavigationFrame/SubNavigationFrame';
import Action from './action/addArticle';

export default {
    data () {
        return {
            CategoryListData: [],
            TagListData: [],
            breadcrumbs:[
                {title: '新增博客文章'},
            ],
            createArticleForm: {
                articleTitle: '',
                articleAuthor: '',
                articleAbstract: '',
                articleTagsID: [],
                articleTagsName: [],
                articleContent: '',
                articleCagetoryID: '',
                articleCagetoryName: ''
            },
            createArticleRules: {
                articleTitle: [{required: true, message: '请输入文章标题'}],
                articleAuthor: [{required: true, message: '请输入文章作者'}],
                articleContent: [{required: true, message: '请输入正文'}],
                articleCagetoryID: [{required: true, message: '请选择分类'}]
            }
        }
    },
    components: {
        SubNavigationFrame
    },
    async mounted () {
        this.$store.commit('showAdminMenu', true);
        this.getCategoryHandler();
        this.getTagsHandler();
        if (this.$route.query.id) this.getArticleDetailHandler();
        
    },
    methods: {
        getCategoryHandler(){
            //获取分类
            Action.paramsDetailGetList({
                PostContent: {
                    filter: {
                        detailParentParamCode: '0001'
                    }
                }
            })
            .then(res => {
                this.CategoryListData = res;
            })
            .catch(err => {
                this.$Message.error(err);
            })
        },
        getTagsHandler(){
            //获取分类
            Action.paramsDetailGetList({
                PostContent: {
                    filter: {
                        detailParentParamCode: '0003'
                    }
                }
            })
            .then(res => {
                this.TagListData = res;
            })
            .catch(err => {
                this.$Message.error(err);
            })
        },
        //提交文章
        submitArticleHandler(){
            Action[this.$route.query.id ? 'articleUpdate' : 'articleCreate']({
                PostContent: this.createArticleForm
            })
            .then(res => {
                this.$Message.success(this.$route.query.id ? '成功修改文章！！！' : '成功添加文章！！！')
                this.$router.push({name: 'articleListPage'})
            })
            .catch(err => {
                if(err.type === 'local') return this.$Message.warning(err.Msg);
                this.$Message.error(err);
            })
        },
        //获取单篇文章数据
        getArticleDetailHandler(){
            Action.articleGetSingle({
                PostContent: {
                    article_id: this.$route.query.id
                }
            })
            .then(res => {
                res.articleTagsID = res.articleTagsID.split(',').map(item => parseInt(item));
                res.articleTagsName = res.articleTagsName.split(',');
                res.articleCagetoryID = parseInt(res.articleCagetoryID)
                this.createArticleForm = res;
            })
            .catch(err => {
                this.$Message.error(err);
            })
        }
        
    }
}
</script>