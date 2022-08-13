<template>
    <div id="Container">
        <div id="Title">
            <h1>Great</h1>
            <h3>Enter your license key</h3>
        </div>
        <section id="content">
            <input type="text" id="LicenseKey" placeholder="License Key" v-model="LicenseKey" />

            <input type="text" id="DeviceID" placeholder="Device ID" v-model="DeviceID" />

            <input type="text" id="UsersName" placeholder="Your Name" v-model="UsersName" />
            <br />
            <button ref="NextPageButton" @click="NextPage()">Continue</button>
        </section>
    </div>
</template>
<style scoped>
#Container {
    text-align: center;
    padding: 32px 10% 0% 10%;
}

#Title {
    display: inline-block;
}

#Title h1 {
    font-size: 48px;
    margin: 0px;
    height: 100%;
    display: inline-block;
}

#content{
    margin-top: 7%;
}

#content input{
    display: inline-block;
    margin: 10px 0px;
    width: 75%;
}
#content button{
    margin-top: 20px;
}
</style>

<script>
export default {
    name: "LicenseKeyEntry",
    data() {
        return {
            LicenseKey: "",
            DeviceID: "",
            UsersName:""
        }
    },
    methods: {
        NextPage() {
            this.$router.push({ name: 'PinCreation', params: {UsersName: this.UsersName}})
        }
    }
}
</script>