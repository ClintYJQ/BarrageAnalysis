import BootstrapVue from 'bootstrap-vue';
import Vue from 'vue';
import Antd from 'ant-design-vue';
import Router from 'vue-router';
import App from './App.vue';
import router from './router';
import 'ant-design-vue/dist/antd.css';
import 'bootstrap/dist/css/bootstrap.css';
import store from './store';

Vue.config.productionTip = false;
Vue.use(BootstrapVue);
Vue.use(Antd);
Vue.use(Router);

new Vue({
  el: '#app',
  router: new Router(router),
  components: { App },
  store,
  render: (h) => h(App),
}).$mount('#app');
