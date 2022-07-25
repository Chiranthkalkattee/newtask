
from django.urls import path
from .views import Candidate_list

urlpatterns = [
    path('candidate/', Candidate_list),
]