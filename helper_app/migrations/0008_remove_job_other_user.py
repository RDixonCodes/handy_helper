# Generated by Django 2.2 on 2021-04-26 21:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('helper_app', '0007_auto_20210426_2036'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='job',
            name='other_user',
        ),
    ]
