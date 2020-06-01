from django.db import models


class User(models.Model):
    mail = models.EmailField()
    password = models.CharField(max_length=24)


class Dollar(models.Model):
    buy_price = models.DecimalField(decimal_places=2, max_digits=30)
    sell_price = models.DecimalField(decimal_places=2, max_digits=30)
    issue_date = models.DateTimeField()
    origin = models.CharField(max_length=200)
