<template>
	<v-card style="width: 100%;">
		<div class="d-flex flex-no-wrap">
			<v-avatar tile size="100" class="rounded my-3 ml-3">
				<v-img :src="artwork"></v-img>
			</v-avatar>

			<div>
				<v-card-title>
					<span class="mr-2">{{ album.name }}</span>

					<v-icon v-if="album.album_type === 'album'">mdi-music-box-multiple-outline</v-icon>
					<v-icon v-if="album.album_type === 'compilation'">mdi-folder-music-outline</v-icon>
					<v-icon v-if="album.album_type === 'single'">mdi-music-box-outline</v-icon>
				</v-card-title>

				<v-card-subtitle>
					<span v-for="(artist, i) in album.artists" :key="i">
						<span v-if="i > 0">,</span>
						{{ artist.name }}</span>
				</v-card-subtitle>

				<v-card-text>
					<div>
						<v-icon class="mr-1">mdi-calendar</v-icon>

						<span>{{ release_date }}</span>
					</div>
				</v-card-text>
			</div>
		</div>
	</v-card>
</template>

<script>
import {getArtwork} from "@/api/Spotify";

export default {
	name: "album",
	props: [
		"album"
	],
	data() {
		return {
			artwork: "",
			release_date: new Date(this.album.release_date).toLocaleString("pt-PT", {
				day: "2-digit",
				month: "2-digit",
				year: "numeric",
			})
		}
	},
	async created() {
		this.artwork = await getArtwork(this.album.uri)
	}
}
</script>

<style scoped>

</style>