const Action = {
	//获取参数列表
	paramsDetailGetList (params) {
        return axios.post(REQUEST_URL.paramsDetailGetList, REQUEST_URL.handleParams(params)).then(result => Promise.resolve(result.data.PostContent));
	}
}

export default Action;