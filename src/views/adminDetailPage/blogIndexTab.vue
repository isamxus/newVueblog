<style lang="scss">
    @import './sass/blogIndexTab';
</style>

<template>
  	<SubNavigationFrame :title="$route.query.paramsName" :breadcrumb="breadcrumbs">
  		<div  slot="navigation" :style="{textAlign:'right',marginTop:'-2.5rem'}">
            <Button @click="$router.push({name: 'Index'})">返回主站</Button>
            <Button @click="$router.go(-1)">返回</Button>
        </div>
        <div class="sub-page-container" :style="{'margin-top': '.5rem','padding-top':'1rem'}" slot="content">
            <Row>
                <Col span="8">
                    <div :style="{marginBottom: '.7rem'}">
                        <Button type="primary" @click="resetFormHandler" ><Icon type="md-add"></Icon>自定义Tab页</Button>
                    </div>
                </Col>
            </Row>
            <Table  :columns="columns" :data="tabListData"></Table>
            <Modal
                v-model="popModal"
                :title="createTabForm.edit ? '编辑Tab页': '新增Tab页'"
                width=800>
                <Form 
                    :style="{marginBottom: '2.5rem'}"
                    ref="createForm"
                    :label-width="110"
                    :model="createTabForm"
                    :rules="createTabRules">
                    <Row>
                        <Col span="16">
                            <FormItem label="Tab页标题：" prop="IndexTabName">
                                <Input v-model="createTabForm.IndexTabName" placeholder="请输入Tab页标题" />
                            </FormItem>
                        </Col>
                    </Row>
                    <Row v-show="createTabForm.IndexTabCode != '000601'">
                        <Col span="16">
                            <FormItem label="Tab页码：" prop="IndexTabCode">
                                <Input v-model="createTabForm.IndexTabCode" placeholder="请输入Tab页码" />
                            </FormItem>
                        </Col>
                    </Row>
                    <Row>
                        <Col span="16">
                            <FormItem label="是否显示：" prop="IsShowTab">
                                <Switch v-model="createTabForm.IsShowTab">
                                    <span slot="open">是</span>
                                    <span slot="close">否</span>
                                </Switch>
                            </FormItem>
                        </Col>
                    </Row>
                    <Row v-show="createTabForm.IndexTabCode != '000601'">
                        <Col span="22">
                            <FormItem  label="Tab内容：" prop="IndexTabContent">
                                <quill-editor v-model="createTabForm.IndexTabContent" style="height: 18rem" />
                            </FormItem>
                        </Col>
                    </Row>
                </Form>
                <div slot="footer" >
                    <Button type="primary" @click="submitFormHandler">确定</Button>
                    <Button @click="popModal=false">取消</Button>
                </div>
            </Modal>
        </div>  
    </SubNavigationFrame>
</template>

<script>
import Action from './action/blogIndexTab';
import SubNavigationFrame from '../../components/SubNavigationFrame/SubNavigationFrame';

const dataFactory = params => Object.assign({
    IndexTabID: '',
    IndexTabName: '',
    IndexTabContent: '',
    IndexTabCode: '',
    IsShowTab: true,
    edit: false
}, params);


export default {
    name: 'articleListPage',
    data () {
        return {
            breadcrumbs:[
                {title: this.$route.query.paramsName}
            ],
            columns:[
                {title: '序号', type: 'index', width: 120},
                {title:'Tab标题',key:'IndexTabName'},
                {title:'操作', align: 'center', render:this.toolColumnRender}
            ],
            searchForm: dataFactory(),
            CategoryListData: [],
            TagListData: [],
            tableData: [],
            PageCount: 0,
            PageNumber: 1,
            PageSize: 10,
            tabListData: [],
            popModal: false,
            createTabForm: dataFactory(),
            createTabRules: {
                IndexTabName: [{required: true, message: '请输入Tab页标题'}],
                IndexTabCode: [{required: true, message: '请输入Tab页码'}]
            }
        }
    },
    components: {
        SubNavigationFrame
    },
    mounted () {
        this.$store.commit('showAdminMenu', true);
        this.getTabListHandler();
    },
    methods: {
        //操作列渲染
        toolColumnRender(h, params) {
            return h('div', [
                   h('Button',{
                        props:{type:'text'},
                        domProps:{innerText: '编辑'},
                        on:{click: e => {
                            e.stopPropagation();
                            this.popModal = true;
                            params.row.edit = true;
                            this.createTabForm = params.row;
                        }
                    }
                }),
                   h('Button',{
                        props:{type:'text'},
                        domProps:{innerText: '删除'},
                        on:{click: e => {
                            e.stopPropagation();
                            if (params.row.IndexTabCode == '000601') return this.$Message.warning('该Tab页不能手动删除')
                            this.deleteTabHandler(params.row.IndexTabID);
                       }
                    }
                })
            ]);
        },
        //重置表单
        resetFormHandler(){
            this.createTabForm = dataFactory();
            this.popModal = true;
        },
        //获取Tab页
        getTabListHandler(){
            Action.tabGetlist()
            .then(res => {
                this.tabListData = res;
            })
            .catch(err => {
                this.$Message.error(err);
            })
        },
        //创建Tab页
        submitFormHandler(){
            if (!this.createTabForm.IndexTabName) return this.$Message.warning('请输入Tab页标题');
            if (!this.createTabForm.IndexTabCode) return this.$Message.warning('请输入Tab页码');
            if(this.tabListData.find(item => item.IndexTabCode === this.createTabForm.IndexTabCode) && !this.createTabForm.edit) return this.$Message.warning('请勿输入重复的Tab页码');
            let submitData = objectCopy(this.createTabForm);
            Action[submitData.edit ? 'TabUpdate' : 'TabCreate']({
                PostContent: submitData
            })
            .then(res => {
                this.getTabListHandler();
                this.popModal = false;
            })
            .catch(err => {
                this.$Message.error(err);
            })
        },
        //删除Tab
        deleteTabHandler(ID){
            if (!ID) return this.$Message.warning('参数ID为空，无法删除！！！');
            const modal = this.$Modal.confirm({
                title: '操作确认'
                ,icon: 'warning'
                ,content: '是否删除此Tab页'
                ,okText: '确定'
                ,showCancel: true
                ,loading: true
                ,onOk: () => {
                    //发起删除参数请求
                    Action.TabDelete({
                        PostContent: {
                            IndexTabID: ID
                        }
                    }).then(result => {
                        this.$Message.success('成功删除Tab页！！！');
                        this.$Modal.remove()
                        this.getTabListHandler();
                    })
                    .catch(err => {
                        this.$Modal.remove()
                        this.$Message.error(err);
                    });
                }
            });
        },
    }
}
</script>