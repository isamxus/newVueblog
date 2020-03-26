const Action = {
	//获取用户数据
	userGetPageList (params) {
        return axios.post(REQUEST_URL.userGetPageList, REQUEST_URL.handleParams(params)).then(result => Promise.resolve(result.data.PostContent));
	},
	//更新用户
	userUpdate (params) {
        return axios.post(REQUEST_URL.userUpdate, REQUEST_URL.handleParams(params)).then(result => Promise.resolve(result.data.PostContent));
	},
	//删除用户数据
	userDelete (params) {
        return axios.post(REQUEST_URL.userDelete, REQUEST_URL.handleParams(params)).then(result => Promise.resolve(result.data.PostContent));
	}
}

export default Action;