<template>
    <Menu :theme="theme" :width="width" :active-name="activeName" :open-names="openNames" @on-select="itemClickHandler">
        <template v-for="(item,index) in items">
            <MenuItem :name="index" v-if="!item.children || item.children.length < 1" :key="item.name">
                <Icon :type="item.icon" />
                {{item.title}}
            </MenuItem>
            <Submenu :name="index" :key="item.name" v-else>
                <template slot="title">
                    <Icon :type="item.icon" />
                    {{item.title}}
                </template>
                <MenuItem  :name="index + '-' + subIndex" v-for="(subItem,subIndex) in item.children" :key="subItem.name">
                    <Icon :type="subItem.icon" />
                    {{subItem.title}}
                </MenuItem>
            </Submenu>
        </template>
    </Menu>
</template>

<script>

export default {
    props:{
        items: Array
        ,activeName: String
        ,openNames: {
            type: Array
            ,default: ()=>{return []}
        }
        ,width: String
        ,theme: String
    }
    ,methods:{
        itemClickHandler(name){
            
            //通过name索引寻找item
            let index = name.toString().split('-'),buoy = this.items[index[0]];
            for(let i = 1;i < index.length;i++) buoy = buoy.children[index[i]];
            
            //触发事件
            this.$emit('item-click', buoy, name);
        }
    }
}
</script>
