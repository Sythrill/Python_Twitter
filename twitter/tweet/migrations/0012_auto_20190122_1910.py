# Generated by Django 2.0.3 on 2019-01-22 19:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tweet', '0011_user_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='image',
            field=models.FileField(blank=True, upload_to='profile_img'),
        ),
    ]
