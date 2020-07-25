<template lang="html">

    <section class="large-image">
        <div class="frame">
            <div v-if="imgIds.length">
                <img :src="getLink()">
                <button class="btn btn-primary" v-on:click="composeMosaic">select this one</button>
                <button class="btn btn-primary" v-on:click="index--">prev</button>
                <button class="btn btn-primary" v-on:click="index++">next</button>
            </div>
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
        };
    },
    methods: {
        getLink() {
            const id = this.imgIds[this.index];
            return `http://localhost:5000/largeimgbyid/${id}`;
        },
        composeMosaic() {
            const payload = {
                id: '69455642_169771750841605_1747183850796859043_n.jpg',
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
  .large-image {
      padding: 30px;
  }

  .frame {
      float: left;
      position: relative;
      width: 400px;
      height: 400px;
  }

  img {
    width: 700px;
    height: 700px;
    object-fit: cover;
    border-radius: 5px;
  }

  .btn {
      margin: 10px;
  }
</style>
