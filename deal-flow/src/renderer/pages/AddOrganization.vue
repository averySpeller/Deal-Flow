<template>
  <div class="">
    <div class="uk-margin">
      <el-row type="flex" class="row-bg" justify="center">
          <el-col :xs="12" :sm="10" :md="8" :lg="6" :xl="6">
          <el-form ref="form" :model="form" label-width="70px">
            <br>
            <el-upload
              class="avatar-uploader uk-flex uk-flex-center uk-margin"
              action="https://jsonplaceholder.typicode.com/posts/"
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
            <el-form-item label="Symbol:">
              <el-input
                v-model="form.stock_symbol"
                type="text"
                clearable
                placeholder="ABC">
              </el-input>
            </el-form-item>
            <el-form-item label="Vision:">
              <el-input
                v-model="form.vision"
                type="text"
                clearable>
              </el-input>
            </el-form-item>
            <el-form-item label="Model:">
              <el-input
                v-model="form.revenue_model"
                type="text"
                clearable>
              </el-input>
            </el-form-item>
            <el-form-item label="revenue:">
              <el-input
                v-model="form.revenue"
                type="text"
                clearable>
              </el-input>
            </el-form-item>
            <el-form-item label="Valuation:">
              <el-input
                v-model="form.valuation"
                type="text"
                clearable>
              </el-input>
            </el-form-item>
            <el-form-item label="line1:">
              <el-input
                v-model="form.line1"
                type="text"
                clearable>
              </el-input>
            </el-form-item>
            <el-form-item label="line2:">
              <el-input
                v-model="form.line2"
                type="text"
                clearable>
              </el-input>
            </el-form-item>
            <el-form-item label="City:">
              <el-input
                v-model="form.city"
                type="text"
                clearable>
              </el-input>
            </el-form-item>
            <el-form-item label="State">
              <el-input
                v-model="form.state"
                type="text"
                clearable>
              </el-input>
            </el-form-item>
            <el-form-item label="Country:">
              <el-input
                v-model="form.country"
                type="text"
                clearable>
              </el-input>
            </el-form-item>
            <el-form-item label="Postal:">
              <el-input
                v-model="form.postal"
                type="text"
                clearable
                placeholder="A1A-1A1">
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
            <el-form-item label="Notes:">
              <el-input
                v-model="form.notes"
                type="textarea"
                clearable
                placeholder="Add Notes">
              </el-input>
            </el-form-item>

            <div class="uk-flex uk-flex-center ">
              <button @click="AddOrganization()" class="uk-button uk-button-primary uk-button-large uk-margin">Add Company!</button><br><br>
            </div>
          </el-form>
          <div class="uk-flex uk-flex-center ">
            <button @click="goBack()" class="uk-button uk-button-secondary uk-button-medium uk-margin">GO BACK</button>
          </div>
        </el-col>
      </el-row>

    </div>
  </div>

</template>

<script>
import axios from 'axios';
export default {
  name: 'AddOrganization',
  data(){
    return{
      name: null,
      imageUrl:'',
      form: {
        name: null,
        stock_symbol: null,
        logo: null,
        vision: null,
        revenue_model: null,
        revenue: null,
        valuation: null,
        phone1: null,
        phone2: null,
        line1: null, //addres1
        line2: null, //address2
        city: null,
        state: null,
        country: null,
        postal: null,
        website: null,
        notes: null
      },

    }
  },
  methods: {
    goBack () {
      window.history.length > 1
        ? this.$router.go(-1)
        : this.$router.push('/')
    },
    AddOrganization(){
      console.log(this.form);

      axios.post('http://24.138.161.30:5000/organizations',this.form).then(response => {
        console.log(this.form);
        console.log(response.data);
        window.history.length > 1
          ? this.$router.go(-1)
          : this.$router.push('/')
      })
      .catch(e => {
        this.errors.push(e)
        console.log(e);
        console.log('i is dead');
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
  },
  created() {
    var myRequest = this.$parent.createGetRequest("organizations")
    axios.get(myRequest).then(response => {

      for(let item of response.data){

        this.orgOptions.push({
          'label': item.name,
          'value': item.organization_id
        })
      }
      this.loading = false;
    })
    .catch(e => {
      this.errors.push(e)
    })
  }

}


</script>

<style scoped>
  .avatar-uploader .el-upload {
    border: 1px dashed #d9d9d9;
    border-radius: 25%;
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
    border-radius: 25%;
  }
  .uk-offcanvas-bar {
    background: #000000;
}
</style>
