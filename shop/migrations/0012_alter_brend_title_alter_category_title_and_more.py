# Generated by Django 4.1.1 on 2022-11-15 09:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0011_remove_clothes_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='brend',
            name='title',
            field=models.CharField(max_length=25, verbose_name='Ad'),
        ),
        migrations.AlterField(
            model_name='category',
            name='title',
            field=models.CharField(max_length=25, verbose_name='Ad'),
        ),
        migrations.AlterField(
            model_name='color',
            name='title',
            field=models.CharField(max_length=25, verbose_name='Ad'),
        ),
        migrations.AlterField(
            model_name='gender',
            name='title',
            field=models.CharField(max_length=25, verbose_name='Ad'),
        ),
        migrations.AlterField(
            model_name='subb_category',
            name='title',
            field=models.CharField(max_length=25, verbose_name='Ad'),
        ),
    ]
