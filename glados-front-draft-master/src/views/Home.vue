<template>
  <div class="flex flex-col h-screen overflow-hidden bg-gray-50">

    <Header />

    <main class="flex-1 w-full px-8 py-10 overflow-y-auto">
      <router-view />
    </main>
  </div>
</template>

<script>
import Header from "@/components/navigations/Header.vue"

export default {
  name: "Home",
  components: { Header }
}
</script>

<style scoped>
main::-webkit-scrollbar {
  width: 8px;
}
main::-webkit-scrollbar-thumb {
  background: #c5c5c5;
  border-radius: 10px;
}
</style>
