const Action = {
	//获取Tab页
	tabGetlist(params){
        return axios.post(REQUEST_URL.TabGetList, REQUEST_URL.handleParams(params)).then(result => Promise.resolve(result.data.PostContent));
	},
	//新增Tab页
	TabCreate(params){
        return axios.post(REQUEST_URL.TabCreate, REQUEST_URL.handleParams(params)).then(result => Promise.resolve(result.data.PostContent));
	},
	//更新Tab页
	TabUpdate(params){
        return axios.post(REQUEST_URL.TabUpdate, REQUEST_URL.handleParams(params)).then(result => Promise.resolve(result.data.PostContent));
	},
	//删除Tab页
	TabDelete(params){
        return axios.post(REQUEST_URL.TabDelete, REQUEST_URL.handleParams(params)).then(result => Promise.resolve(result.data.PostContent));
	}
}

export default Action;