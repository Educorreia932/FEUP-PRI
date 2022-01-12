<template>
	<v-card style="width: 100%;">
		<v-card-title>
			<span class="mr-2">{{ artist.name }}</span>

			<v-icon>mdi-account-music</v-icon>
		</v-card-title>

		<v-card-text>
			<v-icon>mdi-podium</v-icon>

			<span>{{ artist.popularity }}</span>

			<p v-for="genre of artist.genres" :key="genre">
				{{ genre }}
			</p>
		</v-card-text>
	</v-card>
</template>

<script>
export default {
	name: "Artist",
	props: [
		"artist"
	]
}
</script>

<style scoped>

</style>