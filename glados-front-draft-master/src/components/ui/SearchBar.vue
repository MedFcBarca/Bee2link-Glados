<template>
  <div class="relative w-full">
    <input
      type="text"
      :placeholder="placeholder"
      v-model="search"
      @input="$emit('update:modelValue', search)"
      class="w-full px-4 py-2 border border-slate-300 rounded-lg shadow-sm focus:border-indigo-500 focus:ring-2 focus:ring-indigo-200 transition-all"/>

    <svg
      class="w-5 h-5 absolute right-3 top-1/2 -translate-y-1/2 text-slate-400"
      fill="none"
      stroke="currentColor"
      stroke-width="2"
      viewBox="0 0 24 24">
      <path
        stroke-linecap="round"
        stroke-linejoin="round"
        d="M21 21l-4.35-4.35m1.15-5.4A6.5 6.5 0 1110.5 4a6.5 6.5 0 018.3 10.05z" />
    </svg>
  </div>
</template>

<script>
export default {
  name: "SearchBar",
  props: {
    modelValue: String,
    placeholder: {
      type: String,
      default: "Search..." 
    }
  },
  data() {
    return { search: this.modelValue || "" }
  }
}
</script>
