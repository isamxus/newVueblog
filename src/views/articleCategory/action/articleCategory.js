const Action = {
	//获取文章列表
	articleGetList (params) {
        return axios.post(REQUEST_URL.articleGetList, REQUEST_URL.handleParams(params)).then(result => Promise.resolve(result.data.PostContent));
	}
}

export default Action;