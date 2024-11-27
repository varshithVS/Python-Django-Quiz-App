# quiz/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),  # Dashboard page
    path('quiz/', views.quiz, name='quiz'),  # Quiz page
    path('submit/', views.submit_answer, name='submit'),  # Submit quiz answer
]
