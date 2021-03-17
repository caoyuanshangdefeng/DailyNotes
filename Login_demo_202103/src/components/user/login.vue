<template>
  <div class="user_management_basic_page">
      	<form name="form1" action="" method="post" >
     		 <h1>业务系统</h1>
            <input class=input_1  type=text size=15  v-model="username"  placeholder=用户名  ><br />
						<span >{{error.name}}</span><br />
          	<input class=input_1  type=text size=15 v-model="password" placeholder=密码  ><br />
						<span >{{error.pwd}}</span><br />
            <input class=input_3 type="button" @click="login()" value="登录" />
            <input class=input_3 type="button"  @click="register()" value="注册" /> 
       </form>
      </div>
</template>

<script>
export default {
	name:"loginDemo",
	data(){
		return{
			username:'',
			password:'',
			error : {
              name: '',
              pwd : ''
          }
		}
	},
  methods:{
		login() {
          if(!this.username && !this.password) {
							this.error.name = '请输入姓名'
							this.error.pwd = '请输入密码'
              return false
					}
					
					},
    register(){
        this.$router.replace('/register/');
    }
  }
  

}
</script>

<style scoped>
/* .login_page{
  float:left;
} */


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
form{
	position:absolute;
	left:50%;
	top:50%;
	margin-left:-300px;
	margin-top:-220px;
	width:480px;
	height:380px;
	background:url("../../assets/images/b.png") no-repeat;
	/* background:url("../../../static/images/bg_all.jpg") no-repeat;  */
	border-radius:25px;
	color:#fff;
	text-align:center;
	padding:65px;
	/*box-shadow: 0px 0px 15px #0005;*/
}
.input_1{
	outline:none;
	margin-top:10px;
	border:0;
	width:300px;
	height:50px;
	border-radius:15px;
	padding-left:15px;
	font-size:18px;
	color:#999;
}
.input_2{
	margin:20px 0px;
	border:0;
	background:#fff;
}
h1{
	color:#fff;
}
	/*单选*/
.radio_box{ display:inline-block; position:relative;margin:20px 5px;}
.radio_box label{ width:15px; height:15px; position:absolute; top:0; left:0; border:2px solid #3A5367; border-radius:50%; background:#fff; cursor:pointer;}
.radio_box input:checked + label:after{ content:''; width:9px; height:9px; position:absolute; top:3px; left:3px; background:#3A5367; border-radius:50%;}
.check_box em{ margin:0 0 0 5px;}

.input_3{
	outline: none;
	width:50px;
	height:30px;
  border:0;
  
	padding:5px 7px;
	background:#fff;
	border-radius:20px;
	margin:20px 10px;
}
</style>