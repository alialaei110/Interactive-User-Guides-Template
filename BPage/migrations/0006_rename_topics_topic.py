# Generated by Django 4.2.3 on 2023-07-20 07:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('BPage', '0005_rename_devices_topics'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Topics',
            new_name='Topic',
        ),
    ]