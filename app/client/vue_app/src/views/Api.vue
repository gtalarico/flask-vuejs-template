<template>
  <div class="about">
    <h1>Backend Resources</h1>
    <a href="" @click.prevent="fetchResource">Fetch</a><br/>
    <a href="" @click.prevent="fetchSecureResource">Fetch Secure Resource</a>
    <h5>Results</h5>
    <p v-for="r in resources" :key="r.timestamp">
      Server Timestamp: {{r.timestamp | formatTimestamp }}
    </p>
  </div>
</template>

<script>

import $backend from '../backend'

export default {
  name: 'about',
  data () {
    return {
      resources: []
    }
  },
  methods: {
    fetchResource () {
      $backend.fetchResource().then(responseData => {
        this.resources.push(responseData)
      })
    },
    fetchSecureResource () {
      $backend.fetchSecureResource().then(responseData => {
        this.resources.push(responseData)
      })
    }
  }
}

</script>
