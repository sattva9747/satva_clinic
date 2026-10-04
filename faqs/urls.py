from django.urls import path
from .views import PatientQuestionListCreateView

urlpatterns = [
    path("questions/", PatientQuestionListCreateView.as_view()),
]