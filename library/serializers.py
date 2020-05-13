from django.contrib.auth.models import User
from rest_framework import serializers
from library.models import Book


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username']


class BoookSerializer(serializers.ModelSerializer):
    total_page = serializers.IntegerField(min_value=1)
    modified_by = UserSerializer(read_only=True)

    class Meta:
        model = Book
        fields = ['id', 'title', 'total_page',
                  'is_deleted', 'modified_by',
                  'deleted_by', ]
