<style lang="scss">
    @import './sass/paramsDetailPage';
</style>

<template>
  	<SubNavigationFrame :title="$route.query.paramsName" :breadcrumb="breadcrumbs">
  		<div  slot="navigation" :style="{textAlign:'right',marginTop:'-2.5rem'}">
            <Button @click="$router.go(-1)">返回</Button>
        </div>
        <div class="sub-page-container" :style="{'margin-top': '.5rem','padding-top':'1rem'}" slot="content">
        	<Row>
                <Col span="8">
                    <div :style="{marginBottom: '.7rem'}">
                        <Button type="primary"  @click="paramsModal = true"><Icon type="md-add"></Icon>新增{{$route.query.paramsName}}</Button>
                    </div>
                </Col>
            </Row>
            <Table :columns="columns" :data="tableData"></Table>
            <Modal
                v-model="paramsModal"
                :title="createDetailForm.edit ? '编辑' + $route.query.paramsName : '新增' + $route.query.paramsName"
                width=600
                @on-visible-change="$refs.createForm.resetFields()">
                <div>
                    <Form 
                        ref="createForm"
                        :model="createDetailForm"
                        :rules="createDetailRules">
                        <Row>
                            <Col span="24">
                                <FormItem class="item-box" label="名称：" prop="detailName">
                                    <Input v-model="createDetailForm.detailName" placeholder="请输入名称" />
                                </FormItem>
                            </Col>
                            <Col span="24">
                                <FormItem class="item-box" label="权限码：" prop="detailCode">
                                    <Input v-model="createDetailForm.detailCode" placeholder="请输入权限码" />
                                </FormItem>
                            </Col>
                        </Row>
                    </Form>
                </div>
                <div slot="footer">
                    <Button type="primary" @click="createDetailForm.edit ? updateDetailHandler() : addDetailHandler()">确定</Button>
                    <Button @click="paramsModal=false">取消</Button>
                </div>
            </Modal>
        </div>
    </SubNavigationFrame>
</template>

<script>
import Action from './action/paramsDetailPage';
import SubNavigationFrame from '../../components/SubNavigationFrame/SubNavigationFrame';


const dataFactory = (params) => {
    return params ? params : {
        detailName: '',
        detailCode: '',
        detailParentParamID: '',
        detailParentParam: '',
        edit: false
    }
}


export default {
    data () {
        return {
            paramsModal: false,
            breadcrumbs:[
                {title: this.$route.query.paramsName},
            ],
            columns:[
                {title:'名称',key:'detailName'},
                {title:'操作', align: 'center', render:this.toolColumnRender}
            ],
            tableData:[],
            createDetailForm: dataFactory(),
            createDetailRules: {
                detailName: [{required: true, message: '请输入名称'}],
                detailCode: [{required: true, message: '请输入权限码'}]
            },
            filter: {
                detailParentParamID: this.$route.query.id,
                detailParentParamCode: this.$route.query.Code
            }
        }
    },
    components: {
    	SubNavigationFrame
    },
    mounted () {
        this.paramsShowHandler();
    },
    methods: {
        //操作列渲染
        toolColumnRender(h, params) {
            return h('div', [
                   h('Button',{
                        props:{type:'text'},
                        domProps:{innerText: '编辑'},
                        on:{click: e => {
                            this.createDetailForm = dataFactory({
                                detailName: params.row.detailName,
                                detailCode: params.row.detailCode,
                                detailParentParam: params.row.detailParentParam,
                                detailParentParamID: this.$route.query.id,
                                detailParentParamCode: this.$route.query.Code,
                                edit: true,
                                id: params.row.id
                            })
                            this.paramsModal = true;
                            e.stopPropagation();
                            e.stopPropagation();
                        }
                    }
                }),
                   h('Button',{
                        props:{type:'text'},
                        domProps:{innerText: '删除'},
                        on:{click: e => {
                            this.deleteDetailHandler(params.row.id)
                            e.stopPropagation();
                       }
                    }
                })
            ]);
        },
    	//根据参数权限码显示页面
        paramsShowHandler(){
            let _filter = objectCopy(this.filter);
            for (let i in _filter) {
                if (!_filter[i]) delete _filter[i]
            }
            Action.paramsDetailGetList({
                PostContent: {
                    filter: _filter
                }
            })
            .then(res => {
                this.tableData = res;
            })
            .catch(err => {
                this.$Message.error(err);
            })
        },
        //添加参数详情
        addDetailHandler(){
            this.createDetailForm.detailParentParamID = this.$route.query.id;
            this.createDetailForm.detailParentParamCode = this.$route.query.Code;
            this.createDetailForm.detailParentParam = this.$route.query.paramsName;

            Action.paramsDetailCreate({
                PostContent: this.createDetailForm
            })
            .then(res => {
                this.paramsModal = false;
                this.paramsShowHandler();
            })
            .catch(err => {
                this.$Message.error(err);
            })
        },
        //更新参数详情
        updateDetailHandler(){
            Action.paramsDetailUpdate({
                PostContent: this.createDetailForm
            })
            .then(res => {
                this.paramsModal = false;
                this.paramsShowHandler();
            })
            .catch(err => {
                this.$Message.error(err);
            })
        },
        //删除参数详情
        deleteDetailHandler(ID){
            if (!ID) return this.$Message.warning('参数ID为空，无法删除！！！');
            const modal = this.$Modal.confirm({
                title: '操作确认'
                ,icon: 'warning'
                ,content: '是否删除此参数'
                ,okText: '确定'
                ,showCancel: true
                ,loading: true
                ,onOk: () => {
                    //发起删除参数请求
                    Action.paramsDetailDelete({
                        PostContent: {
                            id: ID
                        }
                    }).then(result => {
                        this.$Message.success('成功删除参数！！！');
                        this.$Modal.remove()
                        this.paramsShowHandler();
                    })
                    .catch(err => {
                        this.$Modal.remove()
                        this.$Message.error(err);
                    });
                }
            });
        }
    }
}
</script>
