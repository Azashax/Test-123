from django.db import models


class User(models.Model):
    name = models.CharField(max_length=128)
    description = models.TextField(null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'user'
        verbose_name_plural = 'users'
