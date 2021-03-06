# Generated by Django 4.0.3 on 2022-04-25 07:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='laptops',
            name='Hard_drive_size',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='laptops',
            name='Included_components',
            field=models.CharField(default='\u200eLaptop, Power adapter, User guide, Waranty documents', max_length=80),
        ),
        migrations.AddField(
            model_name='laptops',
            name='USB_2_port',
            field=models.IntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='laptops',
            name='Audio_Details',
            field=models.CharField(default='Speakers , Headphones', max_length=30),
        ),
        migrations.AlterField(
            model_name='laptops',
            name='Graphic_Card_Description',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='laptops',
            name='Maximum_memory',
            field=models.IntegerField(choices=[(16, 16), (12, 12), (8, 8), (4, 4)]),
        ),
        migrations.AlterField(
            model_name='laptops',
            name='Operating_System',
            field=models.CharField(choices=[('Windows 11 Homes', 'Windows 11 Homes'), ('Windows 10', 'Windows 10'), ('Linux', 'Linux'), ('Mac OS', 'Mac OS')], max_length=30),
        ),
        migrations.AlterField(
            model_name='laptops',
            name='Processor_Type',
            field=models.CharField(choices=[('AMD-Series', 'AMD-Series'), ('CORE i3', 'CORE i3'), ('CORE i5', 'CORE i5'), ('CORE i7', 'CORE i7')], max_length=20),
        ),
    ]
