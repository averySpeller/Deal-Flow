<template v-loading="loading" :data="contact">
  <div id ="Contact">
    <el-row>
      <el-col>
        <div class="uk-align-right uk-margin-right">
          <el-button @click="deleteContact()" type="danger">Delete</el-button>
          <router-link :to="{ name:'EditContact', params: { id: this.id }}">
            <el-button>Edit</el-button>
          </router-link>
        </div>
      </el-col>
    </el-row>

    <el-row type="flex" class="row-bg" justify="center">
      <el-col :span="8">
        <div class="uk-flex uk-flex-center uk-inline" style="border-radius: 50%">
          <img  class="avatar" v-bind:src ="contact.avatar">
        </div>

        <div class="title uk-flex uk-flex-center">
          <h1>{{contact.first}} {{contact.last}}</h1>
        </div>
        <div class="title uk-flex uk-flex-center">
          <h4>{{organization.name}}</h4>
          <!-- <router-link tag="h4" :to="{ name: 'Single-Organization', params: { id: contact.company }} ">
            {{contact.company}}
          </router-link> -->
        </div>
        <div class="title uk-flex uk-flex-center">
          <h4>{{this.myTest}}</h4>
        </div>

      </el-col>
    </el-row>
    <div class="uk-divider-vertical uk-margin">
      <hr class="uk-divider-icon"/>
      <el-row id="tagContainer" type="flex" class="row-bg" justify="center">
        <router-link tag="div" :to="{ name:'Tag', params: { id: tag.tag_id }}" v-for="tag in tags" class="tagContainer">
          <div>
            <el-tag
              :key="tag.tag_name"
              closable
              :disable-transitions="false"
              @close="deleteTag(tag)">
              #{{tag.tag_name}}
            </el-tag>
          </div>
        </router-link>



        <el-autocomplete
          class="inline-input input-new-tag"
          v-model="inputTag"
          v-if="inputVisible"
          size="small"
          ref="saveTagInput"
          :fetch-suggestions="searchTags"
          placeholder="Please Input"
          :trigger-on-focus="false"
          @select="handleTagConfirm"
          @keyup.enter.native="handleTagConfirm">
          <i
            uk-icon="icon: hashtag"
            class="el-input__icon"
            slot="prefix">
          </i>
          <template slot-scope="{ item }">
            <div>#{{ item.value }}</div>
          </template>
        </el-autocomplete>

        <el-button v-else class="button-new-tag" size="small" @click="showInput">+ New Tag</el-button>
      </el-row>

      <el-row :gutter="50">
        <el-col :xs="0" :sm="1" :md="2" :lg="3" :xl="3"><div class="grid-content bg-purple"></div></el-col>
        <el-col :xs="12" :sm="11" :md="10" :lg="9" :xl="9">
          <ul>
            <br><br>
            <li><p><strong>Email: </strong>{{contact.email}}</p></li>
            <li><p><strong>Phone: </strong>{{contact.phone1}}</p></li>
            <li><p><strong>Website: </strong>{{contact.website}}</p></li>
          </ul>
        </el-col>
        <el-col  :xs="12" :sm="11" :md="10" :lg="9" :xl="9">
          <div class="uk-flex uk-flex-center uk-inline" >
            <img src="static/imgs/sampleRadarChart.png" height="100" uk-img>
          </div>
          <br><br>
      </ul>
      <el-row type="flex" class="row-bg" justify="center">
        <el-col :span="20">
          Notes:
          <el-input
                      v-model="contact.notes"
                      type="textarea"
                      :autosize="{ minRows: 4, maxRows: 8}"
                      placeholder="Additional Notes" >
                    </el-input>
        </el-col>
      </el-row>


        </el-col>
        <el-col :xs="0" :sm="1" :md="2" :lg="3" :xl="3"><div class="grid-content bg-purple"></div></el-col>
      </el-row>
    </div>
    <br>
    <button @click="goBack()" class="uk-button uk-button-secondary uk-button-large uk-margin">GO BACK</button>

    <ul v-if="errors && errors.length">
      <li v-for="error of errors">
        {{error.message}}
      </li>
    </ul>
  </div>
</template>

