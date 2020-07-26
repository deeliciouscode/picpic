<template lang="html">

    <section v-if="imgIds.length" class="large-image frame">
        <img :src="getLink()" v-on:click="composeMosaic"
             @mouseover="hover = true"
             @mouseleave="hover = false">
        <span v-if="hover">This is a secret message.</span>
        <div class="columns is-vcentered custom-image-bar">
            <b-button rounded v-on:click="prevImg"><i class="fa fa-arrow-circle-left"
                                                      aria-hidden="true"></i></b-button>
            <div class="column" v-for="img in getSmallImgs()" :key="img">
                <img :src="getSmallImgLink(img)" v-on:click="setLargeImg(img)">
            </div>
            <b-button rounded v-on:click="nextImg"><i class="fa fa-arrow-circle-right"
                                                      aria-hidden="true"></i></b-button>
        </div>
    </section>

</template>

<script lang="js">
import axios from 'axios';
import { mapGetters } from 'vuex';

export default {
    name: 'large-image',
    props: [],
    mounted() {

    },
    data() {
        return {
            index: 0,
            largeImgId: '',
            indexSmallImgs: 0,
            hover: false,
        };
    },
    methods: {
        setLargeImg(id) {
            this.largeImgId = id;
        },
        getSmallImgLink(id) {
            return `http://localhost:5000/largeimgbyid/${id}`;
        },
        getSmallImgs() {
            return this.imgIds.slice(this.index, this.index + 5);
        },
        nextImg() {
            if (this.index === this.imgIds.length - 1) {
                this.index = 0;
            } else {
                this.index += 4;
            }
        },
        prevImg() {
            if (this.index === 0) {
                this.index = this.imgIds.length - 1;
            } else {
                this.index -= 4;
            }
        },
        getLink() {
            if (this.largeImgId === '') {
                [this.largeImgId] = this.imgIds;
            }
            return `http://localhost:5000/largeimgbyid/${this.largeImgId}`;
        },
        composeMosaic() {
            const payload = {
                id: this.largeImgId,
            };
            const path = 'http://localhost:5000/composemosaic';
            axios
                .post(path, payload)
                .then((res) => {
                    const interval = setInterval(() => {
                        axios
                            .get(`http://localhost:5000${res.data.Location}`)
                            .then((resp) => {
                                if (resp.status === 200) {
                                    this.downloadMosaic();
                                    clearInterval(interval);
                                }
                            })
                            .catch((err) => {
                                // eslint-disable-next-line
                                console.log(err);
                            });
                    }, 3000);
                    // eslint-disable-next-line
                    console.log(res)
                })
                .catch((err) => {
                    // eslint-disable-next-line
                    console.log(err)
                });
        },
        downloadMosaic() {
            // eslint-disable-next-line
            console.log("download mosaic")
        },
    },
    computed: {
        ...mapGetters([
            'imgIds',
        ]),
    },
};

</script>

<style scoped>

.custom-image-bar{
    margin-top: auto;
}

  .frame {
      float: left;
      position: relative;
      height: 900px;
      width: 600px;
  }

  img {
    width: 100%;
    height: 60%;
    object-fit: cover;
    border-radius: 5px;
  }

  .btn {
      margin: 10px;
  }
</style>
