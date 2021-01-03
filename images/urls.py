from .views import *
from django.urls import path, reverse
from django.views.generic import TemplateView, View

app_name = 'images'

urlpatterns = [
    path('', TemplateView.as_view(template_name='home.html')),

    path('images/all', all_.as_view(), name='all'),
    path('likes/<int:pk>', likes, name='likes'),

    path('images/nature', nature.as_view(), name='nature'),
    path('likes_n/<int:pk>', likes_n, name='likes_n'),

    path('images/space', space.as_view(), name='space'),
    path('likes_s/<int:pk>', likes_s, name='likes_s'),

    path('images/wildlife', wildlife.as_view(), name='wildlife'),
    path('likes_w/<int:pk>', likes_w, name='likes_w'),

    path('images/popular', popular_sort.as_view(), name='popular'),
    path('images/new', newest_sort.as_view(), name='new'),

    path('images/upload', upload, name='upload'),
    path('images/login', login_p, name='login'),
    path('images/logout', logout_p, name='logout'),
    path('images/register', register, name='register'),
]