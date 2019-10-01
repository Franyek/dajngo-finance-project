from django.db import models


class Author(models.Model):
    full_name = models.CharField(max_length=50)
    user_name = models.CharField(max_length=30)

    def __str__(self):
        return self.user_name

