<script setup>
import {onMounted, ref} from "vue";
import {api} from "./api";

const plans = ref([]);      //stores the API response for test plans
const loading = ref(false); //displays UI feedback while the request is in progress
const error = ref("")       //shows a message if API call fails

async function loadPlans() {
  loading.value = true;
  error.value = "";

  try{
    const response = await api.get("/testplans/");
    plans.value = response.data;
  } catch(err){
    error.value = err?.message || "Failed to load test plans.";
  } finally {
    loading.value = false;
  }
}

onMounted(loadPlans);   //runs once component appears in the browser
</script>

<template>
  <main style = "max-width: 900px; margin: 40px; padding: 0 16px; font-family: system-ui;">
    <h1>Flight Test Plans</h1>
    
    <p v-if="loading">Loading test plans...</p>
    <p v-else-if="error" style="color: crimson;">{{error}}</p>

    <ul v-else style="padding-left: 20px;">
      <li v-for="plan in plans" :key = "plan.id" style="margin-bottom: 12px;">
        <strong>{{plan.name}}</strong>
        <span style="margin-left: 8px;">
          - {{plan.status_display}} ({{plan.status}})
        </span>
      </li>
    </ul>
  </main>  
</template>