<template>
  <div id="app">
    <div id="nav">
      <router-link to="/">Home</router-link> |
      <router-link to="/api">API Sample</router-link>
    </div>
    <div id="logos">
      <p>
        <img src="./assets/vue-logo.png">
        <span id="plus">+</span>
        <img src="./assets/flask-logo.png">
      </p>
    </div>
    <router-view/>
  </div>
</template>

<style lang="scss">
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}
#nav {
  padding: 30px;
  a {
    font-weight: bold;
    color: #2c3e50;
    &.router-link-exact-active {
      color: #42b983;
    }
  }
}
#plus {
  padding: 0 20px 0 20px;
  display: inline-block;
  font-size: 50px;
  vertical-align: top;
  line-height: 100px;
}

</style>
