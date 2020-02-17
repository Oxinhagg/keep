<template>
  <div id="app">
    <h1>Keep aplication</h1>
    <AddKeep 
      @add-keep="addKeep" 
    />
    <hr>
    <KeepList 
      v-if="keeps.length"
      v-bind:keeps="keeps"
      @remove-keep="removeKeep"
    />
    <p v-else>No keep!</p>
  </div>
</template>

<script>
import KeepList from '@/components/KeepList'
import AddKeep from '@/components/AddKeep'
import axios from 'axios'
export default {
  name: 'App',
  data() {
    return {
      keeps: [
        
      ]
    }
  },
  mounted() {
    var self = this
    axios  
    .get('http://localhost:5000/keep/')
    .then(function (response) {
      self.keeps = response.data
    })
    .catch(error => console.log('error:', error))
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
