# Generated by Django 3.0.6 on 2020-05-06 14:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='entry',
            name='is_public',
            field=models.BooleanField(default=False),
        ),
    ]
