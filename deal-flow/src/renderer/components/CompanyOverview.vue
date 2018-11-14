<template>
  <el-row :gutter="50">
    <el-col :xs="0" :sm="1" :md="2" :lg="3" :xl="3"><div class="grid-content bg-purple"></div></el-col>
    <el-col :xs="12" :sm="11" :md="10" :lg="9" :xl="9">
        <p><strong>Comapany Vision: </strong> "{{organization.vision}}"</p>
        <p><strong>Website: </strong>{{organization.website}}</p>
        <p><strong>City: </strong>{{organization.city}}</p>
        <p><strong>Country: </strong>{{organization.country}}</p>
        <p><strong>Address: </strong>{{organization.line1}}</p>
        <p v-if="organization.line2"><strong>Address 2: </strong>{{organization.line2}}</p>
        <p><strong>Phone: </strong>{{organization.phone1}}</p>
        <p v-if="organization.phone2"><strong>Phone 2: </strong>{{organization.phone2}}</p>
        <p><strong>Website: </strong>{{organization.website}}</p>

      <p><strong>Contacts: </strong></p>
      <ol>
        <li v-for="contact in contacts">
          <router-link :to="{ name: 'Single-Contact', params: { id: contact.contact_id} }">
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
      <el-row type="flex" class="row-bg" justify="center">
        <el-col :span="20">
          Notes:
          <el-input
            v-model="organization.notes"
            type="textarea"
            :autosize="{ minRows: 4, maxRows: 8}"
            placeholder="Additional Notes" >
          </el-input>
        </el-col>
      </el-row>

    </el-col>
    <el-col :xs="0" :sm="1" :md="2" :lg="3" :xl="3"><div class="grid-content bg-purple"></div></el-col>
  </el-row>
</template>

<script>
export default {
  name: "CompanyOverview",
  props: ['organization', 'contacts']
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
