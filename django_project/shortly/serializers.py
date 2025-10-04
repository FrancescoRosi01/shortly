from rest_framework.serializers import ModelSerializer
from .models import ShortenedUrl


class ShortenedURLSerializer(ModelSerializer):
    model = ShortenedUrl
    fields = '__all__'

