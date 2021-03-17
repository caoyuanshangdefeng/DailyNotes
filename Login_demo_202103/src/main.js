import Vue from 'vue'
import App from './App'
import router from './router'

//导入axios模块
// import axios from "axios"
Vue.config.productionTip = false

/* eslint-disable no-new */
new Vue({
  el: '#app',
  router,
  render: h => h(App)
})

// 4.创建axios实例
// const instance1=axios.create({
//   baseURL:"http://123.207.32.32:8000",
//   timeout:5000,
// })

// instance1({
//   url:"/home/multidata",
//   methods:"get",
// }).then(res=>{
//   console.log(res);
// })

// const instance2=axios.create({
//   baseURL:"http://123.207.32.32:8000",
//   timeout:5000,
//   headers:{},

// })

//5.封装request模块

// import {request} from "./network/request";


// request({
//   url:'/home/multidata'
// },res=>{
//   console.log(res);
//   // this.result=res;
// },err=>{
//   console.log(err);
// })

//使用config
// request({
//   baseConfig:{
//     url:'/home/multidata',
//   },
//   success:function(res){

//   },
//   failure:function(err){

//   }
  
// })
//使用promise
// request({
//   url:'/home/multidata',
// }).then(
//   res=>{
//     console.log(res);
//   }
// ).catch(err=>{
//   console.log(err);
// })