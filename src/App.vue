<!--suppress ALL -->
<template>
  <v-app id="inspire" dark>
    <v-navigation-drawer
      v-model="drawer"
      clipped
      fixed
      app
    >
      <v-list dense>
        <v-list-tile @click="">
          <v-list-tile-action>
            <v-icon>dashboard</v-icon>
          </v-list-tile-action>
          <v-list-tile-content>
            <v-list-tile-title>Dashboard</v-list-tile-title>
          </v-list-tile-content>
        </v-list-tile>
        <v-list-tile @click="">
          <v-list-tile-action>
            <v-icon>settings</v-icon>
          </v-list-tile-action>
          <v-list-tile-content>
            <v-list-tile-title>Settings</v-list-tile-title>
          </v-list-tile-content>
        </v-list-tile>
      </v-list>
    </v-navigation-drawer>
    <v-toolbar app fixed clipped-left>
      <v-toolbar-side-icon @click.stop="drawer = !drawer"></v-toolbar-side-icon>
      <v-toolbar-title>Application</v-toolbar-title>
    </v-toolbar>
    <v-content>
      <v-container fluid fill-height>
        <v-layout justify-center align-center wrap class="getApiWrap" >
          <h1 class=".headline headTitle">Get APIs</h1>
          <v-list>
              <v-list-tile v-for="user in users">
                {{ user.name }}
              </v-list-tile>
          </v-list>
          <v-list>
              <v-list-tile v-for="user in users">
                {{ user.email }}
              </v-list-tile>
          </v-list>
        </v-layout>
      </v-container>
    </v-content>
    <v-footer app fixed>
      <span>&copy; 2018</span>
    </v-footer>
  </v-app>
</template>

<script>
  import axios from 'axios'

  export default {
    name: 'Ladder',
    data () {
      return {
        clipped: false,
        drawer: true,
        fixed: false,
        items: [{
          icon: 'bubble_chart',
          title: 'Inspire'
        }],
        miniVariant: false,
        right: true,
        rightDrawer: false,
        title: 'Vuetify.js',
        users: []
      }
    },
    mounted() {
      console.log('mounted!')

      axios.get('/api/users/')
        .then((response) => {
          this.users = response.data
        })
        .catch((error) => {
          console.log(error)
        })
    },
    methods: {}
  }
</script>
<style scoped>
  .headTitle{width: 100%;text-align: center;}
  .getApiWrap{height: auto!important;}
</style>
