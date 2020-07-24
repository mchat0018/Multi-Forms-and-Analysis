from django.contrib import admin
from django.urls import path
from .views import ( HairProfileWizard,
                FORMS_FOR_HAIR_PROFILE,
                ExternalFactorsWizard,
                FORMS_FOR_EXTERNAL_FACTORS,
                PreferencesWizard,
                FORMS_FOR_PREFERENCES
                )   

urlpatterns=[
    path('hair_profile/',HairProfileWizard.as_view(FORMS_FOR_HAIR_PROFILE),name='hair-profile'),
    path('external_factors/',ExternalFactorsWizard.as_view(FORMS_FOR_EXTERNAL_FACTORS),name='external-factors'),
    path('preferences/',PreferencesWizard.as_view(FORMS_FOR_PREFERENCES),name='preferences'),
]