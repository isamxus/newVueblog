<style lang="scss">
    @import './sass/paramsSettings';
</style>

<template>
  	<SubNavigationFrame :title="$route.meta.title" :breadcrumb="breadcrumbs">
        <div  slot="navigation" :style="{textAlign:'right',marginTop:'-2.5rem'}">
            <Button @click="$router.push({name: 'Index'})">返回主站</Button>
        </div>
        <div class="sub-page-container" :style="{'margin-top': '.5rem','padding-top':'1rem'}" slot="content">
        	<Row>
    			<Col span="8">
    				<div :style="{marginBottom: '.7rem'}">
    					<Button type="primary"  @click="paramsModal = true"><Icon type="md-add"></Icon>新增博客参数</Button>
    				</div>
    			</Col>
    		</Row>
            <div >
                <Table  :columns="columns" :data="tableData"></Table>
            </div>
            <Modal
    			v-model="paramsModal"
    			:title="createParamsForm.edit ? '编辑博客参数' : '新增博客参数'"
    			width=600
    			@on-visible-change="$refs.createForm.resetFields()">
    			<div>
    				<Form 
    					ref="createForm"
    					:model="createParamsForm"
    					:rules="createParamsRules">
    					<Row>
    						<Col span="24">
    							<FormItem class="item-box" label="参数名称：" prop="paramsName">
    								<Input v-model="createParamsForm.paramsName" placeholder="请输入参数名称" />
    							</FormItem>
    						</Col>
    						<Col span="24">
    							<FormItem class="item-box" label="参数权限码：" prop="paramsCode">
    								<Input v-model="createParamsForm.paramsCode" placeholder="请输入参数权限码" />
    							</FormItem>
    						</Col>
    					</Row>
    				</Form>
    			</div>
    			<div slot="footer">
    				<Button type="primary" @click="createParamsForm.edit ? updateParamsHandler() :createParamsHandler()">确定</Button>
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
		paramsName: '',
		paramsCode: '',
		edit: false
	}
}

export default {
    data () {
        return {
        	paramsModal: false,
        	breadcrumbs:[
                {title:'参数设置'},
            ],
            columns:[
                {title:'博客参数',key:'paramsName'},
                {title:'操作', align: 'center', render:this.toolColumnRender}
            ],
            tableData:[],
            createParamsForm: dataFactory(),
            createParamsRules: {
                paramsName: [{required: true, message: '请输入参数名称'}],
                paramsCode: [{required: true, message: '请输入参数权限码'}]
            },
        }
    },
    components: {
    	SubNavigationFrame
    },
    mounted () {
    	//获取参数列表
    	this.getParamsListHandler();
    },
    methods: {
    	//操作列渲染
        toolColumnRender(h, params) {
            return h('div', [
            	   h('Button',{
                        props:{type:'text'},
                        domProps:{innerText: '设置'},
                        on:{click: e => {
                        	let name;
                        	let Code = params.row.paramsCode;
                        	if (Code === '0001' || Code === '0003') name = 'paramsDetailPage';
                            if (Code === '0002') name = 'articleListPage';
                        	if (name) {
                        		this.$router.push({
                        			name: name,
                        			query: {
                        				paramsName: params.row.paramsName,
                        				Code: Code,
                        				id: params.row.id
                        			}
                        		})
                        	}
                        }
                    }
                }),
                   h('Button',{
                        props:{type:'text'},
                        domProps:{innerText: '编辑'},
                        on:{click: e => {
                            this.createParamsForm = dataFactory({
                            	paramsName: params.row.paramsName,
                            	paramsCode: params.row.paramsCode,
                            	edit: true,
                            	id: params.row.id
                            })
                            this.paramsModal = true;
                            e.stopPropagation();
                        }
                    }
                }),
                   h('Button',{
                       	props:{type:'text'},
                       	domProps:{innerText: '删除'},
                       	on:{click: e => {
                       		this.deleteParamsHandler(params.row.id);
                            e.stopPropagation();
                       }
                    }
                })
            ]);
        },
    	//添加参数
    	createParamsHandler(){
  			Action.paramsCreate({
  				PostContent: this.createParamsForm
  			})
			.then(res => {
				this.getParamsListHandler();
				this.paramsModal = false;
			})
			.catch(err => {
				if(err.type === 'local') return this.$Message.warning(err.Msg);
				this.$Message.error(err);
			})
    	},
    	//更新参数
    	updateParamsHandler(){
  			Action.paramsUpdate({
  				PostContent: this.createParamsForm
  			})
			.then(res => {
				this.getParamsListHandler();
				this.paramsModal = false;
			})
			.catch(err => {
				if(err.type === 'local') return this.$Message.warning(err.Msg);
				this.$Message.error(err);
			})
    	},
    	//删除参数
    	deleteParamsHandler(ID){
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
                    Action.paramsDelete({
                        PostContent: {
                        	id: ID
                        }
                    }).then(result => {
                        this.$Message.success('成功删除参数！！！');
                        this.$Modal.remove()
                        this.getParamsListHandler();
                    })
                    .catch(err => {
                        this.$Modal.remove()
                        this.$Message.error(err);
                    });
                }
            });
    	},
    	////获取参数列表
    	getParamsListHandler(){
    		Action.paramsGetList()
			.then(res => {
				this.tableData = res;
			})
			.catch(err => {
				this.$Message.error(err);
			})
    	}
    }
}
</script>
