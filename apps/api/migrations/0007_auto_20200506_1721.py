# Generated by Django 3.0.6 on 2020-05-06 17:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0001_initial'),
        ('api', '0006_auto_20200506_1718'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entry',
            name='owner',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='authentication.User'),
        ),
    ]