<!--suppress ALL -->
<template>
    <v-app id="inspire" indigo>
        <ToolBar/>
        <v-content>
            <v-container fluid fill-height>
                <v-layout justify-center align-center wrap>
                    <v-flex md3 justify-center align-cener>
                        <div class="ladder-item ladder-item-active">
                            <p>unit:{{ ladderList.unit[0].index }}</p>
                            <p>{{ ladderList.unit[0].title }}</p>
                        </div>
                        <div class="ladder-item">
                            <p>unit:{{ ladderList.unit[1].index }}</p>
                            <p>{{ ladderList.unit[1].title }}</p>
                        </div>
                        <div class="ladder-item">
                            <p>unit:{{ ladderList.unit[2].index }}</p>
                            <p>{{ ladderList.unit[2].title }}</p>
                        </div>
                    </v-flex>
                    <v-flex md7 justify-center align-start></v-flex>
                    <v-flex md2 justify-center align-cener></v-flex>
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
      ladderList: []
    }),
    mounted(){
      axios.get('/api/ladder/6/')
        .then((response) => {
          this.ladderList = response.data
        })
        .catch((error) => {
          console.log(error)
        })
    },
    components: {
      'ToolBar': ToolBarComponent,
      'Footer': FoorerComponent,
    }
  }
</script>
<style scoped lang="sass">
    .headTitle
        width: 100%
        text-align: center
    .ladder-item
        background: #CFD8DC
        padding: 10px
        p
            margin: 0
            color: #fff
            font-weight: bold
    .ladder-item-active
        background: #64B5F6
</style>
