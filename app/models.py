from django.db import models

# Create your models here.
class GeneralInfo(models.Model):
    company_name = models.CharField(max_length=100, default='My Company')
    location = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    open_hours = models.CharField(max_length=50, blank=True, null=True)
    video_url = models.URLField(blank=True, null=True)
    twitter_url = models.URLField(blank=True, null=True)
    facebook_url = models.URLField(blank=True, null=True)
    instagram_url = models.URLField(blank=True, null=True)
    linkedin_url = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.company_name
    
class Service(models.Model):
    icon = models.CharField(max_length = 50, blank=True , null=True)
    title = models.CharField(max_length=255,unique=True)
    description = models.TextField()

    def __str__(self):
        return self.title

class Testinomial(models.Model):
    user_name = models.CharField(max_length=50,unique=True)
    user_image = models.CharField(max_length = 255, blank=True, null=True)
    user_role = models.CharField(max_length=150)
    RATING_CHOICES = [(i, str(i)) for i in range(1, 6)]

    rating = models.IntegerField(choices=RATING_CHOICES, blank=True, null=True)
    rivew = models.TextField()
    def __str__(self):
        return f"{self.user_name} - {self.user_role}"


class FrequentlyAskedQuestion(models.Model):
    question = models.CharField(max_length=255)
    answer = models.TextField()

    def __str__(self):
        return self.question