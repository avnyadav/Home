# Generated by Django 2.0.6 on 2018-06-20 12:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_page', '0008_remove_member_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='member',
            name='image',
            field=models.ImageField(blank=True, upload_to='Profile'),
        ),
    ]
