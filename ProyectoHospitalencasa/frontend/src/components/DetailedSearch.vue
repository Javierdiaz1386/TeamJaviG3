<template>
    <div class="container">
        <form action="">
            <label for="">
                <h2>Tipo consulta:</h2>
                <select name="" id="">
                    <option value="Detallada" selected>Detallada</option>

                    <option value="Global">Global</option>

                </select>
                <input id="index" type="number">
                <button type="submit">Consultar</button>
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



                <tr>
                    <td><strong></strong></td>
                    <td><strong></strong></td>
                    <td><strong></strong></td>
                    <td><strong></strong></td>
                    <td><strong></strong></td>
            <td><strong></strong></td>    
                </tr>
            </table>
    </div>
</template>
<script>
export default {
    name: "DetailedSearch",
    data: function () {
        return {
            username: localStorage.getItem('username') || "none"
        }
    }
}





</script>
<style>
.container {
    margin-top: 60px;
    margin-left: 60px;
}

.container select {
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

.container select:focus {
    outline: none;
    border: 2.4px solid #2231a3;
    border-radius: 2px;

}

.container input {
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

.container input:focus {
    outline: none;
    border: 2.4px solid #2231a3;
    border-radius: 2px;

}

.container button {

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

.container button:hover {

    color: #5460c6;
    font-weight: bolder;
    background-color: #beb8b8;
    transition: 0.4s;

}

.container h2 {
    color: #2231a3;
}
table{
    display: flex;
    justify-content: center;
    align-items: flex-start;
    height: 100%;
    padding-top: 30px;
    padding-right: 30px;
    padding-left: 30px;
}


table th{
    border: 3px solid  #2231a3;
    width: 200px;
    height: 30px;
}

table td{
    border: 3px solid #6974da;
    width: 200px;
    height: 30px;
}
</style>