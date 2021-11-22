import Vuex from 'vuex';
import Vue from 'vue';

Vue.use(Vuex);

const store = new Vuex.Store({
  state: {
    bv_id: '',
    video: {},
    Dm_Info: {},
    isPending: true,
  },
  mutations: {
    changeBvid(state, bv) {
      state.bv_id = bv;
    },
    changeVideo(state, video) {
      state.video = video;
    },
    // eslint-disable-next-line camelcase
    changeDmInfo(state, Dm_Info) {
      // eslint-disable-next-line camelcase
      state.Dm_Info = Dm_Info;
    },
    changePendingStatus(state) {
      state.isPending = !state.isPending;
    },
  },
  getters: {
    readBvId(state) {
      return state.bv_id;
    },
    readVideoInfo(state) {
      return state.video;
    },
    readDmInfo(state) {
      return state.Dm_Info;
    },
    readPendingStatus(state) {
      return state.isPending;
    },
  },
  actions: {
    changeBvFun(context, bv) {
      context.commit('changeBvid', bv);
    },
    changeVideo(context, video) {
      context.commit('changeVideo', video);
    },
    // eslint-disable-next-line camelcase
    changeDmInfo(context, Dm_Info) {
      context.commit('changeDmInfo', Dm_Info);
    },
    changePendingStatus(context) {
      context.commit('changePendingStatus');
    },
  },
});

export default store;
