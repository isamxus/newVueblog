<style lang="scss">
    @import './sass/articleDetail';
</style>

<template>
    <SubNavigationFrame :title="$route.meta.title" :breadcrumb="breadcrumbs">
        <div  slot="navigation" :style="{textAlign:'right',marginTop:'-2.5rem'}">
            <Button @click="$router.go(-1)">返回</Button>
        </div>
        <div class="article-detail-page-container" slot="content">
            <div class="article-content-part">
                <h2 :style="{textAlign: 'center'}">{{ articleDetailData.articleTitle }}</h2>
                <div :style="{display: 'flex', justifyContent: 'center', margin: '.7rem'}">
                    <span><Icon type="md-browsers" />分类：{{ articleDetailData.articleCagetoryName }}</span>
                    <span><Icon type="ios-pricetags" />标签：{{ articleDetailData.articleTagsName }}</span>
                    <span><Icon type="md-time" />{{ articleDetailData.CreateTime }}</span>
                </div>
                <p :style="{textIndent: '.7rem'}" v-html="articleDetailData.articleContent"></p>
            </div>
            <div class="comment-content-part">
                
            </div>
        </div>
        
    </SubNavigationFrame>
</template>

<script>
import SubNavigationFrame from '../../components/SubNavigationFrame/SubNavigationFrame';
import Action from './action/articleDetail';
export default {
    data () {
        return {
            articleDetailData: {

            },
            breadcrumbs:[
                {title: this.$route.meta.title}
            ],
        }
    },
    components: {
        SubNavigationFrame
    },
    mounted () {
        this.getAricleDetailHandler();
    },
    methods: {
        //根据ID获取文章
        getAricleDetailHandler(){
            Action.articleGetSingle({
                PostContent: {
                    id: this.$route.query.id
                }
            })
            .then(res => {
                this.articleDetailData = res;
                res.CreateTime = new Date(res.CreateTime).Format('yyyy-MM-dd');
            })
            .catch(err => {
                this.$Message.error(err);
            })
        },
    }
}
</script>
