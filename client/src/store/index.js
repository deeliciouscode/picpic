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
    },
    getters: {
        instaTags: (state) => state.instaTags,
        creds: (state) => state.user,
        imgIds: (state) => state.imgIds,
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
            // eslint-disable-next-line
            alert("Your Username us now set to " +  state.user.username)
        },
        imgLoadLocationStatus(state, payload) {
            state.imgLoadLocationStatus = payload.imgLoadLocationStatus;
        },
        addImgIds(state, payload) {
            // eslint-disable-next-line
            console.log("ids:", payload.imgIds)
            state.imgIds = payload.imgIds;
        },
    },
    actions: {},
});
