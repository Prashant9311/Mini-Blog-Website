# Generated by Django 2.2.10 on 2020-05-14 02:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_myuser_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myuser',
            name='profile_image',
            field=models.ImageField(blank=True, default='profile-default.jpg', upload_to='account/profile_pic'),
        ),
    ]