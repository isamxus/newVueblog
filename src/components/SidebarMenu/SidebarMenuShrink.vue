<template>
    <div :style="{width:width, textAlign: 'center',margin:'auto'}" :active-name="activeName">
        <template v-for="(item,index) in items">
            <Tooltip :style="{display:'block'}" v-if="!item.children || item.children.length < 1" placement="right" :content="item.title">
                <Button :key="item.name" :style="{width:width,fontSize:'1rem'}"  type="text"  @click="itemClickHandler(item, index)" long>
                    <Icon :type="item.icon" :color="iconColor" />
                </Button>
            </Tooltip>
            <!-- 渲染带二级菜单的item -->
            <Dropdown transfer placement="right-start" :style="{display:'block'}" @on-click="itemItemClickHandler" v-else>
                <Button :style="{width:width,fontSize:'1rem'}" type="text" long>
                    <Icon :type="item.icon" :color="iconColor" />
                </Button>
                <DropdownMenu slot="list">
                    <DropdownItem :name="index + '-' + subIndex" v-for="(subItem,subIndex) in item.children" :key="subItem.name">
                        <Icon :type="subItem.icon" />
                        {{subItem.title}}
                    </DropdownItem>
                </DropdownMenu>
            </Dropdown>
        </template>
    </div>
</template>

<script>

export default {
    props:{
        items: Array
        ,activeName: String
        ,width: String
        ,theme: String
        ,iconColor:{
            type:String
            ,default: '#FFF'
        }
    }
    ,methods:{
        itemClickHandler(buoy, index){
            //触发事件
            this.$emit('item-click', buoy, index);
        }
        ,itemItemClickHandler(name){
            //通过name索引寻找item
            let index = name.toString().split('-'),buoy = this.items[index[0]];
            for(let i = 1;i < index.length;i++) buoy = buoy.children[index[i]];
            
            //触发事件
            this.$emit('item-click', buoy, name);
        }
    }
}
</script>