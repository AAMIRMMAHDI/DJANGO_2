# Generated by Django 4.2 on 2025-03-22 21:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0003_remove_changes_icon_class_changes_icon_file'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Changes',
        ),
    ]
