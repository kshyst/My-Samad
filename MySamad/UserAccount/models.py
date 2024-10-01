from django.db import models

# Create your models here.

class UserAccount(models.Model):
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    telegramId = models.CharField(max_length=50)
    token = models.CharField(max_length=50)
    refresh_token = models.CharField(max_length=50)
    token_expiration = models.DateTimeField()

    def __str__(self):
        return self.username