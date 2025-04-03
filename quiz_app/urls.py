from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='home'),                       # home view  
    path('result',views.get_result_and_display,name="get_result_and_display"),            # result view 
]
