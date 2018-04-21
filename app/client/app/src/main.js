import Vue from 'vue'
import router from './router.js'
import store from './store'
import App from './App.vue'

import './filters.js'
import Mixins from './mixins.js'
Vue.mixin(Mixins)

var vue = new Vue({
  el: '#vue-app',
  router,
  store,
  template: '<App/>',
  mixins: [Mixins],
  components: { App }
})
