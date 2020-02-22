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
      var self = this
      axios
      .delete('http://localhost:5000/keep/' + id)
      .then(function (response) {
        self.keeps = self.keeps.filter(k => k.id != id)
        console.log('delete ', id)
      })
      .catch(error => console.log('error:', error))
      // .catch(error => alert('error! сашка саня хуй соси'))

    },
    addKeep(keep){
      var self = this
      axios
      .post('http://localhost:5000/keep/', keep)
      .then(function (response) {
        console.log('response', response)
        self.keeps.push(response.data)
      })
      // .catch(error => alert('error! сашка саня хуй соси'))
      .catch(error => console.log('error:', error))
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
