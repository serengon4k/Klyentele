<template>
    <div id="Container">
        <div id="Title">
            <img alt="Vue logo" src="../../assets/AppLogo/LogoUpClose.svg">
            <h1>The Legal Stuff</h1>
        </div>
        <section id="terms">
            <p>In accordence with the license agreement, terms and conditions, and privacy policy found at the link:
                <br /> https://klyentele.azura4k.com/legal.html<br />
                By continuing forward in this setup, you agree to the installation, usage, and operation of this
                software under the terms
                of all three binding agreements above. If you do so agree, please look below and click the checkbox while carefully reading what it implies. Once done, click the "I agree" button if and only if, you agree.
            </p>
        </section>
        <section id="interaction">
            <label for="AgreeBox"> I agree to the following terms and conditions</label>
            <input id="AgreeBox" type="checkbox" @click="CheckBox()" ref="CheckBox">
            <br />
            <button ref="NextPageButton" @click="NextPage()" :disabled='TermsNotAgreed'>I agree</button>
        </section>
    </div>
</template>
<style scoped>
#Container{
    text-align: center;
    padding: 32px 15% 0px 15%;
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
#terms{
    text-align: left;
    justify-self: auto;
    margin-top: 5%;
}
#interaction{
    margin-top: 10%;
}
#interaction label {
    margin-right: 30px;
}
#interaction button {
    margin-top: 30px;
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
                this.$router.push({name:'LicenseKeyEntry'})
            }
        }
    }
</script>