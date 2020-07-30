from django.contrib import admin
from django.urls import path
from .views import hairProfileSave,externalFactorsSave,preferenceSave   

urlpatterns=[
    path('hair_profile/',hairProfileSave,name='hair-profile'),
    path('external_factors/',externalFactorsSave,name='external-factors'),
    path('preferences/',preferenceSave,name='preferences'),
]
