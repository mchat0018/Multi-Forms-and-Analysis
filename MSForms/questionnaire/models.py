from django.db import models

class HairProfile(models.Model):
    naturally_dried_choices=[
        ('straight','Smooth/Straight'),
        ('wavy','Wavy'),
        ('curly','Curly')
    ]
    naturally_dried_looks=models.CharField(max_length=20,choices=naturally_dried_choices)

    state_choices=[
        ('dry','Dry'),
        ('normal','Normal'),
        ('oily','Oily'),
        ('oily_dry_ends','Oily with dry ends')
    ]
    state=models.CharField(max_length=20,choices=state_choices)

    length_choices=[
        ('short','Short'),
        ('medium','Medium(upto shoulders)'),
        ('Long','Long (longer than shoulders)')
    ]

    length=models.CharField(max_length=30,choices=length_choices)

    thickness_choices=[
        ('thin','Thin/Finer than Thread'),
        ('medium','Medium/Same as Thread'),
        ('coarse','Coarse/Thicker than thread')
    ]
    thickness=models.CharField(max_length=30,choices=thickness_choices)

    volume_choices=[
        ('low','Very low volume'),
        ('moderate','Moderate volume'),
        ('high','Voluminous')
    ]
    volume=models.CharField(max_length=30,choices=volume_choices)

    scalp_choices=[
        ('insensitive','Not sensitive'),
        ('lil_itchy','A little bit itchy'),
        ('itchy','Itchy and Painful')
    ]

    scalp=models.CharField(max_length=30,choices=scalp_choices)

    dandruff_choices=[
        ('no','No'),
        ('little','Little bit'),
        ('lots','A lot')
    ]
    dandruff=models.CharField(max_length=30,choices=dandruff_choices)

    hair_loss_choices=[
        ('low','A few hair strands'),
        ('moderate','A dozen hair strands'),
        ('high','More than a dozen hair strands')
    ]
    hair_loss=models.CharField(max_length=40,choices=hair_loss_choices)


class ExternalFactors(models.Model):
    dyed_choices=[
        ('yes','Yes'),
        ('no','No'),
        ]
    dyed_choices=models.CharField(max_length=5,choices=dyed_choices)

    colored_choices=[
        ('highligthed','Highlighted'),
        ('permanently','Permanent'),
        ('semi-permanently','Semi-Permanent'),
        ('bleached','Bleached')
    ]
    colored=models.CharField(max_length=20,choices=colored_choices)

    chemical_treatment_choices=[
        ('No','Short'),
        ('Yes1','Yes, Straightening or Waving'),
        ('Yes2','Yes, Keratin or Cysteine treatment')
    ]

    chemical_treatment=models.CharField(max_length=40,choices=chemical_treatment_choices)

    appliance_choices=[
        ('dryer','Hair Dryer'),
        ('straightner','Hair Straightner'),
        ('iron','Curling Iron'),
        ('none','None')
    ]
    appliances=models.CharField(max_length=20,choices=appliance_choices)

    volume_choices=[
        ('low','Very low volume'),
        ('moderate','Moderate volume'),
        ('high','Voluminous')
    ]
    volume=models.CharField(max_length=30,choices=volume_choices)

    style_choices=[
        ('hair_oil','Hair Oil'),
        ('gel','Gel or Paste'),
        ('d_shampoo','Dry Shampoo'),
        ('spray','Hair Spray'),
        ('mousse','Mousse'),
        ('none','None')
    ]

    style=models.CharField(max_length=20,choices=style_choices)

    hair_product=models.CharField(max_length=30)

    water_hardness_choices=[
        ('soft','Soft'),
        ('hard','Hard'),
        ('idk','I do not know')
    ]
    water_hardness=models.CharField(max_length=15,choices=water_hardness_choices)

    sunlight_exposure_choices=[
       ('1','1 hour'),
       ('1-3','1-3 hours'),
       ('>3','More than 3 hours')
    ]    
    sunlight_exposure=models.CharField(max_length=20,choices=sunlight_exposure_choices)

class Preferences(models.Model):
    goals=[
        ('shine','Shine'),('smooth','Smoothness'),
        ('len','Lengthen'),('vol','Volume'),
        ('thick','Thickness'),('strength','Strengthen'),
        ('split','Fix split ends'),('anti-dry','Anti-Dryness'),
        ('oily','Oil COntrol'),('anti-frizz','Anti-Frizz'),
        ('damage','Damage Repair'),('dandruff','Anti-dandruff'),
        ('color','Color Protection'),('thermal','Thermal Protection')
    ]
    hair_goals=models.CharField(max_length=30,choices=goals)

    color_choices=[
        ('peach','Peach (with Apricot)'),('pink','Pink (with Strawberry'),
        ('blue','Blue (with Blueberry'),('green','Green (with Avocado)')
    ]
    product_color=models.CharField(max_length=30,choices=color_choices)

    bottle_name=models.CharField(max_length=8)