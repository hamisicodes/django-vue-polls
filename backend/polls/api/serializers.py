from rest_framework import serializers
from polls.models import Question,Choice

class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = ('pk', 'question_text')

class ChoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Choice
        fields = ('pk', 'choice_text', 'votes')

class VoteSerializer(serializers.Serializer):
    choice_id = serializers.IntegerField()
