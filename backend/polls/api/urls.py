from django.shortcuts import render
from django.urls import path
from .views import QuestionView,QuestionDetailView,vote

urlpatterns = [
    path('',QuestionView.as_view()),
    path('<int:pk>/', QuestionDetailView.as_view()),
    path('<int:pk>/vote/', vote),
]