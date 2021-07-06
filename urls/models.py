from django.db import models


class Url(models.Model):
    original_url = models.CharField(max_length=256, unique=True)
    shortened_url = models.CharField(max_length=24)
    created_on = models.DateTimeField(auto_now_add=True)
    random_string = models.CharField(max_length=6, unique=True)

    def __str__(self):
        return f'{self.original_url} -> {self.shortened_url}'
