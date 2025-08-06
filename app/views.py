from django.shortcuts import render
from app.models import GeneralInfo,Service


# Create your views here.
def index(request):
    general_info = GeneralInfo.objects.first()  # Get the first GeneralInfo object
    
    services = Service.objects.all()


    context = {
        'company_name': general_info.company_name,
        'location': general_info.location,
        'email': general_info.email,
        'phone': general_info.phone ,
        'open_hours': general_info.open_hours ,
        'video_url': general_info.video_url ,
        'twitter_url': general_info.twitter_url ,
        'facebook_url': general_info.facebook_url ,
        'instagram_url': general_info.instagram_url ,
        'linkedin_url': general_info.linkedin_url ,

        "services" : services
    }

    print(f"general_info : {context}")

    return render(request,"index.html", context)