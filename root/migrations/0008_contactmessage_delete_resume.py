# Generated by Django 4.2 on 2025-03-03 21:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('root', '0007_faq'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContactMessage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='نام')),
                ('email', models.EmailField(max_length=254, verbose_name='ایمیل')),
                ('subject', models.CharField(max_length=255, verbose_name='موضوع')),
                ('message', models.TextField(verbose_name='پیام')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='تاریخ ایجاد')),
            ],
            options={
                'verbose_name': 'پیام تماس',
                'verbose_name_plural': 'پیام\u200cهای تماس',
            },
        ),
        migrations.DeleteModel(
            name='Resume',
        ),
    ]
