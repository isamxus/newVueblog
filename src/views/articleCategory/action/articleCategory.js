const Action = {
	//获取文章列表
	articleGetList (params) {
        return axios.post(REQUEST_URL.articleGetList, REQUEST_URL.handleParams(params)).then(result => Promise.resolve(result.data.PostContent));
	},
	//获取一盘文章
	articleGetSingle (params) {
        return axios.post(REQUEST_URL.articleGetSingle, REQUEST_URL.handleParams(params)).then(result => Promise.resolve(result.data.PostContent));
	},
	//获取文章列表（分页）
	articleGetPageList (params) {
        return axios.post(REQUEST_URL.articleGetPageList, REQUEST_URL.handleParams(params)).then(result => Promise.resolve(result.data.PostContent));
	},
	
}

export default Action;