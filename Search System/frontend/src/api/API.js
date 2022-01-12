import axios from "axios";

export async function search() {
	return axios.get("http://localhost:8983/solr/music/query?q=*:*")
}