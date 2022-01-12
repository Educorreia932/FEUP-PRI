<template>
	<v-card>
		<v-card-title>
			{{ artist.name }}
		</v-card-title>

		<v-card-text>
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