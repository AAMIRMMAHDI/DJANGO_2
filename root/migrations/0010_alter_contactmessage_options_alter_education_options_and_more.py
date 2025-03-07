# Generated by Django 4.2 on 2025-03-07 16:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('root', '0009_education_experience_service_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='contactmessage',
            options={'verbose_name': 'پیام تماس', 'verbose_name_plural': 'پیام\u200cهای تماس'},
        ),
        migrations.AlterModelOptions(
            name='education',
            options={'verbose_name': 'تحصیلات', 'verbose_name_plural': 'تحصیلات'},
        ),
        migrations.AlterModelOptions(
            name='experience',
            options={'verbose_name': 'تجربه کاری', 'verbose_name_plural': 'تجربه\u200cهای کاری'},
        ),
        migrations.AlterModelOptions(
            name='faq',
            options={'verbose_name': 'سوال متداول', 'verbose_name_plural': 'سوالات متداول'},
        ),
        migrations.AlterModelOptions(
            name='service',
            options={'verbose_name': 'سرویس', 'verbose_name_plural': 'سرویس\u200cها'},
        ),
        migrations.AlterField(
            model_name='contactmessage',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, verbose_name='تاریخ ایجاد'),
        ),
        migrations.AlterField(
            model_name='contactmessage',
            name='email',
            field=models.EmailField(max_length=254, verbose_name='ایمیل'),
        ),
        migrations.AlterField(
            model_name='contactmessage',
            name='message',
            field=models.TextField(verbose_name='پیام'),
        ),
        migrations.AlterField(
            model_name='contactmessage',
            name='name',
            field=models.CharField(max_length=255, verbose_name='نام'),
        ),
        migrations.AlterField(
            model_name='contactmessage',
            name='subject',
            field=models.CharField(max_length=255, verbose_name='موضوع'),
        ),
        migrations.AlterField(
            model_name='education',
            name='degree',
            field=models.CharField(max_length=200, verbose_name='مدرک'),
        ),
        migrations.AlterField(
            model_name='education',
            name='description',
            field=models.TextField(verbose_name='توضیحات'),
        ),
        migrations.AlterField(
            model_name='education',
            name='end_date',
            field=models.DateField(blank=True, null=True, verbose_name='تاریخ پایان'),
        ),
        migrations.AlterField(
            model_name='education',
            name='field_of_study',
            field=models.CharField(max_length=200, verbose_name='رشته تحصیلی'),
        ),
        migrations.AlterField(
            model_name='education',
            name='institution',
            field=models.CharField(max_length=200, verbose_name='مرکز آموزشی'),
        ),
        migrations.AlterField(
            model_name='education',
            name='is_current',
            field=models.BooleanField(default=False, verbose_name='در حال حاضر'),
        ),
        migrations.AlterField(
            model_name='education',
            name='start_date',
            field=models.DateField(verbose_name='تاریخ شروع'),
        ),
        migrations.AlterField(
            model_name='experience',
            name='company',
            field=models.CharField(max_length=200, verbose_name='شرکت'),
        ),
        migrations.AlterField(
            model_name='experience',
            name='description',
            field=models.TextField(verbose_name='توضیحات'),
        ),
        migrations.AlterField(
            model_name='experience',
            name='end_date',
            field=models.DateField(blank=True, null=True, verbose_name='تاریخ پایان'),
        ),
        migrations.AlterField(
            model_name='experience',
            name='is_current',
            field=models.BooleanField(default=False, verbose_name='در حال حاضر'),
        ),
        migrations.AlterField(
            model_name='experience',
            name='position',
            field=models.CharField(max_length=200, verbose_name='موقعیت شغلی'),
        ),
        migrations.AlterField(
            model_name='experience',
            name='start_date',
            field=models.DateField(verbose_name='تاریخ شروع'),
        ),
        migrations.AlterField(
            model_name='faq',
            name='answer',
            field=models.TextField(verbose_name='پاسخ'),
        ),
        migrations.AlterField(
            model_name='faq',
            name='is_active',
            field=models.BooleanField(default=True, verbose_name='فعال'),
        ),
        migrations.AlterField(
            model_name='faq',
            name='question',
            field=models.CharField(max_length=255, verbose_name='سوال'),
        ),
        migrations.AlterField(
            model_name='service',
            name='description',
            field=models.TextField(verbose_name='توضیحات'),
        ),
        migrations.AlterField(
            model_name='service',
            name='image',
            field=models.ImageField(blank=True, default='Default Service', null=True, upload_to='services/', verbose_name='تصویر سرویس'),
        ),
        migrations.AlterField(
            model_name='service',
            name='link',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='لینک به صفحه جزئیات'),
        ),
        migrations.AlterField(
            model_name='service',
            name='title',
            field=models.CharField(max_length=200, verbose_name='عنوان'),
        ),
    ]
