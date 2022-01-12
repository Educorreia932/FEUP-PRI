<template>
	<v-card>
		<v-card-title>
			{{ this.track.name }}
		</v-card-title>

		<v-card-subtitle>
			Britney Spears
		</v-card-subtitle>

		<v-card-text>
			<p>{{ duration }}</p>

			<span v-if="track.explicit">
					<svg xmlns="http://www.w3.org/2000/svg" height="24" viewBox="0 0 24 24" width="24">
						<path d="M0 0h24v24H0z" fill="none"/>
						<path
							d="M19 3H5c-1.1 0-2 .9-2 2v14c0 1.1.9 2 2 2h14c1.1 0 2-.9 2-2V5c0-1.1-.9-2-2-2zm-4 6h-4v2h4v2h-4v2h4v2H9V7h6v2z"/>
					</svg>
				</span>
		</v-card-text>
	</v-card>
</template>

<script>
export default {
	name: "song",
	props: [
		"track"
	],
	computed: {
		duration() {
			const minutes = Math.floor(this.track.duration_ms / 60000);
			const seconds = ((this.track.duration_ms % 60000) / 1000).toFixed(0);

			return minutes + ":" + (seconds < 10 ? '0' : '') + seconds;
		}
	},
}
</script>

<style scoped>

</style>