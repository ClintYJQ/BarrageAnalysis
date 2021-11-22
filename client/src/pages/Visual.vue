<template>
    <div>
        <h1 v-if="this.$store.getters.readPendingStatus">{{ msg }}</h1>
      <a-row :gutter="[8,16]">
          <a-col>
            <div v-if="!this.$store.getters.readPendingStatus"
                 id="date_info" style="width: 500px; height: 500px">
            </div>
          </a-col>
          <a-col :span="12"/>
      </a-row>
    </div>
</template>

<script>

const echarts = require('echarts');

export default {
  name: 'Visual',
  data() {
    return {
      msg: '弹幕获取中',
      Dm_info: {},
    };
  },
  created() {
    if (this.$store.getters.readBvId === '') {
      this.msg = '请输入bv号开始分析';
      this.$router.push('/');
    }
    this.Dm_info = this.$store.getters.readDmInfo;
    if (JSON.stringify(this.Dm_info) !== '{}') {
      console.log('创建成功');
    }
  },
  mounted() {
    const that = this;
    const lineChart = echarts.init(document.getElementById('date_info'));
    lineChart.setOption({
      title: {
        text: '弹幕时间分布',
      },
      tooltip: {},
      xAxis: {
        data: that.Dm_info.date_info.date_list,
      },
      yAxis: {},
      series: [{
        name: '数目',
        type: 'bar',
        data: that.Dm_info.date_info.date_count,
      }],
    });
  },
};
</script>

<style scoped>

</style>
