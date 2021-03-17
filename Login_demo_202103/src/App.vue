<template>
  <div id="app">
    <router-view></router-view>
  </div>
</template>
<script>
export default {
  name: 'App',
//axios学习
  // data:function(){
  //   return { result:'',}
  // },
  // created(){
    // axios({
    //   url:"http://123.207.32.32:8000/home/multidata",

    // }).then(res=>{
    //   // console.log(res);
    //   this.result=res;

    // })
    
  //   request({
  //     url:'/home/multidata',
  //   }).then(
  //     res=>{
  //       // console.log(res);
  //       this.result=res;
  //     }
  //   ).catch(err=>{
  //     console.log(err);
  //   })
  // }
}
</script>

<style>

/* #app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 0px;
 
} */
</style>
