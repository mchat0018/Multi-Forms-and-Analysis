from django import forms
from .models import HairProfile,ExternalFactors,Preferences

class TextureForm(forms.ModelForm):
    texture=forms.ChoiceField(widget=forms.RadioSelect,choices=HairProfile.texture_choices)
    
    class Meta:
        model=HairProfile
        fields=['texture']

class StateForm(forms.ModelForm):
        
    class Meta:
        model=HairProfile
        fields=['state']

class LengthForm(forms.ModelForm):
       
    class Meta:
        model=HairProfile
        fields=['length']

class ThicknessForm(forms.ModelForm):
       
    class Meta:
        model=HairProfile
        fields=['thickness']


class VolumeForm(forms.ModelForm):
       
    class Meta:
        model=HairProfile
        fields=['volume']

class ScalpForm(forms.ModelForm):
    
    class Meta:
        model=HairProfile
        fields=['scalp']

class DandruffForm(forms.ModelForm):

    class Meta:
        model=HairProfile
        fields=['dandruff']

class HairLossForm(forms.ModelForm):
    
    class Meta:
        model=HairProfile
        fields=['hair_loss']


class DyeForm(forms.ModelForm):
    
    class Meta:
        model=ExternalFactors
        fields=['dyed']

class ColoredForm(forms.ModelForm):
    
    class Meta:
        model=ExternalFactors
        fields=['colored']

class ChemicalTreatmentForm(forms.ModelForm):
    
    class Meta:
        model=ExternalFactors
        fields=['chemical_treatment']

class ApplianceForm(forms.ModelForm):
    appliances=forms.ChoiceField(widget=forms.RadioSelect,choices=ExternalFactors.appliance_choices)

    class Meta:
        model=ExternalFactors
        fields=['appliances']

class StyleForm(forms.ModelForm):
    style=forms.ChoiceField(widget=forms.RadioSelect,choices=ExternalFactors.style_choices)

    class Meta:
        model=ExternalFactors
        fields=['style']

class ProductForm(forms.ModelForm):
    
    class Meta:
        model=ExternalFactors
        fields=['hair_product']

class WaterHardnessForm(forms.ModelForm):

    class Meta:
        model=ExternalFactors
        fields=['water_hardness']

class SunlightExposure(forms.ModelForm):

    class Meta:
        model=ExternalFactors
        fields=['sunlight_exposure']

    
class HairGoalsForm(forms.ModelForm):
    hair_goals=forms.ChoiceField(widget=forms.RadioSelect,choices=Preferences.goals)

    class Meta:
        model=Preferences
        fields=['hair_goals']

class ProductColorsForm(forms.ModelForm):
    product_color=forms.ChoiceField(widget=forms.RadioSelect,choices=Preferences.color_choices)

    class Meta:
        model=Preferences
        fields=['product_color']

class BottleNameForm(forms.ModelForm):
    class Meta:
        model=Preferences
        fields=['bottle_name']