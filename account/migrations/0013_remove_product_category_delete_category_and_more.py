# Generated by Django 4.2 on 2025-03-23 09:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0012_product_category_description_alter_category_name_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='category',
        ),
        migrations.DeleteModel(
            name='Category',
        ),
        migrations.DeleteModel(
            name='Product',
        ),
    ]
