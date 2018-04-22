// Vue.js Filters
// https://vuejs.org/v2/guide/filters.html

import Vue from 'vue'

let filters = {

  formatTimestamp (timestamp) {
    let datetime = new Date(timestamp)
    return datetime.toLocaleTimeString('en-US')
  }
}

// Register All Filters on import
Object.keys(filters).forEach(function (filterName) {
  Vue.filter(filterName, filters[filterName])
})
