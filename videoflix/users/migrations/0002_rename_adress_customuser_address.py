# Generated by Django 5.1 on 2024-08-28 20:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customuser',
            old_name='adress',
            new_name='address',
        ),
    ]
