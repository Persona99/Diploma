from django.db import models
from django.contrib.auth.models import AbstractUser
from dice.models import Item
# Create your models here.


class Role(models.TextChoices):
    AUTHORISED = 'AUTHORISED', 'Авторизованный'
    ADMINISTRATOR = 'ADMINISTRATOR', 'Администратор'


class User(AbstractUser):
    role = models.CharField(choices=Role.choices,
                            default=Role.AUTHORISED, max_length=30)


class Comment(models.Model):
    id = models.IntegerField(primary_key=True, null=False, auto_created=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    text = models.TextField()
    rating = models.PositiveSmallIntegerField()
    delete_at = models.DateTimeField(null=True, default=None)
