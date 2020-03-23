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

        //获取参数详情api
        paramsDetailCreate: `${Host.host}ParamsDetailSettings/Create/`,
        paramsDetailUpdate: `${Host.host}ParamsDetailSettings/Update/`,
        paramsDetailGetSingle: `${Host.host}ParamsDetailSettings/GetSingle/`,
        paramsDetailDelete: `${Host.host}ParamsDetailSettings/Delete/`,
        paramsDetailGetList: `${Host.host}ParamsDetailSettings/GetList/`,

        //博客文章api
        articleCreate: `${Host.host}Article/Create/`,
        articleUpdate: `${Host.host}Article/Update/`,
        articleGetSingle: `${Host.host}Article/GetSingle/`,
        articleDelete: `${Host.host}Article/Delete/`,
        articleGetList: `${Host.host}Article/GetList/`,
        articleGetPageList: `${Host.host}Article/GetPageList/`,

        //文章评论api
        commentCreate: `${Host.host}Comment/Create/`,
        commentUpdate: `${Host.host}Comment/Update/`,
        commentGetSingle: `${Host.host}Comment/GetSingle/`,
        commentDelete: `${Host.host}Comment/Delete/`,
        commentGetList: `${Host.host}Comment/GetList/`,
        commentGetPageList: `${Host.host}Comment/GetPageList/`,
    }
}