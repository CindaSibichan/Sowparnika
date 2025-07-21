
from django.urls import path,include
from . views import *


urlpatterns = [
    path('contact-info/',ContactSubmissionAPIView.as_view(),name='contact-info'),
   
]