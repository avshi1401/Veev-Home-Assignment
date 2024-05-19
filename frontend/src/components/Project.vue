<template>
  <td>{{project.project_name}}</td>
  <td>{{project.start_date}}</td>
  <td>{{project.estimated_completion_date}}</td>
  <td>{{project.current_status}}</td>
</template>

<script>
  export default {
    props: ["project"],
  }
</script>

<style scoped>
  td {
    padding: 10px;
    border: 1px solid #ddd;
    text-align: left;
  }
</style>