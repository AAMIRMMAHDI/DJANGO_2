from django.shortcuts import render, redirect
from .models import FAQ, ContactMessage, Service, Experience, Education
from .forms import ContactForm

def home(request):
    faqs = FAQ.objects.filter(is_active=True)
    services = Service.objects.all()
    experiences = Experience.objects.all()
    educations = Education.objects.all()

    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('root:home')
    else:
        form = ContactForm()

    context = {
        'faqs': faqs,
        'services': services,
        'experiences': experiences,
        'educations': educations,
        'form': form,
    }
    
    return render(request, 'root/index.html', context)
