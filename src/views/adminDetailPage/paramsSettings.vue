<style lang="scss">
    @import './sass/paramsSettings';
</style>

<template>
  	<SubNavigationFrame :title="$route.meta.title" :breadcrumb="breadcrumbs">
  		<div  slot="navigation" :style="{textAlign:'right',marginTop:'-2.5rem'}">
            <Button @click="$router.go(-1)">返回</Button>
        </div>
        <div class="sub-page-container" :style="{'margin-top': '.5rem','padding-top':'1rem'}" slot="content">
        	<Row>
    			<Col span="8">
    				<div :style="{marginBottom: '.7rem'}">
    					<Button type="primary"  @click="paramsModal = true"><Icon type="md-add"></Icon>新增博客参数</Button>
    				</div>
    			</Col>
    		</Row>
            <Table :columns="columns" :data="tableData"></Table>

            <Modal
    			v-model="paramsModal"
    			title="新增博客参数"
    			width=600
    			@on-ok="createParamsHandler">
    			<div>
    				<Form>
    					<Row>
    						<Col span="24">
    							<FormItem class="item-box" label="参数名称：">
    								<Input v-model="createParamsForm.paramsName" placeholder="请输入参数名称" />
    							</FormItem>
    						</Col>
    						<Col span="24">
    							<FormItem class="item-box" label="参数权限码：">
    								<Input v-model="createParamsForm.paramsCode" placeholder="请输入参数权限码" />
    							</FormItem>
    						</Col>
    					</Row>
    				</Form>
    			</div>
    		</Modal>
        </div>
    </SubNavigationFrame>
</template>

<script>
import Action from './action/paramsSettings';
import SubNavigationFrame from '../../components/SubNavigationFrame/SubNavigationFrame';

export default {
    data () {
        return {
        	paramsModal: false,
        	breadcrumbs:[
                {title:'参数设置'},
            ],
            columns:[
                {title:'博客参数',key:'paramsName'},
                {title:'操作',width: 150,key:'btn',align: 'center'}
            ],
            tableData:[],
            createParamsForm: {
            	paramsName: '',
            	paramsCode: ''
            }
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
    	//添加参数
    	createParamsHandler(){
  			Action.paramsCreate({
  				PostContent: this.createParamsForm
  			})
			.then(res => {
				console.log(res);
			})
			.catch(err => {
				this.$Message.error(err);
			})
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
