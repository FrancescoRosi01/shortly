from django.urls import path
from .views import GetShortURLView

urlpatterns = [
    path('<str:short_link>/', GetShortURLView.as_view(), name="short_redirect"),
]
