<template>
    <v-row>
        <v-col cols="12">
            <v-row
                class="lighten-5" 
                style="height: 300px;"
            >
                <KeepItem 
                    v-for="keep in keeps"
                    v-bind:keep="keep"
                    v-bind:key=keep.id
                    v-on:remove_keep="removeKeep"
                    class="ma-6 pa-8" 
                ></KeepItem>
            </v-row>
        </v-col>
    </v-row>
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
    
</style>