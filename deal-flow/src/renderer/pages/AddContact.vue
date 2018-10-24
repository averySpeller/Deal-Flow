<template>
  <div>
    <el-row>
      <el-col :span="6">
          Name: <el-input
                    v-model="name"
                    type="text"
                    clearable
                    placeholder="FistName LastName">
                </el-input>
      </el-col>
    </el-row>
    <el-row>
      <el-col :span="6">
          Email: <el-input
                    v-model="form.email"
                    type="text"
                    clearable
                    placeholder="username@domain.com">
                  </el-input>
      </el-col>
    </el-row>
    <el-row>
      <el-col :span="6">
          Phone1: <el-input
                    v-model="form.phone1"
                    type="text"
                    clearable>
                  </el-input>
      </el-col>
    </el-row>
    <el-row>
      <el-col :span="6">
          Phone2: <el-input
                    v-model="form.phone2"
                    type="text"
                    clearable>
                  </el-input>
      </el-col>
    </el-row>
    <el-row>
      <el-col :span="6">
          Website: <el-input
                    v-model="form.website"
                    type="text"
                    clearable>
                  </el-input>
      </el-col>
    </el-row>
    <el-row>
      <el-col :span="12">
          Notes: <el-input
                    v-model="form.notes"
                    type="textarea"
                    :autosize="{ minRows: 4, maxRows: 8}"
                    placeholder="Additional Notes" >
                  </el-input>
      </el-col>
    </el-row>

    <button @click="addContact()">Add contact!</button>
  </div>

</template>

<script>
import axios from 'axios';
export default {
  name: 'AddContact',
  data(){
    return{
      name: null,
      form: {
        first: null,
        last: null,
        email: null,
        phone1: null,
        phone2: null,
        website: null,
        first: null,
        last: null,
        notes: null
      }
    }
  },
  methods: {
    addContact(){
      var splitty = this.name.split(' ');
      this.form.first = splitty[0];
      this.form.last = splitty[1];

      // console.log(splitty);
      console.log(this.form);

      axios.post('http://24.138.161.30:5000/contacts',this.form).then(response => {
        console.log(response.data);
      })
      .catch(e => {
        this.errors.push(e)
        console.log(e);
        console.log('i died');
      })

    }

  }

}


</script>

<style scoped>

</style>
