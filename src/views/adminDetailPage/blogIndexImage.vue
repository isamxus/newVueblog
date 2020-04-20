<style lang="scss">
    @import './sass/blogIndexImage';
</style>

<template>
  	<SubNavigationFrame :title="$route.query.paramsName" :breadcrumb="breadcrumbs">
  		<div  slot="navigation" :style="{textAlign:'right',marginTop:'-2.5rem'}">
            <Button @click="$router.push({name: 'Index'})">返回主站</Button>
            <Button @click="$router.go(-1)">返回</Button>
        </div>
        <div class="sub-page-container" :style="{'margin-top': '.5rem','padding-top':'1rem'}" slot="content">
            <Row>
                <Col span="8">
                    <div :style="{marginBottom: '.7rem'}">
                        <Button type="primary" @click="resetFormHandler"><Icon type="md-add"></Icon>新增轮播图</Button>
                    </div>
                </Col>
            </Row>
            <div :style="{overflow: 'auto'}">
                <Table :style="{minWidth: '1040px'}"  :columns="columns" :data="tableList"></Table>
            </div>
            <Modal
                v-model="popModal"
                :title="createModal.edit ? '编辑' : '新增'"
                width=600>
                <Form
                    ref="createForm"
                    style="padding-right: 2rem"
                    :label-width="100"
                    :model="createModal"
                    :rules="createModalRules">
                    <FormItem  label="轮播图片：" prop="ContractTemplateName">
                        <Upload 
                            ref="uploadFileRef" 
                            :action="uploadUrl" 
                            :format="['jpg','png','jpeg']"
                            :max-size="100000" 
                            :before-upload="file => handleBeforeUploadNum($refs['uploadFileRef'], file)"
                            :on-success="handleSuccess"
                            :on-format-error="handleFormatError"
                            :on-error="handleError" 
                            :on-exceeded-size="handleMaxSize"
                            :show-upload-list="false"
                            :style="{display: 'inline-block'}">
                            <Button>上传图片</Button>
                        </Upload>
                        <p>说明：请上传jpg,jpeg,png格式的图片</p>
                        <div  v-if="createModal.IndexImageUrl" >
                            <div style="font-size: .7rem;word-break: break-all;cursor: pointer;" @click="openUrlHandler(createModal.IndexImageUrl, createModal.IndexImageName)">
                                <Icon type="ios-link" />
                                <span :style="{color:'#2d8cf0',paddingRight:'.2rem'}">
                                {{ createModal.IndexImageName }}
                            </span></div>
                        </div>
                    </FormItem>
                    <FormItem class="sub-page-input-container min-input-container" label="关联文章：" prop="ConnectArticleID">
                        <Cascader :data="articleListData" v-model="selectData"  :load-data="loadArticleData" @on-change="articleSelectHandler"></Cascader>
                    </FormItem>
                    <FormItem label="是否显示：" prop="ShowOnIndex">
                        <Switch v-model="createModal.ShowOnIndex">
                            <span slot="open">是</span>
                            <span slot="close">否</span>
                        </Switch>
                    </FormItem>
                </Form>            
                <div slot="footer" >
                    <Button type="primary" @click="submitDataHandler">确定</Button>
                    <Button @click="popModal=false">取消</Button>
                </div>
            </Modal>
        </div>  
    </SubNavigationFrame>
</template>

<script>
import Action from './action/blogIndexImage';
import SubNavigationFrame from '../../components/SubNavigationFrame/SubNavigationFrame';

const dataFactory = params => Object.assign({
    uploadStatus: null,
    IndexImageName: '',
    IndexImageUrl: '',
    uploadList: [],
    ConnectArticleID: '',
    ConnectArticleName: '',
    ConnectArticleCateID: '',
    ConnectArticleCateName: '',
    ShowOnIndex: false,
    edit: false
}, params);


