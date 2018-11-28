<template>
    <div>
        <canvas v-if="!target" ref="canvas" :width="width" :height="height"></canvas>
    </div>
</template>
<script>
export default {
    name: 'SkillChart',
    mixins: [
        VueCharts.core.default,
    ],
    props: {
        pointbordercolor: {
            default: () => "#fff",
        },
        pointbackgroundcolor: {
            default: () => "rgba(179,181,198,1)",
        }
    },
    data() {
        return {

          pesistence: 2,
          leadership: 2,
          confidence: 2,
          knowledge: 3,
          charisma: 4,

            type: 'radar',
            chart_data: {
                labels: ['persistence','leadership','confidence','knowledge','charisma'],
                datasets: [{
                    label: 'Johnny Cash',
                    backgroundColor: this.backgroundcolor,
                    borderColor: this.bordercolor,
                    pointBackgroundColor: this.pointbackgroundcolor,
                    pointBorderColor: this.pointbordercolor,
                    pointHoverBackgroundColor: "#fff",
                    pointHoverBorderColor: "rgba(179,181,198,1)",
                    // data: [this.persistence,this.leadership,this.confidence,this.knowledge,this.charisma]
                    data: [1,2,3,4,5]
                }],
            },
            options: {
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
}
</script>
