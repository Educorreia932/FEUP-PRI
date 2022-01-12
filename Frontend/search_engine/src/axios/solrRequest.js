new Vue({
  el: '#app',
  data () {
    return {
      info: null
    }
  },
  mounted () {
    axios
      .get('http://localhost:8983/solr/music/query?q=*:*')
      .then(response => (this.info = response))
  }
})