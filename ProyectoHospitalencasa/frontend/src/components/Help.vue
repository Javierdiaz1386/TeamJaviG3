<template>

    <div class="logIn_user">
        <div class="container_logIn_user">
            <h2>Sala de Ayuda</h2>

            <form   v-on:submit.prevent="processLogInUser" >
                <input type="text"  placeholder="Nombre completo">
                <br>
                <input type="email"  placeholder="Correo">
                <br>
                <textarea  name="" id="" cols="30" placeholder="Deje su comentario..." rows="10"></textarea>
              
                <button type="submit">Enviar </button>
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
            user: {
                username:"",
                password:""
            }
        }
    },

    methods: {
        processLogInUser: function(){
            axios.post(
                "https://team-javi-g33.herokuapp.com/login/",
                this.user,
                {headers: {}}
                )
                .then((result) => {
                    let dataLogIn = {
                        username: this.user.username,
                        token_access: result.data.access,
                        token_refresh: result.data.refresh,
                    }
    
                    this.$emit('completedLogIn', dataLogIn)
                })
                .catch((error) => {
    
                    if (error.response.status == "401")
                        alert("ERROR 401: Credenciales Incorrectas.");
                });
        }
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
        height: 80%;
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
    .logIn_user textarea{
        resize: none;
        height: 80px;
        width: 100%;

        box-sizing: border-box;
        padding: 10px 20px;
        margin: 18px auto;

        border: 1px solid #2231a3;
        border-radius: 2px;
        color: rgb(44, 43, 43);
    }
    .logIn_user textarea:focus{
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