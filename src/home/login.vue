<template>
  <div>
    <el-button type='primary' @click="$router.push({ path: '/mainpage' })">跳转到主页面</el-button>
  </div>
</template>

<script>
export default {
  data () {
    return {
      msg: 'Welcome to Your Vue.js App'
    }
  }
}
</script>

<style scoped>
</style>
