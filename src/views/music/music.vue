<style lang="scss">
    @import './sass/music';
</style>

<template>
    <div class="music-container">
        <Row>
            <Button class="backButton" @click="$router.push({name: 'Index'})">返回</Button>
        </Row>
        <div class="music-body-part">
            <div class="music-body-left-part">
                
            </div>
            <div class="music-body-right-part">
                
            </div>
        </div>
    </div>
</template>

<script>
import Action from './action/music';
const dataFactory = params => Object.assign({
  
}, params);



export default {
    data () {
        return {
            
        }
    },
    components: {
        
    },
    computed: {

    },
    mounted () {
        this.$store.commit('showMenu', false);
    },
    methods: {
        
    }
}
</script>