<template>
    <form @submit.prevent="onSubmit">
        <input type="text" v-model="title">
        <button type="submit">Create </button>
    </form>
</template>

<script>
export default {
    data(){
        return{
            title: ''
        }
    },
    methods: {
        onSubmit() {
            if (this.title.trim()){
                const newKeep = {
                    id: Date.now(),
                    title: this.title,
                    body: null
                };

                this.$emit('add-keep', newKeep)
                this.title = ''
            }
        }
    }
}
</script>

<style scoped>
    form {
        display: flex; 
    }
    input {
        width: 400px;
    }
</style>