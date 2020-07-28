import Vue from 'vue';
import Vuex from 'vuex';

Vue.use(Vuex);

export default new Vuex.Store({
    state: {
        user: {
            username: 'some_user',
            password: 'some_password',
        },
        instaTags: [],
        imgLoadLocationStatus: '',
        imgIds: [],
        mosaicImgId: '',
        finalIsReady: false,
    },
    getters: {
        instaTags: (state) => state.instaTags,
        creds: (state) => state.user,
        imgIds: (state) => state.imgIds,
        finalIsReady: (state) => state.finalIsReady,
    },
    mutations: {
        addTag(state, payload) {
            const newTag = {
                tag: payload.tag,
            };
            // eslint-disable-next-line
            if (payload.tag) {
                state.instaTags.push(newTag);
            }
        },
        updateCreds(state, payload) {
            state.user = payload.creds;
        },
        imgLoadLocationStatus(state, payload) {
            state.imgLoadLocationStatus = payload.imgLoadLocationStatus;
        },
        addImgIds(state, payload) {
            // eslint-disable-next-line
            // console.log("ids:", payload.imgIds)
            state.imgIds = payload.imgIds;
        },
        setMosaicImgId(state, payload) {
            state.mosaicImgId = payload.mosaicImgId;
        },
        toggleMosaicDownload(state) {
            state.finalIsReady = !state.finalIsReady;
        },
        clearData(state) {
            state.user = {
                username: 'some_user',
                password: 'some_password',
            };
            state.instaTags = [];
            state.imgLoadLocationStatus = '';
            state.imgIds = [];
            state.mosaicImgId = '';
            state.finalIsReady = false;
        },
    },
    actions: {},
});
