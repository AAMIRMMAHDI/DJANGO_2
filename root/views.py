from django.shortcuts import render, redirect
from .models import Statistic, FAQ, ContactMessage, Service , Experience, Education

from .forms import ContactForm

def home(request):
    experiences = Experience.objects.all().order_by('-start_date')
    educations = Education.objects.all().order_by('-start_date')
    stats = Statistic.objects.first()
    faqs = FAQ.objects.filter(is_active=True)
    services = Service.objects.all()
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save() 
            return redirect('root:home')
    else:
        form = ContactForm()

    context = {
        'stats': stats,
        'faqs': faqs,
        'services': services,
        'form': form,
                'experiences': experiences,
        'educations': educations,
    }
    
    return render(request, 'root/index.html', context)




