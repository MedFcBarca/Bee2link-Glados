<template>
  <span :class="badgeClass">
    <span
      class="w-2 h-2 rounded-full"
      :class="dotClass"></span>
    <span class="capitalize">{{ status }}</span>
  </span>
</template>

<script>
export default {
  name: "Badge",
  props: { status: String },
  computed: {
    dotClass() {
      return {
        on: "bg-green-500",
        off: "bg-red-500",
        unavailable: "bg-gray-500"
      }[this.status]
    },
    badgeClass() {
      return [
        "inline-flex items-center gap-1 px-2 py-0.5 rounded-full text-xs font-semibold shrink-0",
        {
          on: "bg-green-100 text-green-700",
          off: "bg-red-100 text-red-700",
          unavailable: "bg-gray-200 text-gray-700"
        }[this.status]
      ]
    }
  }
}
</script>
