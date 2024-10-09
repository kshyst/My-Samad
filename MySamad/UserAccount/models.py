from django.db import models


# Create your models here.

class UserAccount(models.Model):
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    telegram_id = models.CharField(max_length=50)
    token = models.CharField(max_length=50 , null=True)
    refresh_token = models.CharField(max_length=50 , null=True)
    token_expiration = models.DateTimeField(null=True)
    self = models.ManyToOneRel('Self', on_delete=models.CASCADE , to='Self' , field_name='self')

    def __str__(self):
        return self.username


class Self(models.Model):
    name = models.CharField(max_length=50)
    self_id = models.CharField(max_length=50)

    def __str__(self):
        return self.name