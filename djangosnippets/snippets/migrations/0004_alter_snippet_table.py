# Generated by Django 3.2.6 on 2021-09-03 01:06

from django.db import migrations


class Migration(migrations.Migration):
    atomic = False

    dependencies = [
        ('snippets', '0003_comment'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='snippet',
            table='snippets',
        ),
    ]
