<template lang="html">

    <section class="creator">
        <LargeImage/>
        <TaggAdderBar />
        <Creds />
    </section>

</template>

<script lang="js">
import Creds from './Creds.vue';
import TaggAdderBar from './TaggAdderBar.vue';
import LargeImage from './LargeImage.vue';

export default {
    name: 'creator',
    components: {
        Creds,
        TaggAdderBar,
        LargeImage,
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
