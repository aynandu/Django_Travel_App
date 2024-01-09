from . import views
from django.urls import path

urlpatterns = [
    path('',views.demo,name='demo'), # '' = http://127.0.0.1:8000/
    
   # path('about/',views.about,name='about'),# 'about/' = http://127.0.0.1:8000/about/
   # path('contact/',views.contact,name='contact'),
    #path('resultpage/',views.Result,name='result')
    
]
