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
                                <img src="./assets/book1.jpg"
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
        src1: "./assets/book1.jpg",
        src2: "./assets/book2.jpg",
        src3: "./assets/book3.jpg",
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
      axios.get('/api/ladder/6/')
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
    .g-container
        padding-top: 100px!important
    .project-wrap
        position: relative
    .unit-wrap
        align-items: flex-start
    .unit-head
        margin: 0
        font-size: 18px
        color: #B0BEC5
    .unit-item
        padding: 30px 30px 40px
        margin: 0 0 60px
        height: 90vh
        background: #fff
    .unit-title
        margin: 0 0 30px
        text-align: center
        font-size: 28px
    .unit-point
        text-align: center
    .unit-point-item
        background: #ECEFF1
        padding: 5px 10px
    .unit-image-wrap
        margin: 40px 0
        text-align: center
    .unit-image
        margin: 0 auto
        max-width: 40%
    .unit-description
        font-size: 18px
        border-left: 3px solid #64B5F6
        padding: 0 0 0 10px
        max-width: 80%
        width: 80%
        margin: 0 auto
    .ladder-item
        background: #CFD8DC
        padding: 10px
        border-bottom: 1px solid #546E7A
        cursor: pointer
        p
            margin: 0
            color: #fff
            font-weight: bold
        &:last-of-type
            border-bottom: none
    .ladder-item-active
        background: #64B5F6
    .ladder-inner
        position: fixed
</style>
