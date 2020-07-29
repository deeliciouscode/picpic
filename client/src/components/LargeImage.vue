<template lang="html">

    <section v-if="imgIds.length" class="frame">
        <div class="large-image-frame">
            <img class="large-image" :src="getLink()" />
            <b-button id="select-img-button" v-on:click="composeMosaic">select</b-button>
            <!-- <img v-if="hover" class="loading-indicator" src="../assets/loading.gif"> -->
        </div>
        <div class="columns is-vcentered custom-image-bar">
            <b-button rounded v-on:click="prevImg"><i class="fa fa-arrow-circle-left"
                                                      aria-hidden="true"></i></b-button>
            <div class="column" v-for="img in getSmallImgs()" :key="img">
                <div class="small-img-frame">
                    <img class="small-img" :src="getSmallImgLink(img)"
                         v-on:click="setLargeImg(img)">
                </div>
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
            this.$store.commit({
                type: 'setMosaicImgId',
                mosaicImgId: this.largeImgId,
            });
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
                                    this.$store.commit('toggleMosaicDownload');
                                    clearInterval(interval);
                                }
                            })
                            .catch((err) => {
                                // eslint-disable-next-line
                                console.log(err);
                            });
                    }, 5000);
                    // eslint-disable-next-line
                    console.log(res)
                })
                .catch((err) => {
                    // eslint-disable-next-line
                    console.log(err)
                });
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

  .large-image-frame {
      width: 600px;
      height: 600px;
      position: relative;
      object-fit: cover;
  }

  .large-image {
      width: 100%;
      height: 600px;
      border-radius: 5px;
      object-fit: cover;
      position: absolute;
  }

  .small-img-frame {
      width: 70px;
      height: 70px;
      object-fit: cover;
  }

  .small-img{
      width: 100%;
      height: 70px;
      border-radius: 5px;
      object-fit: cover;
  }

  #select-img-button {
      position: absolute;
      bottom: 10px;
      right: 10px;
  }

  .btn {
      margin: 10px;
  }
</style>
