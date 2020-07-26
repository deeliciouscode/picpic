<template lang="html">

    <section class="creator level">
        <div class="level-left">
            <div class="level-item">
                <LargeImage id="large-img-comp"/>
            </div>
            <div class="level-item">
                <TaggAdderBar id="tag-adder-comp"/>
            </div>
        </div>

        <!-- Right side -->
        <div class="level-right">
            <Creds id="creds-comp"/>
        </div>
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
    padding: 25px;
}

#large-img-comp {
}

#tag-adder-comp {
  max-width: 300px;
  width: 100%;
}

#creds-comp {
    max-width: 300px;
    position: relative;
    width: 100%;
}
</style>
