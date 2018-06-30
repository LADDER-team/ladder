<!--suppress ALL -->
<template>
    <v-app id="inspire" indig　v-scroll="onScroll">
        <ToolBar/>
        <v-content>
            <v-container fluid fill-height class="g-container">
                <v-layout justify-center align-start wrap class="project-wrap">
                    <v-flex md3 justify-center align-cener class="ladder-wrap">
                        <div md3 class="ladder-inner">
                            <div v-for="item in ladderList.unit"
                                 :class="{'ladder-item-active': ladderActive}"
                                 v-on:click="ladderActived"
                                 class="ladder-item">
                                <p>unit:{{ item.index }}</p>
                                <p>{{ item.title }}</p>
                            </div>
                        </div>
                    </v-flex>
                    <v-flex md8 justify-center align-start class="unit-wrap">
                        <div v-for="unit in ladderList.unit" class="unit-item">
                            <p class="unit-head">unit:{{ unit.index }}</p>
                            <h2 class="unit-title">{{ unit.title }}</h2>
                            <v-flex class="unit-image-wrap" justify-center align-center>
                                <img src="./assets/img/book1.jpg"
                                     :alt="defaultImage.alt"
                                     class="unit-image">
                            </v-flex>
                            <div class="unit-description">
                                {{ unit.description }}
                            </div>
                        </div>
                    </v-flex>
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
      drawer: true,
      right: true,
      clipped: false,
      fixed: false,
      miniVariant: false,
      rightDrawer: false,
      ladderActive: false,
      offsetTop: 0,
      defaultImage: {
        src: "http://via.placeholder.com/350x150",
        src1: "./assets/img/book1.jpg",
        src2: "./assets/img/book2.jpg",
        src3: "./assets/img/book3.jpg",
        alt: "placeholder-image"
      },
      title: 'Vuetify.js',
      ladderList: [],
      items: [{
        icon: 'bubble_chart',
        title: 'Inspire'
      }]
    }),
    mounted(){
      axios.get('/api/ladder/15')
        .then((response) => {
          this.ladderList = response.data
        })
        .catch((error) => {
          console.log(error)
        })
    },
    methods: {
      ladderActived(){
        console.log('clicked!')
      },
      onScroll (e) {
        this.offsetTop = window.pageYOffset || document.documentElement.scrollTop
      }
    },
    computed: {
      scrollY(){
        return this.$window.scrollY
      }
    },
    components: {
      'ToolBar': ToolBarComponent,
      'Footer': FoorerComponent,
    }
  }
</script>
<style scoped lang="sass">
    @import "assets/styles/app"

</style>
