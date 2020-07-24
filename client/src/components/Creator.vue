<template lang="html">

    <section class="creator">
        <TaggAdderBar />
        <Creds />
    </section>

</template>

<script lang="js">
import Creds from './Creds.vue';
import TaggAdderBar from './TaggAdderBar.vue';

export default {
    name: 'creator',
    components: {
        Creds,
        TaggAdderBar,
    },
    props: [],
    mounted() {

    },
    data() {
        return {

        };
    },
    methods: {

    },
    computed: {

    },
};

</script>

<style scoped>
.creator {
}
</style>
