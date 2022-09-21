<template>
  <div id="app" class="app">
    <div class="header">
      <header>
        <nav class="container-nav">
          <h2>Capri Health EPS</h2>
            <ul class="ul-nav">
                <li><button v-if="!is_auth" v-on:click="loadHome"> Inicio </button></li>
                <li><button v-if="!is_auth" v-on:click="loadLogIn"> Iniciar Sesión </button></li>
                <li><button v-if="!is_auth" v-on:click="loadSignUp"> Registrarse </button></li>
                <li><button v-if="!is_auth" v-on:click="loadHelp"> Ayuda </button></li>
            </ul>
        </nav>
      </header>
    </div>

    <div class="main-component">
      <div class="main-component">
        <router-view v-on:completedLogIn="completedLogIn" v-on:completedSignUp="completedSignUp" v-on:logOut="logOut">
        </router-view>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'App',

  data: function () {
    return {
      is_auth: false
    }
  },

  components: {
  },

  methods: {
    verifyAuth: function () {
      this.is_auth = localStorage.getItem("isAuth") || false;
      if (this.is_auth == false)
        this.$router.push({ name: "home" });
      else
        this.$router.push({ name: "logIn" });
    },

    loadLogIn: function () {
      this.$router.push({ name: "logIn" })
    },

    loadSignUp: function () {
      this.$router.push({ name: "signUp" })
    },

    loadHome: function () {
      this.$router.push({ name: "home" });
    },

    loadHelp: function(){
      this.$router.push({ name: "help" });
    },

    logOut: function () {
      localStorage.clear();
      alert("Sesión Cerrada");
      this.verifyAuth();
    },

    loadAccount: function () {
      this.$router.push({ name: "account" });
    },

    completedLogIn: function (data) {
      localStorage.setItem("isAuth", true);
      localStorage.setItem("username", data.username);
      localStorage.setItem("token_access", data.token_access);
      localStorage.setItem("token_refresh", data.token_refresh);
      alert("Autenticación Exitosa");
      this.verifyAuth();
    },

    completedSignUp: function (data) {
      alert("Registro Exitoso");
      this.completedLogIn(data);
    },
  },

  created: function () {
    this.verifyAuth()
  }
}
</script>

<style>
  *{
    box-sizing: border-box;
    padding: 0;
    margin: 0;
  }
  header{
    
    background-color: #5460c6;
    display: flex;
    align-items: center;
    width: 100%;
  }
  .container-nav{
    display: flex;
    align-items: center;
    width: 100%;
  }
  .ul-nav{
    z-index: 10;
    display: flex;
    align-items: center;
    width: 70vw;
    justify-content: flex-end;
    list-style: none;
  }
  .container-nav h2 {
    color: white;
    width: 30vw;
    margin: 12px;
  }
  .ul-nav li {
    margin: 12px;
  }
  li button{
    border: none;
    font-size: 15px;
    background-color: transparent;
    color: white;
    
  }
  li button:hover{
    cursor: pointer;
    color: #beb8b8;

  }
</style>