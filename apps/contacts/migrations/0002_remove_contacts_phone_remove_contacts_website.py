# Generated by Django 4.2 on 2023-05-14 11:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contacts',
            name='phone',
        ),
        migrations.RemoveField(
            model_name='contacts',
            name='website',
        ),
    ]