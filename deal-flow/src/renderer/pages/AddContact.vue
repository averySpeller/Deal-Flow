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
                <el-select v-model="form.organization_id" clearable placeholder="Select">
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
          <AddOrganization></AddOrganization>
      </div>
    </div>


  </div>

</template>

<script>
import lib from '../lib'
import AddOrganization from './AddOrganization';
export default {
  name: 'AddContact',
  components:{
        'AddOrganization': AddOrganization,
  },
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
        avatar: null,
        // notes: null,
        organization_id: null,
        // title: null, //UNCOMMENT TO SEND TITLE
        notes: null
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
      var requestFields = this.$parent.$parent.createGetRequest("contacts")

      axios.post(requestFields.myRequest, this.form, requestFields.auth ).then(response => {
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
    }
  },
  created() {
    lib.getRequest('/organizations', response => {
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
