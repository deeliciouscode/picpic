import Vue from 'vue';
import VueRouter from 'vue-router';
import Ping from '../components/Ping.vue';
import Creator from '../components/Creator.vue';

Vue.use(VueRouter);

const routes = [
    {
        path: '/ping',
        name: 'Ping',
        component: Ping,
    },
    {
        path: '/',
        name: 'Creator',
        component: Creator,
    },
];

const router = new VueRouter({
    mode: 'history',
    base: process.env.BASE_URL,
    routes,
});

export default router;
