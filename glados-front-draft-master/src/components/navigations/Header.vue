<template>
  <header
    class="w-full h-16 backdrop-blur-lg bg-white/80 border-b border-gray-200/60 flex items-center px-8 sticky top-0 z-50 shadow-sm">

    <div class="flex items-center">
      <Logo class="w-10" />
    </div>

    <nav class="hidden md:flex gap-10 ml-auto relative items-center">
      <button
        v-for="tab in tabs"
        :key="tab.name"
        @click="goTo(tab.name)"
        class="relative text-gray-600 hover:text-gray-900 font-medium transition-all pb-1"
      >
        {{ tab.label }}

        <span
          v-if="$route.name === tab.name"
          class="absolute left-0 bottom-0 w-full h-[2px] bg-indigo-600 rounded-full animate-slideIn"
        ></span>
      </button>
    </nav>

    <button
      @click="isOpen = !isOpen"
      class="ml-auto md:hidden p-2 text-gray-700 hover:text-gray-900 transition"
    >
      <svg xmlns="http://www.w3.org/2000/svg" class="h-7 w-7"
           fill="none" viewBox="0 0 24 24" stroke="currentColor">
        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
              d="M4 6h16M4 12h16M4 18h16" />
      </svg>
    </button>

    <div
      v-if="isOpen"
      class="absolute top-16 left-0 w-full bg-white shadow-lg border-b md:hidden animate-fadeIn"
    >
      <div
        v-for="tab in tabs"
        :key="tab.name"
        @click="goTo(tab.name); isOpen=false"
        class="px-6 py-4 text-gray-700 text-lg border-b hover:bg-gray-100 transition"
      >
        {{ tab.label }}
      </div>
    </div>

  </header>
</template>

<script>
import Logo from "@/components/ui/Logo.vue"

export default {
  name: "Header",
  components: { Logo },
  data() {
    return {
      isOpen: false,
      tabs: [
        { label: "Dashboard", name: "dashboard" },
        { label: "Rooms", name: "rooms" },
        { label: "About", name: "about" },
      ],
    }
  },
  methods: {
    goTo(name) {
      this.$router.push({ name })
    }
  }
}
</script>

<style scoped>
@keyframes slideIn {
  from { width: 0; opacity: 0; }
  to   { width: 100%; opacity: 1; }
}
.animate-slideIn {
  animation: slideIn 0.25s ease-out;
}

@keyframes fadeIn {
  from { opacity: 0; transform: translateY(-8px); }
  to   { opacity: 1; transform: translateY(0); }
}
.animate-fadeIn {
  animation: fadeIn 0.2s ease-out;
}
</style>