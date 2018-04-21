export default {

  getterOne: (state) => {
    return state.resources[0]
  },
  getterWithArg: (state) => (index) => {
    return state.resources[value]
  }
}
