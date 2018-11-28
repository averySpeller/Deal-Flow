<template>
  <el-autocomplete v-model="state4" :fetch-suggestions="querySearchAsync" placeholder="Please input" @select="handleSelect"></el-autocomplete>

</template>
<script>
export default {
  name: 'SearchBar',
  data() {
    return {
      searchcriteria:"",
    }
  }
}
</script>
