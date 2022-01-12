<template>
	<v-app>
		<v-navigation-drawer app class="px-4 py-4" :width="325">
			<h1>Spot & Find</h1>

			<v-checkbox label="Explicit"></v-checkbox>

			<v-list>
				<v-checkbox label="Album" v-model="checkbox"></v-checkbox>
				<v-checkbox label="Artist" v-model="checkbox"></v-checkbox>
				<v-checkbox label="Track" v-model="checkbox"></v-checkbox>
			</v-list>

			<v-subheader>Track duration</v-subheader>
			<v-slider></v-slider>

			<v-subheader>Artist popularity</v-subheader>
			<v-slider></v-slider>
		</v-navigation-drawer>

		<v-main>
			<v-container fluid>
				<v-form>
					<v-text-field label="Search" prepend-inner-icon="mdi-magnify"></v-text-field>
				</v-form>

				<p>Showing 3 results</p>

				<v-list>
					<v-list-item v-for="track of results" :key="track.uri" class="mb-4" style="width: 35em;">
						<song :track="track"/>
					</v-list-item>
				</v-list>

				<v-pagination v-model="page" :length="1"></v-pagination>
			</v-container>
		</v-main>
	</v-app>
</template>

<style scoped>
</style>

<script>
import Song from "@/components/Song";
import {search} from "@/api/API";

export default {
	components: {
		"song": Song,
	},
	data() {
		return {
			results: [],
			checkbox: true,
			page: 1
		}
	},
	created() {
		search().then((response) => {
			this.results = response.data.response.docs

			console.log(this.results)
		})
	}
}
</script>
