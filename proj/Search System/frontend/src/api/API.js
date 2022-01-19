import axios from "axios";

const API = () => {
	return axios.create({
		baseURL: "http://localhost:8983/solr/music/",
	})
}

export default API
