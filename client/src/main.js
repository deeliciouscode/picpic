import 'bootstrap/dist/css/bootstrap.css';
import Vue from 'vue';
import Buefy from 'buefy';
import App from './App.vue';
import router from './router';
import store from './store';
import 'buefy/dist/buefy.css';
import '@fortawesome/fontawesome-free/css/all.css';
import '@fortawesome/fontawesome-free/js/all';
import 'material-design-icons';

Vue.config.productionTip = false;

Vue.use(Buefy);

new Vue({
    store,
    router,
    render: (h) => h(App),
}).$mount('#app');
