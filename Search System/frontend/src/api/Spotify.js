import Spotify from "node-spotify-api";

export async function getArtwork(uri) {
	const spotify = new Spotify({
		id: "511e04ae8586475cbf6b4b0914228bee",
		secret: "4d9bcb0f2ad548928b345c05a08f286b"
	});

	const type = uri.split(":")[1] + "s"

	const id = uri.split(":")[2]

	return (await spotify.request(`https://api.spotify.com/v1/${type}/${id}`)).images[1].url
}

