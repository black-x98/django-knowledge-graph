<template>
    <div>Lego Colors</div>
    <div v-for="color in legoColors" :key="color.rgb">
    {{color.name}}
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
            this.legoColors = resp;
        }
    }
};
</script>