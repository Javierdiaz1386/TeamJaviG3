<template>
  <div id="app" class="app">
    <div class="header">
      <header>
        <nav id="menu" class="container-nav">
          <h2>Capri Health EPS</h2>
         
          <!-- start nav -->
          <nav id="menu">
            <!-- start menu -->
            <ul>
              <li><a v-on:click="loadHome">Inicio</a></li>
              <li><a >Consulta</a>
                <!-- start menu desplegable -->
                <ul>
                  <li><a v-on:click="loadDetailedSearch">Detallada</a></li>
                  <li><a v-on:click="loadGlobalSearch">Global</a></li>
                </ul>
                <!-- end menu desplegable -->
              </li>
              <li><a v-on:click="loadLogIn">Iniciar Sesion</a></li>
              <li><a >Registrarse</a>
                <!-- start menu desplegable -->
                <ul>
                  <li><a v-on:click="loadSignUpMedico">Médico</a></li>
                  <li><a v-on:click="loadSignUpAuxiliar">Auxiliar</a></li>
                  <li><a v-on:click="loadSignUpPaciente">Paciente</a></li>
                  <li><a v-on:click="loadSignUpFamiliar">Familiar</a></li>
                </ul>
                <!-- end menu desplegable -->
              </li>
              <li><a v-on:click="loadHelp">Ayuda</a></li>
            </ul>
            <!-- end menu -->
          </nav>
          <!-- end nav -->
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

    loadSignUpMedico: function () {
      this.$router.push({ name: "signUpMedico" })
    },

    loadSignUpAuxiliar: function () {
      this.$router.push({ name: "signUpAuxiliar" })
    },

    loadSignUpPaciente: function () {
      this.$router.push({ name: "signUpPaciente" })
    },

    loadSignUpFamiliar: function () {
      this.$router.push({ name: "signUpFamiliar" })
    },


    loadHome: function () {
      this.$router.push({ name: "home" });
    },

    loadHelp: function () {
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
    loadGlobalSearch(){
            this.$router.push({ name: "GlobalSearch" })
        },
    loadDetailedSearch: function () {
      this.$router.push({ name: "DetailedSearch" });
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
* {
  box-sizing: border-box;
  padding: 0;
  margin: 0;
}

header {

  background-color: #5460c6;
  display: flex;
  align-items: center;
  width: 100%;
}

.container-nav {
  display: flex;
  align-items: center;
  width: 100%;
}

.ul-nav {
  z-index: 10;
  display: none;
  align-items: center;
  width: 70vw;
  justify-content: flex-end;
  list-style: none;
}

.container-nav h2 {
  color: white;
  width: 50vw;
  margin: 12px;
}

.ul-nav li {
  margin: 12px;
}

li button {
  border: none;
  font-size: 15px;
  background-color: transparent;
  color: white;

}

li button:hover {
  cursor: pointer;
  color: #beb8b8;

}

/* menu */

#menu ul {
  z-index: 10;
  display: flex;
  align-items: center;
  width: 50vw;
  justify-content: flex-end;
  list-style: none;
 margin:0;
 padding:0;
}

/* items del menu */

#menu ul li {
 background-color:#5460c6;
}

/* enlaces del menu */

#menu ul a {
 display:block;
 color:#fff;
 text-decoration:none;
 font-weight:400;
 font-size:15px;
 padding:10px;
 font-family:"HelveticaNeue", "Helvetica Neue", Helvetica, Arial, sans-serif;

 letter-spacing:1px;
}

/* items del menu */

#menu ul li {
 position:relative;
 float:left;
 margin:0;
 padding:0;
}

/* e*/

/* menu desplegable */

#menu ul ul {
 display:none;
 position:absolute;
 top:100%;
 left:0;
 background:#eee;
 padding:0;
}

/* items del menu desplegable */

#menu ul ul li {
 float:none;
 width:150px
}

/* enlaces de los items del menu desplegable */

#menu ul ul a {
 line-height:120%;
 padding:10px 15px;
}

/* items del menu desplegable al pasar el ratón */

#menu ul li:hover > ul {
 display:block;
}
a{
  cursor: pointer;
}
</style>