<template>
    <h1>Results</h1>
    <ul>
        <li v-for="choice in choices" :key="choice.pk">{{choice.choice_text}}<span>-{{choice.votes}} votes</span></li>
        <button @click="goTodetail()">Vote again</button>
        <br><br><br>
        <button>Back to Questions</button>
    </ul>
</template>

<script>
import axios from 'axios'
export default {
    name: "Results",
    data() {
        return {
            choices: [],
            qid:this.$route.params.id
        }
    },
    
    created () {

        let question_id = this.$route.params.id
        let url = `http://127.0.0.1:8000/api/polls/${question_id}/`
        
        axios.get(url)
        .then(res =>{
            this.choices = res.data
        
         })
        .catch(err => console.log(err))
        
    },

    methods: {goTodetail(questionId=this.qid) {    this.$router.push({name:'QuestionDetail',params:{id:questionId}})  }  }
    
}
</script>

<style >

</style>