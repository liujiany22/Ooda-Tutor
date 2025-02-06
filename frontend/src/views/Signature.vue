<template>
  <div class="esign">
    <h1>画板与正方形测试</h1>
    <div class="esign-box" ref="esignBox">
      <!-- vue-esign 画板 -->
      <vue-esign
        class="esignature"
        ref="esign"
        :width="800"
        :height="300"
        :isCrop="isCrop"
        :lineWidth="lineWidth"
        :lineColor="lineColor"
        v-model:bgColor="bgColor"
        @pointerdown="handlePointerStart"
      />

      <!-- canvas 区域 -->
      <canvas
        ref="canvas"
        :width="800"
        :height="300"
        class="canvas-layer"
        @pointerdown="handleCanvasPointerDown"
        @pointermove="handleCanvasPointerMove"
        @pointerup="handleCanvasPointerUp"
      ></canvas>
    </div>

    <div class="esigh-btns">
      <button @click="handleReset">清空画板</button>
      <button @click="handleGenerate">生成图片</button>
    </div>

    <div class="esigh-result">
      <img v-if="resultImg" :src="resultImg" alt="生成的图片" />
    </div>
  </div>
</template>

<script>
import VueEsign from "vue-esign";

export default {
  name: "UserSignature",
  components: {
    VueEsign,
  },
  data() {
    return {
      lineWidth: 6,
      lineColor: "#000000",
      bgColor: "",
      resultImg: "",
      isCrop: false,
      touchType: "",
      square: {
        x: 50, // 正方形初始位置
        y: 50,
        size: 50,
        dragging: false,
      },
    };
  },
  mounted() {
    this.canvas = this.$refs.canvas;
    this.context = this.canvas.getContext("2d");
    this.drawSquare(); // 绘制初始正方形
  },
  methods: {
    handleReset() {
      this.$refs.esign.reset();
    },
    handleGenerate() {
      this.$refs.esign
        .generate()
        .then((res) => {
          this.resultImg = res;
        })
        .catch((err) => {
          alert(err); // 画布没有签字时会执行这里 'Not Signned'
        });
    },
    handlePointerStart(event) {
      if (event.pointerType === "pen") {
        this.touchType = "使用笔在画板书写";
      } else if (event.pointerType === "touch") {
        this.touchType = "使用手指触摸";
      } else {
        this.touchType = "未知的触摸类型";
      }
      console.log(this.touchType);
    },
    drawSquare() {
      // 清除 canvas 并重新绘制正方形
      this.context.clearRect(0, 0, this.canvas.width, this.canvas.height);
      this.context.fillStyle = "blue";
      const { x, y, size } = this.square;
      this.context.fillRect(x, y, size, size);
    },
    handleCanvasPointerDown(event) {
      const rect = this.canvas.getBoundingClientRect();
      const x = event.clientX - rect.left;
      const y = event.clientY - rect.top;
      const { square } = this;

      // 判断是否点中正方形
      if (
        x >= square.x &&
        x <= square.x + square.size &&
        y >= square.y &&
        y <= square.y + square.size
      ) {
        square.dragging = true;
        square.offsetX = x - square.x;
        square.offsetY = y - square.y;
      }
    },
    handleCanvasPointerMove(event) {
      if (!this.square.dragging) return;

      const rect = this.canvas.getBoundingClientRect();
      const x = event.clientX - rect.left;
      const y = event.clientY - rect.top;

      // 更新正方形的位置
      this.square.x = x - this.square.offsetX;
      this.square.y = y - this.square.offsetY;

      // 边界检测
      const { x: squareX, y: squareY, size } = this.square;
      if (
        squareX < 0 ||
        squareY < 0 ||
        squareX + size > this.canvas.width ||
        squareY + size > this.canvas.height
      ) {
        alert("触碰到边界！");
      }

      this.drawSquare();
    },
    handleCanvasPointerUp() {
      this.square.dragging = false;
    },
  },
};
</script>

<style scoped>
.esign {
  max-width: 1000px;
  margin: auto;
  padding: 10px;
}
.esign-box {
  position: relative;
  width: 800px;
  height: 300px;
  border: 2px solid #ccc;
}
.esignature {
  position: absolute;
  top: 0;
  left: 0;
  z-index: 1;
}
.canvas-layer {
  position: absolute;
  top: 0;
  left: 0;
  z-index: 2;
}
.esigh-btns button {
  color: #fff;
  height: 40px;
  width: 100px;
  font-size: 16px;
  margin-right: 10px;
  outline: none;
  border-radius: 4px;
  background: #f60;
  border: 1px solid transparent;
}
.esigh-btns button:active {
  color: #fff;
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
</style>
