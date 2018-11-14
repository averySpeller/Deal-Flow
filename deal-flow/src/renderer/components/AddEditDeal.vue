<template>
  <div class="">
    <div class="title uk-flex uk-flex-center">
        <h1>{{deal.valuation}}</h1>
    </div>
    <div class="uk-margin">
      <el-row type="flex" class="row-bg" justify="center">
          <el-col :span="18">
          <el-form ref="form" :model="form" label-width="125px">
            <br>
            <el-form-item label="Name:">
              <el-input
                type="text"
                clearable
                disabled
                v-bind:value="organization.name">
              </el-input>
            </el-form-item>
            <el-form-item label="Status:">
              <el-select
                v-model="deal.status"
                placeholder="Select a status">
                <el-option
                  v-for="status in statusOptions"
                  :key="status.value"
                  :label="status.label"
                  :value="status.value">
                </el-option>
              </el-select>
            </el-form-item>
            <el-form-item label="Interest:">
              <el-select
                v-model="deal.interest"
                placeholder="Select an interest level">
                <el-option
                  v-for="item in interestOptions"
                  :key="item.value"
                  :label="item.label"
                  :value="item.value">
                </el-option>
              </el-select>
            </el-form-item>
            <el-form-item label="Raise:">
              <el-input
                v-model="deal.raise"
                type="text"
                clearable
                placeholder="ABC">
              </el-input>
            </el-form-item>
            <el-form-item label="Valuation:">
              <el-input
                v-model="deal.valuation"
                type="text"
                clearable
                placeholder="1 Billion">
              </el-input>
            </el-form-item>
            <el-form-item label="Revenue:">
              <el-input
                v-model="deal.revenue"
                type="text"
                clearable
                placeholder="1 Billion">
              </el-input>
            </el-form-item>
            <el-form-item label="Revenue Model:">
              <el-input
                v-model="deal.revenue_model"
                type="text"
                clearable
                placeholder="1 Billion">
              </el-input>
            </el-form-item>
            <el-form-item label="Round:">
              <el-input
                v-model="deal.round"
                type="text"
                clearable
                placeholder="1 Billion">
              </el-input>
            </el-form-item>
            <el-form-item label="Notes:">
              <el-input
                v-model="deal.notes"
                type="textarea"
                clearable
                placeholder="Add Notes">
              </el-input>
            </el-form-item>
            <FileUploader v-model="deal.slide_deck"></FileUploader>

            <div v-if="deal.editDeal" class="uk-flex uk-flex-center">
              <el-button @click="EditDeal()" type="primary" uk-toggle="target: #offcanvas-addDeal">Edit Deal!</el-button><br><br>
            </div>

            <div v-else class="uk-flex uk-flex-center">
              <el-button @click="AddDeal()" type="primary" uk-toggle="target: #offcanvas-addDeal">Add Deal!</el-button><br><br>
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
import FileUploader from './FileUploader'
export default {
  name: 'AddEditDeal',
  props: ['organization', 'editDeal', 'deal'],

  data(){
    return{
      name: null,
      imageUrl:'',
      form: {
        organization_id: this.$parent.organization.organization_id,
        interest: null,
        status: null,
        valuation: null,
        raise: null,
        revenue: null,
        revenue_model: null,
        round: null,
        slide_deck: null,
        notes: null
      },
      statusOptions: [
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
      status: '',
      interestOptions: [
        {
          value: 'High',
          label: 'High'
        },
        {
          value: 'Medium',
          label: 'Medium'
        },
        {
          value: 'Low',
          label: 'Low'
        }
      ],

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
    AddDeal(){
      this.deal.organization_id = this.$parent.organization.organization_id

      console.log(this.deal);
      lib.postRequest('/deals', this.deal, response => {
        console.log(response.data);
        this.$parent.deals.push(response.data);
        this.$parent.emptyCurrentDeal();
        this.$parent.currentDeal = response.data;

      })



    },
    EditDeal(){
      console.log(this.deal);
      this.deal.organization_id = this.$parent.organization.organization_id

      // lib.postRequest('/deals', this.form, response => {
      //   console.log(this.form);
      //   console.log(response.data);
      //   this.$parent.deals.push(response.data)
      //
      //   goBack();
      // })
      this.$parent.editDeal = false;
    }
  },
  created(){
    console.log("MOUNTED");
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
