import axios from  "axios"
import Vue from 'vue'
Vue.prototype.$http= axios
// promise
export function request(config){
  //1.创建axios实例
  const instance=axios.create({
    baseURL:"http://127.0.0.1:8000/api/v1",
    timeout:1000,
    
  })

  //2.axios的拦截器use()两个参数,是两个函数
  instance.interceptors.request.use(
    config=>{
    console.log(config,'拦截的是配置');
    // 拦截的是配置
    // a.比如config中的一些信息不符合服务器的要求
    //b.比如每次发送网路请求时,都希望在界面中显示一个请求的图标
    //c.某些网络请求(比如登录(携带token)),必须携带一些特殊信息
    return config
  },
  err=>{console.log(err);}

  );

  //2.2相应拦截
  instance.interceptors.response.use(res=>{
    console.log(res);
    return res
  },err=>{
    console.log(err);
  });

  //3.发送真正的网络请求
  // AxiosInstance传入config返回AxiosPromise
  return instance(config)
  
}

// promise
// export function request(config){
//   //1.创建axios实例
//   return new Promise((resolve,reject)=>{
//   const instance=axios.create({
//     baseURL:"http://123.207.32.32:8000",
//     timeout:5000,
    
//   })
//   //2.发送真正的网络请求
//   instance(config)
//   .then(
//     res=>{
//       // console.log(res);
//       resolve(res);
     
//     }).catch(err=>{
   
//     reject(err);
//   })

// })
// }


// config
// export function request(config){
//   //1.创建axios实例
//   const instance=axios.create({
//     baseURL:"http://123.207.32.32:8000",
//     timeout:5000,
    
//   })
//   //2.发送真正的网络请求
//   instance(config.baseConfig)
//   .then(
//     res=>{
//       // console.log(res);
//       config.success(res);
//     }).catch(err=>{
//     // console.log(err);
//     config.failure(err);
//   })

// }




// //success,failure函数
// export function request(config,success,failure){
//   //1.创建axios实例
//   const instance=axios.create({
//     baseURL:"http://123.207.32.32:8000",
//     timeout:5000,
    
//   })
//   //2.发送真正的网络请求
//   instance(config)
//   .then(
//     res=>{
//       // console.log(res);
//       success(res);
//     }).catch(err=>{
//     // console.log(err);
//     failure(err);
//   })

// }