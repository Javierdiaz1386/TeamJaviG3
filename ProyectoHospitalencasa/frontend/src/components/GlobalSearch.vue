<template>
    <div class="container-global-search">
        <form action="">
            <label for="">
                <h2>Pacientes Registrados</h2>

            </label>




        </form>
        <table>

            <tr>
                <th><strong>ID</strong></th>
                <th><strong>Medico</strong></th>
                <th><strong>Usuario</strong></th>
                <th><strong>Fecha de nacimiento</strong></th>
                <th><strong>Dirección</strong></th>
                <th><strong>Ciudad</strong></th>
            </tr>




            <tr v-for="paciente in apiData">
                <td><strong>{{paciente.id}}</strong></td>
                <td><strong></strong>{{paciente.id_psalud}}</td>
                <td><strong></strong>{{paciente.username}}</td>
                <td><strong></strong>{{paciente.fecha_nacimiento}}</td>
                <td><strong></strong>{{paciente.direccion}}</td>
                <td><strong>{{paciente.ciudad}}</strong></td>
           
            </tr>


        </table>
    </div>
</template>
<script>
import axios from 'axios';
import { getAPI } from '@/axios-api';



export default {
    name: "GlobalSearch",
    data: function () {
        return {
            apiData: [],
            
        }

    },
    created() {
        getAPI.get('pacienteDetalles/').then(response => {
            console.log('post api reciviendo data')
            this.apiData = response.data
        }).catch(err => {
            console.log(err)
        })
        

    }
}





</script>
<style>
.container-global-search {
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
}

.container-global-search select {
    height: 40px;
    width: 20%;
    font-size: 15px;
    box-sizing: border-box;
    padding: 10px 20px;
    margin: 18px auto;

    border: 1px solid #2231a3;
    border-radius: 2px;
    color: rgb(44, 43, 43);
}

.container-global-search select:focus {
    outline: none;
    border: 2.4px solid #2231a3;
    border-radius: 2px;

}

.container-global-search input {
    height: 40px;
    width: 20%;

    box-sizing: border-box;
    padding: 10px 20px;
    margin: 18px auto;
    margin-left: 12px;

    border: 1px solid #2231a3;
    border-radius: 2px;
    color: rgb(44, 43, 43);
}

.container-global-search input:focus {
    outline: none;
    border: 2.4px solid #2231a3;
    border-radius: 2px;

}

.container-global-search button {

    width: 12%;
    height: 40px;
    padding: 10px 25px;
    margin: 5px 0 25px 0;
    margin-left: 12px;
    color: #ffffff;
    background: #5460c6;
    border: 1px solid #E5E7E9;

    border-radius: 5px;
}

.container-global-search button:hover {

    color: #5460c6;
    font-weight: bolder;
    background-color: #beb8b8;
    transition: 0.4s;

}

.container-global-search h2 {
    margin-top: 70px;
    color: #2231a3;
}

table {
    
    justify-content: center;
    align-items: flex-start;
    height: 100%;
    padding-top: 30px;
    padding-right: 30px;
    padding-left: 30px;
}


table th {
    border: 3px solid #2231a3;
    width: 200px;
    height: 30px;
}

table td {
    text-align: center;
    border: 3px solid #6974da;
    max-width: 200px;
    max-height: 30px;
    padding: 12px;
}
</style>