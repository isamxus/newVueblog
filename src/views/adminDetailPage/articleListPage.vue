<style lang="scss">
    @import './sass/articleListPage';
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
                        <Button type="primary"  @click="$router.push({name: 'addArticle'})"><Icon type="md-add"></Icon>新增{{$route.query.paramsName}}</Button>
                    </div>
                </Col>
            </Row>
            <div :style="{overflow: 'auto'}">
                <Table :style="{minWidth: '1000px'}" :columns="columns" :data="tableData"></Table>  
            </div>
            <!-- 分页 -->
            <Page
                :style="{paddingTop: '1rem',textAlign: 'center'}"
                :total="PageCount"
                :current="PageNumber"
                :page-size="PageSize"
                placement="top"
                @on-change="e => {PageNumber=e, getAricleListHandler()}" 
                @on-page-size-change="(size) => { PageSize = size, getAricleListHandler() }"
                show-elevator
                show-total
                show-sizer />
            </Page>
        </div>  
    </SubNavigationFrame>
</template>

<script>
import Action from './action/articleListPage';
import SubNavigationFrame from '../../components/SubNavigationFrame/SubNavigationFrame';
//<quill-editor  style="height: 20rem" />
export default {
    name: 'articleListPage',
    data () {
        return {
            breadcrumbs:[
                {title: this.$route.query.paramsName}
            ],
            columns:[
                {title: '序号', type: 'index', width: 120},
                {title:'文章标题',key:'articleTitle'},
                {title:'作者', key:'articleAuthor'},
                {title:'摘要', key:'articleAbstract'},
                {title:'标签', key:'articleTagsName'},
                {title:'创建时间', key:'CreateTime', render: this.TimeRender},
                {title:'操作', align: 'center', render:this.toolColumnRender}
            ],
            tableData: [],
            PageCount: 0,
            PageNumber: 1,
            PageSize: 10
        }
    },
    components: {
        SubNavigationFrame
    },
    mounted () {
        this.$store.commit('showAdminMenu', true);
        this.getAricleListHandler();
    },
    methods: {
        //时间渲染
        TimeRender(h, params) {
            return h('span', {domProps:{innerText:new Date(params.row.CreateTime).Format("yyyy-MM-dd hh:mm")}});
        },
        //操作列渲染
        toolColumnRender(h, params) {
            return h('div', [
                   h('Button',{
                        props:{type:'text'},
                        domProps:{innerText: '编辑'},
                        on:{click: e => {
                            this.$router.push({
                                name: 'addArticle',
                                query: {
                                    id: params.row.article_id
                                }
                            })
                            e.stopPropagation();
                        }
                    }
                }),
                   h('Button',{
                        props:{type:'text'},
                        domProps:{innerText: '删除'},
                        on:{click: e => {
                            this.deleteAricleHandler(params.row.article_id)
                            e.stopPropagation();
                       }
                    }
                })
            ]);
        },
        //获取文章列表
        getAricleListHandler(){
            Action.articleGetPageList({
                PostContent: {
                    _OrderBy: '-CreateTime',
                    PageSize: this.PageSize,
                    PageNumber: this.PageNumber
                }
            })
            .then(res => {
                this.tableData = res.Items;
                this.PageCount = res.TotalItems;
            })
            .catch(err => {
                this.$Message.error(err);
            })
        },
         //删除参数详情
        deleteAricleHandler(ID){
            if (!ID) return this.$Message.warning('参数ID为空，无法删除！！！');
            const modal = this.$Modal.confirm({
                title: '操作确认'
                ,icon: 'warning'
                ,content: '是否删除此文章'
                ,okText: '确定'
                ,showCancel: true
                ,loading: true
                ,onOk: () => {
                    //发起删除参数请求
                    Action.articleDelete({
                        PostContent: {
                            article_id: ID
                        }
                    }).then(result => {
                        this.$Message.success('成功删除文章！！！');
                        this.$Modal.remove()
                        this.getAricleListHandler();
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