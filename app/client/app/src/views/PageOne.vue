<template>
  <section>

    <div class="container">
      <p v-if="isLoading">Loading...</p>
      <panel-component v-else :propsData="'Page One'"/>
    </div>

  </section>
</template>
<script>
import aPanel from '../components/aPanel'

export default {
  name: 'Property',
  components: {
    'panel-component': aPanel
  },
  data () {
    return {

    }
  },
  computed: {
    isLoading () {
      return this.$store.state.resources < 2
    }
  },
  mounted () {
    this.$store.dispatch('fetchResourceOne')
  }
}
</script>

<style lang="sass" scoped>

</style>
