from http import HTTPStatus

from django.shortcuts import redirect
from rest_framework.request import Request
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import ShortenedUrl


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
        record = ShortenedUrl(base_url=request.data.get('long_url'), short_url=short_url, alias=request.data.get('alias'), user=request.user)
        record.save()
        return Response({''},status=status.HTTP_201_CREATED)
