# Generated by Django 3.0.6 on 2020-05-06 00:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Entry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('mood', models.CharField(choices=[('😊', 'happy'), ('😢', 'sad'), ('😡', 'angry'), ('🥰', 'loved'), ('🙄', 'annoyed'), ('🙃', 'confused')], default='happy', max_length=50)),
                ('weather', models.CharField(choices=[('☀️', 'sunny'), ('☁️', 'cloudy'), ('🌧', 'raining')], default='sunny', max_length=50)),
                ('text', models.TextField()),
            ],
            options={
                'verbose_name': 'Entry',
                'verbose_name_plural': 'Entries',
            },
        ),
    ]
