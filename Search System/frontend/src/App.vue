<template>
	<v-app>
		<v-navigation-drawer app class="px-4 py-4" :width="325">
			<h1>Spot & Find</h1>

			<v-checkbox label="Explicit" v-model="explicit"></v-checkbox>

			<v-subheader>Searching by</v-subheader>

			<v-radio-group v-model="searchingBy">
				<v-radio
					v-for="docType in ['Album', 'Artist', 'Track']"
					:key="docType"
					:label="docType"
					:value="docType"
				>
				</v-radio>
			</v-radio-group>

			<v-subheader>Track duration</v-subheader>

			<v-range-slider></v-range-slider>

			<v-subheader>Artist popularity</v-subheader>

			<v-range-slider></v-range-slider>
		</v-navigation-drawer>

		<v-main>
			<v-container fluid>
				<v-form>
					<v-text-field label="Search" prepend-inner-icon="mdi-magnify"></v-text-field>
				</v-form>

				<p>Showing 3 results</p>

				<v-list>
					<v-list-item v-for="track of results" :key="track.uri" class="mb-4" style="width: 35em;">
						<album v-if="searchingBy === 'Album'" :album="{}"/>
						<artist v-if="searchingBy === 'Artist'" :artist="{}"/>
						<song v-if="searchingBy === 'Track'" :track="track"/>
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
import Artist from "@/components/Artist";
import Album from "@/components/Album";
import Song from "@/components/Song";
import Tracks from "@/api/Tracks";

export default {
	components: {
		"artist": Artist,
		"album": Album,
		"song": Song,
	},
	data() {
		return {
			results: [],
			page: 1,
			explicit: true,
			searchingBy: "Track"
		}
	},
	created() {
		Tracks.list().then((results) => {
			this.results = results;
		})
	}
}
</script>
