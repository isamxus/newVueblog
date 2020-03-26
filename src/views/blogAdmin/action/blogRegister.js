const Action = {
	//创建用户
	userCreate (params) {
        return axios.post(REQUEST_URL.userCreate, REQUEST_URL.handleParams(params)).then(result => Promise.resolve(result.data.PostContent));
	}
}

export default Action;