<style lang="scss">
    @import './sass/articleCategory';
</style>

<template>
    <SubNavigationFrame :title="$route.meta.title" :breadcrumb="breadcrumbs">
        <div class="article-category-page-container" slot="content">
            <Table
                :columns="columns" 
                :data="data"/>
        </div>
    </SubNavigationFrame>
</template>

<script>
import SubNavigationFrame from '../../components/SubNavigationFrame/SubNavigationFrame';
import Action from './action/articleCategory';
export default {
    data () {
        return {
            breadcrumbs:[
                {title: '文章分类'},
                {title: this.$route.meta.title}
            ],
            columns: [
                {title: '序号', type: 'index'},
                {title: '标题',  key: 'articleTitle'},
                {title: '作者', key: 'articleAuthor'},
                {title: '文章摘要', key: 'articleAbstract'},
                {title: '创建时间', key: 'articleCreateTime'},
                {title: '操作',align: 'center',width: 180, render: this.toolColumnHandler}
            ],
            data: [
                {
                    articleTitle: '模拟数据1',
                    articleAuthor: '模拟数据1',
                    articleAbstract: '模拟数据1',
                    articleCreateTime: '模拟数据1',
                }
            ]
        }
    },
    components: {
        SubNavigationFrame
    },
    methods: {
        //操作列渲染函数
        toolColumnHandler(h, params){
            return h('div', [
                h('Button',{
                    props:{type:'text'}
                    ,domProps:{innerText: '进入阅读'}
                    ,on:{click: e => {
                        e.stopPropagation();
                    }}
                })
            ]);
        }
    }
}
</script>
