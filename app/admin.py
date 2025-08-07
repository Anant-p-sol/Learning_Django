from django.contrib import admin

# Register your models here.
from app.models import (GeneralInfo,
                        Service,
                        Testinomial,
                        FrequentlyAskedQuestion
                        )

@admin.register(GeneralInfo)
class GeneralInfoAdmin(admin.ModelAdmin):
    
    list_display = [
        'company_name', 'location', 'email', 'phone', 'open_hours',
    ]  # You can customize the admin interface here if needed

    # # show to diable add permission
    # def has_add_permission(self, request, obj=None):
    #     return False
    
    # # show to diable change permission
    # def has_change_permission(self, request, obj=None):
    #     return False
    
    # def has_delete_permission(self, request, obj=None):
    #     return False

    # show to change permission
    readonly_fields = [
        'email', 'phone'
        ]


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = [
        'title','description'
    ] 

    search_fields = [
        'title',
        'description'
    ]


@admin.register(Testinomial)
class Testinomial(admin.ModelAdmin):
    list_display = [
        "user_name",
        "user_role",
        "Display_star",
    ] 

    def Display_star(self,obj):
        return "*" * obj.rating
    
    Display_star.short_description = "rating"


@admin.register(FrequentlyAskedQuestion)
class FrequentlyAskedQuestionAdmin(admin.ModelAdmin):
    list_display = [
        'question', 'answer'
    ]

    search_fields = [
        'question',
        'answer'
    ]