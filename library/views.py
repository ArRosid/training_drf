from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateAPIView,
)
from oauth2_provider.contrib.rest_framework import (
    OAuth2Authentication,
    TokenHasScope,
)

from library.serializers import BoookSerializer
from library.models import Book


class BookListAPIView(ListCreateAPIView):
    serializer_class = BoookSerializer
    queryset = Book.objects.all()
    authentication_classes = [OAuth2Authentication, ]
    permission_classes = [TokenHasScope, ]
    required_scopes = ['read']


class BookUpdateAPIView(RetrieveUpdateAPIView):
    serializer_class = BoookSerializer
    queryset = Book.objects.all()
    lookup_field = 'pk'
    authentication_classes = [OAuth2Authentication, ]
    permission_classes = [TokenHasScope, ]
    required_scopes = ['read']
