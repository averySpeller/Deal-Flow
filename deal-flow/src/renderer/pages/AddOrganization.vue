<template>
  <div class="">
    <div class="uk-margin">
      <div v-on:click="toggleAutocomplete">
        <el-switch v-model="autocompleteForm">
        </el-switch>
      </div>
      <el-row type="flex" class="row-bg" justify="center">
          <el-col :span="18">
          <el-form ref="form" :model="form" label-width="125px">
            <br>
            <FileUploader isImage="true" v-model="form.logo"></FileUploader>
            <el-row type="flex" class="row-bg" justify="center">
              <h1>{{this.form.name}}</h1>
            </el-row>
            <el-form-item label="Name:">
              <el-input
                v-model="form.name"
                type="text"
                clearable
                placeholder="CompanyName">
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
            <el-form-item label="Revenue Model:">
              <el-input
                v-model="form.revenue_model"
                type="text"
                clearable>
              </el-input>
            </el-form-item>
            <el-form-item label="Revenue:">
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

            <div class="uk-flex uk-flex-center ">
              <el-button @click="AddOrganization()" type="primary">Save</el-button><br><br>
            </div>
          </el-form>
        </el-col>
      </el-row>

    </div>
  </div>

</template>

<script>
// import axios from 'axios';
import lib from '../lib'
import FileUploader from '../components/FileUploader'
export default {
  name: 'AddOrganization',
  props: ['continueAddingContact'],
  data(){
    return{
      name: null,
      imageUrl:'',
      autocompleteForm: false,
      form: {
        name: "",
        stock_symbol: "",
        logo: "",
        vision: "",
        revenue_model: "",
        revenue: "",
        valuation: "",
        phone1: "",
        phone2: "",
        line1: "", //addres1
        line2: null, //address2
        city: "",
        state: "",
        country: "",
        postal: "",
        website: ""
      },

    }
  },
  components: {
    'FileUploader': FileUploader
  },
  methods: {
    goBack () {
      window.history.length > 1
        ? this.$router.go(-1)
        : this.$router.push('/')
    },
    AddOrganization(){
      console.log(this.form);

      lib.postRequest('/organizations', this.form, response => {
        console.log(this.form);
        console.log(response.data);
        this.organization_id = response.data.organization_id
        this.$emit('addOrg', this.organization_id)
        this.$emit('addOrg', this.organization_id)
        if (!this.continueAddingContact) {
          this.$router.replace({ name:'Single-Organization', params: {id: this.organization_id}});
        }
      })
    },
    handleAvatarSuccess(res, file) {
      this.imageUrl = "/static/" + file.raw.path.replace(/^.+static/,''); ;
      this.form.logo = this.imageUrl;
      console.log(  "IMAGE PATH: "+this.form.avatar);
      console.log(file.raw.path);
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
    },
    toggleAutocomplete(){
      console.log("IN TOGGLE");
      console.log(this.autocompleteForm);
      if (this.autocompleteForm) {
        this.form.name= "Google";
        this.form.stock_symbol= "GOOG";
        this.form.logo= "";
        this.form.vision= "To organize the world’s information and make it universally accessible and useful";
        this.form.revenue_model= "Ad Revenue";
        this.form.revenue= "$90 Billion";
        this.form.valuation= "$714 Billion";
        this.form.phone1= "123 456 7890";
        this.form.phone2= "098 765 4321";
        this.form.line1= "1600 Amphitheatre Parkway, Mountain View, California, U.S."; //addres1
        this.form.line2= null; //address2
        this.form.city= "Mountain View";
        this.form.state= "California";
        this.form.country= "USA";
        this.form.postal= "35421";
        this.form.website= "https://www.google.com";
        this.form.notes= "";
      }
      else {
        this.form.name= "";
        this.form.stock_symbol= "";
        this.form.logo= "";
        this.form.vision= "";
        this.form.revenue_model= "";
        this.form.revenue= "";
        this.form.valuation= "";
        this.form.phone1= "";
        this.form.phone2= "";
        this.form.line1= ""; //addres1
        this.form.line2= null; //address2
        this.form.city= "";
        this.form.state= "";
        this.form.country= "";
        this.form.postal= "";
        this.form.website= "";
        this.form.notes= "";
      }
    }
  },
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

</style>
