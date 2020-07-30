from django.shortcuts import render
from django.urls import reverse
# from .forms import *
from .models import HairProfile,ExternalFactors,Preferences
# from formtools.wizard.views import SessionWizardView
from django.http import HttpResponseRedirect

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

        obj=HairProfile(texture=texture,state=state,length=length,thickness=thickness,volume=volume,scalp=scalp,dandruff=dandruff,hair_loss=hair_loss, user=request.user)
        obj.save()
        return HttpResponseRedirect(reverse('external-factors'))
    
    return render(request,'questionnaire/index.html')

def externalFactorsSave(request):
    if request.method=='POST':
        dyed=request.POST.get('dyed')
        colored=request.POST.get('colored')
        chemical_treatment=request.POST.get('chemical_treatment')
        appliances=request.POST.get('appliances')
        style=request.POST.get('style')
        hair_product=request.POST.get('hair_product')
        water_hardness=request.POST.get('water_hardness')
        sunlight_exposure=request.POST.get('sunlight_exposure')

        obj=ExternalFactors(dyed=dyed,colored=colored,chemical_treatment=chemical_treatment,appliances=appliances,style=style,hair_product=hair_product,water_hardness=water_hardness,sunlight_exposure=sunlight_exposure, user=request.user)
        obj.save()
        return HttpResponseRedirect(reverse('preferences'))
    
    return render(request,'questionnaire/index2.html')    

def preferenceSave(request):
    if request.method=="POST":
        hair_goals=request.POST.get('hair_goals')
        product_color=request.POST.get('product_color')
        bottle_name=request.POST.get('bottle_name')

        obj=Preferences(hair_goals=hair_goals,product_color=product_color,bottle_name=bottle_name,user=request.user)
        obj.save()
        return HttpResponseRedirect(reverse('outcome'))

    return render(request,'questionnaire.index3.html')
