# Generated by Django 2.0.6 on 2018-06-20 18:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_page', '0012_auto_20180621_0001'),
    ]

    operations = [
        migrations.AddField(
            model_name='member',
            name='height_field',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='member',
            name='width_field',
            field=models.IntegerField(default=0),
        ),
    ]