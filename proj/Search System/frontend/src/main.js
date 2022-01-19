import Vue from 'vue'
import Vuetify from 'vuetify/lib/framework'
import App from './App.vue'
import vuetify from './plugins/vuetify'

Vue.use(Vuetify)
Vue.config.productionTip = false

new Vue({
	vuetify,
	render: h => h(App)
}).$mount('#app')
