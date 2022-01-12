<template>
	<v-card>
		<v-card-text>
			<h2>{{ album.name }}</h2>
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