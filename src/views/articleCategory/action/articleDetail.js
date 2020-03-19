const Action = {
	//获取一盘文章
	articleGetSingle (params) {
        return axios.post(REQUEST_URL.articleGetSingle, REQUEST_URL.handleParams(params)).then(result => Promise.resolve(result.data.PostContent));
	},
}

export default Action;