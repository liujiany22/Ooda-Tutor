const { defineConfig } = require('@vue/cli-service')
module.exports = defineConfig({
  transpileDependencies: true,
  devServer: {
    host: '0.0.0.0', // 监听所有主机地址
    port: 8080, // 自定义端口号（可选）
    allowedHosts: 'all', // 允许所有主机访问
  },
})
