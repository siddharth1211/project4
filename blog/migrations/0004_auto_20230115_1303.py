# Generated by Django 3.2.10 on 2023-01-15 07:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20230114_2232'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='no_of_like',
            field=models.IntegerField(blank=True, default=0),
        ),
        migrations.AddField(
            model_name='blog',
            name='no_of_unlike',
            field=models.IntegerField(blank=True, default=0),
        ),
    ]
