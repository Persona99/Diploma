from django.db import models
from user.models import User
from dice.models import Item
# Create your models here.


class Status(models.TextChoices):
    CREATED = 'CREATED', 'Создан'
    PAID = 'PAID', 'Оплачен'
    PROCESSING = 'PROCESSING', 'В процессе'
    DELIVERY = 'DELIVERY', 'Доставляется'
    FINISHED = 'FINISHED', 'Доставлен'
    CANCELLED = 'CANCELLED', 'Отменен'


class Order(models.Model):
    id = models.IntegerField(primary_key=True, null=False, auto_created=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.CharField(
        choices=Status, default=Status.CREATED, max_length=30)


class UserOrder(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)


class OrderHistory(models.Model):
    order = models.ForeignKey(Order, on_delete=models.DO_NOTHING)
    status = models.CharField(choices=Status, max_length=30)
    create_at = models.DateTimeField(auto_now=True)
