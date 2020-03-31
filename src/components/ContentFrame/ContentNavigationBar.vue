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
                            {{ IsLogin ? userInfo.UserName : '游客' }}
                            <Icon type="md-arrow-dropdown" size="24" />
                        </a>
                        <DropdownMenu v-show="$store.state.IsLogin" slot="list" :style="{textAlign: 'center'}">
                            <DropdownItem name="logout">退出登录</DropdownItem>
                        </DropdownMenu>

                        <DropdownMenu v-show="!$store.state.IsLogin" slot="list" :style="{textAlign: 'center'}">
                            <DropdownItem name="userinfo">登录</DropdownItem>
                            <DropdownItem name="company">注册</DropdownItem>
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
    computed: {
        pageNavShrink(){ return this.$store.state.pageNavShrink },
        IsLogin(){return this.$store.state.IsLogin},
        userInfo(){ return JSON.parse(localStorage.getItem('UserInfo'))},
        userHeadImg(){
            return false;
        },
        showMenu(){return this.$store.state.showMenu;}
    },
    methods: {
    	//用户工具栏点击时处理函数
        userToolHandler(name){
            
        },
        //用户退出时处理函数
        userLogoutHandler(){
            
        }
    }
    
}
</script>