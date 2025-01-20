<template>
  <div class="esign">
    <h1>画板测试</h1>

    <div class="esign-box">
      <vue-esign class="esignature" ref="esign" :width="800" :height="300" :isCrop="isCrop" :lineWidth="lineWidth" :lineColor="lineColor" v-model:bgColor="bgColor" @pointerdown="handlePointerStart"/>
    </div>
    <div class="esigh-btns">
      <button @click="handleReset">清空画板</button> 
      <button @click="handleGenerate">生成图片</button>
    </div>
    <div class="esigh-result">
      <img v-if="resultImg" :src="resultImg" alt="">
    </div>
  </div>
</template>

<script>
import VueEsign from 'vue-esign';

export default {
  name: 'UserSignature',
  components: {
    VueEsign, // 局部注册 vue-esign
  },
  mounted() {
  console.log(this.$refs.signature);
},

  data() {
    return {
    lineWidth: 6,
    lineColor: '#000000',
    bgColor: '',
    resultImg: '',
    isCrop: false
  }
  },
  methods: {
  handleReset () {
    this.$refs.esign.reset()
  },
  handleGenerate () {
    this.$refs.esign.generate().then(res => {
      this.resultImg = res
    }).catch(err => {
      alert(err) // 画布没有签字时会执行这里 'Not Signned'
    })
  },
  handlePointerStart(event) {
      // 检查 pointerType 并设置提示
      if (event.pointerType === 'touch') {
        this.touchType = '使用手指触摸';
      } else if (event.pointerType === 'pen') {
        this.touchType = '使用笔触摸';
      } else {
        this.touchType = '未知的触摸类型';
      }
      alert(this.touchType); // 输出提示
    },
}
};
</script>

<style scoped>
.esign {
  max-width: 1000px;
  margin: auto;
  padding: 10px;
}
.esigh-btns button{
  color: #fff;
  height: 40px;
  width: 100px;
  font-size: 16px;
  margin-right: 10px;
  outline: none;
  border-radius: 4px;
  background: #F60;
  border: 1px solid transparent; 
}
.esigh-btns button:active{ 
  color:#fff; 
  box-shadow: 0px 0px 50px orangered inset; 
}
.esigh-result {
  margin-top: 10px;
}
.esigh-result img {
  display: block;
  max-width: 100%;
  height: auto;
  border: 1px solid #ececee;
}
.esignature {
  margin: 10px 0;
  border: 2px solid #ccc;
}
</style>