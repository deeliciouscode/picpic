(function(t){function e(e){for(var n,o,r=e[0],c=e[1],l=e[2],d=0,g=[];d<r.length;d++)o=r[d],Object.prototype.hasOwnProperty.call(s,o)&&s[o]&&g.push(s[o][0]),s[o]=0;for(n in c)Object.prototype.hasOwnProperty.call(c,n)&&(t[n]=c[n]);u&&u(e);while(g.length)g.shift()();return i.push.apply(i,l||[]),a()}function a(){for(var t,e=0;e<i.length;e++){for(var a=i[e],n=!0,r=1;r<a.length;r++){var c=a[r];0!==s[c]&&(n=!1)}n&&(i.splice(e--,1),t=o(o.s=a[0]))}return t}var n={},s={app:0},i=[];function o(e){if(n[e])return n[e].exports;var a=n[e]={i:e,l:!1,exports:{}};return t[e].call(a.exports,a,a.exports,o),a.l=!0,a.exports}o.m=t,o.c=n,o.d=function(t,e,a){o.o(t,e)||Object.defineProperty(t,e,{enumerable:!0,get:a})},o.r=function(t){"undefined"!==typeof Symbol&&Symbol.toStringTag&&Object.defineProperty(t,Symbol.toStringTag,{value:"Module"}),Object.defineProperty(t,"__esModule",{value:!0})},o.t=function(t,e){if(1&e&&(t=o(t)),8&e)return t;if(4&e&&"object"===typeof t&&t&&t.__esModule)return t;var a=Object.create(null);if(o.r(a),Object.defineProperty(a,"default",{enumerable:!0,value:t}),2&e&&"string"!=typeof t)for(var n in t)o.d(a,n,function(e){return t[e]}.bind(null,n));return a},o.n=function(t){var e=t&&t.__esModule?function(){return t["default"]}:function(){return t};return o.d(e,"a",e),e},o.o=function(t,e){return Object.prototype.hasOwnProperty.call(t,e)},o.p="/";var r=window["webpackJsonp"]=window["webpackJsonp"]||[],c=r.push.bind(r);r.push=e,r=r.slice();for(var l=0;l<r.length;l++)e(r[l]);var u=c;i.push([0,"chunk-vendors"]),a()})({0:function(t,e,a){t.exports=a("56d7")},"034f":function(t,e,a){"use strict";var n=a("85ec"),s=a.n(n);s.a},"2a52":function(t,e,a){"use strict";var n=a("a8f6"),s=a.n(n);s.a},"4a03":function(t,e,a){"use strict";var n=a("aa36"),s=a.n(n);s.a},"56d7":function(t,e,a){"use strict";a.r(e);a("e260"),a("e6cf"),a("cca6"),a("a79d"),a("f9e3");var n=a("2b0e"),s=a("289d"),i=function(){var t=this,e=t.$createElement,a=t._self._c||e;return a("div",{attrs:{id:"app"}},[a("router-view")],1)},o=[],r=(a("034f"),a("2877")),c={},l=Object(r["a"])(c,i,o,!1,null,null,null),u=l.exports,d=a("8c4f"),g=function(){var t=this,e=t.$createElement,a=t._self._c||e;return a("div",{staticClass:"container"},[a("button",{staticClass:"btn btn-primary",attrs:{type:"button"}},[t._v(t._s(t.msg))])])},m=[],f=a("bc3a"),p=a.n(f),h={name:"Ping",data:function(){return{msg:""}},methods:{getMessage:function(){var t=this,e="http://localhost:5000/ping";p.a.get(e).then((function(e){t.msg=e.data})).catch((function(t){console.log(t)}))}},created:function(){this.getMessage()}},b=h,v=Object(r["a"])(b,g,m,!1,null,null,null),I=v.exports,w=function(){var t=this,e=t.$createElement,a=t._self._c||e;return a("section",{staticClass:"creator level"},[a("div",{staticClass:"level-left"},[a("div",{staticClass:"level-item"},[a("LargeImage",{attrs:{id:"large-img-comp"}})],1),a("div",{staticClass:"level-item"},[a("TaggAdderBar",{attrs:{id:"tag-adder-comp"}})],1)]),a("div",{staticClass:"level-right"},[a("Creds",{attrs:{id:"creds-comp"}})],1),a("FileDownloader",{attrs:{id:"file-downloader-comp"}})],1)},y=[],T=function(){var t=this,e=t.$createElement,a=t._self._c||e;return a("section",{staticClass:"creds frame"},[a("form",{on:{submit:function(e){return e.preventDefault(),t.updateCreds(e)}}},[a("b-field",{attrs:{label:"Instagram Tag","label-position":"inside",type:t.tagType,message:t.tagMsg}},[a("b-input",{attrs:{maxlength:"30"},model:{value:t.instaTag,callback:function(e){t.instaTag=e},expression:"instaTag"}})],1),a("b-field",{attrs:{label:"Password","label-position":"inside",type:t.pwType,message:t.pwMsg}},[a("b-input",{attrs:{type:"password",maxlength:"30"},model:{value:t.instaPw,callback:function(e){t.instaPw=e},expression:"instaPw"}})],1),a("b-button",{on:{click:t.updateCreds}},[t._v("Submit")])],1),a("b-button",{staticClass:"clear-data-button",attrs:{type:"is-danger"},on:{click:t.clearData}},[t._v("Clear Data")])],1)},_=[],x={name:"creds",props:[],mounted:function(){},data:function(){return{instaTag:"",instaPw:"",tagMsg:"",tagType:"is-light",pwMsg:"",pwType:"is-light"}},methods:{updateCreds:function(){""===this.instaTag||void 0===this.instaTag?(this.tagType="is-warning",this.tagMsg="You need to type your user tag"):(this.tagType="is-success",this.tagMsg=""),""===this.instaPw||void 0===this.instaPw?(this.pwType="is-warning",this.pwMsg="You need to enter your password"):(this.pwType="is-success",this.pwMsg="",this.$store.commit({type:"updateCreds",creds:{username:this.instaTag,password:this.instaPw}}),this.$buefy.notification.open("Your Username us now set to ".concat(this.$store.state.user.username)))},clearData:function(){var t=this;this.$store.commit("clearData"),p.a.post("http://localhost:5000/cleardata",{what:"all"}).then((function(){t.$buefy.notification.open("Your data was deleted!")})).catch((function(t){console.log(t)}))}},computed:{}},C=x,L=(a("4a03"),Object(r["a"])(C,T,_,!1,null,"a08e666e",null)),O=L.exports,j=function(){var t=this,e=t.$createElement,a=t._self._c||e;return a("section",{staticClass:"tagg-adder-bar"},[a("div",{staticClass:"frame"},[a("ul",{attrs:{id:"added_tags_list"}},t._l(t.instaTags,(function(e){return a("li",{key:e.tag,staticClass:"tag_item"},[t._v(" "+t._s(e.tag)+" ")])})),0),a("form",{on:{submit:function(e){return e.preventDefault(),t.addTag(e)}}},[a("div",{staticClass:"form-group row"},[a("div",{staticClass:"col-12"},[a("input",{directives:[{name:"model",rawName:"v-model.lazy",value:t.nextInstaTag,expression:"nextInstaTag",modifiers:{lazy:!0}}],staticClass:"form-control",attrs:{id:"tag_adder",name:"tag_adder",placeholder:"+ add insta handle",type:"text"},domProps:{value:t.nextInstaTag},on:{change:function(e){t.nextInstaTag=e.target.value}}})])])]),a("b-button",{on:{click:t.loadImages}},[t._v("Submit")])],1)])},M=[],S=a("5530"),$=a("2f62"),k={name:"tagg-adder-bar",props:[],mounted:function(){},data:function(){return{nextInstaTag:""}},methods:{addTag:function(){this.$store.commit({type:"addTag",tag:this.nextInstaTag}),this.nextInstaTag=""},loadImages:function(){var t=this,e={creds:this.creds,tags:this.instaTags},a="http://localhost:5000/nametags";p.a.post(a,e).then((function(e){var a=e.data;t.$store.commit({type:"imgLoadLocationStatus",imgLoadLocationStatus:a.Location});var n=setInterval((function(){p.a.get("http://localhost:5000".concat(t.$store.state.imgLoadLocationStatus)).then((function(e){200===e.status&&(t.getImageIdsFromServer(),clearInterval(n))})).catch((function(t){console.log(t)}))}),15e3)})).catch((function(t){console.log(t)}))},getImageIdsFromServer:function(){var t=this,e="http://localhost:5000/getimgids";p.a.get(e).then((function(e){t.$store.commit({type:"addImgIds",imgIds:e.data.ids})})).catch((function(t){console.log(t)}))}},computed:Object(S["a"])({},Object($["b"])(["instaTags","creds"]))},P=k,D=(a("2a52"),Object(r["a"])(P,j,M,!1,null,"4876d812",null)),R=D.exports,E=function(){var t=this,e=t.$createElement,a=t._self._c||e;return t.imgIds.length?a("section",{staticClass:"frame"},[a("div",{staticClass:"large-image-frame"},[a("img",{staticClass:"large-image",attrs:{src:t.getLink()}}),a("b-button",{attrs:{id:"select-img-button"},on:{click:t.composeMosaic}},[t._v("select")])],1),a("div",{staticClass:"columns is-vcentered custom-image-bar"},[a("b-button",{attrs:{rounded:""},on:{click:t.prevImg}},[a("i",{staticClass:"fa fa-arrow-circle-left",attrs:{"aria-hidden":"true"}})]),t._l(t.getSmallImgs(),(function(e){return a("div",{key:e,staticClass:"column"},[a("div",{staticClass:"small-img-frame"},[a("img",{staticClass:"small-img",attrs:{src:t.getSmallImgLink(e)},on:{click:function(a){return t.setLargeImg(e)}}})])])})),a("b-button",{attrs:{rounded:""},on:{click:t.nextImg}},[a("i",{staticClass:"fa fa-arrow-circle-right",attrs:{"aria-hidden":"true"}})])],2)]):t._e()},F=[],Y=(a("fb6a"),a("3835")),A={name:"large-image",props:[],mounted:function(){},data:function(){return{index:0,largeImgId:"",indexSmallImgs:0}},methods:{setLargeImg:function(t){this.largeImgId=t},getSmallImgLink:function(t){return"http://localhost:5000/largeimgbyid/".concat(t)},getSmallImgs:function(){return this.imgIds.slice(this.index,this.index+5)},nextImg:function(){this.index===this.imgIds.length-1?this.index=0:this.index+=4},prevImg:function(){0===this.index?this.index=this.imgIds.length-1:this.index-=4},getLink:function(){if(""===this.largeImgId){var t=Object(Y["a"])(this.imgIds,1);this.largeImgId=t[0]}return"http://localhost:5000/largeimgbyid/".concat(this.largeImgId)},composeMosaic:function(){var t=this;this.$store.commit({type:"setMosaicImgId",mosaicImgId:this.largeImgId});var e={id:this.largeImgId},a="http://localhost:5000/composemosaic";p.a.post(a,e).then((function(e){var a=setInterval((function(){p.a.get("http://localhost:5000".concat(e.data.Location)).then((function(e){200===e.status&&(t.$store.commit("toggleMosaicDownload"),clearInterval(a))})).catch((function(t){console.log(t)}))}),3e3);console.log(e)})).catch((function(t){console.log(t)}))}},computed:Object(S["a"])({},Object($["b"])(["imgIds"]))},B=A,U=(a("ef74"),Object(r["a"])(B,E,F,!1,null,"135e1917",null)),z=U.exports,J=function(){var t=this,e=t.$createElement,a=t._self._c||e;return t.finalIsReady?a("section",{staticClass:"file-downloader"},[a("div",{staticClass:"box"},[a("b-button",{on:{click:t.downloadMosaic}},[t._v("Download Mosaic")])],1)]):t._e()},G=[],N=(a("d3b7"),a("3ca3"),a("ddb0"),a("2b3d"),{name:"file-downloader",props:[],mounted:function(){},data:function(){return{}},methods:{downloadMosaic:function(){var t=this;p()({url:"http://localhost:5000/final/".concat(this.$store.state.mosaicImgId),method:"GET",responseType:"blob"}).then((function(e){var a=window.URL.createObjectURL(new Blob([e.data])),n=document.createElement("a");n.href=a,n.setAttribute("download","final.jpg"),document.body.appendChild(n),n.click(),t.$store.commit("toggleMosaicDownload")}))}},computed:Object(S["a"])({},Object($["b"])(["finalIsReady"]))}),q=N,H=(a("ed85"),Object(r["a"])(q,J,G,!1,null,"685df87d",null)),K=H.exports,Q={name:"creator",components:{Creds:O,TaggAdderBar:R,LargeImage:z,FileDownloader:K},props:[],mounted:function(){},data:function(){return{}},methods:{},computed:{}},V=Q,W=(a("66cc"),Object(r["a"])(V,w,y,!1,null,"74dbd647",null)),X=W.exports;n["a"].use(d["a"]);var Z=[{path:"/ping",name:"Ping",component:I},{path:"/",name:"Creator",component:X}],tt=new d["a"]({mode:"history",base:"/",routes:Z}),et=tt;n["a"].use($["a"]);var at=new $["a"].Store({state:{user:{username:"some_user",password:"some_password"},instaTags:[],imgLoadLocationStatus:"",imgIds:[],mosaicImgId:"",finalIsReady:!1},getters:{instaTags:function(t){return t.instaTags},creds:function(t){return t.user},imgIds:function(t){return t.imgIds},finalIsReady:function(t){return t.finalIsReady}},mutations:{addTag:function(t,e){var a={tag:e.tag};e.tag&&t.instaTags.push(a)},updateCreds:function(t,e){t.user=e.creds},imgLoadLocationStatus:function(t,e){t.imgLoadLocationStatus=e.imgLoadLocationStatus},addImgIds:function(t,e){t.imgIds=e.imgIds},setMosaicImgId:function(t,e){t.mosaicImgId=e.mosaicImgId},toggleMosaicDownload:function(t){t.finalIsReady=!t.finalIsReady},clearData:function(t){t.user={username:"some_user",password:"some_password"},t.instaTags=[],t.imgLoadLocationStatus="",t.imgIds=[],t.mosaicImgId="",t.finalIsReady=!1}},actions:{}});a("5abe"),a("15f5"),a("7051"),a("7646");n["a"].config.productionTip=!1,n["a"].use(s["a"]),new n["a"]({store:at,router:et,render:function(t){return t(u)}}).$mount("#app")},"66cc":function(t,e,a){"use strict";var n=a("7c93"),s=a.n(n);s.a},"7c93":function(t,e,a){},"85ec":function(t,e,a){},"90fc":function(t,e,a){},a8f6:function(t,e,a){},aa36:function(t,e,a){},c909:function(t,e,a){},ed85:function(t,e,a){"use strict";var n=a("c909"),s=a.n(n);s.a},ef74:function(t,e,a){"use strict";var n=a("90fc"),s=a.n(n);s.a}});
//# sourceMappingURL=app.08df11f5.js.map