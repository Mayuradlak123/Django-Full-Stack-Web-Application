# Generated by Django 3.2.13 on 2023-09-17 06:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='name')),
                ('email', models.CharField(max_length=100, verbose_name='email')),
                ('phone', models.CharField(max_length=100, verbose_name='phone')),
            ],
        ),
    ]
