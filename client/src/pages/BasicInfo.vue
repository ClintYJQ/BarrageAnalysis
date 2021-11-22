<template>
  <div>
    <a-page-header
      style="border: 1px solid rgb(235, 237, 240)"
      v-bind:title="video.title"
      @back="() => $router.go(-1)"
    >
      <template slot="footer">
        <a-tabs default-active-key="1">
          <a-tab-pane key="1" tab="Details" />
        </a-tabs>
      </template>
      <div class="content">
        <div class="main">
          <a-descriptions size="small" :column="2">
            <a-descriptions-item label="Created">
              {{ video.owner.name }}
            </a-descriptions-item>
            <a-descriptions-item label="Association">
              <a v-bind:href="video.link">视频链接</a>
            </a-descriptions-item>
            <a-descriptions-item label="Tag">
              {{ video.tag }}
            </a-descriptions-item>
            <a-descriptions-item label="Creation Time">
              {{ video.pub_date }}
            </a-descriptions-item>
            <a-descriptions-item label="Description">
              {{ video.description }}
            </a-descriptions-item>
          </a-descriptions>
        </div>
        <div class="extra">
          <div
            :style="{
              display: 'flex',
              width: 'max-content',
              justifyContent: 'flex-end',
            }"
          >
            <a-statistic
              title="播放量"
              v-bind:value="video.stat.view"
              :style="{
                marginRight: '32px',
              }"
            />
            <a-statistic title="投币" prefix="$" v-bind:value="video.stat.coin"  :style="{
                marginRight: '32px',
              }"/>
            <a-statistic title="点赞"  v-bind:value="video.stat.like" :style="{
                marginRight: '32px',
              }" />
            <a-statistic title="评论"  v-bind:value="video.stat.reply" />
          </div>
        </div>
      </div>
    </a-page-header>
  </div>
</template>

<script>
export default {
  name: 'BasicInfo',
  data() {
    return {
    // eslint-disable-next-line no-empty
      video: {},
      // eslint-disable-next-line no-unused-expressions
      bv_id: '',
    };
  },
  created() {
    if (this.$store.getters.readBvId === '') {
      this.$router.push('/');
    }
    this.bv_id = this.$store.getters.readBvId;
    this.video = this.$store.getters.readVideoInfo;
  },
};
</script>

<style scoped>
tr:last-child td {
  padding-bottom: 0;
}
#components-page-header-demo-responsive .content {
  display: flex;
}
#components-page-header-demo-responsive .ant-statistic-content {
  font-size: 20px;
  line-height: 28px;
}
@media (max-width: 576px) {
  #components-page-header-demo-responsive .content {
    display: block;
  }

  #components-page-header-demo-responsive .main {
    width: 100%;
    margin-bottom: 12px;
  }

  #components-page-header-demo-responsive .extra {
    width: 100%;
    margin-left: 0;
    text-align: left;
  }
}
</style>
