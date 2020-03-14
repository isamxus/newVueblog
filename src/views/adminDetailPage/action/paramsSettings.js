const Action = {
	//添加参数
	paramsCreate (params) {
        return axios.post(REQUEST_URL.paramsCreate, REQUEST_URL.handleParams(params)).then(result => Promise.resolve(result.data.PostContent));
	},
	//添加参数
	paramsGetList (params) {
        return axios.post(REQUEST_URL.paramsGetList, REQUEST_URL.handleParams(params)).then(result => Promise.resolve(result.data.PostContent));
	}
}

export default Action;

