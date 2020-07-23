from django import forms
from .models import HairProfile,ExternalFactors,Preferences

class TextureForm(forms.ModelForm):
    texture=forms.ChoiceField(widget=forms.CheckboxInput,choices=HairProfile.texture_choices)
    
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

