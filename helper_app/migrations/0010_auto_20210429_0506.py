# Generated by Django 2.2 on 2021-04-29 05:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('helper_app', '0009_job_added_job'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='electrical',
            field=models.BooleanField(default='True'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='job',
            name='pet_care',
            field=models.BooleanField(default='True'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='job',
            name='remodel',
            field=models.BooleanField(default='True'),
            preserve_default=False,
        ),
    ]