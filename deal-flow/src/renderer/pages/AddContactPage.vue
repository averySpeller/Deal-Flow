<template>

<div class="wrapper">
  <div class="title uk-flex uk-flex-center">
    <h1 v-if="editFlag">Edit Contact</h1>
    <h1 v-else>Add Contact</h1>
  </div>
  <AddContact ></AddContact>
</div>
</template>
<script>
import AddContact from './AddContact';

export default {
  name: 'AddContactPage',
  components:{
        'AddContact': AddContact,
  },
  data() {
    return{
      editFlag: false,
    }
  },
  mounted(){
    this.$emit('backButton', true);

    console.log("EDIT DEAL:");
    console.log(this.$route.params.id);
    if (this.$route.params.id) {
      this.editFlag = true
    }
  }
}

</script>
