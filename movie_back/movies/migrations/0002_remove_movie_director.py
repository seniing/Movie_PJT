# Generated by Django 3.2.12 on 2022-05-18 16:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='movie',
            name='director',
        ),
    ]
