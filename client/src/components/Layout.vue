<template>
  <a-layout id="components-layout-demo-top-side">
    <a-layout-header class="header">
      <div class="logo" />
      <div class="searchInput">
        <a-input-search placeholder="请输入视频bv号" enter-button @search="onSearch"/>
      </div>
    </a-layout-header>
    <a-layout-content style="padding: 0 50px">
      <a-breadcrumb style="margin: 16px 0 40px 50px">
      </a-breadcrumb>
      <a-layout style="padding: 24px 0; background: #fff">
        <a-layout-sider width="200" style="background: #fff">
          <a-menu
            :default-selected-keys="[$route.path]"
            :selectedKeys = "[$route.path]"
            mode="inline"
            theme="light"
            style="{height: 100% }"
            @click="menuClick"
          >
            <a-menu-item key="/info">
              <a-icon type="pie-chart" />
              <span>基本信息</span>
            </a-menu-item>
            <a-menu-item key="/visual">
              <a-icon type="desktop" />
              <span>可视化</span>
            </a-menu-item>
            <a-menu-item key="/wordCloud">
              <a-icon type="inbox" />
              <span>云词图下载</span>
            </a-menu-item>
          </a-menu>
        </a-layout-sider>
        <a-layout-content :style="{ padding: '0 24px', minHeight: '280px' }">
          <router-view/>
        </a-layout-content>
      </a-layout>
    </a-layout-content>
    <a-layout-footer style="text-align: center">
      Barrage Analysis ©2021 Created by Yang Jiqian
    </a-layout-footer>
  </a-layout>
</template>

<script>
import { getVideoBv, getVideoDm } from '../api';

export default {
  name: 'LayOut',
  created() {
    this.$router.push('/');
  },
  methods: {
    async onSearch(value) {
      console.log(value);
      getVideoBv(value)
        .then((res) => {
          this.$store.dispatch('changePendingStatus');
          console.log(res.message);
          console.log(res.video.info);
          this.$store.dispatch('changeBvFun', value);
          this.$store.dispatch('changeVideo', res.video.info);
          this.$router.push('/info');
        })
        .catch((err) => {
          console.log(err);
        });
      await getVideoDm(value).then((res) => {
        console.log(res.message);
        console.log(res.Dm_Info);
        this.$store.dispatch('changeDmInfo', res.Dm_Info);
        this.$store.dispatch('changePendingStatus');
      }).catch((err) => {
        console.log(err);
      });
    },
    menuClick({ key }) {
      this.$router.push(
        { path: key },
      );
    },
  },
};
</script>

<style scoped>
#components-layout-demo-top-side .logo {
  width: 120px;
  height: 31px;
  background: rgba(255, 255, 255, 0.2);
  margin: 16px 28px 16px 0;
  float: left;
}

#components-layout-demo-top-side .searchInput {
  width: 250px;
  height: 31px;
  margin: 16px 55px 16px 50px;
  float: left;
}

</style>
