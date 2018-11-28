<template>
    <div class="">
        <el-row :gutter="50">
          <el-col :xs="0" :sm="1" :md="2" :lg="3" :xl="3">
              <div class="grid-content bg-purple"></div>
          </el-col>

          <el-col :xs="24" :sm="24" :md="7" :lg="7" :xl="7">
              <em>Vision: </em>
              <blockquote style="margin-top:0.05em;">
                  {{organization.vision}}
              </blockquote>
              <p v-if="organization.line1||organization.city||organization.country">
                  <em>Address: </em> <br>
                  <span>{{organization.line1}}</span> <br>
                  <span v-if="organization.line2">{{organization.line2}}<br></span>
                  <span v-if="organization.city">{{organization.city}},</span>
                  <span v-if="organization.state">{{organization.state}},</span>
                  <span v-if="organization.country">{{organization.country}}.</span>
              </p>
              <p><em>Website: </em><a>{{organization.website}}</a></p>
              <p v-if="organization.phone1"><em>Phone: </em>{{organization.phone1}}</p>
              <p v-if="organization.phone2"><em>Phone 2: </em>{{organization.phone2}}</p>
            <em>Contacts: </em>
            <ol>
              <li v-for="contact in contacts">
                <router-link :to="{ name: 'Single-Contact', params: { id: contact.contact_id} }">
                  {{contact.first}} {{contact.last}} <span v-if="contact.title">({{contact.title}})</span>
                </router-link>
              </li>
            </ol>
          </el-col>
          <el-col  :xs="24" :sm="24" :md="12" :lg="12" :xl="12">
              <div v-if="organization.line1||organization.city||organization.country">
                  <iframe height="295" width="90%" :src="this.mapString()" frameborder="0" scrolling="no" marginheight="0" marginwidth="0"></iframe>
              </div>
          </el-col>
          <el-col :xs="0" :sm="1" :md="2" :lg="3" :xl="3"><div class="grid-content bg-purple"></div></el-col>

        </el-row>
        <el-row :gutter="50" type="flex" class="row-bg" justify="center">
              <el-col :span="15">
                <em>Notes:</em>
                <Notes v-model="organization.notes"></Notes>
              </el-col>
        </el-row>
    </div>


</template>

<script>
import Notes from '../components/Notes'

export default {
  name: "CompanyOverview",
  props: ['organization', 'contacts'],
  components: {
      'Notes': Notes
  },
  methods: {
      mapString() {
          return "https://maps.google.com/maps?q="+ this.organization.line1.concat('%20').concat(this.organization.city).concat('%20').concat(this.organization.country) +"&t=&z=13&ie=UTF8&iwloc=&output=embed"
      }
  }
}
</script>

<style>
  img {
    margin: 0 auto;
      border-radius: 15%;
      height:250px;
      width:250px;
  }
  .grid-content {
    min-height: 36px;
  }
</style>
