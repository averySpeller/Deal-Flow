<template>
  <div class="">
    <div class="uk-margin">
      <div v-on:click="toggleAutocomplete">
        <el-switch v-model="autocompleteForm">
        </el-switch>
      </div>
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


              <el-form-item label="skill1:">
              <el-row>
                <el-slider
                  v-model="form.skill1"
                  :step="1"
                  :max= "5"
                  show-stops>
                </el-slider>
              </el-row>
               </el-form-item>
               <el-form-item label="skill2:">
               <el-row>
                 <el-slider
                   v-model="form.skill2"
                   :step="1"
                   :max= "5"
                   show-stops>
                 </el-slider>
               </el-row>
                </el-form-item>
                <el-form-item label="skill3:">
                <el-row>
                  <el-slider
                    v-model="form.skill3"
                    :step="1"
                    :max= "5"
                    show-stops>
                  </el-slider>
                </el-row>
                 </el-form-item>
                 <el-form-item label="skill4:">
                 <el-row>
                   <el-slider
                     v-model="form.skill4"
                     :step="1"
                     :max= "5"
                     show-stops>
                   </el-slider>
                 </el-row>
                  </el-form-item>
                  <el-form-item label="skill5:">
                  <el-row>
                    <el-slider
                      v-model="form.skill5"
                      :step="1"
                      :max= "5"
                      show-stops>
                    </el-slider>
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
              <el-button @click="addContact()" type="primary">Add contact!</el-button><br><br>
            </div>
          </el-form>
          <!-- <div class="uk-flex uk-flex-center ">
            <el-button @click="goBack()" type="danger" plain>GO BACK</el-button>
          </div> -->
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
export default {
  name: 'AddContact',
  components:{
        'AddOrganization': AddOrganization,
        'FileUploader': FileUploader
  },
  data(){
    return{
      name: "",
      autocompleteForm: false,
      imageUrl:'',
      form: {
        first: null,
        last: null,
        email: "",
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
        // title: null, //UNCOMMENT TO SEND TITLE
        notes: ""

      },
      title: [],
      orgOptions: [],
      titleOptions:[
        {
          value: 'CEO',
          label: 'CEO'
        },
        {
          value: 'CFO',
          label: 'CFO'
        },
        {
          value: 'CTO',
          label: 'CTO'
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
p0
        this.$router.replace({ name: 'Single-Contact', params: { id: this.response.data.contact_id }})
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
      this.form.phone1= "234 433 3344"
      this.form.phone2= "234 433 5538"
      this.form.website= "johnsnow.info"
      this.form.avatar= ""
      this.form.organization_id= 1
      // this.form.title= null //UNCOMMENT TO SEND TITLE
      this.form.notes= "Rightful heir to Winterfell. Has a dier wolf"
    }
    else {
      console.log("Autofill Fields: OFF");
      this.form.first= null
      this.form.last= null
      this.form.email= ""
      this.form.phone1= ""
      this.form.phone2= ""
      this.form.website= ""
      this.form.avatar= ""
      this.form.organization_id= null
      // this.form.title= null //UNCOMMENT TO SEND TITLE
      this.form.notes= ""
    }
  }
},
created() {
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
