<template>
  <div class="home">
    <h1>Questions</h1>
    <ul>
      <li v-for="question in questions" :key="question.id">
          <Question v-bind:question="question" />
      </li>
      
    </ul>
   
  </div>
</template>

<script>

import axios from 'axios';
import Question from './Question';
export default {
  name: "Home",
  components: {
    Question
  },
  data() {
    return {
      questions:[
       
      ]
    }
  },

  created(){
    axios.get('http://127.0.0.1:8000/api/polls/')
      .then(res =>{
        
        this.questions = res.data
      })
      .catch(err => console.log(err))
  }


};
</script>
