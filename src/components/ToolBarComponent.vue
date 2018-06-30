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
                    <img src="../assets/img/logo.png" alt="avatar">
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
    @import "../assets/styles/toolbar"
</style>