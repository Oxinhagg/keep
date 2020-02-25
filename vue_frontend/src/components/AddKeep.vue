<template>
    <v-card>
        <form
            @submit.prevent="onSubmit"
        >
            <v-text-field 
                label="Title"
                v-model="title"
            ></v-text-field>
            
            <v-textarea
                label="Body"
                dense
                auto-grow
                rows="1"
                row-height="15"
                v-model="body"
            ></v-textarea>
            
            <v-btn type="submit">Create</v-btn>
            
        </form>
    </v-card>
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
    form{
        padding: .5rem 2rem;
    }
    /* 
    form {
        display: flex; 
    } 
    input {
        width: 400px;
    } 
    */
</style>