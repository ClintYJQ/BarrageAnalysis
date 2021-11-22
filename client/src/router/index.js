const router = {
  routes: [
    {
      path: '/',
      name: '404',
      component: () => import('../pages/404'),
    },
    {
      path: '/info',
      name: 'BasicInfo',
      component: () => import('../pages/BasicInfo'),
    },
    {
      path: '/visual',
      name: 'Visual',
      component: () => import('../pages/Visual'),
    },
  ],
};
export default router;
