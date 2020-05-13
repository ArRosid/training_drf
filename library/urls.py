from django.urls import path
from library.views import BookListAPIView

urlpatterns = [
    path('books/', BookListAPIView.as_view(), name='BookListAPIView'),
]