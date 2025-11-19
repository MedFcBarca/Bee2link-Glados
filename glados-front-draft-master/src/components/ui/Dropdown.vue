<template>
  <div
    class="relative"
    ref="dropdown">
    <button
      @click.stop="toggle"
      class="px-4 py-2 bg-white border border-slate-300 rounded-lg shadow-sm hover:shadow-md transition-all text-sm flex items-center gap-2">
      {{ selectedLabel }}
      <svg
        class="w-4 h-4"
        fill="none"
        stroke="currentColor"
        stroke-width="2"
        viewBox="0 0 24 24">
        <path
          stroke-linecap="round"
          stroke-linejoin="round"
          d="M19 9l-7 7-7-7" />
      </svg>
    </button>

    <div
      v-if="open"
      class="absolute z-20 mt-2 w-full bg-white rounded-lg shadow-lg border border-slate-200">
      <div
        v-for="option in options"
        :key="option.value"
        @click="select(option)"
        class="px-4 py-2 hover:bg-slate-100 cursor-pointer text-sm">
        {{ option.label }}
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "Dropdown",
  props: {
    options: {
      type: Array,
      default: () => [] 
    },
    modelValue: String
  },
  data() {
    return { open: false }
  },

  computed: {
    selectedLabel() {
      return this.options.find(o => o.value === this.modelValue)?.label || "Choose"
    }
  },

  mounted() {
    document.addEventListener("click", this.handleClickOutside)
  },
  beforeUnmount() {
    document.removeEventListener("click", this.handleClickOutside)
  },

  methods: {
    toggle() {
      this.open = !this.open
    },

    select(option) {
      this.$emit("update:modelValue", option.value)
      this.open = false
    },

    handleClickOutside(e) {
      if (!this.$refs.dropdown.contains(e.target)) {
        this.open = false
      }
    }
  }
}
</script>
