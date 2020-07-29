<template lang="html">

    <section v-if="finalIsReady" class="file-downloader">
        <div class="box">
            <b-button @click="downloadMosaic">Download Mosaic</b-button>
        </div>
    </section>

</template>

<script lang="js">
import axios from 'axios';
import { mapGetters } from 'vuex';

export default {
    name: 'file-downloader',
    props: [],
    mounted() {

    },
    data() {
        return {

        };
    },
    methods: {
        downloadMosaic() {
            axios({
                url: `http://localhost:5000/final/final-${this.$store.state.mosaicImgId}`,
                method: 'GET',
                responseType: 'blob',
            }).then((response) => {
                const fileURL = window.URL.createObjectURL(new Blob([response.data]));
                const fileLink = document.createElement('a');

                fileLink.href = fileURL;
                fileLink.setAttribute('download', 'final.jpg');
                document.body.appendChild(fileLink);

                fileLink.click();
                this.$store.commit('toggleMosaicDownload');
            });
        },
    },
    computed: {
        ...mapGetters([
            'finalIsReady',
        ]),
    },
};

</script>

<style scoped>
  .file-downloader {
    background-color: rgba(0, 0, 0, 0.8);
  }

  .box {
    position: relative;
    left: 50%;
    transform: translateX(-50%);
    top: 30%;
    max-width: min-content;
    max-height: 100px;
  }
</style>
