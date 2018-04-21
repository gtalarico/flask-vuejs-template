<template>
  <section>

    <div class="card">
      <header class="card-header">
        <p class="card-header-title">
          Page One - {{propsData}}
        </p>
      </header>
      <div class="card-content">
        <div class="content">
          Content
          <div>{{ resources }}</div>
        </div>
      </div>
    </div>

  </section>
</template>

<script>

export default {
  name: 'CustomComponent',
  props: ['propsData'],
  data () {
    return {
    }
  },
  computed: {
    resources () {
      // To display `resourceOne` value from the backend
      return this.$store.state.resources
    }
  },
  mounted () {
    this.$store.dispatch('fetchResourceOne')
  }
}
</script>

<style lang="sass" scoped>


</style>
