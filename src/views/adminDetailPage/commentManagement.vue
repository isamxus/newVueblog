<style lang="scss">
    @import './sass/commentManagement';
</style>

<template>
  	<SubNavigationFrame :title="$route.query.paramsName" :breadcrumb="breadcrumbs">
  		<div  slot="navigation" :style="{textAlign:'right',marginTop:'-2.5rem'}">
            <Button @click="$router.push({name: 'Index'})">返回主站</Button>
            <Button @click="$router.go(-1)">返回</Button>
        </div>
        <div class="sub-page-container" :style="{'margin-top': '.5rem','padding-top':'1rem'}" slot="content">
            <div :style="{overflow: 'auto'}">
                <Table :style="{minWidth: '1400px'}" :columns="columns" :data="commentListData"></Table>
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
import Action from './action/commentManagement';
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
                {title:'评论者',key:'commentAuthor', width: 120},
                {title:'评论内容', key:'commentContent', width: 400},
                {title:'所属文章', key:'parentArticleTitle', width: 200},
                {title:'创建时间', key:'CreateTime',width: 220, render: this.TimeRender},
                {title:'操作', align: 'center', render:this.toolColumnRender}
            ],
            commentListData: [],
            PageCount: 0,
            PageNumber: 1,
            PageSize: 10
        }
    },
    components: {
        SubNavigationFrame
    },
    mounted () {
       this.getCommentListHandler();
    },
    methods: {
        //时间渲染
        TimeRender(h, params) {
            return h('span', {domProps:{innerText:new Date(params.row.CreateTime).Format("yyyy-MM-dd hh:mm")}});
        },
        //获取评论列表
        getCommentListHandler(){
            Action.commentGetPageList({
                PostContent: {
                    _OrderBy: '-CreateTime',
                    PageSize: this.PageSize,
                    PageNumber: this.PageNumber
                }
            })
            .then(res => {
                this.commentListData = res.Items.map(item => {
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
                /*
                   h('Button',{
                        props:{type:'text'},
                        domProps:{innerText: '编辑'},
                        on:{click: e => {
                            e.stopPropagation();
                        }
                    }
                }),*/
                   h('Button',{
                        props:{type:'text'},
                        domProps:{innerText: '删除'},
                        on:{click: e => {
                            this.deleteCommentHandler(params.row.id)
                            e.stopPropagation();
                       }
                    }
                })
            ]);
        },
         //删除评论
        deleteCommentHandler(ID){
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
                    Action.commentDelete({
                        PostContent: {
                            id: ID
                        }
                    }).then(result => {
                        this.$Message.success('成功删除评论！！！');
                        this.$Modal.remove()
                        this.getCommentListHandler();
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