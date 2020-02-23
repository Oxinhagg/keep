<template>
    <v-card
        color="light yellow"
        max-width="344"
        outlined
    >
        <v-list-item three-line>
            <v-list-item-content>
            <v-list-item-title class="headline mb-1">{{ keep.title }}</v-list-item-title>
            <v-list-item-subtitle>{{ keep.body }}</v-list-item-subtitle>
            </v-list-item-content>
        </v-list-item>
    
        <v-card-actions>
            <v-btn 
                text icon color="grey"
                v-on:click="$emit('remove_keep', keep.id)" 
            >
                <v-icon>delete</v-icon>
            </v-btn>
        </v-card-actions>
    </v-card>
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

</style>