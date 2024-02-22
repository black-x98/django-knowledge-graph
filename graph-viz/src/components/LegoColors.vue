<template>
    <div style="background-color: #dddddd;">
    <div style="font: 24px bold; font-weight: 700; padding: 10px;">Lego Colors</div>
    <div v-for="color in legoColors" :key="color">
        <div style="display: flex; justify-content: center;">
        <div style="display: flex; justify-content: space-between;">
            <div style="padding-right: 10px">{{color.name}}</div>
            <div :style="{backgroundColor: '#' + color.rgb, fontSize: '18px', height: '14px', width: '40px' }"></div>
        </div>
        </div>
    </div>
    </div>
</template>

<script>
import axios from 'axios';
export default {
    async created(){
        await this.fetchLegoColors();
    },
    data(){
        return {
            legoColors: []
        }
    },
    methods: {
        async fetchLegoColors(){
            let resp = await axios.get(
                "http://127.0.0.1:8000/lego-colors/"
            );
            this.legoColors = resp.data;
        }
    }
};
</script>