<template>
  <div class="flexrowall">
    <div class="flexcol">
      <el-button type="primary" size="small" @click="upload()" icon="el-icon-s-tools" class="margin10"></el-button>
    </div>
    <el-row class="flexrow">
      <div v-for="item in navList" :key="item.id" style="width:300px;height:250px;margin:10px">
        <el-card :body-style="{ padding: '0px' }">
          <img :src="'/api'+item.path" class="size" @click="moveto(item.url)" />
          <!-- <img :src="require('../assets/'+item.path+'.png')" class="size"/> -->
          <div style="padding: 14px;">
            <span v-text="item.name" class="space"></span>
            <div v-text="item.description" class="space"></div>
            <div>
              <el-button size="small" type="primary" icon="el-icon-edit" circle @click="editUpload(item.id)">
              </el-button>
              <el-button size="small" type="warning" icon="el-icon-star-off" circle @click="colNav(item.id)">
                {{item.collection}}
              </el-button>
              <el-button size="small" type="danger" icon="el-icon-delete" circle @click="delNav(item.id)"></el-button>
            </div>
          </div>
        </el-card>
      </div>
    </el-row>
    <!-- ---------------------------------------------------------------------------------------------------------------->
    <el-dialog title="上传导航信息" :visible.sync="uploadbool" center width="400px" :before-close="clearSubmit">
      <el-form :model="form" label-width="80px">
        <el-form-item label="名称">
          <el-input v-model="form.name" placeholder="填写名称"></el-input>
        </el-form-item>
        <el-form-item label="描述">
          <el-input v-model="form.description" placeholder="填写描述"></el-input>
        </el-form-item>
        <el-form-item label="导航url">
          <el-input v-model="form.url" placeholder="填写导航url"></el-input>
        </el-form-item>
        <el-form-item label="图片">
          <input type="file" accept="image/png, image/jpeg, image/jpg" @change="preview()" ref="choosePic">
          <img ref="upPic" style="width:150px;heigth:150px;">
        </el-form-item>
      </el-form>
      <span slot="footer" class="dialog-footer">
        <el-button size="small" @click="clearSubmit">取 消</el-button>
        <el-button size="small" type="primary" @click="submit()">确 定</el-button>
      </span>
    </el-dialog>

    <el-dialog title="修改导航信息" :visible.sync="editbool" center width="400px" :before-close="clearEditSubmit">
      <el-form :model="editForm" label-width="80px">
        <el-form-item label="名称">
          <el-input v-model="editForm.name" placeholder="填写名称"></el-input>
        </el-form-item>
        <el-form-item label="描述">
          <el-input v-model="editForm.description" placeholder="填写描述"></el-input>
        </el-form-item>
        <el-form-item label="导航url">
          <el-input v-model="editForm.url" placeholder="填写导航url"></el-input>
        </el-form-item>
        <el-form-item label="图片">
          <input type="file" accept="image/png, image/jpeg, image/jpg" @change="preview1()" ref="choosePic1">
          <img :src="upPic1" ref="upPic1" style="width:150px;heigth:150px;">
        </el-form-item>
      </el-form>
      <span slot="footer" class="dialog-footer">
        <el-button size="small" @click="clearEditSubmit">取 消</el-button>
        <el-button size="small" type="primary" @click="editSubmit()">确 定</el-button>
      </span>
    </el-dialog>
  </div>
</template>

<script>
  import {
    upload,
    getNavList,
    delNav,
    editNav,
    collectNav,
    getNavInfo
  } from "../api/api";
  export default {
    components: {},
    data() {
      return {
        upPic1: '',
        form: {
          name: '',
          description: '',
          url: '',
          logobase: ''
        },
        editForm: {},
        uploadbool: false,
        editbool: false,
        imageUrl: '',
        navList: []
      };
    },
    computed: {},
    watch: {},
    methods: {
      //收藏+1
      colNav(id) {
        let para = {
          id: id
        }
        collectNav(para).then((res) => {
          if (res.data) {
            this.$message({
              type: "success",
              message: "收藏+1"
            })
            this.getList()
          }
        })
      },
      //删除导航
      delNav(id) {
        let para = {
          id: id
        }
        delNav(para).then((res) => {
          if (res.data.result) {
            this.$message({
              type: "success",
              message: res.data.msg
            })
            this.getList()
          }
        })
      },
      //修改导航-----------------------------------------------------
      editUpload(id) {
        let para = {
          id: id
        }
        getNavInfo(para).then((res) => {
          this.editForm = res.data;
          this.upPic1 = '/api' + res.data.path
          this.editbool = true;
        })
      },
      editSubmit() {
        let para = Object.assign({}, this.editForm);
        console.log(para)
        editNav(para).then((res) => {
          if (res.data.result) {
            this.$message({
              type: "success",
              message: res.data.msg
            })
            this.clearEditSubmit();
            this.getList();
          } else {
            this.$message({
              type: "success",
              message: res.data.msg
            })
          }
        })
      },
      clearEditSubmit() {
        this.editbool = false;
      },
      preview1() {
        var that = this
        let f = that.$refs.choosePic1.files[0];
        let fr = new FileReader();
        fr.readAsDataURL(f);
        //异步函数
        fr.onload = function () {
          // console.log(this.result)
          that.editForm.logobase = this.result;
          that.$refs.upPic1.src = that.editForm.logobase;
        }
      },
      //新增导航--------------------------------------------------
      upload() {
        this.uploadbool = true;
      },
      submit() {
        let para = Object.assign({}, this.form);
        console.log(para)
        upload(para).then((res) => {
          if (res.data.result) {
            this.$message({
              type: "success",
              message: res.data.msg
            })
            this.clearSubmit();
            this.getList();
          } else {
            this.$message({
              type: "warning",
              message: res.data.msg
            })
          }
        })
      },
      clearSubmit() {
        this.uploadbool = false;
        this.form = {
          name: '',
          description: '',
          url: '',
          logobase: ''
        };  
        // 清空图片预览效果
        this.$refs.choosePic.value = '';
        this.$refs.upPic.src = '';
      },
      //预览显示图片并把base64传给form.logobase
      preview() {
        var that = this
        let f = that.$refs.choosePic.files[0];
        console.log(f)
        let fr = new FileReader();
        fr.readAsDataURL(f);
        //异步函数
        fr.onload = function () {
          // console.log(this.result)
          that.form.logobase = this.result;
          that.$refs.upPic.src = that.form.logobase;
        }
      },
      // 获取导航列表
      getList() {
        let para = {}
        getNavList(para).then((res) => {
          this.navList = res.data
        })
      },
      // 导航跳转
      moveto(e) {
        // console.log(e)
        window.open(e)
      },
    },
    created() {
      // 初始化刷新获取导航列表
      this.getList()
    },
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
  .size {
    width: 100px;
    height: 100px;
    padding: 10px
  }

  .flexrowall {
    display: flex;
    flex-direction: row;
    flex-wrap: nowrap;
  }

  .flexrow {
    display: flex;
    flex-direction: row;
    flex-wrap: wrap;
  }

  .flexcol {
    display: flex;
    flex-direction: column;
    flex-wrap: nowrap;
  }

  .space {
    margin: 10px
  }

  .margin10 {
    margin-top: 10px;
  }

</style>
