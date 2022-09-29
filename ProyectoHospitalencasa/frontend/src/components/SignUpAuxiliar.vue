<template>

    <div class="signUp_user">
        <div class="container_signUp_user">
            <h2>Registro de Auxiliar</h2>

            <form v-on:submit.prevent="processSignUp">
                <select name="rol"  type="text" v-model="form.rol" placeholder="Rol">
                    <option value="Medico">Medico</option>
                    <option value="Auxiliar">Auxiliar</option>
                    </select>
                <br>
                <input  name="especialidad" v-model="form.especialidad" type="text"  placeholder="Especialidad">
                <br>
                <input name="username_id" v-model="form.username" type="text" placeholder="Username_id">
                <br>
                <button type="submit"  v-on:click="guardarInfo">Guardar</button>
            </form>
        </div>
    </div>
</template>

<script>
import axios from 'axios';
export default {
    name: "SignUp",
    data: function () {
        return {
            user: {
                username: "",
                password: "",
                name: "",
                email: "",
                account: {
                    lastChangeDate: (new Date()).toJSON().toString(),
                    balance: 0,
                    isActive: true
                }
            },
            form:{
                
                "rol": "",
                "especialidad": "",
                "username": ""
            }
        }
    },
    methods: {
        
        guardarInfo(){
            axios.post('https://team-javi-g33.herokuapp.com/crearPsalud/',this.form).then(data=>{
                // this.form.especialidad = ''
                // this.form.rol = ''
                // this.form.username = ''
                alert('Registro creado.')
            }).catch(err=>{
            console.log(err)
            console.log(this.form.rol)
                alert('Error al guardar')
            })
        }
    }
}
</script>

<style>
.signUp_user {
    margin: 0;
    padding: 0%;
    height: 100%;
    width: 100%;
    display: flex;
    justify-content: center;
    align-items: center;
}

.container_signUp_user {
    border: 3px solid #2231a3;
    border-radius: 10px;
    width: 25%;
    height: 85%;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
}

.signUp_user h2 {
    margin-top: 25px;
    margin-bottom: 10px;
    color: #2231a3;
}

.signUp_user form {
    width: 70%;
}

.signUp_user input {
    height: 30px;
    width: 100%;
    box-sizing: border-box;
    padding-left: 10px;
    margin: 5px 0;
    border: 1px solid #2231a3;
    color: rgb(44, 43, 43);
    
}
.signUp_user select {
    height: 30px;
    width: 100%;
    box-sizing: border-box;
    padding-left: 10px;
    margin: 5px 0;
    border: 1px solid #2231a3;
}
.signUp_user input:focus{
        outline: none;
        border: 2.4px solid #2231a3;
        border-radius: 2px;

    }

.signUp_user button {
    width: 100%;
    height: 40px;
    padding: 10px 25px;
    margin: 5px 0 25px 0;
    color: #ffffff;
        background: #5460c6;
        border: 1px solid #E5E7E9;

        border-radius: 5px;
}

.signUp_user button:hover {

    color: #5460c6;
        font-weight: bolder;
        background-color: #beb8b8;
        transition: 0.4s;
       
}


</style>