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
                        <Checkbox  v-model="value.IsSelected"  v-for="(value, key) in item.children" :key="key" >{{ value.Name }}</Checkbox>
                    </div>
                    
                </div>
                <div slot="footer">
                    <Button type="primary" @click="checkBoxselHandler">确定</Button>
                    <Button @click="popModal=false">取消</Button>
                </div>
            </Modal>
        </div>  
    </SubNavigationFrame>
</template>

<script>
import Action from './action/usersManagement';
import SubNavigationFrame from '../../components/SubNavigationFrame/SubNavigationFrame';


const dataFactory = () => {
    return  [
                {
                    title: '页面权限',
                    children: [
                        { Name: '博客首页', Code: '00', IsSelected: false},
                        { Name: '后台管理', Code: '01', IsSelected: false}
                    ] 
                },
                {
                    title: '参数权限',
                    children: [
                        { Name: '文章分类', Code: '0001', IsSelected: false},
                        { Name: '文章设置', Code: '0002', IsSelected: false},
                        { Name: '文章标签', Code: '0003', IsSelected: false},
                        { Name: '文章评论', Code: '0004', IsSelected: false},
                        { Name: '用户管理', Code: '0005', IsSelected: false},
                        { Name: '首页Tab页', Code: '0006', IsSelected: false},
                    ]
                }
            ]
}
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
            AuthList: dataFactory(),
            allSelected: [],
            user_id: ''
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
        //获取用户列表
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
                            this.user_id = params.row.user_id;
                            //校验权限
                            let JusList = params.row.Jurisdiction.split(',');
                            this.AuthList = dataFactory();  
                            let fn = arr => {
                                for (let i = 0; i < arr.length; i++) {
                                    if (arr[i].children && arr[i].children.length>0) {
                                        fn(arr[i].children);
                                        continue
                                    }
                                    if (JusList.findIndex(item => item == arr[i].Code) != -1) {
                                        arr[i].IsSelected = true;
                                    }
                                }
                            }
                            fn(this.AuthList);
                            e.stopPropagation();
                        }
                    }
                }),

                   h('Button',{
                        props:{type:'text'},
                        domProps:{innerText: '删除'},
                        on:{click: e => {
                            if (params.row.IsSuperUser) return this.$Message.warning('无法删除超级用户！！！')
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
        checkBoxselHandler(){
            let allSelected = [];
            let fn = (arr) => {
                for(let i = 0; i < arr.length; i++){
                    if (arr[i].children && arr[i].children.length > 0) {
                        fn(arr[i].children);
                        continue;
                    }
                    if (arr[i].IsSelected) {
                        allSelected.push(arr[i].Code);
                    }
                }
            }
            fn(this.AuthList);

            //发起更新用户权限请求
            Action.userUpdate({
                PostContent: {
                    user_id: this.user_id,
                    Jurisdiction: allSelected.join(',')
                }
            })
            .then(res => {
                this.getUsersListHandler();
                this.popModal = false;
            })
            .catch(err => {
                this.$Message.error(err);
            })
        }
    }
}
</script>