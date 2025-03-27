from django.contrib import admin
from .models import Stats

admin.site.register(Stats)
from django.contrib import admin
from .models import *

@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ("title", "percentage")
    search_fields = ("title",)


from django.contrib import admin
from .models import Resume, Experience



class ExperienceInline(admin.TabularInline):
    model = Experience
    extra = 1  # امکان اضافه کردن چندین تجربه کاری

class ResumeAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "phone")  # نمایش این اطلاعات در لیست
    inlines = [ExperienceInline]  # نمایش آموزش و تجربه در صفحه ویرایش

# ثبت مدل در پنل ادمین
admin.site.register(Resume, ResumeAdmin)


from django.contrib import admin
from .models import ContactMessage

@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'subject', 'created_at')
    search_fields = ('name', 'email', 'subject')


from django.contrib import admin
from .models import Service

admin.site.register(Service)

