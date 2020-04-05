const Action = {
	//添加参数
	paramsCreate (params) {
		let PostContent = params.PostContent;
		if(!PostContent.paramsName) return Promise.reject({Msg: '请输入参数名称', type: 'local'});
		if(!PostContent.paramsCode) return Promise.reject({Msg: '请输入参数权限码', type: 'local'});
        return axios.post(REQUEST_URL.paramsCreate, REQUEST_URL.handleParams(params)).then(result => Promise.resolve(result.data.PostContent));
	},
	//更新参数
	paramsUpdate (params) {
		let PostContent = params.PostContent;
		if(!PostContent.paramsName) return Promise.reject({Msg: '请输入参数名称', type: 'local'});
		//if(!PostContent.paramsCode) return Promise.reject({Msg: '请输入参数权限码', type: 'local'});
        return axios.post(REQUEST_URL.paramsUpdate, REQUEST_URL.handleParams(params)).then(result => Promise.resolve(result.data.PostContent));
	},
	//获取单个参数
	paramsGetSingle (params) {
        return axios.post(REQUEST_URL.paramsGetSingle, REQUEST_URL.handleParams(params)).then(result => Promise.resolve(result.data.PostContent));
	},
	//删除参数
	paramsDelete (params) {
        return axios.post(REQUEST_URL.paramsDelete, REQUEST_URL.handleParams(params)).then(result => Promise.resolve(result.data.PostContent));
	},
	//获取参数列表
	paramsGetList (params) {
        return axios.post(REQUEST_URL.paramsGetList, REQUEST_URL.handleParams(params)).then(result => Promise.resolve(result.data.PostContent));
	}
}

export default Action;

