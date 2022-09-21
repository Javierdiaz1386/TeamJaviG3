<template>
    <div class="container-home">
        <div class="texto">
            <img src="../../public/logo.png" alt="">
            <h1>Capri Health EPS</h1>
            <p>Hospitalización En Casa</p>
        </div>
        <div class="img">
            <img src="../../public/enfermera.jpg" alt="">
        </div>
    </div>
</template>
<script>
export default {
    name: "Home",
    data: function () {
        return {
            username: localStorage.getItem('username') || "none"
        }
    }
}
</script>
<style>
    .main-component{
        height: 90%;
    }
    .container-home{
        display: flex;
        align-items: center;
        width: 100%;
        height: 100%;
        justify-content: center;
    }
    .texto{
        display: flex;
        flex-direction: column;
        align-items: center;
    }
    .img{
        display: flex;
        flex-direction: column;
        justify-content: center;
        
        height: 691.99px;
        width: 400px;
    }
    .texto img{
        width: 400px;
        height: 400px;
    }
    .texto h1{
        color: #2231a3;
        font-weight: bold;
        font-size: 80px;
        margin-bottom: 12px;
    }
    .texto p{
        border: 1px solid #2231a3;
        padding-left: 40px;
        padding-right: 40px;
        font-size: 40px;
        border-radius: 30px;
    }
    .img img{
       z-index: 20;
    }
    #app{
        height: 100vh;
    }
</style>
