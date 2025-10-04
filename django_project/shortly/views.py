from http import HTTPStatus

from django.shortcuts import redirect
from rest_framework.request import Request
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import ShortenedUrl
from .serializers import ShortenedURLSerializer


class GetShortURLView(APIView):
    def get(self, request: Request, short_link: str):
        try:
            obj = ShortenedUrl.objects.get(short_url=short_link,user=request.user)
            # temporary redirect (HTTP 302)
            return redirect(obj.base_url)
        except ShortenedUrl.DoesNotExist:
            return Response(status=404)

class PostShortURLView(APIView):
    def post(self, request : Request):
        short_url = "" # TODO : write a function for creating short url
        serializer = ShortenedURLSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'short_url': short_url},status=status.HTTP_201_CREATED)
        return Response({'error':'data provided is not valid'},status=status.HTTP_400_BAD_REQUEST)