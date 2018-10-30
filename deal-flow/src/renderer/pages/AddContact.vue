<template>
  <div class="">
    <div class="uk-margin">
      <el-row type="flex" class="row-bg" justify="space-between">
        <el-col :span="6"/>
        <el-col :span="6">
          <el-form ref="form" :model="form" label-width="70px">
            <br>
            <el-upload
              class="avatar-uploader uk-flex uk-flex-center uk-margin"
              action="getImageFilePath()"
              :show-file-list="false"
              :on-success="handleAvatarSuccess"
              :before-upload="beforeAvatarUpload">
              <img v-if="imageUrl" :src="imageUrl" class="avatar">
              <i v-else class="el-icon-plus avatar-uploader-icon"></i>
            </el-upload>
            <el-form-item label="Name:">
              <el-input
                v-model="name"
                type="text"
                clearable
                placeholder="FistName LastName">
              </el-input>
            </el-form-item>
            <el-form-item label="Email:">
              <el-input
                v-model="form.email"
                type="text"
                clearable
                placeholder="username@domain.com">
              </el-input>
            </el-form-item>
            <el-form-item label="Phone1:">
              <el-input
                v-model="form.phone1"
                type="text"
                clearable>
              </el-input>
            </el-form-item>
            <el-form-item label="Phone2:">
              <el-input
                v-model="form.phone2"
                type="text"
                clearable>
              </el-input>
            </el-form-item>
            <el-form-item label="Website:">
              <el-input
                v-model="form.website"
                type="text"
                clearable>
              </el-input>
            </el-form-item>
            <div class="uk-flex uk-flex-center ">
              <button @click="addContact()" class="uk-button uk-button-primary uk-button-large uk-margin">Add contact!</button><br><br>
            </div>
          </el-form>
          <div class="uk-flex uk-flex-center ">
            <button @click="goBack()" class="uk-button uk-button-secondary uk-button-medium uk-margin">GO BACK</button>
          </div>
        </el-col>
        <el-col :span="6"/>
      </el-row>

    </div>
  </div>

</template>

<script>
import axios from 'axios';
export default {
  name: 'AddContact',
  data(){
    return{
      name: null,
      imageUrl:'',
      form: {
        first: null,
        last: null,
        email: null,
        phone1: null,
        phone2: null,
        website: null,
        first: null,
        last: null,
        notes: null
      }
    }
  },
  methods: {
    goBack () {
      window.history.length > 1
        ? this.$router.go(-1)
        : this.$router.push('/')
    },
    addContact(){
      var splitty = this.name.split(' ');
      this.form.first = splitty[0];
      this.form.last = splitty[1];

      // console.log(splitty);
      console.log(this.form);

      axios.post('http://24.138.161.30:5000/contacts',this.form).then(response => {
        console.log(response.data);
        window.history.length > 1
          ? this.$router.go(-1)
          : this.$router.push('/')
      })
      .catch(e => {
        this.errors.push(e)
        console.log(e);
        console.log('i died');
      })

    },
    handleAvatarSuccess(res, file) {
      this.imageUrl = URL.createObjectURL(file.raw);
    },
    beforeAvatarUpload(file) {
      const isJPG = file.type === 'image/jpeg';
      const isLt2M = file.size / 1024 / 1024 < 2;

      if (!isJPG) {
        this.$message.error('Avatar picture must be JPG format!');
      }
      if (!isLt2M) {
        this.$message.error('Avatar picture size can not exceed 2MB!');
      }
      return isJPG && isLt2M;
    }

  }

}


</script>

<style>
  .avatar-uploader .el-upload {
    border: 1px dashed #d9d9d9;
    border-radius: 6px;
    cursor: pointer;
    position: relative;
  }
  .avatar-uploader .el-upload:hover {
    border-color: #409EFF;
  }
  .avatar-uploader-icon {
    font-size: 28px;
    color: #8c939d;
    width: 178px;
    height: 178px;
    line-height: 178px;
    text-align: center;
  }
  .avatar {
    width: 178px;
    height: 178px;
    display: block;
  }
</style>
