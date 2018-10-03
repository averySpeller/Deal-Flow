<template>
  <div>
    <h1>Contact Me</h1>
  <p>
    <ul>
      <li>Email: {{email}}</li>
      <li>Website: {{web}}</li>
    </ul>
  </p>
  </div>
</template>

<script>
export default {
  name: 'Contacts',
  data(){
    return {
      email: 'email@email.com',
      web: 'dealflow.com'
    }
  }
}
</script>
view raw
