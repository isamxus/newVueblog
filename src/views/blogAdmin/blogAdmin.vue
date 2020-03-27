<style lang="scss" scoped>
    @import './sass/blogAdmin';
</style>

<template>
    <div class="login-container">
        <div class="login-form-contain">
            <Row>
                <Col span="24">
                    <h1>{{$route.meta.title}}</h1>
                </Col>
            </Row>
            <Form class="login-form">
                <Row>
                    <Col span="20" offset="2">
                        <FormItem prop="User">
                            <Input v-model="loginForm.UserName" type="text" placeholder="请输入用户名称" size="large">
                                <Icon size="24" type="ios-person-outline" slot="prepend"></Icon>
                            </Input>
                        </FormItem>
                    </Col>
                    <Col span="20" offset="2">
                        <FormItem prop="Password">
                            <Input v-model="loginForm.PassWord" type="text" placeholder="请输入登录密码" size="large">
                                <Icon size="24" type="ios-lock-outline" slot="prepend"></Icon>
                            </Input>
                        </FormItem>
                    </Col>
                    <Col span="8" offset="8">
                        <FormItem prop="User">
                            <Button type="primary" size="large" long @click="submitFormHandler">登录</Button>
                        </FormItem>
                    </Col>
                </Row>
                <Row>
                    <Col span="8">
                        <span @click="$router.push({name: 'Index'})" :style="{cursor: 'pointer'}"><<<返回主页</span>
                    </Col>
                    <Col span="8" offset="8" v-if="$route.meta.title=='用户登录'">
                        <span @click="$router.push({name: 'register'})" :style="{cursor: 'pointer'}">前往注册>>></span>
                    </Col>
                </Row>
            </Form>
        </div>
    </div>
</template>

<script>
import Action from './action/blogAdmin';
export default {
    data () {
        return {
            loginForm: {
                UserName: '',
                PassWord: '',
            }
        }
    },
    mounted () {
        this.$store.commit('showMenu', false);
    },
    methods: {
        //登录表单提交处理函数
        submitFormHandler () {
            Action.userLogin({
                PostContent: this.loginForm
            })
            .then(res => {
                if (res.status) {
                    this.$store.state.UserInfo = res.PostContent.map(item => {
                        item.Jurisdiction = item.Jurisdiction.split(',')
                        return item;
                    });
                    if (this.$route.meta.title=='用户登录') {
                        this.$router.push({name: 'Index'});
                    } else {
                        this.$router.push({name: 'paramsSettings'});
                    }
                }
            })
            .catch(err => {
                if(err.type === 'local') return this.$Message.warning(err.Msg);
                this.$Message.error(err);
            })
            /*Action.submitLoginForm(this.loginForm)
            .then(res => {
                console.log(res);
            })
            .catch(err => {
                this.$Message.error('发生了错误，请联系管理员');
                console.log(err);
            })*/
        }
    }
}
</script>
