const Host = {
    host: 'http://127.0.0.1:8000/'
};

module.exports = {
    Urls: {
        testAxios: `${Host.host}`,
        //参数设置api
        paramsCreate: `${Host.host}ParamsSettings/Create/`,
        paramsUpdate: `${Host.host}ParamsSettings/Update/`,
        paramsGetSingle: `${Host.host}ParamsSettings/GetSingle/`,
        paramsDelete: `${Host.host}ParamsSettings/Delete/`,
        paramsGetList: `${Host.host}ParamsSettings/GetList/`,
    }
}