import Vue from 'vue';
import Vuex from 'vuex';

Vue.use(Vuex);

export default new Vuex.Store({
    state: {
        user: {
            username: 'some user',
            password: 'some password',
        },
        instaTags: [],
        imgLoadLocationStatus: '',
    },
    getters: {
        instaTags: (state) => state.instaTags,
        creds: (state) => state.user,
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
    },
    actions: {},
});
