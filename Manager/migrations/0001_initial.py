# Generated by Django 2.0.6 on 2018-06-20 06:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Manager',
            fields=[
                ('manager_id', models.CharField(max_length=8, primary_key=True, serialize=False)),
                ('manager_name', models.CharField(max_length=100)),
                ('manager_pass', models.CharField(max_length=100)),
                ('manager_email', models.EmailField(blank=True, max_length=254)),
            ],
        ),
    ]
