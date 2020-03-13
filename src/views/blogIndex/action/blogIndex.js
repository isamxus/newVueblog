import QS from 'qs';

const Action = {
	testAxios (params) {
        return axios.post(REQUEST_URL.testAxios, REQUEST_URL.handleParams(params)).then(result => Promise.resolve(result));
	}
}

export default Action;

