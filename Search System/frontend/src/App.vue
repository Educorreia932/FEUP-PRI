<template>
	<v-app>
		<v-navigation-drawer app class="px-4 py-4" :width="325">
			<h1>Spot & Find</h1>

			<v-checkbox label="Explicit" v-model="explicit"></v-checkbox>

			<v-subheader>Searching by</v-subheader>

			<v-radio-group v-model="searchingBy" class="mt-0">
				<v-radio
					v-for="docType in ['Album', 'Artist', 'Track']"
					:key="docType"
					:label="docType"
					:value="docType"
				>
				</v-radio>
			</v-radio-group>
		</v-navigation-drawer>

		<v-main>
			<v-container fluid>
				<v-form @submit.prevent="retrieveResults(searchTerms)">
					<v-text-field
						label="Search"
						prepend-inner-icon="mdi-magnify"
						v-model="searchTerms"
					></v-text-field>
				</v-form>

				<p>
					Found <span class="primary--text">{{ found }}</span> results
				</p>

				<v-list>
					<v-list-item
						v-for="result of results[searchingBy].filter(r => explicit? true: r.explicit === explicit)"
						:key="result.uri"
						class="mb-4"
						style="width: 35em;"
					>
						<album v-if="searchingBy === 'Album'" :album="result"/>
						<artist v-if="searchingBy === 'Artist'" :artist="result"/>
						<song v-if="searchingBy === 'Track'" :track="result"/>
					</v-list-item>
				</v-list>

				<v-pagination
					v-model="page"
					:length="numPages"
					:total-visible="7"
				></v-pagination>
			</v-container>
		</v-main>
	</v-app>
</template>

<style scoped>
</style>

<script>
import Artist from "@/components/Artist";
import Album from "@/components/Album";
import Song from "@/components/Song";
import Tracks from "@/api/Tracks";

export default {
	components: {
		"artist": Artist,
		"album": Album,
		"song": Song,
	},
	data() {
		return {
			results: {
				"Albums": [],
				"Artists": [],
				"Tracks": [],
			},
			found: 0,
			resultsPerPage: 10,
			page: 1,
			explicit: true,
			searchingBy: "Track",
			searchTerms: ""
		}
	},
	computed: {
		numPages() {
			return Math.floor(this.found / this.resultsPerPage);
		},
	},
	methods: {
		unique(array) {
			const distinct = []

			for (const a of array) {
				let found = false

				for (const b of distinct)
					if (a.name === b.name) {
						found = true;

						break;
					}

				if (!found)
					distinct.push(a)
			}

			return distinct
		},
		retrieveResults(searchTerms = "*") {
			if (searchTerms === "")
				searchTerms = "*"

			const start = (this.page - 1) * this.resultsPerPage

			Tracks.search(start, searchTerms, this.explicit).then((response) => {
				this.results = {}

				const albums = response.docs.map(item => item.albums).flat();
				const artists = response.docs.map(item => item.artists).flat();

				this.results["Album"] = this.unique(albums)
				this.results["Artist"] = this.unique(artists)
				this.results["Track"] = response.docs;

				this.found = response.found;
			})
		}
	},
	created() {
		this.retrieveResults();
	},
	watch: {
		page: function () {
			this.retrieveResults(this.searchTerms)
		},
	},
}
</script>
