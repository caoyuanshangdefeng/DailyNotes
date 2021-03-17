import Vue from 'vue'
import Router from 'vue-router'

// import loginDemo from "@/components/user/login"
// import registerDemo from "@/components/user/register"
Vue.use(Router)
const Login = () => import ('@/components/user/login')
const Register = () => import ('@/components/user/register')

export default new Router({
  mode: 'history',
  routes: [
    {
      path:'',
      //redirect重定向
      redirect:'/loginDemo/'
     },
    {
      path: '/loginDemo/',
      component: Login
    },

    {
      path: '/register/',
      component: Register
  }]


  
})
