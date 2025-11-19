<template>
  <div class="w-full space-y-10">

    <h1 class="text-4xl font-bold text-slate-900 tracking-tight">
      Rooms Overview
    </h1>

    <div class="grid md:grid-cols-2 gap-6">

      <div class="bg-white rounded-2xl p-4 shadow-sm border w-full overflow-hidden">
        <h2 class="text-lg font-semibold text-slate-800 mb-4">
          Devices by Room
        </h2>

        <apexchart
          type="pie"
          width="100%"
          :height="chartHeight"
          :options="pieOptions"
          :series="pieSeries"/>
      </div>

      <div class="bg-white rounded-2xl p-4 shadow-sm border w-full overflow-hidden">
        <h2 class="text-lg font-semibold text-slate-800 mb-4">
          Devices by Type
        </h2>

        <apexchart
          type="bar"
          width="100%"
          :height="chartHeight"
          :options="barTypeOptions"
          :series="barTypeSeries"/>
      </div>

    </div>

  </div>
</template>

<script>
import coreApi from "@/providers/core-api"
import VueApexCharts from "vue3-apexcharts"

export default {
  name: "Rooms",
  components: { apexchart: VueApexCharts },

  data() {
    return {
      rooms: [],

      chartHeight: window.innerWidth < 768 ? 220 : 300,

      pieOptions: {},
      pieSeries: [],

      barTypeOptions: {},
      barTypeSeries: [],
    }
  },

  created() {
    this.loadRooms()
  },

  methods: {
    loadRooms() {
      coreApi.glados.getRooms()
        .then(data => {
          this.rooms = data.map(r => ({
            ...r,
            entity_count: r.entities ? r.entities.length : 0
          }))


          const labels = this.rooms.map(r => r.name)
          const counts = this.rooms.map(r => r.entity_count)

          this.pieOptions = {
            chart: { toolbar: { show: false } },
            labels,
            legend: {
              position: "bottom",
              fontSize: window.innerWidth < 768 ? "12px" : "14px"
            },
            dataLabels: {
              enabled: true,
              style: { fontSize: window.innerWidth < 768 ? "11px" : "14px" },
              formatter: (val, opts) => 
                opts.w.config.labels[opts.seriesIndex]
            }
          }
          this.pieSeries = counts


          const typeCount = {}

          this.rooms.forEach(room => {
            room.entities?.forEach(e => {
              if (!typeCount[e.type]) typeCount[e.type] = 0
              typeCount[e.type]++
            })
          })

          const typeLabels = Object.keys(typeCount)
          const typeValues = Object.values(typeCount)

          this.barTypeOptions = {
            chart: { toolbar: { show: false } },
            xaxis: {
              categories: typeLabels,
              labels: { style: { fontSize: window.innerWidth < 768 ? "11px" : "13px" } }
            },
            dataLabels: { enabled: false },
            legend: { show: false },
            plotOptions: {
              bar: {
                borderRadius: 6,
                horizontal: false
              }
            },
            grid: {
              padding: {
                left: 10,
                right: 10
              }
            },
            colors: ["#6366F1"]
          }

          this.barTypeSeries = [
            {
              name: "Devices",
              data: typeValues 
            }
          ]
        })
    }
  }
}
</script>
