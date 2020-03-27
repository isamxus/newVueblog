const Action = {
	//用户登录
	userLogin (params) {
		let PostContent = params.PostContent;
		if(!PostContent.UserName) return Promise.reject({Msg: '请输入用户名', type: 'local'});
		if(!PostContent.PassWord) return Promise.reject({Msg: '请输入密码', type: 'local'});
        return axios.post(REQUEST_URL.userLogin, REQUEST_URL.handleParams(params)).then(result => Promise.resolve(result.data));
	}
}

export default Action;