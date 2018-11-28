<template>
  <div class="small">
    <Radar v-if="loaded" :chart-data="datacollection"></Radar>
    <!-- <button @click="fillData()">Randomize</button> -->
<p>props: {{skill1}},{{skill2}},{{skill3}},{{skill4}},{{skill5}} </p>
<p>selectors: {{values.skill1}},{{values.skill2}},{{values.skill3}},{{values.skill4}},{{values.skill5}} </p>
    <div class="block">
    <span class="demonstration">Persistence:</span>
    <el-slider @change="changeSkills"
      v-model="values.skill1"
      :step="1"
      :max= "5"
      show-stops>
    </el-slider>
    </div>
    <div class="block">
      <span class="demonstration">Leadership:</span>
      <el-slider @change="changeSkills"
        v-model="values.skill2"
        :step="1"
        :max= "5"
        show-stops>
      </el-slider>
    </div>
    <div class="block">
      <span class="demonstration">Confidence:</span>
      <el-slider @change="changeSkills"
        v-model="values.skill3"
        :step="1"
        :max= "5"
        show-stops>
      </el-slider>
    </div>
    <div class="block">
      <span class="demonstration">Knowledge:</span>
      <el-slider @change="changeSkills"
        v-model="values.skill4"
        :step="1"
        :max= "5"
        show-stops>
      </el-slider>
    </div>
    <div class="block">
      <span class="demonstration">Charisma:</span>
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

  export default {
    name: 'Deals',
    components: {
      Radar
    },
      // async mounted () {
      //   this.loaded = false
      //     try {
      //       this.fillData()
      //       this.loaded = true
      //     } catch (e) {
      //       console.error(e)
      //     }
      // },
    props:{
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
    },
    data () {
      return {

            loaded: false,
            chartdata: null,

        datacollection: null,
        values:{
          skill1: this.skill1,
          skill2: this.skill2,
          skill3: this.skill3,
          skill4: this.skill4,
          skill5: this.skill5
        },
        options: {
          responsive: true,
            scale: {
                reverse: false,
                ticks: {
                    beginAtZero: this.beginzero
                }
            },
            title: {
              display: true,
              position: 'top',
              text: 'Skills Chart'
            }
        },
      }
    },
    async mounted () {
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
          labels: ['skil1','skill2','skill3','skill4','skill5'],
          datasets: [
            {
              label: 'Skills',
              // backgroundColor: '#f87979',
              data: this.skillList()
             },

            // {
            //   label: 'Data two',
            //   // backgroundColor: '#f87979',
            //   data: [this.getRandomInt(), this.getRandomInt(), this.getRandomInt()]
            // },
            // {
            //   label: 'Data three',
            //   // backgroundColor: '#f87979',
            //   data: [this.getRandomInt(), this.getRandomInt(), this.getRandomInt()]
            // }
          ]
        };

      },
      changeSkills (){
        this.datacollection = {
          labels: ['skil1','skill2','skill3','skill4','skill5'],
          datasets: [
            {
              label: 'Skills',
              data: this.skillList(),
             },
          ]
        }
      },
      skillList (){
        return([parseInt(this.values.skill1),parseInt(this.values.skill2),parseInt(this.values.skill3),parseInt(this.values.skill4),parseInt(this.values.skill5),])
      }
    }
  }
</script>

<style>
  .small {
    max-width: 600px;
    margin:  150px auto;
  }
</style>
