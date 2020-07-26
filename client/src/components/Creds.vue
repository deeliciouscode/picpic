<template lang="html">
    <!-- TODO: v-on.submit.prevent to not reload the page! -->
    <section class="creds frame">

        <form v-on:submit.prevent="updateCreds">
            <b-field label="Instagram Tag"
                     label-position="inside"
                     :type="tagType"
                     :message="tagMsg">
                <b-input v-model.lazy="instaTag" maxlength="30"></b-input>
            </b-field>

            <b-field label="Password"
                     label-position="inside"
                     :type="pwType"
                     :message="pwMsg">
                <b-input v-model.lazy="instaPw" type="password" maxlength="30"></b-input>
            </b-field>
            <b-button @click="updateCreds">Submit</b-button>
        </form>

    </section>

</template>

<script lang="js">

export default {
    name: 'creds',
    props: [],
    mounted() {

    },
    data() {
        return {
            instaTag: '',
            instaPw: '',
            tagMsg: '',
            tagType: 'is-light',
            pwMsg: '',
            pwType: 'is-light',
        };
    },
    methods: {
        updateCreds() {
            if (this.instaTag === '' || this.instaTag === undefined) {
                this.tagType = 'is-warning';
                this.tagMsg = 'You need to type your user tag';
            } else {
                this.tagType = 'is-success';
                this.tagMsg = '';
            }

            if (this.instaPw === '' || this.instaPw === undefined) {
                this.pwType = 'is-warning';
                this.pwMsg = 'You need to enter your password';
            } else {
                this.pwType = 'is-success';
                this.pwMsg = '';
                this.$store.commit({
                    type: 'updateCreds',
                    creds: {
                        username: this.instaTag,
                        password: this.instaPw,
                    },
                });
                this.$buefy.notification.open(`Your Username us now set to ${this.$store.state.user.username}`);
            }
        },
    },
    computed: {

    },
};

</script>

<style scoped>
.frame {
      float: left;
      position: relative;
      height: 900px;
      width: 300px;
  }

.creds {
}
</style>
