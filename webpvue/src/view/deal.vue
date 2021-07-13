<template>
  <div>
    <el-row>
      <el-col :span='2'>
        <el-image style='width:100px;heigth:100px' :src='noface' fit="fit" alt='111' :preview-src-list="srcList">
        </el-image>
      </el-col>
      <el-col :span='22'></el-col>
    </el-row>
  </div>
</template>

<script>
  export default {
    components: {},
    data() {
      return {
        img1: require('../assets/img1.jpg'),
        img2: require('../assets/img2.jpg'),
        img3: require('../assets/img3.jpg'),
        noface: require('../assets/无脸男.png'),
        srcList: [
          require('../assets/img1.jpg'),
          require('../assets/img2.jpg'), ,
          require('../assets/img3.jpg'),
        ]
      };
    },
    computed: {},
    watch: {},
    methods: {},
    created() {},
    mounted() {},
    beforeCreate() {},
    beforeMount() {},
    beforeUpdate() {},
    updated() {},
    beforeDestroy() {},
    destroyed() {},
    activated() {},
  }

</script>
<style scoped>

</style>
