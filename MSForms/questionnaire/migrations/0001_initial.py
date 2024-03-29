# Generated by Django 3.0.8 on 2020-07-22 13:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ExternalFactors',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dyed_choices', models.CharField(choices=[('yes', 'Yes'), ('no', 'No')], max_length=5)),
                ('colored', models.CharField(choices=[('highligthed', 'Highlighted'), ('permanently', 'Permanent'), ('semi-permanently', 'Semi-Permanent'), ('bleached', 'Bleached')], max_length=20)),
                ('chemical_treatment', models.CharField(choices=[('No', 'Short'), ('Yes1', 'Yes, Straightening or Waving'), ('Yes2', 'Yes, Keratin or Cysteine treatment')], max_length=40)),
                ('appliances', models.CharField(choices=[('dryer', 'Hair Dryer'), ('straightner', 'Hair Straightner'), ('iron', 'Curling Iron'), ('none', 'None')], max_length=20)),
                ('volume', models.CharField(choices=[('low', 'Very low volume'), ('moderate', 'Moderate volume'), ('high', 'Voluminous')], max_length=30)),
                ('style', models.CharField(choices=[('hair_oil', 'Hair Oil'), ('gel', 'Gel or Paste'), ('d_shampoo', 'Dry Shampoo'), ('spray', 'Hair Spray'), ('mousse', 'Mousse'), ('none', 'None')], max_length=20)),
                ('hair_product', models.CharField(max_length=30)),
                ('water_hardness', models.CharField(choices=[('soft', 'Soft'), ('hard', 'Hard'), ('idk', 'I do not know')], max_length=15)),
                ('sunlight_exposure', models.CharField(choices=[('1', '1 hour'), ('1-3', '1-3 hours'), ('>3', 'More than 3 hours')], max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='HairProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('naturally_dried_looks', models.CharField(choices=[('straight', 'Smooth/Straight'), ('wavy', 'Wavy'), ('curly', 'Curly')], max_length=20)),
                ('state', models.CharField(choices=[('dry', 'Dry'), ('normal', 'Normal'), ('oily', 'Oily'), ('oily_dry_ends', 'Oily with dry ends')], max_length=20)),
                ('length', models.CharField(choices=[('short', 'Short'), ('medium', 'Medium(upto shoulders)'), ('Long', 'Long (longer than shoulders)')], max_length=30)),
                ('thickness', models.CharField(choices=[('thin', 'Thin/Finer than Thread'), ('medium', 'Medium/Same as Thread'), ('coarse', 'Coarse/Thicker than thread')], max_length=30)),
                ('volume', models.CharField(choices=[('low', 'Very low volume'), ('moderate', 'Moderate volume'), ('high', 'Voluminous')], max_length=30)),
                ('scalp', models.CharField(choices=[('insensitive', 'Not sensitive'), ('lil_itchy', 'A little bit itchy'), ('itchy', 'Itchy and Painful')], max_length=30)),
                ('dandruff', models.CharField(choices=[('no', 'No'), ('little', 'Little bit'), ('lots', 'A lot')], max_length=30)),
                ('hair_loss', models.CharField(choices=[('low', 'A few hair strands'), ('moderate', 'A dozen hair strands'), ('high', 'More than a dozen hair strands')], max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='Preferences',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hair_goals', models.CharField(choices=[('shine', 'Shine'), ('smooth', 'Smoothness'), ('len', 'Lengthen'), ('vol', 'Volume'), ('thick', 'Thickness'), ('strength', 'Strengthen'), ('split', 'Fix split ends'), ('anti-dry', 'Anti-Dryness'), ('oily', 'Oil COntrol'), ('anti-frizz', 'Anti-Frizz'), ('damage', 'Damage Repair'), ('dandruff', 'Anti-dandruff'), ('color', 'Color Protection'), ('thermal', 'Thermal Protection')], max_length=30)),
                ('product_color', models.CharField(choices=[('peach', 'Peach (with Apricot)'), ('pink', 'Pink (with Strawberry'), ('blue', 'Blue (with Blueberry'), ('green', 'Green (with Avocado)')], max_length=30)),
                ('bottle_name', models.CharField(max_length=8)),
            ],
        ),
    ]
