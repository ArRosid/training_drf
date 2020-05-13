from rest_framework import serializers
from library.models import Book


class BoookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['id', 'title', 'total_page']