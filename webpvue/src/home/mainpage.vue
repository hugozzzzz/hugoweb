<template>
  <div style="width:100%;height:100%">
    <el-container style='height:100%;'>
      <el-header class="flexrowall">
        <el-menu class="el-menu-demo" mode="horizontal" background-color="#409eff" text-color="#fff"
          active-text-color="#ffd04b" router style='height:100%'>
          <el-menu-item style='margin-left:2%'>
            <i :class="(isCollapse)?'el-icon-s-unfold':'el-icon-s-fold'" @click="changeNav" style="font-size:35px;color:white"></i>
          </el-menu-item>
          <el-menu-item index="/mainpage/deal" style='margin-left:30%'>处理中心</el-menu-item>
          <el-submenu index="2">
            <template slot="title">我的工作台</template>
            <el-menu-item index="/mainpage/heart">爆炸的心</el-menu-item>
          </el-submenu>
          <el-menu-item index="/mainpage/info">个人中心</el-menu-item>
          <el-menu-item @click='showbool = true'>来吧展示</el-menu-item>
        </el-menu>
      </el-header>
      <el-container>
        <el-aside width="200px" style='height:100%'>
          <el-menu default-active="1" class="el-menu-vertical-demo" style='height:100%' background-color="#545c64"
            text-color="#fff" active-text-color="#ffd04b" router :default-openeds="openIndex" :collapse="isCollapse">
            <el-submenu index="1">
              <template slot="title">
                <i class="el-icon-menu"></i>
                <span slot="title">菜单</span>
              </template>
              <el-menu-item-group>
                <el-menu-item index="/mainpage/nav">导航</el-menu-item>
                <el-menu-item index="/mainpage/heart">爆炸的心</el-menu-item>
                <el-menu-item index="/mainpage/info">info</el-menu-item>
                <el-menu-item index="/mainpage/deal">deal</el-menu-item>
              </el-menu-item-group>
            </el-submenu>
          </el-menu>
        </el-aside>
        <el-main style='padding:2px;margin:2px'>
          <router-view></router-view>
        </el-main>
      </el-container>
    </el-container>
    <!-- ---------------------------------------------------------------------------------------------------- -->
    <el-drawer :visible.sync="showbool" direction="rtl" :before-close="handleClose" :withHeader='false'>
      <el-image :src='noface'>
      </el-image>
    </el-drawer>
  </div>

</template>

<script>
  export default {
    components: {},
    data() {
      return {
        noface: require('../assets/无脸男.png'),
        showbool: false,
        //导航栏
        openIndex: ['1'],
        isCollapse: false,
      };
    },
    computed: {},
    watch: {},
    methods: {
      handleClose() {
        this.showbool = false
      },
      // 导航栏折叠
      changeNav(){
        if(this.isCollapse){
          this.isCollapse = false;
        }else{
          this.isCollapse = true;
        }
      }
    },
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
  .el-header {
    padding: 0px
  }

</style>
