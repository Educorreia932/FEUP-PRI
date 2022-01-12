<template>
	<v-card style="width: 100%;">
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
			{{ album.release_date }}
		</v-card-text>
	</v-card>
</template>

<script>
export default {
	name: "album",
	props: [
		"album"
	]
}
</script>

<style scoped>

</style>