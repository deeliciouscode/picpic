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

        <FileDownloader id="file-downloader-comp"/>
    </section>

</template>

<script lang="js">
import Creds from './Creds.vue';
import TaggAdderBar from './TaggAdderBar.vue';
import LargeImage from './LargeImage.vue';
import FileDownloader from './FileDownloader.vue';

export default {
    name: 'creator',
    components: {
        Creds,
        TaggAdderBar,
        LargeImage,
        FileDownloader,
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

#file-downloader-comp {
    position: fixed;
    width: 100%;
    height: 100%;
    top: 0px;
    left: 0px;
}
</style>
