# Generated by Django 2.1.4 on 2020-05-09 14:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('musicapp', '0002_auto_20200504_1748'),
    ]

    operations = [
        migrations.AddField(
            model_name='artist',
            name='logo_url',
            field=models.URLField(blank=True, max_length=250),
        ),
    ]