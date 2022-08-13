<template>
    <div id="Container">
        <div id="Title">
            <h1>Excellent {{ UsersName }}</h1>
            <h3>Lets set your pin up</h3>
        </div>
        <section id="content">
            <input inputmode="numeric" type="number" id="Pin"
                placeholder="Enter New Pin" v-model="Pin"/>

            <input inputmode="numeric" type="number" id="ConfirmPin"
                placeholder="Confirm Pin" v-model="ConfirmPin"/>
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

#content {
    margin-top: 7%;
}

#content input {
    display: inline-block;
    margin: 10px 0px;
    width: 75%;
    -webkit-text-security: disc;
}

#content button {
    margin-top: 50px;
}
</style>

<script>
export default {
    name: "SignUp",
    props: ["UsersName"],
    data(){
        return {
            Pin: '',
            ConfirmPin: ''
        }
    },
    methods: {
        NextPage() {
            this.$router.push({ name: 'SetupFinish' })
        }
    }
}
</script>