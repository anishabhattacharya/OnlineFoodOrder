# Generated by Django 3.0.7 on 2020-09-03 03:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pwn', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AdminLoginModel',
            fields=[
                ('username', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('password', models.CharField(max_length=50)),
                ('otp', models.IntegerField(default=1234)),
            ],
        ),
    ]
