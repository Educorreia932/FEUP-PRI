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
					Britney Spears
				</v-card-subtitle>

				<v-card-text>
					<div>
						<v-icon class="mr-1">mdi-calendar</v-icon>

						<span>{{ album.release_date }}</span>
					</div>
				</v-card-text>
			</div>
		</div>
	</v-card>
</template>

<script>
import {getArtwork} from "@/api/spotify";

export default {
	name: "album",
	props: [
		"album"
	],
	data() {
		return {
			artwork: ""
		}
	},
	async created() {
		this.artwork = await getArtwork(this.album.uri)
	}
}
</script>

<style scoped>

</style>