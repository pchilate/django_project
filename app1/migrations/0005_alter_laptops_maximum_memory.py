# Generated by Django 4.0.3 on 2022-04-25 20:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0004_alter_laptops_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='laptops',
            name='Maximum_memory',
            field=models.IntegerField(choices=[(32, 32), (16, 16), (12, 12), (8, 8), (4, 4)]),
        ),
    ]
