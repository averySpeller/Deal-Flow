<template>
  <div>
    <el-row :gutter="50">
      <el-col :xs="0" :sm="1" :md="2" :lg="3" :xl="3"><div class="grid-content bg-purple"></div></el-col>
      <el-col :xs="12" :sm="11" :md="10" :lg="9" :xl="9">
        <ul>
          <el-row :gutter="15">
            <el-col :span="12">
              <strong class="uk-align-right">Valuation:</strong>
            </el-col>
            <el-col :span="12">
              {{organization.valuation}}
            </el-col>
          </el-row>
          <el-row :gutter="15">
            <el-col :span="12">
              <strong class="uk-align-right">Stock Symbol:</strong>
            </el-col>
            <el-col :span="12">
              {{organization.stock_symbol}}
            </el-col>
          </el-row>
          <el-row :gutter="15">
            <el-col :span="12">
              <strong class="uk-align-right">Revenue:</strong>
            </el-col>
            <el-col :span="12">
              {{organization.revenue}}
            </el-col>
          </el-row>
          <el-row :gutter="15">
            <el-col :span="12">
              <strong class="uk-align-right">Revenue Model:</strong>
            </el-col>
            <el-col :span="12">
              {{organization.revenue_model}}
            </el-col>
          </el-row>
          <!-- <li><p><strong>Address: </strong>{{organization.address.street}} "Street, "{{organization.address.suite}}", "{{organization.address.city}}", "{{organization.address.zipcode}}</p></li> -->
        </ul>
      </el-col>
      <el-col  :xs="12" :sm="11" :md="10" :lg="9" :xl="9">
        <el-row :gutter="15">
          <el-col :span="12">
            <strong class="uk-align-right">Status:</strong>
          </el-col>
          <el-col :span="12">
            {{organization.revenue_model}}
          </el-col>
        </el-row>
        <el-row :gutter="15">
          <el-col :span="12">
            <strong class="uk-align-right">Raise:</strong>
          </el-col>
          <el-col :span="12">
            {{organization.revenue_model}}
          </el-col>
        </el-row>
        <el-row :gutter="15">
          <el-col :span="12">
            <strong class="uk-align-right">Raise Type:</strong>
          </el-col>
          <el-col :span="12">
            {{organization.revenue_model}}
          </el-col>
        </el-row>
        <el-row :gutter="15">
          <el-col :span="12">
            <strong class="uk-align-right">Round:</strong>
          </el-col>
          <el-col :span="12">
            {{organization.revenue_model}}
          </el-col>
        </el-row>

      </el-col>
      <el-col :xs="0" :sm="1" :md="2" :lg="3" :xl="3"><div class="grid-content bg-purple"></div></el-col>
    </el-row>



    <el-row :gutter="50" type="flex" class="row-bg" justify="center">
      <el-col :span="12">
        Notes:
        <el-input
          v-model="organization.notes"
          type="textarea"
          :autosize="{ minRows: 4, maxRows: 8}"
          placeholder="Additional Notes" >
        </el-input>
      </el-col>
    </el-row>
  </div>
</template>

<script>
export default {
  name: 'DealOverview',
  props: ['organization']

}
</script>
<style scoped>
  .grid-content {
    min-height: 36px;
  }

</style>
