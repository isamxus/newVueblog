const Action = {
	//用户登录
	userLogin (params) {
        return axios.post(REQUEST_URL.userLogin, REQUEST_URL.handleParams(params)).then(result => Promise.resolve(result.data.PostContent));
	}
}

export default Action;