export default {
    data () {
        return {
            breadcrumbs:[
                {title: this.$route.query.paramsName}   
            ],
            columns:[
                {title: '序号', type: 'index', width: 120},
                {title: '关联文章', key: 'ConnectArticleName'},
                {title: '首页显示', render: this.ShowOnIndexRender},
                {title:'操作', align: 'center', render:this.toolColumnRender}
            ],
            tableList: [],
            uploadUrl: REQUEST_URL.IndexImageUpload,
            popModal: false,
            createModal: dataFactory(),
            createModalRules: {
                ConnectArticleID: [{required: true, message: '请选择关联文章'}],
            },
            articleListData: [],
            selectData: []
            
        }
    },
    components: {
        SubNavigationFrame
    },
    mounted () {
        this.$store.commit('showAdminMenu', true);
        this.getCategoryHandler();
        this.getImageListHandler();
    },
    methods: {
        ShowOnIndexRender(h, params){
            return h('span', {domProps:{innerText: params.row.ShowOnIndex ? '是' : '否'}});
        },
        //操作列渲染
        toolColumnRender(h, params) {
            return h('div', [
                   h('Button',{
                        props:{type:'text'},
                        domProps:{innerText: '编辑'},
                        on:{click: e => {
                            e.stopPropagation();
                            this.createModal = params.row;
                            this.selectData = [this.createModal.ConnectArticleCateID, this.createModal.ConnectArticleID];
                            this.popModal = true;
                            params.row.edit = true;
                            
                        }
                    }
                }),
                   h('Button',{
                        props:{type:'text'},
                        domProps:{innerText: '删除'},
                        on:{click: e => {
                            e.stopPropagation();
                            if (!params.row.IndexImageID) return this.$Message.warning('参数ID为空，无法删除！！！');
                            const modal = this.$Modal.confirm({
                                title: '操作确认'
                                ,icon: 'warning'
                                ,content: '是否删除此轮播图'
                                ,okText: '确定'
                                ,showCancel: true
                                ,loading: true
                                ,onOk: () => {
                                    //发起删除轮播图请求
                                    Action.IndexImageDelete({
                                        PostContent: {
                                            IndexImageID: params.row.IndexImageID
                                        }
                                    }).then(result => {
                                        this.$Message.success('成功删除轮播图！！！');
                                        this.$Modal.remove()
                                        this.getImageListHandler();
                                    })
                                    .catch(err => {
                                        this.$Modal.remove()
                                        this.$Message.error(err);
                                    });
                                }
                            });
                        }
                    }
                })
            ]);
        },
         //重置表单
        resetFormHandler(){
            this.createModal = dataFactory();
            this.popModal = true;
        },
        //图片上传前钩子
        handleBeforeUploadNum(com, file) {
            if(!com) return (this.handleError({Msg: '无法获取上传组件', State: -1}, file, this.createModal.uploadList), false);
            if(com.$props.maxSize && (file.size / 1024 > com.$props.maxSize)) return (this.handleError({Msg: '文件体积过大，无法上传', State: -1}, file, this.createModal.uploadList), false);
            
            this.createModal.uploadStatus = this.$Message.loading({content:'正在上传文档，请稍等...', duration:0});
            const checkNum = this.createModal.uploadList.length;
            if(checkNum) this.$refs.uploadFileRef.clearFiles();
        },
        //上传成功钩子
        handleSuccess(res,file,fileList) {
            if(res.State != 1){
                this.handleError(res, file, fileList);
                return fileList.splice(fileList.length - 1 , 1);
            }
            console.log(file)
            this.createModal.uploadStatus();
            this.createModal.uploadStatus = null;
            
            if(res.State != 1){
                this.handleError(res, file, fileList);
                return fileList.splice(fileList.length - 1 , 1);
            }
            let form = this.createModal;
            form.IndexImageName = file.name;
            form.IndexImageUrl = file.response.PostContent.Address;
            
        },
         //上传文档错误钩子
        handleFormatError(file,fileList) {
            this.createModal.uploadStatus();
            this.createModal.uploadStatus = null;
            this.$Message.warning('文件格式错误，请重新上传');
        },
         //上传失败钩子
        handleError(error,file,fileList) {
            this.createModal.uploadStatus();
            this.createModal.uploadStatus = null;
            this.$Message.warning(error && error.Msg || '文件上传失败');
        },
        //上传文档大于15M钩子
        handleMaxSize(file) {
            this.createModal.uploadStatus();
            this.createModal.uploadStatus = null;
            this.$Message.warning('超出文件大小限制，文档不能超过 15M');
        },
        //打开图片
        openUrlHandler(url, fileName){
            let strUrl = `${REQUEST_URL.IndexImageDownload}${url}`;
            window.open(strUrl);
        },
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
                this.articleListData = res.map(item => {
                    return {
                        value: item.detail_params_id,
                        label: item.detailName,
                        children: [],
                        loading: false
                    }
                });
            })
            .catch(err => {
                this.$Message.error(err);
            })
        },
        //加载数据
        loadArticleData(item, callback){
            item.loading = true;
            //获取文章列表
            Action.articleGetList({
                PostContent: {
                    filter: {
                        articleCagetoryID: item.value
                    }
                }
            })
            .then(res => {
                item.children = res.map(e => {
                    return {
                        value: e.article_id,
                        label: e.articleTitle,
                        parentName: e.articleCagetoryName,
                        parentID: e.articleCagetoryID
                    }
                })
                item.loading = false;
                callback();
            })
            .catch(err => {
                this.$Message.error(err);
            })

        },
        //关联文章选择
        articleSelectHandler(value, selectedData){
            if (selectedData.length == 0) return;
            let batch = selectedData[selectedData.length - 1];
            this.createModal.ConnectArticleCateID = batch.parentID;
            this.createModal.ConnectArticleCateName = batch.parentName;
            this.createModal.ConnectArticleID = batch.value;
            this.createModal.ConnectArticleName = batch.label;
        },
        //获取轮播图集合
        getImageListHandler(){
            Action.IndexImageGetList()
            .then(res => {
                this.tableList = res;
            })
            .catch(err => {
                this.$Message.error(err);
            })
        },
        //提交表单处理
        submitDataHandler(){
            if (!this.createModal.IndexImageName) return this.$Message.warning('请上传图片');
            if (!this.createModal.ConnectArticleID) return this.$Message.warning('请选择关联文章');
            Action[ this.createModal.edit ? 'IndexImageUpdate' : 'IndexImageCreate']({
                PostContent: this.createModal
            })
            .then(res => {
                this.popModal = false;
                this.getImageListHandler();
            })
            .catch(err => {
                this.$Message.error(err);
            })
        }
    }
}
</script>