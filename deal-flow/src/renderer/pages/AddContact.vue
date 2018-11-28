<template>
  <div class="">
    <div class="uk-margin">
      <div v-if="!editContactBool" v-on:click="toggleAutocomplete">
        <el-switch v-model="autocompleteForm">
        </el-switch>
      </div>
      <el-row type="flex" class="row-bg" justify="center">
        <el-col :xs="22" :sm="22" :md="18" :lg="16" :xl="12">
          <el-form ref="form" :model="form" label-width="70px">
            <br>
            <el-row type="flex" class="row-bg" justify="center">
              <el-col :xs="16" :sm="14" :md="12" :lg="10" :xl="10">

                <FileUploader isImage="true" v-model="form.avatar"></FileUploader>
                <el-form-item label="Name:">
                  <el-input
                    v-model="name"
                    type="text"
                    clearable
                    placeholder="John Smith">
                  </el-input>
                </el-form-item>
                <el-form-item label="Title:">
                  <el-select
                    v-model="form.title"
                    filterable
                    allow-create
                    placeholder="Select a title">
                    <el-option
                      v-for="item in this.titleOptions"
                      :label="item.label"
                      :value="item.value">
                    </el-option>
                  </el-select>
                </el-form-item>
                <el-form-item label="Email:">
                  <el-input
                    v-model="form.email"
                    type="text"
                    clearable
                    placeholder="name@mail.com">
                  </el-input>
                </el-form-item>
                <el-form-item label="Phone1:">
                  <el-input
                    v-model="form.phone1"
                    type="text"
                    placeholder="(123) 456-7890"
                    clearable>
                  </el-input>
                </el-form-item>
                <el-form-item label="Phone2:">
                  <el-input
                    v-model="form.phone2"
                    type="text"
                    placeholder="(123) 456-7890"
                    clearable>
                  </el-input>
                </el-form-item>
                <el-form-item label="Website:">
                  <el-input
                    v-model="form.website"
                    type="text"
                    clearable
                    placeholder="www.domain.com">
                  </el-input>
                </el-form-item>

                <el-form-item label="Company:">
                <el-row>
                  <el-col :span="16">
                    <el-select @click="loadSelect()" v-model="form.organization_id" filterable placeholder="Select">
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

              </el-col>
            </el-row>

            <!-- <el-form-item label="Persistence:">
            <el-row>
              <el-slider
                v-model="form.skill1"
                :step="1"
                :max= "5"
                show-stops>
              </el-slider>
            </el-row>
             </el-form-item>
             <el-form-item label="Leadership:">
             <el-row>
               <el-slider
                 v-model="form.skill2"
                 :step="1"
                 :max= "5"
                 show-stops>
               </el-slider>
             </el-row>
              </el-form-item>
              <el-form-item label="Confidence:">
              <el-row>
                <el-slider
                  v-model="form.skill3"
                  :step="1"
                  :max= "5"
                  show-stops>
                </el-slider>
              </el-row>
               </el-form-item>
               <el-form-item label="Knowledge:">
               <el-row>
                 <el-slider
                   v-model="form.skill4"
                   :step="1"
                   :max= "5"
                   show-stops>
                 </el-slider>
               </el-row>
                </el-form-item>
                <el-form-item label="Charisma:">
                <el-row>
                  <el-slider
                    v-model="form.skill5"
                    :step="1"
                    :max= "5"
                    show-stops>
                  </el-slider>
                </el-row>
                 </el-form-item> -->
              <el-form-item label="Notes:">
                <Notes v-model="form.notes"></Notes>
              </el-form-item>


            <div class="uk-flex uk-flex-center ">
              <el-button v-if="!editContactBool"  @click="addContact()" type="primary">Create</el-button>
              <el-button v-else @click="editContact()" type="primary">Edit</el-button><br><br>
            </div>
          </el-form>
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
import AddOrganization from './AddOrganization';
import FileUploader from '../components/FileUploader'
import Notes from '../components/Notes'
export default {
  name: 'AddContact',
  components:{
    'AddOrganization': AddOrganization,
    'FileUploader': FileUploader,
    'Notes': Notes
  },
  data(){
    return{
      name: "",
      autocompleteForm: false,
      editContactBool: false,
      imageUrl:'',
      form: {
        first: null,
        last: null,
        email: "",
        title: null,
        phone1: "",
        phone2: "",
        website: "",
        avatar: "",
        // notes: null,
        organization_id: null,
        skill1: 0,
        skill2: 0,
        skill3: 0,
        skill4: 0,
        skill5: 0,

        notes: ""

      },
      title: [],
      orgOptions: [],
      titleOptions:[
        {
          value: 'Chief Executive Officer',
          label: 'CEO'
        },
        {
          value: 'Chief Financial Officer',
          label: 'CFO'
        },
        {
          value: 'Chief Technology Officer',
          label: 'CTO'
        },
        {
          value: 'Chief Operations Officer',
          label: 'COO'
        },
        {
          value: 'Other',
          label: 'Other'
        }
      ]
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
      // var requestFields = this.$parent.$parent.createGetRequest("contacts")
        lib.postRequest('/contacts', this.form, response => {
        console.log(response.data);
        this.$router.replace({ name: 'Single-Contact', params: { id: this.response.data.contact_id }})
      })

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
      this.imageUrl = "/static/" + file.raw.path.replace(/^.+static/,''); ;
      this.form.avatar = this.imageUrl;
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
  },
  toggleAutocomplete() {
    if (this.autocompleteForm) {
      console.log("Autofill Fields: ON");
      this.name= "John Snow"
      this.form.first= "John"
      this.form.last= "Snow"
      this.form.email= "johnsnow@gmail.com"
      this.form.phone1= "(234) 433-3344"
      this.form.phone2= "(234) 433-5538"
      this.form.website= "www.johnsnow.info"
      this.form.avatar= ""
      this.form.organization_id= 1
      this.form.notes= "Rightful heir to Winterfell."
    }
    else {
      console.log("Autofill Fields: OFF");
      this.name= ""
      this.form.first= null
      this.form.last= null
      this.form.email= ""
      this.form.phone1= ""
      this.form.phone2= ""
      this.form.website= ""
      this.form.avatar= ""
      this.form.organization_id= null
      this.form.notes= ""
    }
  }
},
created() {

  this.$emit('backButton', true);

  console.log("IN ADD CONTACT");
  console.log(this.$route.params.id);

  if (this.$route.params.id) {
    this.editContactBool = true;
    lib.getRequest('/contacts/'.concat(this.$route.params.id).concat("?fields=avatar"), response => {
      this.contact = response.data
      console.log(response.data);
       this.name = response.data['first'] + ' ' + response.data['last'];
       this.form = response.data;
      console.log(myRequest);
    })
  }

  this.loadSelect()
}
}


</script>

<style>
  .avatar-uploader .el-upload {
    border: 1px dashed #d9d9d9;
    border-radius: 50%;
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
    border-radius: 50%;
  }
</style>
<style scoped>
.uk-offcanvas-bar{
  width: 50%;
  background: #fff
}
</style>
