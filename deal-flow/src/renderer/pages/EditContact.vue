<template>
  <div>
    <el-upload
      class="avatar-uploader"
      action="getImageFilePath"
      :show-file-list="false"
      :on-success="handleAvatarSuccess"
      :before-upload="beforeAvatarUpload">
      <img v-if="imageUrl" :src="imageUrl" class="avatar">
      <i v-else class="el-icon-plus avatar-uploader-icon"></i>
    </el-upload>
    <el-row>
      <el-col :span="6">
          Name: <el-input
                    v-model="name"
                    type="text"
                    clearable
                    placeholder="FistName LastName">
                </el-input>
      </el-col>
    </el-row>
    <el-row>
      <el-col :span="6">
          Email: <el-input
                    v-model="form.email"
                    type="text"
                    clearable
                    placeholder="username@domain.com">
                  </el-input>
      </el-col>
    </el-row>
    <el-row>
      <el-col :span="6">
          Phone1: <el-input
                    v-model="form.phone1"
                    type="text"
                    clearable>
                  </el-input>
      </el-col>
    </el-row>
    <el-row>
      <el-col :span="6">
          Phone2: <el-input
                    v-model="form.phone2"
                    type="text"
                    clearable>
                  </el-input>
      </el-col>
    </el-row>
    <el-row>
      <el-col :span="6">
          Website: <el-input
                    v-model="form.website"
                    type="text"
                    clearable>
                  </el-input>
      </el-col>
    </el-row>
    <el-row>
      <el-col :span="12">
          Notes: <el-input
                    v-model="form.notes"
                    type="textarea"
                    :autosize="{ minRows: 4, maxRows: 8}"
                    placeholder="Additional Notes" >
                  </el-input>
      </el-col>
    </el-row>

    <button @click="editContact()">Edit contact!</button><br>
    <button @click="goBack()" class="uk-button uk-button-secondary uk-button-large uk-margin">GO BACK</button>
  </div>

</template>

<script>
import axios from 'axios';
import router from '../router'
export default {
  name: 'EditContact',
  data(){
    return{
      contact_id: 0,
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
  created() {
    var requestFields = this.$parent.createGetRequest("contacts/".concat(this.$route.params.id))

    axios.get(requestFields.myRequest, requestFields.auth).then(response => {
      this.contact = response.data
      console.log(response.data);
       this.name = response.data['first'] + ' ' + response.data['last'];
       this.form.email = response.data['email'];
       this.form.phone1 = response.data['phone1'];
       this.form.phone2 = response.data['phone2'];
       this.form.website = response.data['website'];
       this.form.notes = response.data['notes'];
      console.log(requestFields.myRequest);
    })
    .catch(e => {
      this.errors.push(e)
    })
  },
  methods: {
    goBack () {
      window.history.length > 1
        ? this.$router.go(-1)
        : this.$router.push('/')
    },
    editContact(){
      var splitty = this.name.split(' ');
      this.form.first = splitty[0];
      this.form.last = splitty[1];

      // console.log(splitty);
      console.log(this.form);

      axios.put('http://24.138.161.30:5000/contacts/'.concat(this.$route.params.id),this.form).then(response => {
        console.log(response.data);
        console.log(response.header);

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

<style scoped>

</style>
