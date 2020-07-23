from django.db import models

class HairProfile(models.Model):
    texture_choices=[
        ('1','Smooth/Straight'),
        ('2','Wavy'),
        ('3','Curly')
    ]
    texture=models.CharField(max_length=1,choices=texture_choices)

    state_choices=[
        ('1','Dry'),
        ('2','Normal'),
        ('3','Oily'),
        ('4','Oily with dry ends')
    ]
    state=models.CharField(max_length=1,choices=state_choices)

    length_choices=[
        ('1','Short'),
        ('2','Medium(upto shoulders)'),
        ('3','Long (longer than shoulders)')
    ]

    length=models.CharField(max_length=1,choices=length_choices)

    thickness_choices=[
        ('1','Thin/Finer than Thread'),
        ('2','Medium/Same as Thread'),
        ('3','Coarse/Thicker than thread')
    ]
    thickness=models.CharField(max_length=1,choices=thickness_choices)

    volume_choices=[
        ('1','Very low volume'),
        ('2','Moderate volume'),
        ('3','Voluminous')
    ]
    volume=models.CharField(max_length=1,choices=volume_choices)

    scalp_choices=[
        ('1','Not sensitive'),
        ('2','A little bit itchy'),
        ('3','Itchy and Painful')
    ]

    scalp=models.CharField(max_length=1,choices=scalp_choices)

    dandruff_choices=[
        ('1','No'),
        ('2','Little bit'),
        ('3','A lot')
    ]
    dandruff=models.CharField(max_length=1,choices=dandruff_choices)

    hair_loss_choices=[
        ('1','A few hair strands'),
        ('2','A dozen hair strands'),
        ('3','More than a dozen hair strands')
    ]
    hair_loss=models.CharField(max_length=1,choices=hair_loss_choices)


class ExternalFactors(models.Model):
    dyed_choices=[
        ('1','Yes'),
        ('2','No'),
    ]
    dyed_choices=models.CharField(max_length=1,choices=dyed_choices)

    colored_choices=[
        ('1','Highlighted'),
        ('2','Permanent'),
        ('3','Semi-Permanent'),
        ('4','Bleached')
    ]
    colored=models.CharField(max_length=1,choices=colored_choices)

    chemical_treatment_choices=[
        ('1','Short'),
        ('2','Yes, Straightening or Waving'),
        ('3','Yes, Keratin or Cysteine treatment')
    ]

    chemical_treatment=models.CharField(max_length=1,choices=chemical_treatment_choices)

    appliance_choices=[
        ('1','Hair Dryer'),
        ('2','Hair Straightner'),
        ('3','Curling Iron'),
        ('4','None')
    ]
    appliances=models.CharField(max_length=1,choices=appliance_choices)

    volume_choices=[
        ('1','Very low volume'),
        ('2','Moderate volume'),
        ('3','Voluminous')
    ]
    volume=models.CharField(max_length=1,choices=volume_choices)

    style_choices=[
        ('1','Hair Oil'),
        ('2','Gel or Paste'),
        ('3','Dry Shampoo'),
        ('4','Hair Spray'),
        ('5','Mousse'),
        ('6','None')
    ]

    style=models.CharField(max_length=1,choices=style_choices)

    hair_product=models.CharField(max_length=30)

    water_hardness_choices=[
        ('1','Soft'),
        ('2','Hard'),
        ('3','I do not know')
    ]
    water_hardness=models.CharField(max_length=1,choices=water_hardness_choices)

    sunlight_exposure_choices=[
       ('1','1 hour'),
       ('2','1-3 hours'),
       ('3','More than 3 hours')
    ]    
    sunlight_exposure=models.CharField(max_length=1,choices=sunlight_exposure_choices)

class Preferences(models.Model):
    goals=[
        ('1','Shine'),('2','Smoothness'),
        ('3','Lengthen'),('4','Volume'),
        ('5','Thickness'),('6','Strengthen'),
        ('7','Fix split ends'),('8','Anti-Dryness'),
        ('9','Oil COntrol'),('10','Anti-Frizz'),
        ('11','Damage Repair'),('12','Anti-dandruff'),
        ('13','Color Protection'),('14','Thermal Protection')
    ]
    hair_goals=models.CharField(max_length=30,choices=goals)

    color_choices=[
        ('1','Peach (with Apricot)'),('2','Pink (with Strawberry'),
        ('3','Blue (with Blueberry'),('4','Green (with Avocado)')
    ]
    product_color=models.CharField(max_length=30,choices=color_choices)

    bottle_name=models.CharField(max_length=8)