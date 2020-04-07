const Action = {
	//创建用户
	userCreate (params) {
		let PostContent = params.PostContent;
		if(!PostContent.UserName) return Promise.reject({Msg: '请输入用户名', type: 'local'});
		if(!PostContent.PassWord) return Promise.reject({Msg: '请输入密码', type: 'local'});
		if(!PostContent.PassWordConfirm) return Promise.reject({Msg: '请再次输入密码', type: 'local'});
		if(PostContent.PassWordConfirm != PostContent.PassWord) return Promise.reject({Msg: '两次输入的密码不一致', type: 'local'});
        return axios.post(REQUEST_URL.userCreate, REQUEST_URL.handleParams(params)).then(result => Promise.resolve(result.data.PostContent));
	}
}

export default Action;