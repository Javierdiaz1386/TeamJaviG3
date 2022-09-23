import axios from 'axios'

const getAPI = axios.create({
    baseURL:'https://team-javi-g33.herokuapp.com/',
    timeout: 10000,
})

export {getAPI}