from django.contrib import admin

# Register your models here.
from app.models import GeneralInfo

@admin.register(GeneralInfo)
class GeneralInfoAdmin(admin.ModelAdmin):
    
    list_display = [
        'company_name', 'location', 'email', 'phone', 'open_hours',
    ]  # You can customize the admin interface here if needed

    # show to diable add permission
    def has_add_permission(self, request, obj=None):
        return False
    
    # show to diable change permission
    def has_change_permission(self, request, obj=None):
        return False
    
    def has_delete_permission(self, request, obj=None):
        return False                