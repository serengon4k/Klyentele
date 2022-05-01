<template>
    <div id="Container">
        <div id="Title">
            <img alt="Vue logo" src="../../assets/AppLogo/LogoUpClose.svg"> <h1>The Legal Stuff</h1>
        </div>
        <section>

        </section>
       
        <label for="AgreeBox"> I agree to the following terms and conditions</label>
        <input id="AgreeBox" type="checkbox" @click="CheckBox()" ref="CheckBox">
        <button ref="NextPageButton" @click="NextPage()" :disabled='TermsNotAgreed'>I agree</button>
    </div>
</template>
<style scoped>
#Container{
    text-align: center;
    padding-top: 32px;
}
#Title{
    display: inline-block;
}

#Title h1{
    font-size: 48px;
    margin: 0px;
    height: 100%;
    display: inline-block;
}
#Title img{
    width: 88px;
    height: auto;
    display: inline-block;
}

</style>

<script>
    export default {
        name: "LicenseAgreement",
        data(){
            return {
                TermsNotAgreed: true
            }
        },
        methods: {
            CheckBox(){
                const Checkbox = this.$refs.CheckBox.checked
                if ( Checkbox == true) {
                    //Returns disabled to be false
                    this.TermsNotAgreed = false
                }
                else if (Checkbox == false) {
                    //Returns disabled to be true
                    this.TermsNotAgreed = true
                }
            },
            NextPage(){
                this.$router.push({name:'ModeSelection'})
            }
        }
    }
</script>