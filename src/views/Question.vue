<template>
    
    <div @click="goTodetail(question.pk)">
        {{question.question_text}}
    </div>   
</template>

<script>
export default {
    name:"Question",
    props:["question"],
    methods: {goTodetail(qId) {    this.$router.push({name:'QuestionDetail',params:{id:qId}})  }  }
}
</script>

<style lang="stylus" scoped>

</style>