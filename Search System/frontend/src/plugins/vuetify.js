import Vue from 'vue';
import Vuetify from 'vuetify/lib/framework';

Vue.use(Vuetify);

export default new Vuetify({
	theme: {
		dark: false,
		themes: {
			light: {
				primary: "#1db954",
				secondary: "#1ed760"
			}
		}
	},
});
