from django.db import models

# Create your models here.


class Role(models.TextChoices):
    AUTHORISED = 'AUTHORISED', 'Авторизованный'
    ADMINISTRATOR = 'ADMINISTRATOR', 'Администратор'


class Item(models.Model):
    id = models.IntegerField(primary_key=True, null=False, auto_created=True)
    name = models.CharField(max_length=100, unique=True, null=False)
    price = models.PositiveIntegerField(null=False)
    stock = models.PositiveIntegerField(null=False, default=0)
    description = models.TextField()


class ItemHistory(models.Model):
    dice = models.ForeignKey(Item, on_delete=models.DO_NOTHING)
    name = models.CharField(max_length=100, unique=True, null=False)
    price = models.PositiveIntegerField(null=False)
    description = models.TextField()
    create_at = models.DateTimeField(auto_now=True)
