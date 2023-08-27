import { createStore } from 'vuex'
import UserStore from './user'
export default new createStore({
  ...UserStore
})
