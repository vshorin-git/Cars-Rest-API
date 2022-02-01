from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model

class Car(models.Model):
    vin = models.CharField(verbose_name='Vin', db_index=True, unique=True, max_length=50)
    color = models.CharField(verbose_name='Color', max_length=50)
    brand = models.CharField(verbose_name='Brand', max_length=50)
    CAR_TYPES = (
        (1, 'Sedan'),
        (2, 'Coupe'),
        (3, 'Sports car'),
        (4, 'Minivan'),
    )
    car_type = models.IntegerField(verbose_name='Car type', choices=CAR_TYPES, max_length=1)
    user = models.ForeignKey(User, verbose_name='User', on_delete=models.CASCADE)


