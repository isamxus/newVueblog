const Action = {
	testAxios (params) {
        return axios.post(REQUEST_URL.testAxios).then(result => Promise.resolve(result));
	}
}

export default Action;

