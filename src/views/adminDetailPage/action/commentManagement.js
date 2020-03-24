const Action = {
	//获取评论列表（分页）
	commentGetPageList (params) {
        return axios.post(REQUEST_URL.commentGetPageList, REQUEST_URL.handleParams(params)).then(result => Promise.resolve(result.data.PostContent));
	},
	//删除评论
	commentDelete (params) {
        return axios.post(REQUEST_URL.commentDelete, REQUEST_URL.handleParams(params)).then(result => Promise.resolve(result.data.PostContent));
	}
}

export default Action;