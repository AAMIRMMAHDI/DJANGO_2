# Generated by Django 4.2 on 2025-03-27 18:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0019_portfolio'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='experience',
            name='resume',
        ),
        migrations.DeleteModel(
            name='Portfolio',
        ),
        migrations.DeleteModel(
            name='Experience',
        ),
        migrations.DeleteModel(
            name='Resume',
        ),
    ]
