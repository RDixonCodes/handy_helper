# Generated by Django 2.2 on 2021-04-26 22:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('helper_app', '0008_remove_job_other_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='added_job',
            field=models.ManyToManyField(related_name='added_jobs', to='helper_app.User'),
        ),
    ]
