<template>
  <div class="">
    <div class="uk-margin">
      <div class="title uk-flex uk-flex-center">
          <h1>Edit Company</h1>
      </div>
      <el-row type="flex" class="row-bg" justify="center">
          <el-col :span="18">
          <el-form ref="form" :model="form" label-width="125px">
            <br>
            <FileUploader isImage="true" v-model="form.logo"></FileUploader>
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
                placeholder="A1A 1A1">
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
              <el-button @click="EditOrganization()">Save</el-button><br>
            </div>
          </el-form>
        </el-col>
      </el-row>

    </div>
  </div>

</template>
<script>
import lib from '../lib'
import FileUploader from '../components/FileUploader'
import router from '../router'
export default {
  name: 'EditOrganization',
  data(){
    return{
      // contact_id: 0,
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
      }
    }
  },
  components:{
    'FileUploader': FileUploader
  },
  created() {
    this.$emit('backButton', true);

    lib.getRequest('/organizations/'.concat(this.$route.params.id).concat("?fields=logo"), response => {
      this.contact = response.data
      console.log("Request Completed: Organization");
      console.log(response.data);
       this.form.name = response.data['name'];
       this.form.stock_symbol = response.data['stock_symbol'];
       this.form.logo = response.data['logo'];
       this.form.vision = response.data['vision'];
       this.form.revenue_model = response.data['revenue_model'];
       this.form.revenue = response.data['revenue'];
       this.form.valuation = response.data['valuation'];
       this.form.phone1 = response.data['phone1'];
       this.form.phone2 = response.data['phone2'];
       this.form.line1 = response.data['line1']; //addres1
       this.form.line2 = response.data['line2']; //address2
       this.form.city = response.data['city'];
       this.form.state = response.data['state'];
       this.form.country = response.data['country'];
       this.form.postal = response.data['postal'];
       this.form.website = response.data['website'];
       this.form.notes = response.data['notes'];
    })


    //
    // var requestFields = this.$parent.createGetRequest("contacts/".concat(this.$route.params.id))
    //
    // axios.get(requestFields.myRequest, requestFields.auth).then(response => {
    //   this.contact = response.data
    //   console.log(response.data);
    //    this.name = response.data['first'] + ' ' + response.data['last'];
    //    this.form.email = response.data['email'];
    //    this.form.phone1 = response.data['phone1'];
    //    this.form.phone2 = response.data['phone2'];
    //    this.form.website = response.data['website'];
    //    this.form.notes = response.data['notes'];
    //   console.log(myRequest);
    // })
    // .catch(e => {
    //   this.errors.push(e)
    // })
  },
  methods: {
    goBack () {
      window.history.length > 1
        ? this.$router.go(-1)
        : this.$router.push('/')
    },
    EditOrganization(){

      // console.log(splitty);
      console.log(this.form);

    lib.putRequest('/organizations/'.concat(this.$route.params.id), this.form, response => {
      console.log(response.data);
      console.log(response.header);

      window.history.length > 1
        ? this.$router.go(-1)
        : this.$router.push('/')
      })
    },

  }

}


</script>

<style scoped>

</style>
