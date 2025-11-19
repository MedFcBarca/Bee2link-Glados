<template>
  <div class="w-full relative">

    <h1 class="text-3xl font-bold text-slate-800 mb-6 tracking-tight flex items-center gap-3">
      Smart Home Dashboard
      <div
        v-if="isSpeaking"
        class="voice-orb"></div>
    </h1>

    <div
      v-if="isSpeaking"
      class="flex justify-center mb-6">
      <div class="voice-wave">
        <span
          v-for="n in 10"
          :key="n"
          class="wave-bar"></span>
      </div>
    </div>

    <div class="flex flex-wrap gap-4 mb-8 items-center">

      <SearchBar
        v-model="searchQuery"
        placeholder="Search devices..."/>

      <Dropdown
        v-model="selectedType"
        :options="typeOptions"/>

      <Dropdown
        v-model="selectedStatus"
        :options="statusOptions"/>

      <div class="flex items-center gap-3 ml-auto">
        
        <button
          @click="speakReport"
          class="px-4 py-2 bg-indigo-600 hover:bg-indigo-700 text-white rounded-lg shadow transition flex items-center gap-2">
          🧠 AI Voice Report
        </button>

        <button
          ref="voiceButtonRef"
          @click.stop="toggleVoiceSettings"
          class="px-3 py-2 bg-slate-200 hover:bg-slate-300 rounded-lg text-sm transition">
          🎤 Voice Settings
        </button>

        <button
          v-if="isSpeaking"
          @click="stopSpeech"
          class="px-3 py-2 bg-red-500 hover:bg-red-600 text-white rounded-lg text-sm transition">
          ⛔ Stop
        </button>

      </div>
    </div>

    <div
      v-if="showVoiceSettings"
      ref="voiceSettingsRef"
      class="absolute top-16 right-4 bg-white border shadow-xl rounded-lg p-5 w-80 z-50">
      <h3 class="font-bold text-lg mb-3">🎤 Voice Settings</h3>

      <label class="text-sm">Voice</label>
      <select
        v-model="selectedVoice"
        class="w-full border p-2 rounded mb-3">
        <option
          v-for="v in availableVoices"
          :key="v.voice.voiceURI"
          :value="v.voice.voiceURI">
          {{ v.label }}
        </option>
      </select>

      <label class="text-sm">Pitch (tone)</label>
      <input
        type="range"
        min="0.5"
        max="2"
        step="0.1"
        v-model="pitch"
        class="w-full mb-3"/>

      <label class="text-sm">Speed</label>
      <input
        type="range"
        min="0.5"
        max="2"
        step="0.1"
        v-model="rate"
        class="w-full mb-3"/>

      <button
        class="px-3 py-2 bg-indigo-500 text-white rounded w-full"
        @click="showVoiceSettings = false">
        Done
      </button>
    </div>

    <div class="grid gap-6 lg:grid-cols-3 xl:grid-cols-4 md:grid-cols-2 grid-cols-1 transition-all">
      
      <EntityCard
        v-for="e in filteredEntities"
        :key="e.id"
        :entity="e"
        @edit="openEditor"/>

    </div>

    <EditEntityModal
      v-if="showModal"
      :entity="selectedEntity"
      @close="showModal = false"
      @updated="applyUpdate"/>

  </div>
</template>


<script>
import coreApi from "@/providers/core-api"
import EntityCard from "@/components/entities/EntityCard.vue"
import Dropdown from "@/components/ui/Dropdown.vue"
import SearchBar from "@/components/ui/SearchBar.vue"
import EditEntityModal from "@/components/entities/EditEntityModal.vue"

