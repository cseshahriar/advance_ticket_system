# Generated by Django 3.1.6 on 2021-02-01 16:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tickets', '0003_auto_20210201_2255'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='priority',
            options={'verbose_name': 'priority', 'verbose_name_plural': 'priorities'},
        ),
    ]
