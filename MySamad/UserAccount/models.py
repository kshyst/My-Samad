from django.db import models


# Create your models here.

class UserAccount(models.Model):
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    telegramId = models.CharField(max_length=50)
    token = models.CharField(max_length=50)
    refresh_token = models.CharField(max_length=50)
    token_expiration = models.DateTimeField()
    selfs = models.ManyToOneRel('Selfs', on_delete=models.CASCADE)

    def __str__(self):
        return self.username


class Selfs(models.Model):
    name = models.CharField(max_length=50)
    id = models.CharField(max_length=50)

    def __str__(self):
        return self.name