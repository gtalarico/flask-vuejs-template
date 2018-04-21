import axios from 'axios'

const IS_PRODUCTION = process.env.NODE_ENV === 'production'
const API_URL = IS_PRODUCTION ? '/api/' : 'http://localhost:5000/api/'

let $axios = axios.create({
  baseURL: API_URL,
  timeout: 5000,
  headers: {'Content-Type': 'application/json'}
})

$axios.interceptors.response.use(function (response) {
  return response
}, function (error) {
  console.log(error)
  return Promise.reject(error)
})

export default {

  fetchResourceOne () {
    return $axios.get(`resource/one`)
      .then(response => response.data)
  },

  fetchResourceTwo (resourceId) {
    return $axios.get(`secure-resource/${resourceId}`,
      {'headers': {'authorization': 'token'}})
      .then(response => response.data)
  }
}
