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
                                <FormItem class="item-box" label="名称：" prop="paramsName">
                                    <Input v-model="createDetailForm.paramsName" placeholder="请输入名称" />
                                </FormItem>
                            </Col>
                            <Col span="24">
                                <FormItem class="item-box" label="权限码：" prop="paramsCode">
                                    <Input v-model="createDetailForm.paramsCode" placeholder="请输入权限码" />
                                </FormItem>
                            </Col>
                        </Row>
                    </Form>
                </div>
                <div slot="footer">
                    <Button type="primary" @click="">确定</Button>
                    <Button @click="paramsModal=false">取消</Button>
                </div>
            </Modal>
        </div>
    </SubNavigationFrame>
</template>

<script>
import Action from './action/paramsSettings';
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
                paramsName: [{required: true, message: '请输入名称'}],
                paramsCode: [{required: true, message: '请输入权限码'}]
            },
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
                            e.stopPropagation();
                       }
                    }
                })
            ]);
        },
    	//根据参数权限码显示页面
        paramsShowHandler(){
            let Code = this.$route.query.Code;
            //博客文章分类设置
            if (Code === '0001') {

            }
        }
    }
}
</script>
