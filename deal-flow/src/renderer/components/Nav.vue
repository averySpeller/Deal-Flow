<template>
  <div>
    <button class="uk-button uk-button-default uk-margin-small-right" type="button" uk-toggle="target: #offcanvas-push">Nav bar</button>
    <nav>

      <div id="offcanvas-push" uk-offcanvas="mode: push; overlay: true; flip: true">
        <div class="uk-offcanvas-bar">
            <button class="uk-offcanvas-close" type="button" uk-close></button>
            <li class="nav-item" v-for="routes in links">
              <router-link
                v-bind:key="routes.id"
                :to="`${routes.page}`">{{routes.text}}
              </router-link>
            </li>
        </div>
      </div>

<!--

      <li class="nav-item" v-for="routes in links">
        <router-link
          v-bind:key="routes.id"
          :to="`${routes.page}`">{{routes.text}}
        </router-link>
      </li> -->
    </nav>
  </div>
</template>
<script>
export default {
  name: 'Nav',
  data() {
    return {
      links: [
        {
          id: 0,
          text: 'Dashboard',
          page:'/Dahsboard'
        },
        {
          id: 1,
          text: 'Login',
          page:'/Login'
        },
        {
          id: 2,
          text: 'Contacts',
          page:'/Contacts'
        },
        {
          id: 3,
          text: 'Organizations',
          page:'/Organizations'
        },
        {
          id: 4,
          text: 'Deals',
          page:'/Deals'
        },
        {
          id: 5,
          text: 'Settings',
          page:'/Settings'
        },
        {
          id: 6,
          text: 'Contact Catalogue',
          page:'/ContactCatalogue'
        }
      ]
    }
  }
}
</script>
