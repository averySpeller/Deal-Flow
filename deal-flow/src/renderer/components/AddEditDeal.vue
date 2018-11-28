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
            <el-form-item label="Round:">
              <el-select
                v-model="deal.round"
                placeholder="Select a round">
                <el-option
                  v-for="round in rounds"
                  :key="round.value"
                  :label="round.label"
                  :value="round.value">
                </el-option>
              </el-select>
            </el-form-item>
            <el-form-item label="Raise:">
              <el-input
                v-model="deal.raise"
                type="text"
                clearable
                placeholder="$xx Million (USD)">
              </el-input>
            </el-form-item>
            <el-form-item label="Valuation:">
              <el-input
                v-model="deal.valuation"
                type="text"
                clearable
                placeholder="$xx Million (USD)">
              </el-input>
            </el-form-item>
            <el-form-item label="Revenue:">
              <el-input
                v-model="deal.revenue"
                type="text"
                clearable
                placeholder="$xx Million (USD)">
              </el-input>
            </el-form-item>
            <el-form-item label="Revenue Model:">
              <el-input
                v-model="deal.revenue_model"
                type="text"
                clearable
                placeholder="SaaS, License, Retail, etc">
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
            <FileUploader v-model="deal.slide_deck" v-bind:fileList="this.fileList"></FileUploader>

            <div class="uk-flex uk-flex-center">
              <el-button v-if="editDeal" @click="EditDeal()" type="primary" uk-toggle="target: #offcanvas-addDeal">Save</el-button>
              <el-button v-else @click="AddDeal()" type="primary" uk-toggle="target: #offcanvas-addDeal">Save</el-button><br><br>
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
  props: ['organization', 'editDeal', 'deal', 'fileList'],

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
      rounds: [
          { value: 'Seed', label: 'Seed' },
          { value: 'Angel', label: 'Angel' },
          { value: 'Series A', label: 'Series A' },
          { value: 'Series B', label: 'Series B' },
          { value: 'Series C', label: 'Series C' },
      ],
      statusOptions: [
        {
          value: 'In Progress',
          label: 'In Progress'
        },
        {
          value: 'Funded',
          label: 'Funded'
        },
        {
          value: 'Not Funded',
          label: 'Not Funded'
        },
        {
          value: 'Other',
          label: 'Other'
        }
      ],
      status: '',
      interestOptions: [
        { value: 'High', label: 'High'},
        { value: 'Medium', label: 'Medium' },
        { value: 'Low', label: 'Low' }
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

      lib.putRequest('/deals/'.concat(this.deal.deal_id), this.deal, response => {
        console.log("Request Completed: Updated Deal #".concat(this.deal.deal_id));
        console.log(response.data);
        this.$parent.editDeal = false;
      })
    }
  },
  created(){
    //CREATION
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
