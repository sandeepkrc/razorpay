# Generated by Django 3.1.7 on 2021-04-26 06:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('payapp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='coffe',
            name='email',
        ),
    ]
