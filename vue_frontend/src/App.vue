<template>
  <v-app id="keep">
    <v-app-bar
      app
      clipped-left
      color="amber"
    >
      <v-app-bar-nav-icon @click="drawer = !drawer" />
      <span class="title ml-3 mr-5">&nbsp;<span class="font-weight-light">Keep</span></span>
      <v-text-field
        solo-inverted
        flat
        hide-details
        label="Search"
        prepend-inner-icon="search"
      />

      <v-spacer />
    </v-app-bar>
  <v-navigation-drawer
      v-model="drawer"
      app
      clipped
      color="grey lighten-4"
    >
      <v-list
        dense
        class="grey lighten-4"
      >
        <template v-for="(item, i) in items">
          <v-row
            v-if="item.heading"
            :key="i"
            align="center"
          >
            <v-col cols="6">
              <v-subheader v-if="item.heading">
                {{ item.heading }}
              </v-subheader>
            </v-col>
            <v-col
              cols="6"
              class="text-right"
            >
              <v-btn
                small
                text
              >edit</v-btn>
            </v-col>
          </v-row>
          <v-divider
            v-else-if="item.divider"
            :key="i"
            dark
            class="my-4"
          />
          <v-list-item
            v-else
            :key="i"
            link
          >
            <v-list-item-action>
              <v-icon>{{ item.icon }}</v-icon>
            </v-list-item-action>
            <v-list-item-content>
              <v-list-item-title class="grey--text">
                {{ item.text }}
              </v-list-item-title>
            </v-list-item-content>
          </v-list-item>
        </template>
      </v-list>
    </v-navigation-drawer>
    <v-content>
      <v-container
        class="lighten-4"
      >
        <AddKeep
          @add-keep='addKeep'
        />
      </v-container>
      
      <v-container
        fluid
        class="lighten-4"
      >
        <KeepList 
          v-if="keeps.length"
          v-bind:keeps="keeps"
          @remove-keep="removeKeep"
        />
        <p v-else>No keep!</p>
      </v-container>
    </v-content>
  </v-app>
</template>

<script>
import KeepList from '@/components/KeepList'
import AddKeep from '@/components/AddKeep'
import axios from 'axios'
export default {
  name: 'App',
  props: {
      source: String,
    },
  data() {
    return {
      drawer: null,
      keeps: [
        
      ],
      items: [
        { icon: 'lightbulb_outline', text: 'Notes' },
        { icon: 'touch_app', text: 'Reminders' },
        { divider: true },
        { heading: 'Labels' },
        { icon: 'add', text: 'Create new label' },
        { divider: true },
        { icon: 'archive', text: 'Archive' },
        { icon: 'delete', text: 'Trash' },
        { divider: true },
        { icon: 'settings', text: 'Settings' },
        { icon: 'chat_bubble', text: 'Trash' },
        { icon: 'help', text: 'Help' },
        { icon: 'phonelink', text: 'App downloads' },
        { icon: 'keyboard', text: 'Keyboard shortcuts' },
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

    },
    addKeep(keep){
      var self = this
      axios
      .post('http://localhost:5000/keep/', keep)
      .then(function (response) {
        console.log('response', response)
        self.keeps.push(response.data)
      })
      .catch(error => console.log('error:', error))
    }
  }
}
</script>

<style>
#keep .v-navigation-drawer__border {
  display: none
}
</style>
