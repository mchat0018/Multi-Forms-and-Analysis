from django.shortcuts import render
from .forms import *
from .models import HairProfile,ExternalFactors,Preferences
from formtools.wizard.views import SessionWizardView

FORMS_FOR_HAIR_PROFILE=[
    ('0', TextureForm),
    ('1', StateForm),
    ('3', LengthForm),
    ('4', ThicknessForm),
    ('5', VolumeForm),
    ('6', ScalpForm),
    ('7', DandruffForm),
    ('8', HairLossForm)
]

TEMPLATES_FOR_HAIR_PROFILE={
    '0': 'questionnaire/texture.html',
    '1': 'questionnaire/state.html',
    '2': 'questionnaire/length.html',
    '3': 'questionnaire/thickness.html',
    '4': 'questionnaire/volume.html',
    '5': 'questionnaire/scalp.html',
    '6': 'questionnaire/dandruff.html',
    '7': 'questionnaire/hair_loss.html'
}

class HairProfileWizard(SessionWizardView):
    
    def get_template_names(self):
        return [TEMPLATES_FOR_HAIR_PROFILE[self.steps.current]]
    
    def done(self,form_list,**kwargs):
        pass