const Action = {
	testAxios (params) {
        return axios.post(REQUEST_URL.testAxios, REQUEST_URL.handleParams(params)).then(result => Promise.resolve(result));
	},
	//获取登录状态
	getStatusInfo(params){
        return axios.post(REQUEST_URL.userCheckStatus, REQUEST_URL.handleParams(params)).then(result => Promise.resolve(result));
	}
}

export default Action;

