import axios from 'axios'


let $axios = axios.create({
    baseURL: 'http://127.0.0.1:5000/api/',
    timeout: 5000,
    headers: {'Content-Type': 'application/json'}
})

$axios.interceptors.response.use(function (response) {
    return response
  }, function (error) {
    console.log(error)
    return Promise.reject(error)
  });

export default {

  fetchResourceOne () {
    return $axios.get(`resource/one`)
      .then(response => response.data)
  },

  fetchResourceTwo (resourceId) {
    return $axios.get(`resource/two/${resourceId}`)
      .then(response => response.data)
  }
}
