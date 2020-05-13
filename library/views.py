from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView,
)
from oauth2_provider.contrib.rest_framework import (
    OAuth2Authentication,
    TokenHasScope,
)

from rest_framework.response import Response
from rest_framework import status
from library.serializers import BoookSerializer
from library.models import Book


class BookListAPIView(ListCreateAPIView):
    serializer_class = BoookSerializer
    queryset = Book.objects.filter(is_deleted=False)
    authentication_classes = [OAuth2Authentication, ]
    permission_classes = [TokenHasScope, ]
    required_scopes = ['read']


class BookUpdateAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = BoookSerializer
    queryset = Book.objects.all()
    lookup_field = 'pk'
    authentication_classes = [OAuth2Authentication, ]
    permission_classes = [TokenHasScope, ]
    required_scopes = ['read']

    def perform_update(self, serializer):
        return serializer.save(
            modified_by=self.request.user,
        )

    def perform_destroy(self, instance):
        instance.is_deleted = True
        instance.deleted_by = self.request.user
        instance.save()

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        serializer = self.get_serializer(instance)
        return Response(serializer.data, status=status.HTTP_204_NO_CONTENT)
