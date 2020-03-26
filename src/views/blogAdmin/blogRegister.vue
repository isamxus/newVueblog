<style lang="scss" scoped>
    @import './sass/blogRegister';
</style>

<template>
    <div class="login-container">
        <div class="login-form-contain">
            <Row>
                <Col span="24">
                    <h1>用户注册</h1>
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
                            <Input v-model="loginForm.PassWord" type="text" placeholder="请输入你的密码" size="large">
                                <Icon size="24" type="ios-lock-outline" slot="prepend"></Icon>
                            </Input>
                        </FormItem>
                    </Col>
                    <Col span="20" offset="2">
                        <FormItem prop="Password">
                            <Input v-model="loginForm.passwordConfirm" type="text" placeholder="请再次输入密码" size="large">
                                <Icon size="24" type="ios-lock-outline" slot="prepend"></Icon>
                            </Input>
                        </FormItem>
                    </Col>
                    <Col span="8" offset="8">
                        <FormItem prop="User">
                            <Button type="primary" size="large" long @click="createUserHandler">确定</Button>
                        </FormItem>
                    </Col>
                </Row>
                <Row>
                    <Col span="8">
                        <span :style="{cursor: 'pointer'}" @click="$router.push({name: 'login'})"><<<返回登陆页面</span>
                    </Col>
                </Row>
            </Form>
        </div>
    </div>
</template>

<script>
import Action from './action/blogRegister';
export default {
    data () {
        return {
            loginForm: {
                UserName: '',
                PassWord: '',
                PassWordConfirm: ''
            }
        }
    },
    mounted () {
        this.$store.commit('showMenu', false);
    },
    methods: {
        //添加参数
        createUserHandler(){
            Action.userCreate({
                PostContent: this.loginForm
            })
            .then(res => {
               
            })
            .catch(err => {
                this.$Message.error(err);
            })
        },
    }
}
</script>
