# Generated by Django 4.2.7 on 2023-11-23 14:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='image_alt',
        ),
    ]