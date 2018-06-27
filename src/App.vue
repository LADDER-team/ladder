<!--suppress ALL -->
<template>
    <v-app id="inspire" indigo>
        <ToolBar/>
        <v-content>
            <v-container fluid fill-height>
                <v-layout justify-center align-center wrap class="getApiWrap">
                    <h2 class="headline headTitle">Ladder title</h2>

                </v-layout>
            </v-container>
        </v-content>
        <Footer/>
    </v-app>
</template>

<script>
  import axios from 'axios'
  import ToolBarComponent from './components/ToolBarComponent'
  import FoorerComponent from './components/FooterComponent'

  export default {
    name: 'Ladder',
    data: () => ({
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
    }),
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
    components: {
      'ToolBar': ToolBarComponent,
      'Footer': FoorerComponent
    }
  }
</script>
<style scoped lang="sass">
    .headTitle
        width: 100%
        text-align: center
</style>
