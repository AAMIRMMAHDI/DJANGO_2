from django.db import models

class Stats(models.Model):
    happy_clients = models.IntegerField(default=0)
    projects = models.IntegerField(default=0)
    hours_of_support = models.IntegerField(default=0)
    hard_workers = models.IntegerField(default=0)

    def __str__(self):
        return "Statistics"
from django.db import models

class Skill(models.Model):
    title = models.CharField(max_length=100, verbose_name="عنوان")
    percentage = models.IntegerField(verbose_name="درصد", help_text="عدد بین 0 تا 100")

    def __str__(self):
        return f"{self.title} - {self.percentage}%"



from django.db import models

class Resume(models.Model):
    name = models.CharField(max_length=255)
    summary = models.TextField()
    address = models.CharField(max_length=255)
    phone = models.CharField(max_length=20)
    email = models.EmailField()


class Experience(models.Model):
    resume = models.ForeignKey(Resume, on_delete=models.CASCADE, related_name="experience")
    job_title = models.CharField(max_length=255)
    company = models.CharField(max_length=255)
    years = models.CharField(max_length=10)
    description = models.TextField()


from django.db import models

class ContactMessage(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    subject = models.CharField(max_length=255)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Message from {self.name}"




from django.db import models

class Service(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='services', default='services/default0.jpg')
    description = models.TextField()
    
    def __str__(self):
        return self.title







