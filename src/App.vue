<template>
  <div id="nav">
    <!-- <router-link to="/">Home</router-link> |
    <router-link to="/about">About</router-link> -->
    <router-view />
  </div>
  
</template>

<style>
 * {
    box-sizing: border-box;
    margin: 0;
    padding: 10px;
  }

  body{
    font-family:Arial, Helvetica, sans-serif;
    line-height:1.4
  }

  .btn {
    display: inline-block;
    border: none;
    background: #555;
    color:#fff;
    padding: 7px 20px;
    cursor: pointer;
  }

  .btn:hover{
    background: #666;
  }
</style>
