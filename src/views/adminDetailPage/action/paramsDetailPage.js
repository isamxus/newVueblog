const Action = {
	//添加参数
	paramsDetailCreate (params) {
		let PostContent = params.PostContent;
		if(!PostContent.detailName) return Promise.reject({Msg: '请输入参数名称', type: 'local'});
		if(!PostContent.detailCode) return Promise.reject({Msg: '请输入参数权限码', type: 'local'});
        return axios.post(REQUEST_URL.paramsDetailCreate, REQUEST_URL.handleParams(params)).then(result => Promise.resolve(result.data.PostContent));
	},
	//更新参数
	paramsDetailUpdate (params) {
		let PostContent = params.PostContent;
		if(!PostContent.detailName) return Promise.reject({Msg: '请输入参数名称', type: 'local'});
		if(!PostContent.detailCode) return Promise.reject({Msg: '请输入参数权限码', type: 'local'});
        return axios.post(REQUEST_URL.paramsDetailUpdate, REQUEST_URL.handleParams(params)).then(result => Promise.resolve(result.data.PostContent));
	},
	//获取单个参数
	paramsDetailGetSingle (params) {
        return axios.post(REQUEST_URL.paramsDetailGetSingle, REQUEST_URL.handleParams(params)).then(result => Promise.resolve(result.data.PostContent));
	},
	//删除参数
	paramsDetailDelete (params) {
        return axios.post(REQUEST_URL.paramsDetailDelete, REQUEST_URL.handleParams(params)).then(result => Promise.resolve(result.data.PostContent));
	},
	//获取参数列表
	paramsDetailGetList (params) {
        return axios.post(REQUEST_URL.paramsDetailGetList, REQUEST_URL.handleParams(params)).then(result => Promise.resolve(result.data.PostContent));
	}
}

export default Action;