export default {
  name: "Dashboard",
  components: {
    EntityCard,
    Dropdown,
    SearchBar,
    EditEntityModal 
  },

  data() {
    return {
      entities: [],
      searchQuery: "",
      selectedType: "all",
      selectedStatus: "all",

      selectedEntity: null,
      showModal: false,

      availableVoices: [],
      selectedVoice: null,
      pitch: 1,
      rate: 1,

      showVoiceSettings: false,
      isSpeaking: false,

      typeOptions: [
        {
          label: "All Types",
          value: "all" 
        },
        {
          label: "Light",
          value: "light" 
        },
        {
          label: "Sensor",
          value: "sensor" 
        },
        {
          label: "Switch",
          value: "switch" 
        },
        {
          label: "Multimedia",
          value: "multimedia" 
        },
        {
          label: "Air Conditioner",
          value: "air_conditioner" 
        }
      ],

      statusOptions: [
        {
          label: "All Status",
          value: "all" 
        },
        {
          label: "On",
          value: "on" 
        },
        {
          label: "Off",
          value: "off" 
        },
        {
          label: "Unavailable",
          value: "unavailable" 
        }
      ]
    }
  },

  mounted() {
    document.addEventListener("click", this.handleClickOutside)
  },
  beforeUnmount() {
    document.removeEventListener("click", this.handleClickOutside)
  },

  created() {
    this.loadEntities()
    this.loadVoices()
  },

  computed: {
    filteredEntities() {
      return this.entities.filter(e => {
        if (this.selectedType !== "all" && e.type !== this.selectedType) return false
        if (this.selectedStatus !== "all" && e.status !== this.selectedStatus) return false
        if (this.searchQuery && !e.name.toLowerCase().includes(this.searchQuery.toLowerCase())) return false
        return true
      })
    }
  },

  methods: {

    handleClickOutside(e) {
      if (!this.showVoiceSettings) return

      const modal = this.$refs.voiceSettingsRef
      const button = this.$refs.voiceButtonRef

      if (modal && !modal.contains(e.target) && !button.contains(e.target)) {
        this.showVoiceSettings = false
      }
    },

    toggleVoiceSettings() {
      this.showVoiceSettings = !this.showVoiceSettings
    },

    loadEntities() {
      coreApi.glados.getEntities()
        .then(data => (this.entities = data))
        .catch(console.error)
    },

    openEditor(entity) {
      this.selectedEntity = entity
      this.showModal = true
    },

    applyUpdate(newData) {
      coreApi.glados.updateEntity(this.selectedEntity.id, newData)
        .then(res => {
          Object.assign(this.selectedEntity, res)
          this.showModal = false
        })
    },

    stopSpeech() {
      window.speechSynthesis.cancel()
      this.isSpeaking = false
    },

    loadVoices() {
      const load = () => {
        const all = window.speechSynthesis.getVoices()
        const FEMALE_HINTS = ["female", "woman", "samantha", "victoria", "amelie", "julie"]
        const MALE_HINTS   = ["male", "man", "daniel", "fred", "alex", "antoine", "thomas"]

        const detectGender = v => {
          const name = v.name.toLowerCase()
          if (FEMALE_HINTS.some(h => name.includes(h))) return "female"
          if (MALE_HINTS.some(h => name.includes(h))) return "male"
          if (v.lang === "fr-FR") return name.includes("neural") ? "female" : "male"
          if (v.lang.startsWith("en")) return "female"
          return "unknown"
        }

        const groups = {
          english: {
            male: [],
            female: [] 
          },
          french: {
            male: [],
            female: [] 
          }
        }

        all.forEach(v => {
          const gender = detectGender(v)
          if (v.lang.startsWith("en")) groups.english[gender]?.push(v)
          if (v.lang === "fr-FR") groups.french[gender]?.push(v)
        })

        const result = []

        if (groups.english.male[0]) result.push({
          label: "🇺🇸 English — Male",
          voice: groups.english.male[0] 
        })
        if (groups.english.female[0]) result.push({
          label: "🇺🇸 English — Female",
          voice: groups.english.female[0] 
        })
        if (groups.french.male[0]) result.push({
          label: "🇫🇷 French — Male",
          voice: groups.french.male[0] 
        })
        if (groups.french.female[0]) result.push({
          label: "🇫🇷 French — Female",
          voice: groups.french.female[0] 
        })

        this.availableVoices = result

        if (!this.selectedVoice && result.length)
          this.selectedVoice = result[0].voice.voiceURI
      }

      load()
      window.speechSynthesis.onvoiceschanged = load
    },

    speakReport() {
      this.stopSpeech()

      if (!this.availableVoices.length) return

      let voice = window.speechSynthesis.getVoices()
        .find(v => v.voiceURI === this.selectedVoice)

      const utter = new SpeechSynthesisUtterance()
      utter.voice = voice
      utter.pitch = this.pitch
      utter.rate = this.rate

      let text = `Here is the status of your smart home. I found ${this.entities.length} devices. `

      this.entities.forEach(e => {
        const name = e.name.replace(/_/g, " ")
        const status = e.status === "on" ? "is turned on"
          : e.status === "off" ? "is currently off"
            : "is unavailable"
        const value = e.value ? `with a value of ${e.value}` : ""
        text += `${name} ${status} ${value}. `
      })

      utter.text = text
      utter.onstart = () => this.isSpeaking = true
      utter.onend = () => this.isSpeaking = false

      window.speechSynthesis.speak(utter)
    }
  }
}
</script>



<style>
.voice-orb {
  width: 14px;
  height: 14px;
  border-radius: 9999px;
  background: #4f46e5;
  position: relative;
  box-shadow: 0 0 10px #6366f1, 0 0 20px #818cf8;
}

.voice-orb::after {
  content: "";
  position: absolute;
  inset: 0;
  border-radius: 9999px;
  border: 2px solid rgba(99, 102, 241, 0.7);
  animation: orbPulse 1.4s ease-out infinite;
}

@keyframes orbPulse {
  0% { opacity: 1; transform: scale(1); }
  70% { opacity: 0; transform: scale(2.8); }
  100% { opacity: 0; transform: scale(3); }
}

.voice-wave {
  display: flex;
  align-items: flex-end;
  gap: 3px;
  margin-left: 10px;
  height: 20px;
}

.wave-bar {
  width: 3px;
  height: 6px;
  background: linear-gradient(180deg, #818cf8, #4f46e5);
  border-radius: 4px;
  animation: waveBounce 0.8s infinite ease-in-out;
  filter: drop-shadow(0 0 6px rgba(99, 102, 241, 0.6));
}

.wave-bar:nth-child(odd) { animation-delay: 0.1s; }
.wave-bar:nth-child(3n) { animation-delay: 0.2s; }
.wave-bar:nth-child(4n) { animation-delay: 0.25s; }

@keyframes waveBounce {
  0% { height: 6px; }
  50% { height: 20px; }
  100% { height: 6px; }
}
</style>