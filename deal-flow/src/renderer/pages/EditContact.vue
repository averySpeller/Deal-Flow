<template>
  <div class="">
    <div class="uk-margin">
      <el-row type="flex" class="row-bg" justify="center">
        <el-col :xs="12" :sm="10" :md="8" :lg="6" :xl="6">
          <el-form ref="form" :model="form" label-width="70px">
            <br>
            <FileUploader isImage="true" v-model="form.avatar"></FileUploader>
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

            <el-form-item label="Company:">
            <el-row>

              <el-col :span="16">
                <el-select @click="loadSelect()" v-model="form.organization_id" clearable placeholder="Select">
                    <el-option
                      v-for="item in this.orgOptions"
                      :label="item.label"
                      :value="item.value">
                    </el-option>
                </el-select >
              </el-col>
              <el-col :span="4">
                <el-button uk-toggle="target: #offcanvas-addOrganization" type="success" icon="el-icon-plus" plain></el-button>
              </el-col>



           </el-row>
            </el-form-item>
            <el-form-item label="Notes:">
              <el-input
                v-model="form.notes"
                type="textarea"
                clearable
                placeholder="Add Notes">
              </el-input>
            </el-form-item>
            <!-- <el-form-item label="Title:">
              <el-select
                v-model="this.title"
                multiple
                filterable
                allow-create
                default-first-option
                placeholder="Select a title">
                <el-option
                  v-for="item in this.titleOptions"
                  :label="item.label"
                  :value="item.value">
                </el-option>
              </el-select>
            </el-form-item> -->
            <div class="uk-flex uk-flex-center ">
                  <el-button @click="editContact()" type="primary">Edit contact!</el-button><br>
            </div>
          </el-form>
          <div class="uk-flex uk-flex-center ">
            <el-button @click="goBack()" type="danger" plain>GO BACK</el-button>
          </div>
        </el-col>
      </el-row>

    </div>

    <div id="offcanvas-addOrganization" uk-offcanvas="mode: slide; overlay: true; flip: true">
      <div class="uk-offcanvas-bar">
        <button class="uk-offcanvas-close" type="button" uk-close></button>
        <div class="title uk-flex uk-flex-center">
            <h1>Add Company</h1>
        </div>
          <AddOrganization v-on:addOrg="loadIt($event)"></AddOrganization>
      </div>
    </div>


  </div>
</template>

<script>
import lib from '../lib'
import FileUploader from '../components/FileUploader'
import router from '../router'
import AddOrganization from './AddOrganization';
export default {
  name: 'EditContact',
  components:{
        'AddOrganization': AddOrganization,
  },
  data(){
    return{
      contact_id: 0,
      name: null,
      imageUrl:'',
      orgOptions: [],
      form: {
        first: null,
        last: null,
        email: null,
        phone1: null,
        phone2: null,
        website: null,
        first: null,
        last: null,
        notes: null,
        avatar: null,
        organization_id: null,

      }
    }
  },
  components:{
    'FileUploader': FileUploader
  },
  created() {


    lib.getRequest('/contacts/'.concat(this.$route.params.id).concat("?fields=avatar"), response => {
      this.contact = response.data
      console.log(response.data);
       this.name = response.data['first'] + ' ' + response.data['last'];
       this.form.email = response.data['email'];
       this.form.phone1 = response.data['phone1'];
       this.form.phone2 = response.data['phone2'];
       this.form.website = response.data['website'];
       this.form.first = response.data['first'];
       this.form.last = response.data['last'];
       this.form.notes = response.data['notes'];
       this.form.avatar = response.data['avatar'];
       this.form.organization_id = response.data['organization_id'];
      console.log(myRequest);
    })

        this.loadSelect()
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
      console.log(this.form);

    lib.putRequest('/contacts/'.concat(this.$route.params.id), this.form, response => {
      console.log(response.data);
      console.log(response.header);

      window.history.length > 1
        ? this.$router.go(-1)
        : this.$router.push('/')
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
    },
    loadIt(arg) {
      this.loadSelect()
      this.form.organization_id=arg
    },

    loadSelect() {
      lib.getRequest('/organizations', response => {
        console.log(response);
        for(let item of response.data){
          this.orgOptions.push({
            'label': item.name,
            'value': item.organization_id
          })
        }
        this.loading = false;
      })
    }
  }

}


</script>

<style>

</style>
<style scoped>
.uk-offcanvas-bar{
  width: 50%;
  background: #fff
}
</style>
