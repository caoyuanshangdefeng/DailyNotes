<template>
  <div id="app">
    <div id="tab-bar">
      <div class="tab-bar-item">首页</div>
      <div class="tab-bar-item">分类</div>
      <div class="tab-bar-item">购物车</div>
      <div class="tab-bar-item">我的</div>
    </div>
  </div>
</template>

<script>


export default {
  name: 'App',
  components: {
   
  }
}
</script>

<style>
  @import './assets/css/base.css';
  #tab-bar {
    display: flex;
     /*使用flex进行水平分布*/
     background-color: #f6f6f6;
     position:fixed;
     left: 0;
     right: 0;
     bottom: 0;
     box-shadow: 0 -2px 1px rgba(100,100,100,0.08);


  }
  .tab-bar-item{
    flex: 1;
    /* flex: 1 可以对item进行均分 */
    text-align: center;
    /* item进行居中 */
    height: 49px;
    /*  49px一般的tabbar高度*/
    
  }


</style>
