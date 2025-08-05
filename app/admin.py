from django.contrib import admin

# Register your models here.
from app.models import GeneralInfo

@admin.register(GeneralInfo)
class GeneralInfoAdmin(admin.ModelAdmin):
    pass  # You can customize the admin interface here if needed