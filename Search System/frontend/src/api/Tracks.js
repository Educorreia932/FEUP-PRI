import API from "@/api/API";

Object.unflatten = function (data) {
	if (Object(data) !== data || Array.isArray(data))
		return data;

	const regex = /\.?([^.[\]]+)|\[(\d+)]/g, resultholder = {};

	for (const p in data) {
		let cur = resultholder, prop = "", m;

		while ((m = regex.exec(p))) {
			cur = cur[prop] || (cur[prop] = (m[2] ? [] : {}));
			prop = m[2] || m[1];
		}

		cur[prop] = data[p];
	}

	return resultholder[""] || resultholder;
};

export default {
	search(start, searchTerms) {
		return API()
			.get("query", {
				params: {
					q: searchTerms,
					defType: "edismax",
					start: start,
					qf: "name^5 lyrics^3 artists.name^1 artists.genres albums.name^3",
				}
			})
			.then((response) => {
				const docs = response.data.response.docs;

				// Iterate over retrieved documents
				docs.forEach((doc, k) => {
					doc = Object.unflatten(doc)
					const fields = [doc.artists, doc.albums]

					fields.forEach((field, i) => {
						const obj = []

						for (let i = 0; i < field.uri.length; i++)
							obj.push({})

						Object.entries(field).forEach(([key, value]) => {
							for (let j = 0; j < obj.length; j++)
								obj[j][key] = value[j]
						})

						fields[i] = obj
					})

					doc.artists = fields[0]
					doc.albums = fields[1]

					doc.albums.artists = []

					for (const artist of doc.artists)
						doc.albums.artists.push(artist)

					docs[k] = doc;

				})

				return {
					"docs": docs,
					"found": response.data.response.numFound
				}
			})
	}
}