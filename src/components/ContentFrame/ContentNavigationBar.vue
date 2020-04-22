<style lang="scss">
    @import './sass/ContentNavigationBar';
</style>

<template>
	<div class="content-navigation-bar" :style="{left: !showMenu ? 0 : pageNavShrink ? '3.5rem' : '12rem', paddingLeft: showMenu ? null : 0}">
		<Button :class="{'toggle-lev-nav':true,'mirror':pageNavShrink}" v-if="showMenu" type="text" @click="$store.commit('pageNavShrink',!$store.state.pageNavShrink)">
            <Icon type="ios-list" />
        </Button>
        <div class="navigation-tool">
            <slot name="navigation" />
        	<div class="base-tool">
                <!-- 消息通知 -->
                <Tooltip content="您有1条未读消息" v-if="false">
                    <Button type="text">
                        <Badge dot>
                            <Icon type="ios-bell" size="26"></Icon>
                        </Badge>
                    </Button>
                </Tooltip>
                <div class="drop-down-tool">
                    <!-- 用户头像&用户名 -->
                    <Dropdown @on-click="userToolHandler">
                        <img :src="userHeadImg" v-if="userHeadImg">
                        <div :style="{display: 'flex',alignItems: 'center'}" v-else>
                            <Icon type="md-contact" size="36" />
                        </div>
                        <a href="javascript:void(0)">
                            {{ userInfo ? userInfo.UserName : '游客' }}
                            <Icon type="md-arrow-dropdown" size="24" />
                        </a>
                        <DropdownMenu @on-click="userToolHandler" v-show="$store.state.IsLogin" slot="list" :style="{textAlign: 'center'}">
                            <DropdownItem  name="usersettings">个人信息</DropdownItem>
                            <DropdownItem  name="logout">退出登录</DropdownItem>
                        </DropdownMenu>

                        <DropdownMenu v-show="!$store.state.IsLogin" slot="list" :style="{textAlign: 'center'}" @on-click="userToolHandler">
                            <DropdownItem name="userinfo">登录</DropdownItem>
                            <DropdownItem name="register">注册</DropdownItem>
                        </DropdownMenu>
                    </Dropdown>
                </div>
            </div>
        </div>
	</div>
</template>

<script>
export default {
	props:{
        
    },
    data () {
        return {
            UserName: ''
        }
    },
    computed: {
        pageNavShrink(){ return this.$store.state.pageNavShrink },
        IsLogin(){return this.$store.state.IsLogin},
        userInfo(){ return this.$store.state.UserInfo},
        userHeadImg(){
            return false;
        },
        showMenu(){return this.$store.state.showMenu;},
    },
    mounted () {

    },
    methods: {
    	//用户工具栏点击时处理函数
        userToolHandler(name){
            if (name == 'userinfo') {
                this.$router.push({
                    name: 'login'
                })
            }
            if (name == 'register') {
                this.$router.push({
                    name: 'register'
                })
            }
            if (name == 'usersettings') {
                this.$router.push({
                    name: 'userSettings'
                })
            }
            if (name == 'logout') {
                const modal = this.$Modal.confirm({
                    title: '操作确认'
                    ,icon: 'warning'
                    ,content: '是否退出登录'
                    ,okText: '确定'
                    ,showCancel: true
                    ,loading: true
                    ,onOk: () => {

                        this.$Modal.remove();
                        localStorage.removeItem('Token');
                        this.$store.state.IsLogin = false;
                        this.$Message.warning('你已退出登录！！！')
                        if (window.location.href.search('adminDetailPage') != -1) {
                            this.$router.push({
                                name: 'blogAdmin'
                            })
                        }
                    }
                });
            }
        },
    }
    
}
</script>