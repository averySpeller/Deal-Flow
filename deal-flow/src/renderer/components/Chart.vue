<!--~~~~~~~~~~~~~~~~~~~~~~Chart~~~~~~~~~~~~~~~~~~~~~~~~~~~~~-->
<!--
Used to display skill radar chart for either contact or company (call using isContact or isCompany)
saves/updates to eiter one on change. Label names hardcoded for con or org

References: Radar.vue
props:{
  id: null,
  isContact: Boolean,
  isDeal: Boolean,
  skill1:{
    default: 0
  },
  skill2:{
    default: 0
  },
  skill3:{
    default: 0
  },
  skill4:{
    default: 0
  },
  skill5:{
    default: 0
  }
-->
<template>
  <div class="small">
    <Radar v-if="loaded" :chart-data="datacollection" :options="options" ></Radar>
    <div class="block">
    <span class="demonstration">{{skill1Name}}:</span>
    <el-slider @change="changeSkills"
      v-model="values.skill1"
      :step="1"
      :max= "5"
      show-stops>
    </el-slider>
    </div>
    <div class="block">
      <span class="demonstration">{{skill2Name}}:</span>
      <el-slider @change="changeSkills"
        v-model="values.skill2"
        :step="1"
        :max= "5"
        show-stops>
      </el-slider>
    </div>
    <div class="block">
      <span class="demonstration">{{skill3Name}}:</span>
      <el-slider @change="changeSkills"
        v-model="values.skill3"
        :step="1"
        :max= "5"
        show-stops>
      </el-slider>
    </div>
    <div class="block">
      <span class="demonstration">{{skill4Name}}:</span>
      <el-slider @change="changeSkills"
        v-model="values.skill4"
        :step="1"
        :max= "5"
        show-stops>
      </el-slider>
    </div>
    <div class="block">
      <span class="demonstration">{{skill5Name}}:</span>
      <el-slider @change="changeSkills"
        v-model="values.skill5"
        :step="1"
        :max= "5"
        show-stops>
      </el-slider>
    </div>
</div>
  </div>
</template>

<script>
  import Radar from '../components/Radar.vue'
  import lib from '../lib'
  export default {
    name: 'Chart',
    components: {
      Radar
    },
    props:{
      id: null,
      isContact: Boolean,
      isDeal: Boolean,
      skill1:{
        default: 0
      },
      skill2:{
        default: 0
      },
      skill3:{
        default: 0
      },
      skill4:{
        default: 0
      },
      skill5:{
        default: 0
      },

    },
    data () {
      return {
        labels: ['skil1','skill2','skill3','skill4','skill5'],
        backgroundColor: null,
        loaded: false,
        chartdata: null,
        skill1Name: 'skill1',
        skill2Name: 'skill2',
        skill3Name: 'skill3',
        skill4Name: 'skill4',
        skill5Name: 'skill5',
        datacollection: null,
        values:{
          skill1: this.skill1,
          skill2: this.skill2,
          skill3: this.skill3,
          skill4: this.skill4,
          skill5: this.skill5
        },
        requestString: null,
        options:{
            responsive: true,
            maintainAspectRatio: true,
            scale: {
                ticks: {
                    beginAtZero: true,
                    stepSize: 1,
                    max: 5
                }
            }
        },
      }
    },
    async mounted () {
      if(this.isContact){
        this.labels = ['Persistence','Leadership','Confidence','Knowledge','Charisma']
        this.skill1Name = 'Persistence'
        this.skill2Name = 'Leadership'
        this.skill3Name = 'Confidence'
        this.skill4Name = 'Knowledge'
        this.skill5Name = 'Charisma'
        this.backgroundColor = 'rgba(0,255,255,0.3)'
      }else if(this.isDeal){
        this.labels = ['Potential','People','Risk','Management','Recognition']
        this.skill1Name = 'Potential'
        this.skill2Name = 'People'
        this.skill3Name = 'Risk'
        this.skill4Name = 'Management'
        this.skill5Name = 'Recognition'
        this.backgroundColor = 'rgba(255, 111, 117,0.3)'
      }

      this.loaded = false
      try{
          this.fillData()
          this.loaded = true
      }catch(e){
        console.error(e)
      }

    },

    methods: {
      fillData () {
        console.log('filling Data');
        this.datacollection = {
          labels: this.labels,
          datasets: [
            {
              label: 'Skills',
              // backgroundColor: '#f87979',
              backgroundColor: this.backgroundColor,
              data: this.skillList()
             },
          ],

        };
      },
      changeSkills (){
        this.datacollection = {
          labels: this.labels,
          datasets: [
            {
              label: 'Skills',
              backgroundColor: this.backgroundColor,
              data: this.skillList(),
             },
          ]
        }
        if(this.isContact){
          this.requestString = "/contacts/"
        }else if(this.isDeal){
          this.requestString = "/deals/"
        }
        console.log("Put values are: "+this.values);
        lib.putRequest(this.requestString.concat(this.id), this.values, response => {
          console.log(response.data);
          console.log(response.header);
        })
      },
      skillList (){
        return([parseInt(this.values.skill1),parseInt(this.values.skill2),parseInt(this.values.skill3),parseInt(this.values.skill4),parseInt(this.values.skill5),])
      }
    }
  }
</script>

<style>
  .small {
    max-width: 325px;
    margin:  0 auto;

  }
  .demonstration {
    font-size: 13px !important;
  }
  .block {
      margin-top: -6px;
      margin-bottom: -6px;
  }
</style>
