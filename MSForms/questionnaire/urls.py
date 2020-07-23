from django.contrib import admin
from django.urls import path
from .views import HairProfileWizard,FORMS_FOR_HAIR_PROFILE

urlpatterns=[
    path('hair_profile/',HairProfileWizard.as_view(FORMS_FOR_HAIR_PROFILE),name='hair-profile'),
]