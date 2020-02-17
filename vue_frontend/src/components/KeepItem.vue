<template>
    <div id="keep">
        <div
            id="keep_title">
            {{ keep.title }}
        </div>
        <div 
            id="keep_body"
            role="textbox"
            aria-multiline="true"
            dir="ltr"
        >
            {{ keep.body }}
        </div>
        <div
            id="keep_button">
            <button class="rm" 
                    v-on:click="$emit('remove_keep', keep.id)">&times;</button>
        </div>
    </div>
</template>

<script>
export default {
    props: {
        keep:{
            type: Object,
            required: true
        }
    }
}
</script>

<style scoped>
    #keep {
        border: 1px solid #ccc;
        border-radius: 10px;
        padding: .5rem 2rem;
        margin: 1rem;
        width: 240px;
        background-color: #ABDB57;
        text-align: left;
    }

    #keep_button {
        text-align: right;
    }

    input {
        margin-right: 1rem;
    }
</style>