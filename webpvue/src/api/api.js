import axios from 'axios';
let base = '/api';
export const upload = params =>{return axios.post(`${base}/upload`,JSON.stringify(params),{headers:{'Content-Type': 'application/json'}}); };
export const getNavList = params =>{return axios.post(`${base}/getNavList`,JSON.stringify(params),{headers:{'Content-Type': 'application/json'}}); };
export const delNav = params =>{return axios.post(`${base}/delNav`,JSON.stringify(params),{headers:{'Content-Type': 'application/json'}}); };
export const editNav = params =>{return axios.post(`${base}/editNav`,JSON.stringify(params),{headers:{'Content-Type': 'application/json'}}); };
export const collectNav = params =>{return axios.post(`${base}/collectNav`,JSON.stringify(params),{headers:{'Content-Type': 'application/json'}}); };
export const getNavInfo = params =>{return axios.post(`${base}/getNavInfo`,JSON.stringify(params),{headers:{'Content-Type': 'application/json'}}); };
// export const acticleList = params => { return axios.get(`${base}/acticle/list`, { params: params }); };