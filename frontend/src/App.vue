<template>
  <v-app id="inspire">
    <!-- <v-system-bar app>
      <v-spacer></v-spacer>
      <v-icon>mdi-wifi-off</v-icon>
      <v-icon>mdi-signal-off</v-icon>
      <v-icon>mdi-airplane</v-icon>
    </v-system-bar> -->

    <v-app-bar app hide-on-scroll dense flat>
      <v-app-bar-nav-icon
        @click="drawer = !drawer"
      ></v-app-bar-nav-icon>

      <v-toolbar-title @click="() => $router.name != 'Home' || $router.go({name: 'Home'})" style="cursor: pointer;">E Pustakalay</v-toolbar-title>
      <v-spacer></v-spacer>

      <v-btn
        icon
        @click="changeTheme"
      >
        <v-icon>mdi-theme-light-dark</v-icon>
      </v-btn>
      

      <v-menu left bottom>
        <template v-slot:activator="{ on, attrs }">
          <v-btn icon v-bind="attrs" v-on="on">
            <v-icon>mdi-dots-vertical</v-icon>
          </v-btn>
        </template>

        <v-list>
          <v-list-item
            v-for="n in 1"
            :key="n"
            @click="() => {}"
          >
            <v-list-item-title
              >View Books</v-list-item-title
            >
          </v-list-item>
        </v-list>
      </v-menu>
    </v-app-bar>

    <v-navigation-drawer v-model="drawer" fixed app temporary>
      <template v-slot:prepend>
        <v-list-item two-line>
          <v-list-item-avatar>
            <img
              :src="require('@/assets/Images/responsive.svg')"
            />
          </v-list-item-avatar>

          <v-list-item-content>
            <v-list-item-title
              >shyamkumar</v-list-item-title
            >
            <v-list-item-subtitle
              >admin</v-list-item-subtitle
            >
          </v-list-item-content>
        </v-list-item>
      </template>
      <v-divider></v-divider>
      <v-list nav dense>
        <v-list-item-group>
          <v-list-item :to="{name: 'Home'}">
            <v-list-item-icon>
              <v-icon>mdi-home</v-icon>
            </v-list-item-icon>
            <v-list-item-title>Home</v-list-item-title>
          </v-list-item>

          <v-list-item :to="{name: 'About'}">
            <v-list-item-icon>
              <v-icon>mdi-decagram</v-icon>
            </v-list-item-icon>
            <v-list-item-title>About us</v-list-item-title>
          </v-list-item>

          <v-list-item :to="{name: 'Terms'}">
            <v-list-item-icon>
              <v-icon>mdi-information</v-icon>
            </v-list-item-icon>
            <v-list-item-title>Terms</v-list-item-title>
          </v-list-item>

        </v-list-item-group>
      </v-list>
      <template v-slot:append>
        <div class="pa-2">
          <v-btn :to="{name: 'Login'}" block> Login url </v-btn>
        </div>
      </template>
    </v-navigation-drawer>

    <v-main>
      
    <v-alert
      :value="alert"
      color="pink"
      dark
      border="top"
      icon="mdi-home"
      transition="scale-transition"
    >
      Phasellus tempus. Fusce ac felis sit amet ligula pharetra condimentum. In dui magna, posuere eget, vestibulum et, tempor auctor, justo. Pellentesque posuere. Curabitur ligula sapien, tincidunt non, euismod vitae, posuere imperdiet, leo.

      Phasellus nec sem in justo pellentesque facilisis. Phasellus magna. Cras risus ipsum, faucibus ut, ullamcorper id, varius ac, leo. In hac habitasse platea dictumst. Praesent turpis.
    </v-alert>
      <router-view></router-view>
    </v-main>

    <v-footer absolute app>
        <v-row no-gutters justify="center">
          <v-col
          class="text-center py-4"
          cols="12"
          >
            <v-icon>mdi-copyright</v-icon> All right Reversed by — <strong>Shyamkumar Yadav</strong> {{ new Date().getFullYear() }} 
          </v-col>

        </v-row>
    </v-footer>
    
  </v-app>
</template>

<script>
// import { mapGetters } from 'vuex'
export default {
  name: 'App',
  data: () => ({
    drawer: false,
    name: 'shyamkumar yadav',
    alert: false
  }),
  created(){
    const theme = localStorage.getItem('elibrary-theme') === "true"
    this.$vuetify.theme.dark = theme
  },
  methods:{
    changeTheme(){
      localStorage.setItem('elibrary-theme', !this.$vuetify.theme.dark)
      this.$vuetify.theme.dark = !this.$vuetify.theme.dark
    }
  },
  computed:{
  }
};
</script>