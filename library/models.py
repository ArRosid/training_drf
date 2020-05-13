from django.db import models
from django.conf import settings


class Book(models.Model):
    title = models.CharField(max_length=100)
    total_page = models.IntegerField()
    modified_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        null=True, blank=True,
        related_name='book_modified_by'
    )
    is_deleted = models.BooleanField(default=False)
    deleted_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        null=True, blank=True,
        related_name='book_deleted_by'
    )

    def __str__(self):
        return self.title
