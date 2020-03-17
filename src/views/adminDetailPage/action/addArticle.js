const Action = {
	//获取参数列表
	paramsDetailGetList (params) {
        return axios.post(REQUEST_URL.paramsDetailGetList, REQUEST_URL.handleParams(params)).then(result => Promise.resolve(result.data.PostContent));
	},
	//添加文章
	articleCreate (params) {
		let PostContent = params.PostContent;
		if(!PostContent.articleTitle) return Promise.reject({Msg: '请输入文章标题', type: 'local'});
		if(!PostContent.articleAuthor) return Promise.reject({Msg: '请输入作者', type: 'local'});
		if(!PostContent.articleContent) return Promise.reject({Msg: '请输入文章正文', type: 'local'});
		if(!PostContent.articleCagetoryID) return Promise.reject({Msg: '请输入文章分类', type: 'local'});
		PostContent.articleTagsID = PostContent.articleTagsID.join(',');
		PostContent.articleTagsName = PostContent.articleTagsName.join(',');
        return axios.post(REQUEST_URL.articleCreate, REQUEST_URL.handleParams(params)).then(result => Promise.resolve(result.data.PostContent));
	},
	//更新文章
	articleUpdate (params) {
		let PostContent = params.PostContent;
		if(!PostContent.articleTitle) return Promise.reject({Msg: '请输入文章标题', type: 'local'});
		if(!PostContent.articleAuthor) return Promise.reject({Msg: '请输入作者', type: 'local'});
		if(!PostContent.articleContent) return Promise.reject({Msg: '请输入文章正文', type: 'local'});
		if(!PostContent.articleCagetoryID) return Promise.reject({Msg: '请输入文章分类', type: 'local'});
		PostContent.articleTagsID = PostContent.articleTagsID.join(',');
		PostContent.articleTagsName = PostContent.articleTagsName.join(',');
        return axios.post(REQUEST_URL.articleUpdate, REQUEST_URL.handleParams(params)).then(result => Promise.resolve(result.data.PostContent));
	},
	//获取一盘文章
	articleGetSingle (params) {
        return axios.post(REQUEST_URL.articleGetSingle, REQUEST_URL.handleParams(params)).then(result => Promise.resolve(result.data.PostContent));
	},
	//获取文章列表
	articleGetList (params) {
        return axios.post(REQUEST_URL.articleGetList, REQUEST_URL.handleParams(params)).then(result => Promise.resolve(result.data.PostContent));
	}
}

export default Action;