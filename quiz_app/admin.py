from django.contrib import admin
from .models import Questions
# Register your models here.

class admin_extender(admin.ModelAdmin):
    list_display = ['questions','option_a','option_b','option_c','option_d','answer']


admin.site.register(Questions,admin_extender)               # registering the model in the admin site to access it using django default admin pannel 

