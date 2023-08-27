const loginUser = (state, payload) => {
    state.data.user = payload
}
const updateUserToken = (state, payload) => {
    state.data.user.token = payload
}

export default {
    loginUser,
    updateUserToken
}