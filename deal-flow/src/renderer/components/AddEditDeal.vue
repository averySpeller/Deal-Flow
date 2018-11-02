<template>
  <div class="">
    <div class="uk-margin">
      <el-row type="flex" class="row-bg" justify="center">
          <el-col :span="18">
          <el-form ref="form" :model="form" label-width="125px">
            <br>
            <el-form-item label="Org_ID:">
              <el-input
                v-model="form.organization_id"
                type="text"
                clearable
                disabled
                v-bind:value="organization.organization_id">
              </el-input>
            </el-form-item>
            <el-form-item label="Name:">
              <el-input
                type="text"
                clearable
                disabled
                v-bind:value="organization.organization_id">
              </el-input>
            </el-form-item>
            <el-form-item label="Status:">
              <el-select
                v-model="form.status"
                placeholder="Select a status">
                <el-option
                  v-for="item in options"
                  :key="item.value"
                  :label="item.label"
                  :value="item.value">
                </el-option>
              </el-select>
            </el-form-item>
            <el-form-item label="Interest:">
              <el-input
                v-model="form.interest"
                type="text"
                clearable
                placeholder="ABC">
              </el-input>
            </el-form-item>
            <el-form-item label="Raise:">
              <el-input
                v-model="form.raise"
                type="text"
                clearable
                placeholder="ABC">
              </el-input>
            </el-form-item>
            <el-form-item label="Valuation:">
              <el-input
                v-model="form.valuation"
                type="text"
                clearable
                placeholder="1 Billion">
              </el-input>
            </el-form-item>
            <el-form-item label="Revenue:">
              <el-input
                v-model="form.revenue"
                type="text"
                clearable
                placeholder="1 Billion">
              </el-input>
            </el-form-item>
            <el-form-item label="Revenue Model:">
              <el-input
                v-model="form.revenue_model"
                type="text"
                clearable
                placeholder="1 Billion">
              </el-input>
            </el-form-item>
            <el-form-item label="Round:">
              <el-input
                v-model="form.round"
                type="text"
                clearable
                placeholder="1 Billion">
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
              <el-button @click="AddDeal()" type="primary">Add Deal!</el-button><br><br>
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
export default {
  name: 'AddEditDeal',
  props: ['organization'],

  data(){
    return{
      name: null,
      imageUrl:'',
      form: {
        organization_id: this.$parent.organization.organization_id,
        interest: "Interested in many things",
        status: "inProgress",
        valuation: "$34 Million",
        raise: "$3 Million",
        revenue: "$245 Million a year",
        revenue_model: "Building and selling things",
        round: null,
        slide_deck: null,
        notes: null
      },
      options: [
        {
          value: 'inProgress',
          label: 'In Progress'
        },
        {
          value: 'funded',
          label: 'Funded'
        },
        {
          value: 'notFunded',
          label: 'Not Funded'
        },
        {
          value: 'Other',
          label: 'Other'
        }
      ],
      status: ''

    }
  },
  methods: {
    goBack () {
      window.history.length > 1
        ? this.$router.go(-1)
        : this.$router.push('/')
    },
    AddDeal(){
      console.log(this.form);
      this.form.organization_id = this.$parent.organization.organization_id

      lib.postRequest('/deals', this.form, response => {
        console.log(this.form);
        console.log(response.data);
        this.$parent.deals.push(response.data)


      })
    }
  },
  mounted(){
    console.log("STUFF");
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

</style>
