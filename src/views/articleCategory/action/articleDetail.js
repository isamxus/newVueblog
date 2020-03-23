const Action = {
	//获取一盘文章
	articleGetSingle (params) {
        return axios.post(REQUEST_URL.articleGetSingle, REQUEST_URL.handleParams(params)).then(result => Promise.resolve(result.data.PostContent));
	},
	//创建一条评论
	commentCreate (params) {
		let PostContent = params.PostContent;
		if(!PostContent.commentContent) return Promise.reject({Msg: '请输入评论内容', type: 'local'});
		if(!PostContent.parentArticleID) return Promise.reject({Msg: '创建评论失败', type: 'local'});
        return axios.post(REQUEST_URL.commentCreate, REQUEST_URL.handleParams(params)).then(result => Promise.resolve(result.data.PostContent));
	},
	//获取评论列表（分页）
	commentGetPageList (params) {
        return axios.post(REQUEST_URL.commentGetPageList, REQUEST_URL.handleParams(params)).then(result => Promise.resolve(result.data.PostContent));
	}
}

export default Action;