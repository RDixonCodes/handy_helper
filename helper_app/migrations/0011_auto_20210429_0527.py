# Generated by Django 2.2 on 2021-04-29 05:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('helper_app', '0010_auto_20210429_0506'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='job',
            name='electrical',
        ),
        migrations.RemoveField(
            model_name='job',
            name='pet_care',
        ),
        migrations.RemoveField(
            model_name='job',
            name='remodel',
        ),
    ]
