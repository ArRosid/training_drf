from django.urls import path
from library.views import BookListAPIView, BookUpdateAPIView

app_name = 'library'

urlpatterns = [
    path('books/', BookListAPIView.as_view(), name='BookListAPIView'),
    path('books/<int:pk>/', BookUpdateAPIView.as_view(), name="BookUpdateAPIView"),
]
