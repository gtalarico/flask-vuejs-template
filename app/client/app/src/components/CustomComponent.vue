<template>
  <section>

    <div class="card">
      <header class="card-header">
        <p class="card-header-title">
          Page One
        </p>
      </header>
      <div class="card-content">
        <div class="content">
          Content
        </div>
      </div>
    </div>

  </section>
</template>

<script>

export default {
  name: 'CustomComponent',
  data () {
    return {

    }
  },
  watch: {
    viewToggleOther (bool) {
      this.setToggle('other', bool)
    }
  },
  methods: {
    setToggle: function (name, bool) {
      console.log('Toggle Called')
      // this.$store.commit('setToggle', [name, bool])
    }
  },
  computed: {
    floors () {
      return this.$store.state.floors
    }
  },
  mounted () {

  }
}
</script>

<style lang="sass" scoped>


</style>
