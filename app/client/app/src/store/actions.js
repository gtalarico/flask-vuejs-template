import $backend from './backend'

export default {

  fetchResourceOne: function (context) {
    $backend.fetchResourceOne().then((responseData) => {
      context.commit('setResource', responseData)
    })
  },

  fetchResourceTwo: function (context, resourceId) {
    $backend.fetchResourceTwo(resourceId).then((responseData) => {
      context.commit('setResource', responseData)
    })
  }
}
