<style lang="scss">
    @import './sass/articleCategory';
</style>

<template>
    <SubNavigationFrame :title="$route.meta.title" :breadcrumb="breadcrumbs">
        <div class="article-category-page-container" slot="content">
            <Row type="flex" justify="space-around">
                <Col span="11">
                    <Card :style="{height: '180px', cursor: 'pointer'}">
                        <p >Content of card</p>
                        <p>Content of card</p>
                        <p>Content of card</p>
                    </Card>
                </Col>
                <Col span="11">
                    <Card :style="{height: '180px', cursor: 'pointer'}">
                        <p>Content of card</p>
                        <p>Content of card</p>
                        <p>Content of card</p>
                    </Card>
                </Col>
            </Row>
            <!-- 分页 -->
            <Page
                :style="{paddingTop: '1rem',textAlign: 'center'}"
                :total="100"
                :current="1"
                :page-size="10"
                placement="top"
                show-elevator
                show-total
                show-sizer />
            </Page>
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
            data: [
                {
                    articleTitle: '模拟数据1',
                    articleAuthor: '模拟数据1',
                    articleAbstract: '模拟数据1',
                    articleCreateTime: '2019-08-11',
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
