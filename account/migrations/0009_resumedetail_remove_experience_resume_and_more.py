# Generated by Django 4.2 on 2025-03-23 09:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0008_education_experience_resume_delete_resumeitem_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='ResumeDetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('section_title', models.CharField(max_length=255, verbose_name='عنوان بخش')),
                ('title', models.CharField(max_length=255, verbose_name='عنوان')),
                ('institution', models.CharField(blank=True, max_length=255, null=True, verbose_name='مکان (دانشگاه/شرکت)')),
                ('year', models.CharField(blank=True, max_length=50, null=True, verbose_name='سال')),
                ('description', models.TextField(blank=True, null=True, verbose_name='توضیحات')),
            ],
        ),
        migrations.RemoveField(
            model_name='experience',
            name='resume',
        ),
        migrations.RemoveField(
            model_name='resume',
            name='address',
        ),
        migrations.AddField(
            model_name='resume',
            name='location',
            field=models.CharField(default='', max_length=255, verbose_name='آدرس'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='resume',
            name='email',
            field=models.EmailField(max_length=254, verbose_name='ایمیل'),
        ),
        migrations.AlterField(
            model_name='resume',
            name='name',
            field=models.CharField(max_length=255, verbose_name='نام'),
        ),
        migrations.AlterField(
            model_name='resume',
            name='phone',
            field=models.CharField(max_length=20, verbose_name='تلفن'),
        ),
        migrations.AlterField(
            model_name='resume',
            name='summary',
            field=models.TextField(verbose_name='خلاصه رزومه'),
        ),
        migrations.DeleteModel(
            name='Education',
        ),
        migrations.DeleteModel(
            name='Experience',
        ),
        migrations.AddField(
            model_name='resumedetail',
            name='resume',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='details', to='account.resume'),
        ),
    ]
