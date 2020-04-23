const Host = {
    host: 'http://127.0.0.1:8000/',
    //host: 'http://www.amxus.info/'
};

module.exports = {
    Urls: {
        //静态资源下载
        staticDownload: `${Host.host}media/`,

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

        //用户管理api
        userCreate: `${Host.host}User/Create/`,
        userUpdate: `${Host.host}User/Update/`,
        userDelete: `${Host.host}User/Delete/`,
        userChangePassword: `${Host.host}User/ChangePassword/`,
        userGetPageList: `${Host.host}User/GetPageList/`,
        userLogin: `${Host.host}User/Login/`,
        userCheckStatus: `${Host.host}User/CheckLoginStatus/`,
        userImageUpload: `${Host.host}UserImage/Upload/`,


        //首页Tab api
        TabCreate: `${Host.host}Tab/Create/`,
        TabUpdate: `${Host.host}Tab/Update/`,
        TabGetSingle: `${Host.host}Tab/GetSingle/`,
        TabDelete: `${Host.host}Tab/Delete/`,
        TabGetList: `${Host.host}Tab/GetList/`,

        //首页轮播图 api
        IndexImageUpload: `${Host.host}IndexImage/Upload/`,
        IndexImageDownload: `${Host.host}media/`,
        IndexImageCreate: `${Host.host}IndexImage/Create/`,
        IndexImageUpdate: `${Host.host}IndexImage/Update/`,
        IndexImageGetSingle: `${Host.host}IndexImage/GetSingle/`,
        IndexImageDelete: `${Host.host}IndexImage/Delete/`,
        IndexImageGetList: `${Host.host}IndexImage/GetList/`,

    }
}