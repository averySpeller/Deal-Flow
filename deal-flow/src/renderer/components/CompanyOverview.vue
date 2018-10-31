<template>
  <el-row :gutter="50">
    <el-col :xs="0" :sm="1" :md="2" :lg="3" :xl="3"><div class="grid-content bg-purple"></div></el-col>
    <el-col :xs="12" :sm="11" :md="10" :lg="9" :xl="9">
      <ul>
        <p><strong>Comapany Vision: </strong> "{{organization.vision}}"</p>
        <br><br>
        <li><p><strong>Website: </strong>{{organization.website}}</p></li>
        <!-- <li><p><strong>Address: </strong>{{organization.address.street}} "Street, "{{organization.address.suite}}", "{{organization.address.city}}", "{{organization.address.zipcode}}</p></li> -->
      </ul>

      <p><strong>Contacts: </strong></p>
      <ol>
        <li v-for="contact in contacts">
          <router-link :to="{ name: 'Single-Contact', params: { contact_id: contact.contact_id} }">
            {{contact.first}}
          </router-link>
        </li>
      </ol>
    </el-col>
    <el-col  :xs="12" :sm="11" :md="10" :lg="9" :xl="9">
      <div class="uk-flex uk-flex-center uk-inline">
        <img src="static/imgs/sampleRadarChart.png" height="100" uk-img>
      </div>
      <br><br>
      <div class="uk-flex uk-flex-center uk-inline">
        <p>NOTES GO HERE</p>
      </div>

    </el-col>
    <el-col :xs="0" :sm="1" :md="2" :lg="3" :xl="3"><div class="grid-content bg-purple"></div></el-col>
  </el-row>
</template>

<script>
export default {
  props: ['organization', 'contacts']
}
</script>

<style>
.grid-content {
  min-height: 36px;
}
</style>
