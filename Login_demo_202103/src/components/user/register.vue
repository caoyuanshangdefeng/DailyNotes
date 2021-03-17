<template>
  <div>
    
    昵称<input type="text" v-model="username" placeholder="请输入用户名"><br/>
    密码<input type="password"  v-model="password" placeholder="请输入密码"><br/>
    邮箱<input type="text" size="30" v-model="uemail" placeholder="请输入邮箱"><br/>
    
    <input  type="button"  @click="register()" value="注册" /> 
  </div>
  

</template>

<script>

import {request} from "../../network/request";
export default {
  name:'register',
  data(){
    return {
      
        username:'',
        password:'',
        uemail:'',
       
    
      }
    
  },
  methods:{
   register(){
    //   var phones = /^(\+?0?86\-?)?1[345789]\d{9}$/
    //   if (!phones.test(this.phoneinput)){
    //     this.error.phonecont="请输入正确的值"
    //   }else{
    //   this.$router.replace('/loginDemo');
    // }
    request({
      url:'/register/',
      method:'post',
      data:{'username':this.username,'password':this.password,
      'uemail':this.uemail}
      }).then(
      res=>{
        console.log('444',res);
        if(res.status == 200){
          this.$router.replace('/loginDemo/');
        }

    
      }
    ).catch(err=>{
      console.log(err);
    })
    // this.$router.replace('/loginDemo');
    },

  
  }

}
</script>

<style>

</style>