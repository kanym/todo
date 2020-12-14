from django.db import models
from django.utils import timezone



class ListPage (models.Model):
    title = models.CharField(max_length = 150)
    body = models.TextField()
    create_date = models.DateField(default=timezone.now)

    def __str__(self):
        return self.title


