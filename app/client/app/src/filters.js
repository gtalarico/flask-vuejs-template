// Vue.js Filters
// https://vuejs.org/v2/guide/filters.html

import Vue from 'vue'

let filters = {

  formatNumber (value) {
  	let val = (value / 1)
		return val.toString().replace(/\B(?=(\d{3})+(?!\d))/g, ',')
	}
}

// Register Filters
Object.keys(filters).forEach(function (filterName) {
  Vue.filter(filterName, filters[filterName])
})
