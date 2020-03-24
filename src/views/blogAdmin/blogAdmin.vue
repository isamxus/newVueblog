<style lang="scss" scoped>
    @import './sass/blogAdmin';
</style>

<template>
    <div class="login-container">
        <div class="login-form-contain">
            <Row>
                <Col span="24">
                    <h1>博客后台管理系统</h1>
                    <h2>Blog Management System</h2>
                </Col>
            </Row>
            <Form class="login-form">
                <Row>
                    <Col span="20" offset="2">
                        <FormItem prop="User">
                            <Input v-model="loginForm.username" type="text" placeholder="请输入用户名称" size="large">
                                <Icon size="24" type="ios-person-outline" slot="prepend"></Icon>
                            </Input>
                        </FormItem>
                    </Col>
                    <Col span="20" offset="2">
                        <FormItem prop="Password">
                            <Input v-model="loginForm.password" type="text" placeholder="请输入登录密码" size="large">
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
                username: '',
                password: ''
            }
        }
    },
    mounted () {
        this.$store.commit('showMenu', false);
    },
    methods: {
        //登录表单提交处理函数
        submitFormHandler () {
            this.$router.push({name: 'paramsSettings'});
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
