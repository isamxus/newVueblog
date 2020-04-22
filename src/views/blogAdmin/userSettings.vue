<style lang="scss">
    @import './sass/userSettings';
</style>

<template>
  	<SubNavigationFrame :title="$route.meta.title" :breadcrumb="breadcrumbs">
  		<div class="user_setting_container" slot="content">
            <Row>
                <div :style="{textAlign: 'right'}">
                    <Button type="primary">修改密码</Button>
                    <Button>返回主页</Button>
                </div>
            </Row>
            <Row>
                <Col span="8" offset="8" :style="{textAlign: 'center', marginBottom: '.7rem'}">
                    <Avatar v-show="!imageUrl" icon="ios-person" size="100" />
                    <Avatar v-show="imageUrl" :src="imageUrl" size="100" />
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
                            <Input v-model="settingForm.UserName" :readonly="!settingForm.Edit"  placeholder="请输入用户名" />
                            <Icon  type="ios-create-outline" /><span v-show="!settingForm.Edit" :style="{color: '#2b85e4', cursor: 'pointer'}" @click="settingForm.Edit=true">修改</span><span v-show="settingForm.Edit" :style="{color: '#2b85e4', cursor: 'pointer'}" @click="settingForm.Edit=false">完成</span>
                        </FormItem>
                    </Form>
                </Col>
                <Col span="6" offset="9">
                    <Button type="primary" @click="submitDataHandler" long>确认修改</Button>
                </Col>
            </Row>
  		</div>
	</SubNavigationFrame>
</template>

<script>
import SubNavigationFrame from '../../components/SubNavigationFrame/SubNavigationFrame';
import Action from './action/userSettings';
const dataFactory = params => Object.assign({
    user_id: '',
    UserName: '',
    UserHeadImg: '',
    Edit: false,
    uploadStatus: null,
    uploadList: []
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
            imageUrl: '',
            uploadUrl: REQUEST_URL.userImageUpload,
		}
	},
	components: {
		SubNavigationFrame
	},
    computed: {

    },
	mounted () {
        this.setInfoHandler();
	},
	methods: {
        //设置用户信息
        setInfoHandler(){
            let userinfo = this.$store.state.UserInfo;
            this.imageUrl = userinfo.UserHeadImg ? `${REQUEST_URL.staticDownload}${userinfo.UserHeadImg}` : '';
            this.settingForm.UserName = userinfo.UserName;
            this.settingForm.user_id = userinfo.user_id;
        },
        //图片上传前钩子
        handleBeforeUploadNum(com, file) {
            if(!com) return (this.handleError({Msg: '无法获取上传组件', State: -1}, file, this.settingForm.uploadList), false);
            if(com.$props.maxSize && (file.size / 1024 > com.$props.maxSize)) return (this.handleError({Msg: '文件体积过大，无法上传', State: -1}, file, this.settingForm.uploadList), false);
            
            this.settingForm.uploadStatus = this.$Message.loading({content:'正在上传文档，请稍等...', duration:0});
            const checkNum = this.settingForm.uploadList.length;
            if(checkNum) this.$refs.uploadFileRef.clearFiles();
        },
        //上传成功钩子
        handleSuccess(res,file,fileList) {
            if(res.State != 1){
                this.handleError(res, file, fileList);
                return fileList.splice(fileList.length - 1 , 1);
            }
            this.settingForm.uploadStatus();
            this.settingForm.uploadStatus = null;
            
            if(res.State != 1){
                this.handleError(res, file, fileList);
                return fileList.splice(fileList.length - 1 , 1);
            }
            let form = this.settingForm;
            form.UserHeadImg = file.response.PostContent.Address;
            this.imageUrl =  `${REQUEST_URL.staticDownload}${form.UserHeadImg}`;
            //form.IndexImageName = file.name;
            //form.IndexImageUrl = file.response.PostContent.Address;
            
        },
         //上传文档错误钩子
        handleFormatError(file,fileList) {
            this.settingForm.uploadStatus();
            this.settingForm.uploadStatus = null;
            this.$Message.warning('文件格式错误，请重新上传');
        },
         //上传失败钩子
        handleError(error,file,fileList) {
            this.settingForm.uploadStatus();
            this.settingForm.uploadStatus = null;
            this.$Message.warning(error && error.Msg || '文件上传失败');
        },
        //上传文档大于15M钩子
        handleMaxSize(file) {
            this.settingForm.uploadStatus();
            this.settingForm.uploadStatus = null;
            this.$Message.warning('超出文件大小限制，文档不能超过 15M');
        },
        //提交表单
        submitDataHandler(){
            if (this.settingForm.Edit) return this.$Message.warning('请点击完成修改');
            Action.userUpdate({
                PostContent: {
                    user_id: this.settingForm.user_id,
                    UserName: this.settingForm.UserName,
                    UserHeadImg: this.settingForm.UserHeadImg
                }
            })
            .then(res => {
                
            })
            .catch(err => {
                this.$Message.error(err);
            })
        }
	}
}
</script>