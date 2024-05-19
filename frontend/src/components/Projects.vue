<template>
  <table>
    <tr>
      <th>Project Name</th>
      <th>Start Date</th>
      <th>Estimated Completion Date</th>
      <th>Current Status</th>
    </tr>
    <tr v-for="project in projects">
      <Project :project="project"/>
    </tr>
  </table>
</template>

<script>
import Project from "./Project.vue";
import axios from "axios"

export default {
  components: {Project},
  data() {
    return {
      projects: [],
    }
  },
  beforeMount() {
    axios.get(
        "rows"
    ).then(
        res => {
          this.projects = res.data
        }
    )
  }
}

</script>

<style scoped>
  table {
    border-collapse: collapse;
    width: 100%;
  }

  tr:nth-child(even) {
    background-color: #f2f2f2;
  }

  th {
    background-color: #eee;
    font-weight: bold;
    padding: 10px;
    border: 1px solid #ddd;
    text-align: left;
  }
</style>