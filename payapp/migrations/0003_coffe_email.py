# Generated by Django 3.1.7 on 2021-04-26 09:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payapp', '0002_remove_coffe_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='coffe',
            name='email',
            field=models.CharField(default=2, max_length=25),
            preserve_default=False,
        ),
    ]
