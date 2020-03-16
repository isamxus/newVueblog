<style lang="scss">
    @import './sass/addArticle';
</style>

<template>
  	<SubNavigationFrame  :title="'新增博客文章'" :breadcrumb="breadcrumbs">
        <div  slot="navigation" :style="{textAlign:'right',marginTop:'-2.5rem'}">
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
                        <FormItem  label="文章摘要：" prop="articleAbstract">
                            <Input type="text" v-model="createArticleForm.articleAbstract" placeholder="请输入文章摘要：" />
                        </FormItem>
                    </Col>
                </Row>
                <Row>
                    <Col span="8">
                        <FormItem class="sub-page-input-container min-input-container" label="文章分类：" prop="articleCagetoryName">
                            <Select
                                transfer 
                                filterable
                                clearable
                                label-in-value
                                v-model="createArticleForm.articleCagetoryID" 
                                @on-change="e => {
                                    if(!e) return;
                                    createArticleForm.articleCagetoryName = e.label
                                }">
                                <Option 
                                    v-for="(item,key) in CategoryListData" 
                                    :value="item.id" 
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
                        <Button type="primary" @click="">确认</Button>
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
            breadcrumbs:[
                {title: '新增博客文章'},
            ],
            createArticleForm: {
                articleTitle: '',
                articleAuthor: '',
                articleAbstract: '',
                articleContent: '',
                articleCagetoryID: '',
                articleCagetoryName: ''
            },
            createArticleRules: {
                articleTitle: [{required: true, message: '请输入文章标题'}],
                articleAuthor: [{required: true, message: '请输入作者'}],
                articleContent: [{required: true, message: '请输入正文'}],
                articleCagetoryName: [{required: true, message: '请选择分类'}]
            }
        }
    },
    components: {
        SubNavigationFrame
    },
    mounted () {
        this.getCategoryHandler();
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
        }
        
    }
}
</script>