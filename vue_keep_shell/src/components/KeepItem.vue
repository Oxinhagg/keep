<template>
    <li>
        <span>
            {{ keep.title }}
        </span>
        <button class="rm" 
                v-on:click="$emit('remove_keep', keep.id)">&times;</button>
    </li>
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
    li {
        border: 1px solid #ccc;
        display: flex;
        justify-content: space-between;
        padding: .5rem 2rem;
        margin-bottom: 1rem;
    }

    input {
        margin-right: 1rem;
    }
</style>