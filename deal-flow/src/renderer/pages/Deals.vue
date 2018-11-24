
<template>
    <div>
        <canvas v-if="!target" ref="canvas" :width="width" :height="height"></canvas>

        <div class="block">
        <span class="demonstration">Persistence:</span>
        <el-slider @change="change"
          v-model="values.pesistence"
          :step="1"
          :max= "5"
          show-stops>
        </el-slider>
        </div>
        <div class="block">
          <span class="demonstration">Leadership:</span>
          <el-slider
            v-model="values.leadership"
            :step="1"
            :max= "5"
            show-stops>
          </el-slider>
        </div>
        <div class="block">
          <span class="demonstration">Confidence:</span>
          <el-slider
            v-model="values.confidence"
            :step="1"
            :max= "5"
            show-stops>
          </el-slider>
        </div>
        <div class="block">
          <span class="demonstration">Knowledge:</span>
          <el-slider
            v-model="values.knowledge"
            :step="1"
            :max= "5"
            show-stops>
          </el-slider>
        </div>
        <div class="block">
          <span class="demonstration">Charisma:</span>
          <el-slider
            v-model="values.charisma"
            :step="1"
            :max= "5"
            show-stops>
          </el-slider>
        </div>
    </div>
</template>
<script>
export default {
    mixins: [
        VueCharts.core.default,
    ],
  mounted () {
    this.renderChart(this.chartData, this.options)
  },
    props: {
        pointbordercolor: {
            default: () => "#fff",
        },
        pointbackgroundcolor: {
            default: () => "rgba(179,181,198,1)",
        },
        data: {
          default: () => [2,3,2,4,5],
        }
    },
    data() {
        return {
          values:{
            pesistence: 20,
            leadership: 3,
            confidence: 2,
            knowledge: 4,
            charisma: 5,
          },
            type: 'radar',
            chart_data: {
              // pesistence: 2,
              // leadership: 3,
              // confidence: 2,
              // knowledge: 4,
              // charisma: 5,

                labels: ['persistence','leadership','confidence','knowledge','charisma'],
                datasets: [{
                    label: 'Johnny Cash',
                    backgroundColor: this.backgroundcolor,
                    borderColor: this.bordercolor,
                    pointBackgroundColor: this.pointbackgroundcolor,
                    pointBorderColor: this.pointbordercolor,
                    pointHoverBackgroundColor: "#fff",
                    pointHoverBorderColor: "rgba(179,181,198,1)",
                    data: this.data
                    // data: []
                    //  data: [this.persistence,this.leadership,this.confidence,this.knowledge,this.charisma]
                    // data: [2,3,2,4,5]
                }],
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
        };
    },
    // created(){
    //   this.chart_data.data.push[this.values];
    // },
    // mounted(){
    //   this.renderChart()
    // },
    watch: {
  chartData () {
    this.$data._chart.update()
  }
},
    methods: {
      change() {
        this.renderChart()
        console.log("The value is: " + this.values.persistence);
        //HERE I can't get "event.target"
      }
    }
}
</script>
