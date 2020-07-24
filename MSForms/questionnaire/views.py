from django.shortcuts import render
from .forms import *
from .models import HairProfile,ExternalFactors,Preferences
from formtools.wizard.views import SessionWizardView


FORMS_FOR_HAIR_PROFILE=[
    ('0', TextureForm),
    ('1', StateForm),
    ('2', LengthForm),
    ('3', ThicknessForm),
    ('4', VolumeForm),
    ('5', ScalpForm),
    ('6', DandruffForm),
    ('7', HairLossForm)
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

    def get_form(self,step=None,data=None,files=None):
        form=super().get_form(step,data,files)
        if step is None:
            step=self.steps.current
        if step=='7':
            form.instance.user=self.request.user
        return form
        
    def done(self,form_list,**kwargs):
        pass

FORMS_FOR_EXTERNAL_FACTORS=[
    ('0', DyeForm),
    ('1', ColoredForm),
    ('2', ChemicalTreatmentForm),
    ('3', ApplianceForm),
    ('4', StyleForm),
    ('5', ProductForm),
    ('6', WaterHardnessForm),
    ('7', SunlightExposure)
]

TEMPLATES_FOR_EXTERNAL_FACTORS={
    '0': 'questionnaire/dyed.html',
    '1': 'questionnaire/colored.html',
    '2': 'questionnaire/chemical_treatment.html',
    '3': 'questionnaire/appliances.html',
    '4': 'questionnaire/style.html',
    '5': 'questionnaire/hair_product.html',
    '6': 'questionnaire/water_hardness.html',
    '7': 'questionnaire/sunlight_exposure.html'
}

def check_if_color(wizard):
    cleaned_data=wizard.get_cleaned_data_for_step('0') or {}
    return cleaned_data.get('dyed') == '1'


class ExternalFactorsWizard(SessionWizardView):
    condition_dict={'1':check_if_color}

    def get_template_names(self):
        return [TEMPLATES_FOR_EXTERNAL_FACTORS[self.steps.current]]
    
    def get_form(self,step=None,data=None,files=None):
        form=super().get_form(step,data,files)
        if step is None:
            step=self.steps.current
        if step=='7':
            form.instance.user=self.request.user
        return form
    
    def done(self,form_list,**kwargs):
        pass

FORMS_FOR_PREFERENCES=[
    ('0', HairGoalsForm),
    ('1', ProductColorsForm),
    ('2', BottleNameForm)
]

TEMPLATES_FOR_PREFERENCES={
    '0': 'questionnaire/hair_goals.html',
    '1': 'questionnaire/product_color.html',
    '2': 'questionnaire/bottle_name.html'
}

class PreferencesWizard(SessionWizardView):
    
    def get_template_names(self):
        return [TEMPLATES_FOR_PREFERENCES[self.steps.current]]
    
    def get_form(self,step=None,data=None,files=None):
        form=super().get_form(step,data,files)
        if step is None:
            step=self.steps.current
        if step=='2':
            form.instance.user=self.request.user
        return form
    
    def done(self,form_list,**kwargs):
        pass
