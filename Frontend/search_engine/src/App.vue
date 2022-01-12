<template>
  <!-- App.vue -->

  <v-app>

    <v-app-bar app clipped-left height="100">
      <v-form v-on:submit="search">
      <!-- -->
      <v-text-field
        color="#123456"
        background-color="#AABBCC"
        label = "Search.."
        class = "shrink "
      ></v-text-field> 
      <button type="submit">Search</button>
      </v-form>
    </v-app-bar>

    <v-navigation-drawer
    clipped
    app
    >
    </v-navigation-drawer>

    <!-- Sizes your content based upon application components -->
    <v-main>

      <!-- Provides the application the proper gutter -->
      <v-container fluid>
        <!-- 
        <v-text-field
          color="#123456"
          background-color="#AABBCC"
          label = "Search.."
          class = "post"
        ></v-text-field>-->
      </v-container>
    </v-main>

    <v-footer app>
      <!-- -->
    </v-footer>
  </v-app>
</template>

<style scoped>
</style>

<script>
import axios from 'axios'

export default {
  setup() {
    
  },
  el: '#app',
  data () {
    return {
      info: null
    }
  },
  methods: {
    /*search(e) {
      e.preventDefault()
      console.log("bruh")

      const Http = new XMLHttpRequest();
      const url='http://localhost:8983/solr/music/query?q=*:*';
      Http.open("GET", url);
      Http.send();

      Http.onreadystatechange = (e) => {
        console.log(document.querySelector(".post"))
        var a = JSON.parse(Http.responseText)
        console.log(a.response.docs[0])

      }

    }*/
    async search(e){
      e.preventDefault()
      //let response = axios.get('http://localhost:8983/solr/music/query?q=*:*')
      //console.log(response)
      const response = await axios.get("http://localhost:8983/solr/music/query?q=*:*")
      console.log(response)
    }
    }
  }
</script>
