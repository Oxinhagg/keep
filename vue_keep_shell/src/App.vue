<template>
  <div id="app">
    <h1>Keep aplication</h1>
    <AddKeep 
      @add-keep="addKeep" 
    />
    <hr>
    <KeepList 
      v-bind:keeps="keeps"
      @remove-keep="removeKeep"
    />
  </div>
</template>

<script>
import KeepList from '@/components/KeepList'
import AddKeep from '@/components/AddKeep'
export default {
  name: 'App',
  data() {
    return {
      keeps: [
        {id: 1, title: 'Keep 1', body: 'Body keep 1' },
        {id: 2, title: 'Keep 2', body: 'Body keep 2' },
        {id: 3, title: 'Keep 3', body: 'Body keep 3' }
      ]
    }
  },
  components: {
    KeepList, AddKeep
  },
  methods: {
    removeKeep(id) {
      this.keeps = this.keeps.filter(k => k.id != id)
    },
    addKeep(keep){
      this.keeps.push(keep)
    }
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
