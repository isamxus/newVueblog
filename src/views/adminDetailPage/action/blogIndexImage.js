const Action = {
	//获取参数列表
	paramsDetailGetList (params) {
        return axios.post(REQUEST_URL.paramsDetailGetList, REQUEST_URL.handleParams(params)).then(result => Promise.resolve(result.data.PostContent));
	},
	//获取文章列表
	articleGetList(params){
        return axios.post(REQUEST_URL.articleGetList, REQUEST_URL.handleParams(params)).then(result => Promise.resolve(result.data.PostContent));
	},
	//获取轮播图集合
	IndexImageGetList(params){
        return axios.post(REQUEST_URL.IndexImageGetList, REQUEST_URL.handleParams(params)).then(result => Promise.resolve(result.data.PostContent));
	},
	//新增轮播图
	IndexImageCreate(params){
        return axios.post(REQUEST_URL.IndexImageCreate, REQUEST_URL.handleParams(params)).then(result => Promise.resolve(result.data.PostContent));
	},
	//更新轮播图
	IndexImageUpdate(params){
        return axios.post(REQUEST_URL.IndexImageUpdate, REQUEST_URL.handleParams(params)).then(result => Promise.resolve(result.data.PostContent));
	},
	//删除轮播图
	IndexImageDelete(params){
        return axios.post(REQUEST_URL.IndexImageDelete, REQUEST_URL.handleParams(params)).then(result => Promise.resolve(result.data.PostContent));
	}
}

export default Action;