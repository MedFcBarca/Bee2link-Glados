<template>
  <div class="group bg-white rounded-xl p-5 border border-slate-200 shadow-sm hover:shadow-xl hover:-translate-y-1 transition-all cursor-pointer relative overflow-hidden">

    <div class="absolute top-0 left-0 w-1 h-full bg-indigo-500/60 opacity-0 group-hover:opacity-100 transition"></div>

    <div class="flex items-center justify-between">
      
      <div class="flex items-center gap-3">
        <component
          :is="iconComponent"
          class="w-8 h-8 text-indigo-600" />
        <h2 class="font-semibold text-slate-800 text-xl truncate max-w-[150px] block">
          {{ entity.name }}
        </h2>

      </div>

      <div class="flex items-center gap-3">
        <Badge :status="entity.status" />
        <button
          @click.stop="$emit('edit', entity)"
          class="hover:bg-slate-100 p-2 rounded transition">
          ✏️
        </button>
      </div>
    </div>

    <div class="border-t my-4"></div>

    <div class="flex flex-col gap-3 text-sm">

      <div class="flex justify-between">
        <span class="text-slate-500">Type</span>
        <span class="font-medium capitalize">{{ entity.type }}</span>
      </div>

      <div
        v-if="entity.value"
        class="flex justify-between">
        <span class="text-slate-500">Value</span>
        <span class="font-medium">{{ entity.value }}</span>
      </div>

      <div class="flex justify-between">
        <span class="text-slate-500">Created</span>
        <span class="font-medium">{{ formattedDate }}</span>
      </div>

    </div>

  </div>
</template>

<script>
import {
  BoltIcon,
  ComputerDesktopIcon,
  FireIcon,
  LightBulbIcon,
  TvIcon
} from "@heroicons/vue/24/solid"

import Badge from "@/components/ui/Badge.vue"

export default {
  name: "EntityCard",
  components: {
    Badge,
    LightBulbIcon,
    TvIcon,
    FireIcon,
    BoltIcon,
    ComputerDesktopIcon 
  },

  props: { entity: Object },

  computed: {
    iconComponent() {
      return {
        light: LightBulbIcon,
        sensor: FireIcon,
        switch: BoltIcon,
        multimedia: TvIcon,
        air_conditioner: ComputerDesktopIcon
      }[this.entity.type] || LightBulbIcon
    },
    formattedDate() {
      return new Date(this.entity.created_at).toLocaleDateString()
    }
  }
}
</script>

<style scoped>
</style>
