import Vue from 'vue'
import backend from './backend'

export default {

  fetchResourceOne: function  (context) {
    backend.fetchResourceOne().then((responseData) => {
      context.commit('setResource', responseData)
    })
  },

  fetchResourceTwo: function  (context, resouceId) {
  	backend.fetchResourceTwo(resouceId).then((responseData) => {
  		context.commit('setResource', responseData)
  	})
  }
}
