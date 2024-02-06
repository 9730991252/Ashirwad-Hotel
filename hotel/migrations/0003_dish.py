# Generated by Django 5.0.1 on 2024-02-03 04:03

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotel', '0002_dish_category'),
    ]

    operations = [
        migrations.CreateModel(
            name='Dish',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dish_name', models.CharField(max_length=100)),
                ('dish_marathi_name', models.CharField(default=True, max_length=100)),
                ('price', models.FloatField(default=0)),
                ('added_date', models.DateTimeField(auto_now_add=True, null=True)),
                ('status', models.IntegerField(default=1)),
                ('added_by', models.ForeignKey(default=True, on_delete=django.db.models.deletion.PROTECT, to='hotel.admin')),
                ('dish_category', models.ForeignKey(default=True, on_delete=django.db.models.deletion.PROTECT, to='hotel.dish_category')),
            ],
        ),
    ]
