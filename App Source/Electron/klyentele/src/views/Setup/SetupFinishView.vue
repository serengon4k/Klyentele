<template>
    <div id="Container">
        <section id="Title">
            <h1>All Done</h1>
            <p>Ok, We’re all set. Welcome (First Name), lets get started.</p>
        </section>
    <section id="Content">
        <img alt="Vue logo" src="../../assets/AppLogo/LogoUpClose.svg">
        <br>
        <button @click="NextPage()">Lets Go</button>

    </section>
    </div>
</template>
<style scoped>
#Container {
    text-align: center;
    padding-top: 7%;
}

#Introduction {
    display: inline-block;
}

#Introduction p {
    text-align: center;
    width: 100%;
    height: auto;
    display: block;
    margin: 0%;
}

h1 {
    font-size: 48px;
    margin-bottom: 0px;
}

img {
    width: 189px;
    height: 211px;
}

br {
    margin: 0;
    padding: 0;
    height: 0;
    border: none;
}
</style>
<script>
export default ({
    name: 'SetupFinish',
    methods: {
        NextPage() {
            console.log("Next Clicked")
            this.$router.push({ name: 'LicenseAgreement' })
        }
    }
})
</script>
