<template>
  <div class="home-div">
    <h1 class="home-header">Projects Details</h1>
    <Projects/>
  </div>
</template>

<script setup>
import Projects from "./components/Projects.vue";
</script>

<style>
  .home-div {
    display: block;
  }

  .home-header {
    text-align: center;
    margin-bottom: 20px;
  }
</style>