import { createRouter, createWebHistory} from 'vue-router';

import UserSignature from '@/views/Signature.vue';

const routes = [
  {
    path: '/',
    name: 'Signature',
    component: UserSignature,
  },
];

const router = new createRouter({
  history: createWebHistory(),
  routes,
});

export default router;
