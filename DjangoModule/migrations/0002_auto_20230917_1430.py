# Generated by Django 3.2.13 on 2023-09-17 09:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DjangoModule', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='age',
            field=models.IntegerField(default=1, verbose_name='age'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='student',
            name='department',
            field=models.CharField(default=1, max_length=100, verbose_name='department'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='student',
            name='roll',
            field=models.CharField(default=1, max_length=200, verbose_name='roll'),
            preserve_default=False,
        ),
    ]
