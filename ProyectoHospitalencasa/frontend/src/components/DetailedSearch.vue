<template>
    <div class="container-detailed-search">
        <form action="">
            <label for="">
                <h2>Seleccione ID paciente:</h2>

                <input v-model="ids" id="index" type="number">
                
                    <input id='consul' v-on:click="loads" type="button" value="Consultar">
                

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



          
        </table>
    </div>
</template>
<script>
import { getAPI } from '@/axios-api';
export default {

    name: "DetailedSearch",
    data: function () {
        return {
            ids: '',
            apiData: [],
            username: localStorage.getItem('username') || "none"
        }
    },
    created() {
        getAPI.get('pacienteDetalles/').then(response => {
            console.log('post api reciviendo data')
            this.apiData = response.data
        }).catch(err => {
            console.log(err)
        })


    },
    methods:{
        loads(){
            this.$router.push("DetailedSearchIds/"+this.ids );
        }
    }
}





</script>
<style>
.container-detailed-search {
    margin-top: 60px;
    margin-left: 60px;
}





.container-detailed-search input {
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

.container-detailed-search input:focus {
    outline: none;
    border: 2.4px solid #2231a3;
    border-radius: 2px;

}

#consul {

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

#consul:hover {

    color: #5460c6;
    font-weight: bolder;
    background-color: #beb8b8;
    transition: 0.4s;

}

.container-detailed-search h2 {
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

#consul {
    cursor: pointer;
}
</style>