<template>
  <div>
    <el-row>
      <el-col>
        <div class="uk-align-right uk-margin-right">
            <el-button v-on:click="toggleEdit" uk-toggle="target: #offcanvas-addDeal">Edit</el-button>
            <el-button @click="deleteDeal()" type="danger">Delete</el-button>
        </div>
      </el-col>
    </el-row>
    <el-row :gutter="50">
        <el-col :xs="0" :sm="1" :md="2" :lg="1" :xl="1"><div class="grid-content bg-purple"></div></el-col>
        <el-col :xs="24" :sm="24" :md="10" :lg="12" :xl="12">
            <div style="padding:0.5em;float:left;">
                <p v-if=""><em>Revenue:</em> ${{deal.revenue}} <font color="lightgrey">(Million)</font></p>
                <p><em>Revenue Model:</em> {{deal.revenue_model}}</p>
                <p><em>Valuation:</em> ${{deal.valuation}} <font color="lightgrey">(Million)</font></p>
            </div>
            <div style="padding:0.5em; padding-left:4em;float:left;">
                <p><em>Raise:</em> ${{deal.raise}} <font color="lightgrey">(Million)</font></p>
                <p><em>Round:</em> {{deal.round}}</p>
                <p><em>Interest:</em> {{deal.interest}}<span v-if="deal.status">({{deal.status}})</span></p>
            </div>
            <br>
            <div style="clear:both;">
                <div v-if="deal.slide_deck">
                    <em>Slide Deck:</em>
                    <webview class="pdfViewer" v-bind:src="deal.slide_deck" plugins></webview>
                </div>
                <div v-else>
                    <em>Notes:</em>
                    <Notes v-model="deal.notes"></Notes>
                </div>
            </div>
      </el-col>
      <el-col  :xs="24" :sm="24" :md="10" :lg="10" :xl="10">
        <!--calling radar chart, pass isContact or isOrganization to determin the label names -->
            <Chart
              v-if="!loading"
              isDeal
              :id = "deal.deal_id"
              :skill1 = "deal.skill1"
              :skill2 = "deal.skill2"
              :skill3 = "deal.skill3"
              :skill4 = "deal.skill4"
              :skill5 = "deal.skill5">
            </Chart>
      </el-col>
      <el-col :xs="0" :sm="1" :md="2" :lg="3" :xl="3"><div class="grid-content bg-purple"></div></el-col>
    </el-row>
    <el-row v-if="deal.slide_deck" :gutter="50" type="flex" class="row-bg" justify="center">
          <el-col :span="15">
              <br>
            <em>Notes:</em>
            <Notes v-model="deal.notes"></Notes>
          </el-col>
    </el-row>
  </div>
</template>

<script>
import Notes from '../components/Notes'
import Chart from '../components/Chart';
import lib from '../lib'
export default {
  name: 'DealOverview',
  props: ['organization', 'deal'],
  components:{
    'Chart': Chart,
    'Notes': Notes
  },
  data(){
    return{
      loading: false
    }
  },
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
      this.$parent.scrollToTop();
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
  .million{
    color: blue
  }
  .pdfViewer{
    border-radius: 10%;
    position: relative;
    width: 100%
  }
  .pdfViewer:before{
    content: "";
    padding-top: 70%; 	/* initial ratio of 1:1*/
  }

</style>
