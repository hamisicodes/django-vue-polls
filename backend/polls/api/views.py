from rest_framework.generics import ListAPIView
from rest_framework.views import APIView
from .serializers import QuestionSerializer,ChoiceSerializer,VoteSerializer
from polls.models import  Question,Choice
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.shortcuts import get_object_or_404
from rest_framework import status



class QuestionView(ListAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer



class QuestionDetailView(APIView):
    def get_object(self, pk):
        try:
            return Question.objects.get(pk=pk)
        except Question.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        question = self.get_object(pk)
        choices = question.choice_set.all()
        serializer = ChoiceSerializer(choices, many=True)
        return Response(serializer.data)


@api_view(['PATCH'])
def vote(request, pk):
    question = get_object_or_404(Question, pk=pk)
    serializer = VoteSerializer(data=request.data)
    if serializer.is_valid():
        choice = get_object_or_404(Choice, pk=serializer.validated_data['choice_id'], question=question)
        choice.votes += 1
        choice.save()
        return Response("Voted")
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
 

