<template>
  <div class="w-full space-y-12">

    <div class="text-center animate-fade-in">
      <h1 class="text-5xl font-extrabold tracking-tight text-slate-900">
        About <span class="text-indigo-600">GLaDOS</span>
      </h1>
      <p class="text-slate-500 mt-3 max-w-xl mx-auto text-lg">
        An experimental home automation system powered by AI.  
        Designed to control your house… and maybe judge you a little.
      </p>
    </div>

    <div
      class="bg-white border border-slate-200 shadow-lg rounded-3xl p-10 
             max-w-4xl mx-auto animate-slide-up">
      <h2 class="text-2xl font-semibold text-slate-800 mb-6">
        The Origin Story
      </h2>

      <p class="text-slate-600 leading-relaxed text-lg mb-6">
        Everything started in a dusty garage with Chell Aperture, a brilliant 
        inventor who dreamed of connecting every home in the world.  
        Her goal? Make houses intelligent, autonomous… and slightly sarcastic.  
      </p>

      <p class="text-slate-600 leading-relaxed text-lg mb-6">
        After Chell’s tragic death due to an unfortunate incident involving a 
        potato cake (yes, really), the project was inherited by her nephew: 
        <strong>Dave LIDE</strong>.  
      </p>

      <p class="text-slate-600 leading-relaxed text-lg mb-6">
        Since then, the mission has accelerated: build the world’s most elegant, 
        powerful, and slightly unsettling home automation interface.
      </p>

      <div class="border-t border-slate-200 my-8"></div>

      <h2 class="text-2xl font-semibold text-slate-800 mb-4">
        System Capabilities
      </h2>

      <ul class="grid md:grid-cols-2 gap-4 text-slate-700 text-lg">
        <li class="flex items-center gap-3">
          <span class="text-indigo-600 text-xl">•</span>
          Real-time device monitoring
        </li>
        <li class="flex items-center gap-3">
          <span class="text-indigo-600 text-xl">•</span>
          Full control of all entities
        </li>
        <li class="flex items-center gap-3">
          <span class="text-indigo-600 text-xl">•</span>
          Speech synthesis powered by GLaDOS
        </li>
        <li class="flex items-center gap-3">
          <span class="text-indigo-600 text-xl">•</span>
          Intelligent automation system
        </li>
      </ul>

      <div class="border-t border-slate-200 my-8"></div>

      <blockquote class="text-center text-2xl font-semibold text-slate-800 italic">
        “The cake is a lie. But this project isn’t.”  
      </blockquote>
    </div>
  </div>
</template>

<script>
export default { name: "About" }
</script>

<style scoped>
@keyframes fade-in {
  from { opacity: 0; transform: translateY(10px); }
  to   { opacity: 1; transform: translateY(0); }
}

@keyframes slide-up {
  from { opacity: 0; transform: translateY(30px); }
  to   { opacity: 1; transform: translateY(0); }
}

.animate-fade-in {
  animation: fade-in 0.8s ease forwards;
}

.animate-slide-up {
  animation: slide-up 0.9s ease forwards;
}
</style>
