from django.contrib import admin
from .models import *

@admin.register(Statistic)
class StatisticAdmin(admin.ModelAdmin):
    list_display = ('years_experience', 'projects_completed', 'happy_clients')


admin.site.register(Service)
admin.site.register(FAQ)
admin.site.register(ContactMessage)
admin.site.register(Experience)
admin.site.register(Education)

