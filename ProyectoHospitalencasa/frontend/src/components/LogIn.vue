<template>

    <div class="logIn_user">
        <div class="container_logIn_user">
            <h2>Iniciar sesión</h2>

            <form   v-on:submit.prevent="processLogInUser" >
                <input type="text" v-model="user.username" placeholder="Usuario">
                <br>
                <input type="password" v-model="user.password" placeholder="Contraseña">
                <br>
                <button type="submit" v-on="processLogInUser&&verificarUsuario">Ingresar </button>
            </form>
        </div>

    </div>

</template>

<script>
import axios from 'axios';

export default {
    name: "LogIn",
    
    data: function(){
        return {
            apiData:[],
            user: {
                username:"",
                password:""
            }
        }
    },

    methods: {
        
        verificarUsuario(){
            localStorage.setItem("isAuth", true);
            
        },
        processLogInUser: function(){
            axios.get("https://team-javi-g33.herokuapp.com/usuarioDetalles/",)
                .then((result) => {
                    this.apiData = result.data
                    
                })
                
        },
    }
}
</script>

<style>
    
    .logIn_user{
        margin: 0;
        padding: 0%;
        height: 100%;
        width: 100%;
    
        display: flex;
        justify-content: center;
        align-items: center;
    }

    .container_logIn_user {
        border: 3px solid #2231a3;
        border-radius: 10px;
        width: 25%;
        height: 60%;
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
    }

    .logIn_user h2{
        color: #2231a3;
    }

    .logIn_user form{
        width: 70%;
    }

    .logIn_user input{
        height: 40px;
        width: 100%;

        box-sizing: border-box;
        padding: 10px 20px;
        margin: 18px auto;

        border: 1px solid #2231a3;
        border-radius: 2px;
        color: rgb(44, 43, 43);
    }
    .logIn_user input:focus{
        outline: none;
        border: 2.4px solid #2231a3;
        border-radius: 2px;

    }

    .logIn_user button{
        width: 100%;
        height: 40px;
        font-weight: bolder;
        color: #ffffff;
        background: #5460c6;
        border: 1px solid #E5E7E9;

        border-radius: 5px;
        padding: 10px 25px;
        
        margin: 18px auto;
    }

    .logIn_user button:hover{
        color: #5460c6;
        font-weight: bolder;
        background-color: #beb8b8;
        transition: 0.4s;
       
    }

</style>