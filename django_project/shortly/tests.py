from django.test import TestCase

# Create your tests here.

from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth.models import User
from .models import ShortenedUrl


class GetShortURLViewTest(APITestCase):

    def setUp(self):
        # Create a test user
        self.user = User.objects.create_user(username='testuser', password='testpass')
        # Create a test shortened URL
        self.short_url_obj = ShortenedUrl.objects.create(
            base_url="https://example.com/long/path",
            short_url="abc123",
            alias="Example",
            user=self.user
        )

    def test_redirect_success(self):
        """
        Should return 302 redirect to the original URL
        """
        url = reverse('short_redirect', args=['abc123'])
        response = self.client.get(url)
        # Assert that it redirects
        self.assertEqual(response.status_code, status.HTTP_302_FOUND)
        # Check that the redirect location is correct
        self.assertEqual(response['Location'], "https://example.com/long/path")

    def test_redirect_failure(self):
        """
        Should return HTTP 404
        """
        url = reverse('short_redirect', args=['abc1234'])
        response = self.client.get(url)
        # Assert that it redirects
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
