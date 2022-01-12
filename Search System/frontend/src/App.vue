<template>
	<v-app>
		<v-navigation-drawer app class="px-4 py-4">
			<h1>Spot & Find</h1>

			<v-checkbox label="Explicit"></v-checkbox>

			<v-list>
				<v-checkbox label="Album"></v-checkbox>
				<v-checkbox label="Artist"></v-checkbox>
				<v-checkbox label="Track"></v-checkbox>
			</v-list>

			<!--			<v-date-picker></v-date-picker>-->
			<v-slider label="Track duration"></v-slider>
			<v-slider label="Artist popularity"></v-slider>
		</v-navigation-drawer>

		<v-main>
			<v-container fluid>
				<v-form>
					<v-text-field label="Search" prepend-inner-icon="mdi-magnify"></v-text-field>
				</v-form>

				<v-list>
					<v-list-item v-for="track of tracks" :key="track.uri">
						<v-list-item-content>
							<song :track="track" class="mb-4"/>
						</v-list-item-content>
					</v-list-item>

					<v-list-item>
						<artist :artist="artist"></artist>
					</v-list-item>
				</v-list>
			</v-container>
		</v-main>
	</v-app>
</template>

<style scoped>
</style>

<script>
import axios from 'axios'
import Song from "@/components/Song";
import Artist from "@/components/Artist";

export default {
	setup() {

	},
	components: {
		"song": Song,
		"artist": Artist
	},
	data() {
		return {
			tracks: [
				{
					"uri": "spotify:track:6I9VzXrHxO9rA9A5euc8Ak",
					"name": "Toxic",
					"duration_ms": 198800,
					"lyrics": "Baby, can't you see I'm calling?\nA guy like you should wear a warning\nIt's dangerous, I'm falling\nThere's no escape, I can't wait\nI need a hit, baby, give me it\nYou're dangerous, I'm lovin' it\n\nToo high, can't come down\nLosing my head, spinnin' 'round and 'round\nDo you feel me now?\n\nWith a taste of your lips, I'm on a ride\nYou're toxic, I'm slippin' under\nWith a taste of a poison paradise\nI'm addicted to you\nDon't you know that you're toxic?\nAnd I love what you do\nDon't you know that you're toxic?\n\nIt's getting late to give you up\nI took a sip from my devil's cup\nSlowly, it's taking over me\n\nToo high, can't come down\nIt's in the air and it's all around\nCan you feel me now?\n\nWith a taste of your lips, I'm on a ride\nYou're toxic, I'm slippin' under\nWith a taste of a poison paradise\nI'm addicted to you\nDon't you know that you're toxic?\nAnd I love what you do\nDon't you know that you're toxic?\nDon't you know that you're toxic?\n\nWith a taste of your lips, I'm on a ride\nYou're toxic, I'm slippin' under\nWith a taste of a poison paradise\nI'm addicted to you\nDon't you know that you're toxic?\nWith a taste of your lips, I'm on a ride\nYou're toxic, I'm slippin' under (Toxic)\nWith a taste of a poison paradise\nI'm addicted to you\nDon't you know that you're toxic?\n\nIntoxicate me now with your lovin' now\nI think I'm ready now (I think I'm ready now)\nIntoxicate me now with your lovin' now\nI think I'm ready now",
					"acousticness": 0.0249,
					"danceability": 0.774,
					"energy": 0.838,
					"instrumentalness": 0.025,
					"liveness": 0.242,
					"loudness": -3.914,
					"mode": 0,
					"speechiness": 0.114,
					"tempo": 143.04,
					"time_signature": 4,
					"valence": 0.924,
					"explicit": true,
				},
			],
			artist: {
				"uri": "spotify:artist:26dSoYclwsYLMAKD3tpOr4",
				"name": "Britney Spears",
				"popularity": 84,
				"explicit": 0,
				"genres": [
					"dance pop",
					"pop",
					"post-teen pop"
				]
			}
		}
	},
	methods: {
		async search(e) {
			e.preventDefault()

			const response = await axios.get("http://localhost:8983/solr/music/query?q=*:*")
			console.log(response)
		}
	}
}
</script>
