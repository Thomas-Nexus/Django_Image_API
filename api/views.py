from .custom import *
from images.models import *
from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response


class ImageAPI(generics.RetrieveAPIView):

    renderer_classes = [JPEGRenderer]
    def get(self, request, *args, **kwargs):
        queryset = Images.objects.get(id=self.kwargs['id']).image
        data = queryset
        return Response(data, content_type='image/jpg')