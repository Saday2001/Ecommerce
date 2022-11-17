# Generated by Django 4.1.1 on 2022-09-30 10:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0005_basket'),
    ]

    operations = [
        migrations.CreateModel(
            name='Checkout',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=25)),
                ('last_name', models.CharField(max_length=25)),
                ('kart', models.PositiveIntegerField(max_length=16)),
                ('date', models.DateField()),
                ('kod', models.IntegerField(max_length=3)),
            ],
        ),
    ]