# Generated by Django 2.2.10 on 2020-05-13 19:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_post_author'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='slug',
            field=models.CharField(blank=True, max_length=60, unique=True),
        ),
    ]