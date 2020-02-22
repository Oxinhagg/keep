<template>
    <form @submit.prevent="onSubmit">
        <input type="text" placeholder="title" v-model="title"><br>
        <input type="text" placeholder="body" v-model="body"><br>
        <button type="submit">Create </button>
    </form>
</template>

<script>
export default {
    data(){
        return{
            title: '',
            body: ''
        }
    },
    methods: {
        onSubmit() {
            if (this.title.trim()){
                const newKeep = {
                    id: Date.now(),
                    title: this.title,
                    body: this.body
                };

                this.$emit('add-keep', newKeep)
                this.title = ''
                this.body = ''
            }
        }
    }
}
</script>

<style scoped>
    /* form {
        display: flex; 
    } */
    input {
        width: 400px;
    }
</style>