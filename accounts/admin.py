from django.contrib import admin
from .models import Profile
from django.utils.safestring import mark_safe



@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'get_image', 'phone']
    
    def get_image(self, obj):
        if obj.image:
            return mark_safe(f'<img src="{obj.image.url}" width="150"/')
        else:   
            return 'Not image'
