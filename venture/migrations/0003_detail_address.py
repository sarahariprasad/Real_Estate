# Generated by Django 3.1.2 on 2020-10-15 14:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('venture', '0002_auto_20201015_1857'),
    ]

    operations = [
        migrations.AddField(
            model_name='detail',
            name='address',
            field=models.CharField(default='', max_length=500),
        ),
    ]
