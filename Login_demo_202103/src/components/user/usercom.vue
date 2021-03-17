<template>

  <div class="user_management_basic_page">
    <login-demo></login-demo>
    <!-- <register-demo></register-demo> -->
    
  </div>

</template>

<script>
import loginDemo from "./login"
import registerDemo from"./register"

export default {
name:"usercom",

components:{
  loginDemo,
  registerDemo,
},
// data(){
//     return{
//       current:'loginDemo'
//     }
//   },
// methods:{
//   cur(s){
    
//     this.current=s
//   }

// }
}
</script>

<style scoped>
.user_management_basic_page{
  position: absolute;
    height: 100%;
    width:100%;
		margin:0px;
		padding:0px;
    background:url("../../assets/images/bg_all.jpg") no-repeat;
    /* background:red; */
		background-size: 100% ;
		
  }
  
</style>