<style lang="scss">
    @import './sass/articleListPage';
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
                        <Button type="primary"  @click="$router.push({name: 'addArticle'})"><Icon type="md-add"></Icon>新增{{$route.query.paramsName}}</Button>
                    </div>
                </Col>
            </Row>
            <Table :columns="columns" :data="tableData"></Table>
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
                {title:'文章标题',key:'articleTitle'},
                {title:'作者', key:'articleAuthor'},
                {title:'摘要', key:'articleAbstract'},
                {title:'标签', key:'articleTags'},
                {title:'创建时间', key:'CreateTime'},
                {title:'操作', align: 'center', render:this.toolColumnRender}
            ],
            tableData: []
        }
    },
    components: {
        SubNavigationFrame
    },
    mounted () {
        
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
    }
}
</script>