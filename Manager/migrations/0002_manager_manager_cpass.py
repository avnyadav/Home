# Generated by Django 2.0.6 on 2018-06-20 07:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Manager', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='manager',
            name='manager_cpass',
            field=models.CharField(default=90, max_length=100),
            preserve_default=False,
        ),
    ]
