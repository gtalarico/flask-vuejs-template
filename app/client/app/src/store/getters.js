export default {

  getterOne: (state) => {
    return state.resourceOne
  },
  getterWithArg: (state) => (value) => {
    return state.resourceOne + value
  }
}
