<template lang="html">

    <section class="tagg-adder-bar">
        <div class="frame">
            <ul id="added_tags_list">
                <li v-for="item in instaTags" :key="item.tag" class="tag_item">
                    {{ item.tag }}
                </li>
            </ul>

            <form v-on:submit.prevent="addTag">
                <div class="form-group row">
                    <div class="col-12">
                        <input v-model.lazy="nextInstaTag" id="tag_adder" name="tag_adder"
                               placeholder="+ add insta handle"
                               type="text" class="form-control">
                    </div>
                </div>
            </form>

            <b-button @click="loadImages">Submit</b-button>
        </div>
    </section>
</template>

<script lang="js">
import axios from 'axios';
import { mapGetters } from 'vuex';

export default {
    name: 'tagg-adder-bar',
    props: [],
    mounted() {
    },
    data() {
        return {
            nextInstaTag: '',
        };
    },
    methods: {
        addTag() {
            // eslint-disable-next-line
            this.$store.commit({
                type: 'addTag',
                tag: this.nextInstaTag,
            });
            this.nextInstaTag = '';
        },
        loadImages() {
            const payload = {
                creds: this.creds,
                tags: this.instaTags,
            };
            const path = 'http://localhost:5000/nametags';
            axios
                .post(path, payload)
                .then((res) => {
                    const { data } = res;
                    this.$store.commit({
                        type: 'imgLoadLocationStatus',
                        imgLoadLocationStatus: data.Location,
                    });
                    const interval = setInterval(() => {
                        axios
                            .get(`http://localhost:5000${this.$store.state.imgLoadLocationStatus}`)
                            .then((resp) => {
                                if (resp.status === 200) {
                                    this.getImageIdsFromServer();
                                    clearInterval(interval);
                                }
                            })
                            .catch((err) => {
                                // eslint-disable-next-line
                                console.log(err);
                            });
                    }, 3000);
                })
                .catch((error) => {
                    // eslint-disable-next-line
                    console.log(error);
                });
        },
        getImageIdsFromServer() {
            const path = 'http://localhost:5000/getimgids';
            axios
                .get(path)
                .then((res) => {
                    this.$store.commit({
                        type: 'addImgIds',
                        imgIds: res.data.ids,
                    });
                })
                .catch((error) => {
                    // eslint-disable-next-line
                    console.log(error);
                });
        },
    },
    computed: {
        ...mapGetters([
            'instaTags',
            'creds',
        ]),
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

.tagg-adder-bar {
}

#added_tags_list {
  padding-inline-start: 0;
}

.tag_item {
  list-style-type: none;
  background-color: rgb(255, 255, 255);
  width: min-content;
  padding: 1px 3px 1px 3px;
  margin-bottom: 10px;
  border-radius: 5px;
}
</style>
