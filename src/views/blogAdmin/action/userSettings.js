const Action = {
	//创建用户
	userUpdate (params) {
        return axios.post(REQUEST_URL.userUpdate, REQUEST_URL.handleParams(params)).then(result => Promise.resolve(result.data.PostContent));
	},
	//修改密码
	userChangePassword(params){
        return axios.post(REQUEST_URL.userChangePassword, REQUEST_URL.handleParams(params)).then(result => Promise.resolve(result.data.PostContent));
	}
}

export default Action;