<template>
	<v-card style="width: 100%;">
		<div class="d-flex flex-no-wrap">
			<v-avatar tile size="100" class="rounded my-3 ml-3">
				<v-img :src="artwork"></v-img>
			</v-avatar>

			<div>
				<v-card-title>
					<span class="mr-2">{{ artist.name }}</span>

					<v-icon>mdi-account-music</v-icon>
				</v-card-title>

				<v-card-subtitle>
					<div class="mt-2">
						<v-chip v-for="genre of artist.genres" :key="genre" class="mr-2">
							{{ genre }}
						</v-chip>
					</div>
				</v-card-subtitle>

				<v-card-text>
					<div>
						<v-icon class="mr-1">mdi-podium</v-icon>

						<span>{{ artist.popularity }}/100</span>
					</div>
				</v-card-text>
			</div>
		</div>
	</v-card>
</template>

<script>
import {getArtwork} from "@/api/Spotify";

export default {
	name: "Artist",
	props: [
		"artist"
	],
	data() {
		return {
			artwork: ""
		}
	},
	async created() {
		this.artwork = await getArtwork(this.artist.uri)
	}
}
</script>

<style scoped>

</style>