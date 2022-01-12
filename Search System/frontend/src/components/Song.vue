<template>
	<v-card style="width: 100%;">
		<v-card-title>
			<span class="mr-1">{{ track.name }}</span>

			<v-icon>mdi-music-note</v-icon>

			<v-spacer></v-spacer>

			<v-icon v-if="track.explicit">
				mdi-alpha-e-box
			</v-icon>

			<v-btn
				depressed
				icon
				@click="show = !show"
			>
				<v-icon>{{ show ? 'mdi-chevron-up' : 'mdi-chevron-down' }}</v-icon>
			</v-btn>
		</v-card-title>

		<v-card-subtitle>
			Britney Spears
		</v-card-subtitle>

		<v-card-text>
			<div>
				<v-icon class="mr-1">mdi-clock-outline</v-icon>

				<span>{{ duration }}</span>
			</div>

			<v-expand-transition>
				<p class="lyrics mt-4" v-show="show">
					{{ track.lyrics }}
				</p>
			</v-expand-transition>
		</v-card-text>
	</v-card>
</template>

<script>
export default {
	name: "song",
	props: [
		"track"
	],
	data() {
		return {
			show: false
		}
	},
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
.lyrics {
	white-space: pre-line;
}
</style>