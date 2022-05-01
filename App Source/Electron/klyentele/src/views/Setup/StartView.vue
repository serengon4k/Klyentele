<template>
    <div id="Container">
        <img alt="Vue logo" src="../../assets/AppLogo/LogoUpClose.svg">
        <br>
        <div id="Introduction">
            <h1>Klyentele</h1>
            <p>by Azura4k</p>
        </div>
        <br>
        <button @click="NextPage()">Next</button>
        <br>
        <button @click="AboutPage()">About</button>
    </div>
</template>
<style scoped>
#Container{
    text-align: center;
    padding-top: 32px;
}
#Introduction{
    display: inline-block;
}
#Introduction p{
    text-align: left;
    width: 100%;
    height: auto;
    display: block;
    margin: 0%;
}
h1{
    font-size: 48px;
    margin-bottom: 0px;
}
img{
    width: 189px;
    height: 211px;
}
br{
    margin: 0;
    padding: 0;
    height: 0;
    border: none;
}
</style>
<script>
export default({
    name: 'SetupStart',
    methods: {
        NextPage(){
            console.log("Next Clicked")
            this.$router.push({name:'LicenseAgreement'})
        },
        AboutPage(){
            console.log("About Clicked")

        }

        }
})
</script>
