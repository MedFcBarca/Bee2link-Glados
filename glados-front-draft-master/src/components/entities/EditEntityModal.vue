<template>
  <div class="fixed inset-0 bg-black/40 backdrop-blur-sm flex items-center justify-center z-50">
    <div class="bg-white rounded-xl p-6 shadow-xl w-96 animate-fadeIn">
      
      <h2 class="text-xl font-bold mb-4">Edit {{ entity.name }}</h2>

      <div class="flex flex-col gap-4">

        <div>
          <label class="text-sm text-slate-500">Name</label>
          <input
            v-model="form.name"
            class="w-full border p-2 rounded-lg">
        </div>

        <div>
          <label class="text-sm text-slate-500">Status</label>
          <select
            v-model="form.status"
            class="w-full border p-2 rounded-lg">
            <option value="on">On</option>
            <option value="off">Off</option>
            <option value="unavailable">Unavailable</option>
          </select>
        </div>

        <div>
          <label class="text-sm text-slate-500">Value</label>
          <input
            v-model="form.value"
            class="w-full border p-2 rounded-lg">
        </div>

      </div>

      <div class="flex justify-end gap-3 mt-6">
        <button
          @click="$emit('close')"
          class="px-4 py-2 bg-slate-200 rounded-lg">
          Cancel
        </button>

        <button
          @click="update"
          class="px-4 py-2 bg-indigo-600 text-white rounded-lg">
          Save
        </button>
      </div>

    </div>
  </div>
</template>

<script>
export default {
  name: "EditEntityModal",
  props: {
    entity: {
      type: Object,
      required: true 
    }
  },
  emits: ["close", "updated"],

  data() {
    return {
      form: {
        name: this.entity.name,
        status: this.entity.status,
        value: this.entity.value
      }
    }
  },

  methods: {
    update() {
      const data = { ...this.form }
      if (!data.value) delete data.value  
      this.$emit("updated", data)
    }
  }
}
</script>

<style>
@keyframes fadeIn {
  from { opacity: 0; transform: scale(0.96); }
  to { opacity: 1; transform: scale(1); }
}
</style>
