# Generated by Django 4.0.2 on 2022-02-01 11:27

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vin', models.CharField(db_index=True, max_length=50, unique=True, verbose_name='Vin')),
                ('color', models.CharField(max_length=50, verbose_name='Color')),
                ('brand', models.CharField(max_length=50, verbose_name='Brand')),
                ('car_type', models.IntegerField(choices=[(1, 'Sedan'), (2, 'Coupe'), (3, 'Sports car'), (4, 'Minivan')], max_length=1, verbose_name='Car type')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='User')),
            ],
        ),
    ]