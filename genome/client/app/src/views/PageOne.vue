<template>
  <section>

    <div class="container">
      <custom-component :data="'DataFromParent'"/>
    </div>

  </section>
</template>
<script>
import CustomComponent from '../components/CustomComponent'

export default {
  name: 'Property',
  components: {
    'custom-component': CustomComponent
  },
  data () {
    return {

    }
  },
  computed: {
    isLoading () {
      return this.$store.state.isLoading
    }
  }
}
</script>

<style lang="sass" scoped>

</style>
