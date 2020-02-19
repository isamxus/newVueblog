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
                            <i :style="{fontSize: '1.8rem'}" class="iconfont icon-icon-user-img"></i>
                        </div>
                        <a href="javascript:void(0)">
                            {{ userInfo ? userInfo.UserName : '&lt;unknown&gt;' }}
                            <Icon type="arrow-down-b"></Icon>
                        </a>
                        <DropdownMenu slot="list" :style="{textAlign: 'center'}">
                            <DropdownItem name="userinfo">个人信息</DropdownItem>
                            <DropdownItem name="company">我的企业</DropdownItem>
                            <DropdownItem name="logout" divided>退出</DropdownItem>
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
        userInfo(){ return this.$store.state.userInfo },
        userHeadImg(){
            return false;
        },
        showMenu(){return this.$store.state.showMenu;}
    },
    methods: {
    	//用户工具栏点击时处理函数
        userToolHandler(name){
            switch(name){
                case 'logout':
                    this.userLogoutHandler();
                    break;
                case 'userinfo':
                    this.$router.push({path: '/PersonalSettings/PersonalSetting'});
                    break;
                case 'company': 
                    this.$router.push({path: '/PersonalSettings/EnterpriseApplyInfo'});
                    break;
                    
            }
        },
        //用户退出时处理函数
        userLogoutHandler(){
            
        }
    }
    
}
</script>