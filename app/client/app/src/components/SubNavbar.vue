<template>
  <nav class="tabs is-small">
    <ul>
      <router-link tag="li" activeClass='is-active' :to="{ path: 'one'}"><a>Page One</a></router-link>
      <router-link tag="li" activeClass='is-active' :to="{ path: 'two'}"><a>Page Two</a></router-link>
    </ul>
  </nav>
</template>

<script>
export default {
  name: 'SubNavbar'
}
</script>

<style lang="sass" scoped>

.tabs
	background-color: darken($background, 2)

</style>
