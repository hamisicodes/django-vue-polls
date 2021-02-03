<template>
    
    <div>
          <form @submit="vote">
            <div v-for="choice in choices" :key="choice.pk">
                <input type="radio" id="choice.pk" v-model="selectedChoice" name="selectedChoice" :value="choice.pk">
                <label for="choice.pk">{{choice.choice_text}}</label><br>
            </div>
            <input type="submit" value="submit" class="btn">
          </form>
    </div>
    

</template>


<script>
import axios from 'axios'
export default {
    name: 'QuestionDetail',
    data() {
    return {
      selectedChoice:1,
      choices:[
       
      ]
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
    methods: {
        vote(e){
            e.preventDefault()
            let question_id = this.$route.params.id

            axios.patch(`http://127.0.0.1:8000/api/polls/${question_id}/vote/`,
                { 
                    choice_id: this.selectedChoice
                }, 
            )
            .then(res => {
                console.log(res)
                this.$router.push({name:'Results'})
            })
            .catch(err => console.log(err))
        }
    }

}
</script>

<style lang="stylus" scoped>

</style>