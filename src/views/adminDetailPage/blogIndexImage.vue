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
            <Table  :columns="columns" :data="tableList"></Table>
            <Modal
                v-model="popModal"
                :title="'编辑Tab页'"
                width=600>
                <Form
                    ref="createForm"
                    style="padding-right: 2rem"
                    :label-width="100"
                    :model="createModal"
                    :rules="createModalRules">
                    <FormItem label="轮播图片：" prop="ContractTemplateName">
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
                </Form>            
                <div slot="footer" >
                    <Button type="primary" @click="">确定</Button>
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
    uploadList: []
}, params);


export default {
    data () {
        return {
            breadcrumbs:[
                {title: this.$route.query.paramsName}
            ],
            columns:[
                {title: '序号', type: 'index', width: 120},
                {title: '链接文章'},
                {title:'操作', align: 'center', render:this.toolColumnRender}
            ],
            tableList: [],
            uploadUrl: REQUEST_URL.IndexImageUpload,
            popModal: false,
            createModal: dataFactory(),
            createModalRules: {},
            
        }
    },
    components: {
        SubNavigationFrame
    },
    mounted () {
        this.$store.commit('showAdminMenu', true);
    },
    methods: {
        //操作列渲染
        toolColumnRender(h, params) {
            return h('div', [
                   h('Button',{
                        props:{type:'text'},
                        domProps:{innerText: '编辑'},
                        on:{click: e => {
                            e.stopPropagation();
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
                       }
                    }
                })
            ]);
        },
         //重置表单
        resetFormHandler(){
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
        }
    }
}
</script>