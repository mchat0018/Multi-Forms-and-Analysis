from django.shortcuts import render
from django.urls import reverse
from .forms import *
from .models import HairProfile,ExternalFactors,Preferences
from formtools.wizard.views import SessionWizardView
from django.http import HttpResponseRedirect
# from django.contrib import messages


# FORMS_FOR_HAIR_PROFILE=[
#     ('0', TextureForm),
#     ('1', StateForm),
#     ('2', LengthForm),
#     ('3', ThicknessForm),
#     ('4', VolumeForm),
#     ('5', ScalpForm),
#     ('6', DandruffForm),
#     ('7', HairLossForm)
# ]

# TEMPLATES_FOR_HAIR_PROFILE={
#     '0': 'questionnaire/texture.html',
#     '1': 'questionnaire/state.html',
#     '2': 'questionnaire/length.html',
#     '3': 'questionnaire/thickness.html',
#     '4': 'questionnaire/volume.html',
#     '5': 'questionnaire/scalp.html',
#     '6': 'questionnaire/dandruff.html',
#     '7': 'questionnaire/hair_loss.html'
# }

# class HairProfileWizard(SessionWizardView):
    
#     def get_template_names(self):
#         return [TEMPLATES_FOR_HAIR_PROFILE[self.steps.current]]

#     def get_form(self,step=None,data=None,files=None):
#         form=super().get_form(step,data,files)
#         if step is None:
#             step=self.steps.current
#         if step=='7':
#             form.instance.user=self.request.user
#         return form

#     def get(self, request, *args, **kwargs):
#         try:
#             return self.render(self.get_form())
#         except KeyError:
#             return super().get(request, *args, **kwargs)
        
#     def done(self,form_list,form_dict,**kwargs):
#         obj=HairProfile()
#         obj.texture=form_dict['0'].save()
#         obj.state=form_dict['1'].save()
#         obj.length=form_dict['2'].save()
#         obj.thickness=form_dict['3'].save()
#         obj.volume=form_dict['4'].save()
#         obj.scalp=form_dict['5'].save()
#         obj.dandruff=form_dict['6'].save()
#         obj.hair_loss=form_dict['7'].save()
#         obj.user=self.request.user
        
#         obj.save()
#         return reverse('external-factors')

# def HairProfileView(request):
#     if request.method=='POST':
#         form1=TextureForm(request.POST)
#         form2=StateForm(request.POST)
#         form3=LengthForm(request.POST)
#         form4=ThicknessForm(request.POST)
#         form5=VolumeForm(request.POST)
#         form6=ScalpForm(request.POST)
#         form7=DandruffForm(request.POST)
#         form8=HairLossForm(request.POST)

#         obj=HairProfile(texture=form1.save(),state=form2.save(),length=form3.save(),thickness=form4.save(),volume=form5.save(),scalp=form6.save(),dandruff=form7.save(),hair_loss=form8.save(),user=request.user)
#         obj.save()
#         return HttpResponseRedirect(reverse('external-factors'))

#     else:
#         form1=TextureForm()
#         form2=StateForm()
#         form3=LengthForm()
#         form4=ThicknessForm()
#         form5=VolumeForm()
#         form6=ScalpForm()
#         form7=DandruffForm()
#         form8=HairLossForm()

#     context={
#         'form1':form1,'form2':form2,'form3':form3,'form4':form4,'form5':form5,'form6':form6,'form7':form7,'form8':form8
#     }
#     return render(request,'questionnaire/index.html',context)

def hairProfileSave(request):
    if request.method=='POST':
        texture=request.POST.get('texture')
        state=request.POST.get('state')
        length=request.POST.get('length')
        thickness=request.POST.get('thickness')
        volume=request.POST.get('volume')
        scalp=request.POST.get('scalp')
        dandruff=request.POST.get('dandruff')
        hair_loss=request.POST.get('hair_loss')

        obj=HairProfile(texture=texture,state=state,length=length,thickness=thickness,volume=volume,scalp=scalp,dandruff=dandruff,hair_loss=hair_loss)
        obj.save()
        return HttpResponseRedirect(reverse('external-factors'))
    
    return render(request,'questionnaire/index2.html')


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

    def get(self, request, *args, **kwargs):
        try:
            return self.render(self.get_form())
        except KeyError:
            return super().get(request, *args, **kwargs)
    
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
