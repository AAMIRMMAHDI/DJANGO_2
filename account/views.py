from django.shortcuts import render, redirect
from .models import *
from .forms import ContactForm

def home(request):
    resume = Resume.objects.first()  # دریافت اولین رزومه
    services = Service.objects.all()
    context = {
        "stats": Stats.objects.first(),  # دریافت اولین رکورد از Stats
        "skills": Skill.objects.all(),  # دریافت تمام مهارت‌ها
        "resume": resume,
        "experience_list": Experience.objects.filter(resume=resume) if resume else [],  # دریافت تجربیات مرتبط در صورت وجود رزومه
         "services": services
    }
    
    # بررسی اینکه آیا درخواست POST است و فرم تماس ارسال شده است
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()  # ذخیره پیام تماس در دیتابیس

            # ارسال پیام تایید به قالب
            context['message_sent'] = "Your message has been sent successfully!"  # نمایش پیام تایید
            return redirect('home')  # ری‌دایرکت به صفحه اصلی پس از ارسال فرم
        else:
            context['error_message'] = "There was an error with your submission."  # نمایش پیام خطا در صورت بروز مشکل در فرم
    
    else:
        form = ContactForm()  # در صورتی که درخواست GET باشد، فرم خالی نمایش داده می‌شود

    context['form'] = form  # افزودن فرم به context برای نمایش در قالب
    return render(request, "home/index.html", context)
