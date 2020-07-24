<template lang="html">
    <!-- TODO: v-on.submit.prevent to not reload the page! -->
    <section class="creds">
        <link rel="stylesheet"
              href="https://maxcdn.bootstrapcdn.com/font-awesome/4.7.0/css/font-awesome.min.css">
        <form v-on:submit.prevent="updateCreds">
            <div class="form-group row">
                <div class="col-12">
                    <div class="input-group">
                        <div class="input-group-prepend">
                            <div class="input-group-text">
                                <i class="fa fa-instagram"></i>
                            </div>
                        </div>
                        <input v-model.lazy="instaTag" id="text"
                               name="text" placeholder="Your Instagram Name"
                               type="text" class="form-control" required="required">
                    </div>
                </div>
            </div>
            <div class="form-group row">
                <div class="col-12">
                    <div class="input-group">
                        <div class="input-group-prepend">
                            <div class="input-group-text">
                                <i class="fa fa-lock"></i>
                            </div>
                        </div>
                        <input v-model.lazy="instaPw" id="insta_password" name="insta_password"
                               placeholder="Your Password" type="password"
                               class="form-control" required="required">
                    </div>
                </div>
            </div>
            <div class="form-group row">
                <div class="col-12">
                    <button name="submit" type="submit" class="btn btn-primary">
                        Submit
                    </button>
                </div>
            </div>
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

        };
    },
    methods: {
        updateCreds() {
            this.$store.commit({
                type: 'updateCreds',
                creds: {
                    username: this.instaTag,
                    password: this.instaPw,
                },
            });
        },
    },
    computed: {

    },
};

</script>

<style scoped>
.creds {
    max-width: 300px;
    position: absolute;
    padding: 30px;
    right: 30px;
    width: 100%;
}
</style>
