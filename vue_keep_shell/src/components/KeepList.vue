<template>
    <div> 
        <ul>
            <KeepItem 
                v-for="keep in keeps"
                v-bind:keep="keep"
                v-on:remove_keep="removeKeep"
            />
        </ul>
    </div>
</template>

<script>
import KeepItem from '@/components/KeepItem'
export default {
    props: ['keeps'],
    components: {
        KeepItem
    },
    methods: {
        removeKeep(id){
            this.$emit('remove-keep', id)           
        } 
    }
}
</script>

<style scoped>
    ul {
        list-style: none;
        margin: 0;
        padding: 0;
    }
</style>