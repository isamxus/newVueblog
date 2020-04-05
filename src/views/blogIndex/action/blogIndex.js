const Action = {
	testAxios (params) {
        return axios.post(REQUEST_URL.testAxios, REQUEST_URL.handleParams(params)).then(result => Promise.resolve(result));
	},
	//获取登录状态
	getStatusInfo(params){
        return axios.post(REQUEST_URL.userCheckStatus, REQUEST_URL.handleParams(params)).then(result => Promise.resolve(result.data.PostContent));
	},
	//获取文章列表
	articleGetList (params) {
        return axios.post(REQUEST_URL.articleGetList, REQUEST_URL.handleParams(params)).then(result => Promise.resolve(result.data.PostContent));
	},
	//获取Tab页
	tabGetlist(params){
        return axios.post(REQUEST_URL.TabGetList, REQUEST_URL.handleParams(params)).then(result => Promise.resolve(result.data.PostContent));
	}
}

export default Action;

