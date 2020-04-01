<style lang="scss">
    @import './sass/usersManagement';
</style>

<template>
  	<SubNavigationFrame :title="$route.query.paramsName" :breadcrumb="breadcrumbs">
  		<div  slot="navigation" :style="{textAlign:'right',marginTop:'-2.5rem'}">
            <Button @click="$router.push({name: 'Index'})">返回主站</Button>
            <Button @click="$router.go(-1)">返回</Button>
        </div>
        <div class="sub-page-container" :style="{'margin-top': '.5rem','padding-top':'1rem'}" slot="content">
            <div :style="{overflow: 'auto'}">
                <Table :columns="columns" :data="usersListData"></Table>
            </div>
            <!-- 分页 -->
            <Page
                :style="{paddingTop: '1rem',textAlign: 'center'}"
                :total="PageCount"
                :current="PageNumber"
                :page-size="PageSize"
                placement="top"
                @on-change="e => {PageNumber=e, getUsersListHandler()}" 
                @on-page-size-change="(size) => { PageSize = size, getUsersListHandler()}"
                show-elevator
                show-total
                show-sizer />
            </Page>
            <Modal
                v-model="popModal"
                :title="'设置用户权限'"
                width=600>
                <div v-for="(item, index) in AuthList" :key="index">
                    <h4>{{ item.title }}</h4>
                    <div :style="{padding: '.7rem'}">
                        <Checkbox border   v-for="(value, key) in item.children" :key="key" @on-change="e => checkBoxselHandler(e, value)">{{ value.Name }}</Checkbox>
                    </div>
                    
                </div>
                <div slot="footer">
                    <Button type="primary" @click="">确定</Button>
                    <Button @click="popModal=false">取消</Button>
                </div>
            </Modal>
        </div>  
    </SubNavigationFrame>
</template>

<script>
import Action from './action/usersManagement';
import SubNavigationFrame from '../../components/SubNavigationFrame/SubNavigationFrame';
//<quill-editor  style="height: 20rem" />
export default {
    name: 'commentManagement',
    data () {
        return {
            breadcrumbs:[
                {title: this.$route.query.paramsName}
            ],
            columns:[
                {title: '序号', type: 'index', width: 120},
                {title:'用户名',key:'UserName', width: 120},
                {title:'创建时间', key:'CreateTime',width: 220, render: this.TimeRender},
                {title:'操作', align: 'center', render:this.toolColumnRender}
            ],
            usersListData: [],
            PageCount: 0,
            PageNumber: 1,
            PageSize: 10,
            popModal: false,
            checkAllGroup: [],
            AuthList: [
                {
                    title: '页面权限',
                    children: [
                        { Name: '博客首页', Code: '00', IsSelect: false},
                        { Name: '后台管理', Code: '01', IsSelect: false}
                    ] 
                }
            ]
        }
    },
    components: {
        SubNavigationFrame
    },
    mounted () {
        this.$store.commit('showAdminMenu', true);
        this.getUsersListHandler();
    },
    methods: {
        //时间渲染
        TimeRender(h, params) {
            return h('span', {domProps:{innerText:new Date(params.row.CreateTime).Format("yyyy-MM-dd hh:mm")}});
        },
        //获取评论列表
        getUsersListHandler(){
            Action.userGetPageList({
                PostContent: {
                    _OrderBy: '-CreateTime',
                    PageSize: this.PageSize,
                    PageNumber: this.PageNumber
                }
            })
            .then(res => {
                this.usersListData = res.Items.map(item => {
                    item.CreateTime = new Date(item.CreateTime).Format('yyyy-MM-dd hh:mm');
                    return item;
                });
                this.PageCount = res.TotalItems;
            })
            .catch(err => {
                this.$Message.error(err);
            })
        },
        //操作列渲染
        toolColumnRender(h, params) {
            return h('div', [
                   h('Button',{
                        props:{type:'text'},
                        domProps:{innerText: '编辑'},
                        on:{click: e => {
                            this.popModal = true;
                            e.stopPropagation();
                        }
                    }
                }),
                   h('Button',{
                        props:{type:'text'},
                        domProps:{innerText: '删除'},
                        on:{click: e => {
                            this.deleteUserHandler(params.row.user_id);
                            e.stopPropagation();
                       }
                    }
                })
            ]);
        },
        //删除参数
        deleteUserHandler(ID){
            if (!ID) return this.$Message.warning('参数ID为空，无法删除！！！');
            const modal = this.$Modal.confirm({
                title: '操作确认'
                ,icon: 'warning'
                ,content: '是否删除此用户'
                ,okText: '确定'
                ,showCancel: true
                ,loading: true
                ,onOk: () => {
                    //发起删除参数请求
                    Action.userDelete({
                        PostContent: {
                            user_id: ID
                        }
                    }).then(result => {
                        this.$Message.success('成功删除用户！！！');
                        this.$Modal.remove()
                        this.getUsersListHandler();
                    })
                    .catch(err => {
                        this.$Modal.remove()
                        this.$Message.error(err);
                    });
                }
            });
        },
        //选择权限处理函数
        /*authSelectHandler(data, arr){
            console.log(data)
        },*/
        //复选框选中处理函数
        checkBoxselHandler(e, value){
            console.log(value)
        }
    }
}
</script>