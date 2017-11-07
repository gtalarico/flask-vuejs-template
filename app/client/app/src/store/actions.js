import Vue from 'vue'
import backend from './backend'

export default {

  fetchResouceOne: function  (context) {
    backend.fetchResouceOne(function(responseData) {
      context.commit('setResource', responseData)
    })
  },

  fetchResouceTwo: function  (context, resouceId) {
  	backend.fetchResouceTwo(resouceId, function(responseData) {
  		context.commit('setResource', responseData)
  	})
  }
}
