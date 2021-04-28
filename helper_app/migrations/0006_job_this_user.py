# Generated by Django 2.2 on 2021-04-26 19:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('helper_app', '0005_auto_20210426_1626'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='this_user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='this_user_job', to='helper_app.User'),
            preserve_default=False,
        ),
    ]