<script>
import lib from '../lib'
export default {
  name: 'Single-Contact',
  data(){
    return {
      id: 0,
      myTest:"WRONG",
      contact: {},
      errors: [],
      organization: {},
      tags: [],
      tagSuggestions: [],
      inputVisible: false,
      inputTag: '',
      loading:true
    }
  },
  methods:{
    goBack () {
      window.history.length > 1
        ? this.$router.go(-1)
        : this.$router.push('/')
    },
    deleteContact(){

      lib.deleteRequest("/contacts/".concat(this.contact.contact_id), response => {
        window.history.length > 1
          ? this.$router.go(-1)
          : this.$router.push('/')

      })
    },

    //Dynamic tag control methods.
    deleteTag(tag) {
      lib.deleteRequest("/tagmappings/".concat(tag.tagmapping_id), response => {
        console.log(response.data);
        this.tags.splice(this.tags.indexOf(tag), 1);
      })
    },
    showInput() {
      this.inputVisible = true;
      this.$nextTick(_ => {
        this.$refs.saveTagInput.$refs.input.focus();
      });
    },

    //tag submit
    handleTagConfirm(item) {
      console.log("Handle input confirm");
      console.log(item);

      if (item instanceof KeyboardEvent){
        console.log("We have keyboard Event");
        //NEED to create New Tag
        let inputTag = this.inputTag;
        if (inputTag) {
          var newTag = {"tag_name": inputTag, "tag_color": "blue"}
          lib.postRequest("/tags", newTag, response => {
            console.log(response.data);

            this.tagSuggestions.push({"value": response.data.tag_name, "tag_id": response.data.tag_id, "tag_color": response.data.tag_color,})

            var newTagMapping = {"tag_id": response.data.tag_id, "contact_id": this.contact.contact_id}

            lib.postRequest("/tagmappings", newTagMapping, response => {
              console.log(response.data);
              this.tags.push({"tag_id": newTagMapping.tag_id, "tag_name": newTag.tag_name, "tag_color": newTag.tag_color, "tagmapping_id": response.data.tagmapping_id});
            })
          })
        }

        //get tag id back from tag
        //add Tag Mapping for tag
      }
      else {
        console.log("preExisting tag");
        console.log("Found a repeated Tag: ".concat(item.tag_id));

        var newTagMapping = {"tag_id": item.tag_id, "contact_id": this.contact.contact_id}
        console.log(newTagMapping);

        lib.postRequest("/tagmappings", newTagMapping, response => {
          console.log(response.data);
          this.tags.push({"tag_id": item.tag_id, "tag_name": item.value, "tag_color": item.tag_color, "tagmapping_id": response.data.tagmapping_id});
        })
      }
      //
      // let inputTag = this.inputTag;
      // if (inputTag) {
      //   this.tags.push(inputTag);
      // }
      this.inputVisible = false;
      this.inputTag = '';
    },

    // AutoComplete methods
    searchTags(queryString, cb) {
      var tagSuggestions = this.tagSuggestions;
      var results = queryString ? tagSuggestions.filter(this.createFilter(queryString)) : tagSuggestions;
      // call callback function to return suggestions
      console.log(results);
      cb(results);
    },
    createFilter(queryString) {
      return (tagSuggestion) => {
        return (tagSuggestion.value.toLowerCase().indexOf(queryString.toLowerCase()) === 0);
      };
    }
  },
  created() {
    this.id = this.$route.params.id;
    console.log("Getting contact info for contact #".concat(this.$route.params.id));

    lib.getRequest("/contacts/".concat(this.id), response => {
      this.contact = response.data;

      lib.getRequest("/organizations/".concat(this.contact.organization_id), response => {
        this.organization = response.data
      })

      lib.getRequest('/tagmappings?contact_id='.concat(this.contact.contact_id), response => {

        var tagIds = "";
        var tm = {};

        for (var i = 0; i < response.data.length; i++) {
          if (tagIds !== "") {
            tagIds = tagIds.concat(",");
          }
          tagIds = tagIds.concat(response.data[i].tag_id);
          tm[response.data[i].tag_id] = response.data[i].tagmapping_id;
        }
        console.log(tm);

        if (tagIds !== "") {
          lib.getRequest('/tags?tag_id='.concat(tagIds), response => {

            console.log(response.data);

            for (var i = 0; i < response.data.length; i++) {
              response.data[i].tagmapping_id = tm[response.data[i].tag_id]
            }
            console.log(response.data);
            this.tags = response.data;
          })
        }
      })

      lib.getRequest('/tags', response => {

        console.log(response.data);

        var myTagSuggestions = []
        for (var i = 0; i < response.data.length; i++) {
          myTagSuggestions.push({"value": response.data[i].tag_name, "tag_id": response.data[i].tag_id, "tag_color": response.data[i].tag_color,})
        }

        this.tagSuggestions = myTagSuggestions;

      })
      this.loading = false;
    })

    if (typeof(Storage) !== "undefined") {
      // Store
      // Retrieve
      this.myTest = localStorage.getItem("testMe");
    } else {
      this.myTest = "Sorry, your browser does not support Web Storage...";
    }

  }
}
</script>
<style scoped>

  #title{
    text-align: center;
    margin: 0 auto;
  }
  img .avatar{
    margin: 0 auto;
      border-radius: 50%;
      width: 350px;
      height: 350px;
  }
  .grid-content {
    min-height: 36px;
  }

  .tagContainer:first-child {
    margin-top: 0 !important;
    margin-left: 0 !important;
  }
  .tagContainer{
    margin-left: 10px;
  }
  .button-new-tag {
    margin-left: 10px;
    height: 32px;
    line-height: 30px;
    padding-top: 0;
    padding-bottom: 0;
  }
  .input-new-tag {
    width: 150px;
    margin-left: 10px;
  }

</style>
