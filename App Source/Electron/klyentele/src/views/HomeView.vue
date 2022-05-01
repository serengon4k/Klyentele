<template>
  <div class="home">
    <img alt="Vue logo" src="../assets/AppLogo/LogoUpClose.png">
  </div>
</template>
<script>
//let fs = require('fs')
// @ is an alias to /src

export default {
  name: 'HomeView',
  components: {
    
  },
  mounted(){
    const Test = true
     if(Test == true){
       this.$router.push({name: 'SetupStart'})
     }
  }
}
</script>
