# Generated by Django 2.0.6 on 2018-06-20 19:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_page', '0013_auto_20180621_0004'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='member',
            name='height_field',
        ),
        migrations.RemoveField(
            model_name='member',
            name='width_field',
        ),
        migrations.AlterField(
            model_name='member',
            name='image',
            field=models.ImageField(blank=True, height_field=300, null=True, upload_to='profile', width_field=300),
        ),
    ]
