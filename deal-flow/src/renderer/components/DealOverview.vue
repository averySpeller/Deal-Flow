<template>
  <div>
    <el-row>
      <el-col>
        <div class="uk-align-right uk-margin-right">
          <el-button @click="deleteDeal()" type="danger">Delete Deal</el-button>

          <el-button v-on:click="toggleEdit" uk-toggle="target: #offcanvas-addDeal">Edit</el-button>
        </div>
      </el-col>
    </el-row>
    <h1>THIS: {{this.deal.deal_id}}</h1>
    <el-row :gutter="50">
      <el-col :xs="0" :sm="1" :md="2" :lg="3" :xl="3"><div class="grid-content bg-purple"></div></el-col>
      <el-col :xs="12" :sm="11" :md="10" :lg="9" :xl="9">
        <ul>
          <el-row :gutter="15">
            <el-col :span="12">
              <strong class="uk-align-right">Valuation:</strong>
            </el-col>
            <el-col :span="12">
              {{deal.valuation}}
            </el-col>
          </el-row>
          <el-row :gutter="15">
            <el-col :span="12">
              <strong class="uk-align-right">Stock Symbol:</strong>
            </el-col>
            <el-col :span="12">
              {{deal.stock_symbol}}
            </el-col>
          </el-row>
          <el-row :gutter="15">
            <el-col :span="12">
              <strong class="uk-align-right">Revenue:</strong>
            </el-col>
            <el-col :span="12">
              {{deal.revenue}}
            </el-col>
          </el-row>
          <el-row :gutter="15">
            <el-col :span="12">
              <strong class="uk-align-right">Revenue Model:</strong>
            </el-col>
            <el-col :span="12">
              {{deal.revenue_model}}
            </el-col>
          </el-row>
          <!-- <li><p><strong>Address: </strong>{{organization.address.street}} "Street, "{{organization.address.suite}}", "{{organization.address.city}}", "{{organization.address.zipcode}}</p></li> -->
        </ul>
      </el-col>
      <el-col  :xs="12" :sm="11" :md="10" :lg="9" :xl="9">
        <el-row :gutter="15">
          <el-col :span="12">
            <strong class="uk-align-right">Status:</strong>
          </el-col>
          <el-col :span="12">
            {{deal.status}}
          </el-col>
        </el-row>
        <el-row :gutter="15">
          <el-col :span="12">
            <strong class="uk-align-right">Raise:</strong>
          </el-col>
          <el-col :span="12">
            {{deal.raise}}
          </el-col>
        </el-row>
        <el-row :gutter="15">
          <el-col :span="12">
            <strong class="uk-align-right">Raise Type:</strong>
          </el-col>
          <el-col :span="12">
            {{deal.raise_type}}
          </el-col>
        </el-row>
        <el-row :gutter="15">
          <el-col :span="12">
            <strong class="uk-align-right">Round:</strong>
          </el-col>
          <el-col :span="12">
            {{deal.round}}
          </el-col>
        </el-row>

      </el-col>
      <el-col :xs="0" :sm="1" :md="2" :lg="3" :xl="3"><div class="grid-content bg-purple"></div></el-col>
    </el-row>



    <el-row :gutter="50" type="flex" class="row-bg" justify="center">
      <el-col :span="12">
        Notes:
        <el-input
          v-model="deal.notes"
          type="textarea"
          :autosize="{ minRows: 4, maxRows: 8}"
          placeholder="Additional Notes" >
        </el-input>
      </el-col>
    </el-row>
<br><br>
    <el-row :gutter="50" type="flex" class="row-bg" justify="center">
      <el-col :span="12">
        PDF:
        <!-- static/pdfs/Prototyping.pdf -->
        <!-- <webview v-bind:src="deal.slide_deck" plugins></webview> -->
        <webview v-bind:src="deal.slide_deck" plugins></webview>
      </el-col>
    </el-row>

  </div>
</template>

<script>
import lib from '../lib'
export default {
  name: 'DealOverview',
  props: ['organization', 'deal'],

  methods: {
    deleteDeal(){
      var dealIndex = this.$parent.deals.indexOf(this.deal)
      console.log(dealIndex);
      if (dealIndex > -1) {
        this.$parent.deals.splice(dealIndex, 1);
      }

      console.log("Deleting Deal #".concat(this.deal.deal_id));
      lib.deleteRequest("/deals/".concat(this.deal.deal_id), response => {
        console.log(response);
      })
    },
    toggleEdit(){
      this.$parent.editDeal = true;
      console.log(this.$parent.editDeal);
    }
  }

}
</script>
<style scoped>
  .grid-content {
    min-height: 36px;
  }

</style>
