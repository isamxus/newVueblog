<style lang="scss">
    @import './sass/userSettings';
</style>

<template>
  	<SubNavigationFrame :title="$route.meta.title" :breadcrumb="breadcrumbs">
  		<div class="user_setting_container" slot="content">
            <Row>
                <Col span="8" offset="8" :style="{textAlign: 'center', marginBottom: '.7rem'}">
                    <Avatar icon="ios-person" size="100" />
                </Col>
                <Col span="6" offset="9">
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
                        :style="{display: 'inline-block', width: '100%'}">
                        <Button long>更换头像</Button>
                    </Upload>
                </Col>
            </Row>
            <Row>
                <Col span="24" :style="{display: 'flex', justifyContent: 'center', marginTop: '1.4rem'}">
                    <Form
                        ref="settingForm"
                        :label-width="100"
                        :model="settingForm"
                        :rules="settingFormRules">
                        <FormItem class="sub-page-input-container min-input-container" label="用户名：" prop="UserName">
                            <Input  placeholder="请输入用户名" />
                            <Icon type="ios-create-outline" /><span :style="{color: '#2b85e4', cursor: 'pointer'}">修改</span>
                        </FormItem>
                    </Form>
                </Col>
                <Col span="6" offset="9" :style="{textAlign: 'center'}">
                    <Button type="primary">修改密码</Button>
                    <Button>返回主页</Button>
                </Col>
            </Row>
  		</div>
	</SubNavigationFrame>
</template>

<script>
import SubNavigationFrame from '../../components/SubNavigationFrame/SubNavigationFrame';
import Action from './action/userSettings';
const dataFactory = params => Object.assign({

}, params);



export default {
	data () {
		return {
            breadcrumbs:[
                {title: this.$route.meta.title}
            ],
            settingForm: dataFactory(),
            settingFormRules: {

            },
            uploadUrl: ''
		}
	},
	components: {
		SubNavigationFrame
	},
    computed: {

    },
	mounted () {

	},
	methods: {
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
	}
}
</script>