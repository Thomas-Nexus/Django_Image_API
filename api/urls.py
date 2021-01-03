from .views import *
from django.urls import path

urlpatterns = [
    path('id/<id>', ImageAPI.as_view()),
]