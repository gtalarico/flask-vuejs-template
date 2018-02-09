import axios from 'axios'


let $backend = axios.create({
    baseURL: 'http://127.0.0.1:5000/api/',
    timeout: 5000,
    headers: {'Content-Type': 'application/json'}
})

$backend.interceptors.response.use(function (response) {
    return response
  }, function (error) {
    console.log(error)
    return Promise.reject(error)
  });

export default {

  fetchResourceOne () {
    return $backend.get(`resource/one`)
      .then(response => response.data)
  },

  fetchResourceTwo (resourceId) {
    return $backend.get(`resource/two/${resourceId}`)
      .then(response => response.data)
  }
}
