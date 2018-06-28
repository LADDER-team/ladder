<template>
    <v-toolbar class="g-toolbar" fixed>
        <v-toolbar-title class="g-toolbar-logo">LADDER</v-toolbar-title>
        <v-flex xs5 sm4 md2 class="g-search-wrap">
            <v-text-field
                    class="g-search-field"
                    name="input-1"
                    rows=1
                    row-height=10
                    prepend-icon="search"
                    hide-details
            />
        </v-flex>
        <v-spacer/>
        <v-toolbar-items class="hidden-sm-and-down avatar">
            <v-btn
                    class="contribution-btn"
                    depressed
                    round
            >投稿する</v-btn>
            <v-flex
                xs12
                sm6
                md8
                text-xs-center
                layout
                align-center
                justify-center
                class="avatar-wrap"
            >
                <v-avatar
                    :tile=false
                    :size=40
                    color="grey lighten-4"
                >
                    <img src="../assets/logo.png" alt="avatar">
                </v-avatar>
            </v-flex>
        </v-toolbar-items>
    </v-toolbar>
</template>

<script>
  export default {
    name: "toolbar-component"
  }
</script>

<style scoped lang="sass">
    .g-toolbar
        background: #4694F2
    .g-toolbar-logo
        color: #fff
    .g-search-wrap
        padding: 10px 0
        margin: 0 0 0 30px
    .g-search-field
        padding: 5px 10px 0
        background: #fff
        border-radius: 30px
    .input-group__details
        display: none
    .avatar-wrap
        margin: 0 0 0 30px
    .contribution-btn
        background-color: #64B5F6!important
        max-height: 30px
        height: 30px
        color: #fff
        font-weight: bold
</style>