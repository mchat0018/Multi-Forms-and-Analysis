# Generated by Django 3.0.8 on 2020-07-24 09:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questionnaire', '0004_auto_20200724_1239'),
    ]

    operations = [
        migrations.AlterField(
            model_name='externalfactors',
            name='chemical_treatment',
            field=models.CharField(choices=[('1', 'No'), ('2', 'Yes, Straightening or Waving'), ('3', 'Yes, Keratin or Cysteine treatment')], max_length=1),
        ),
    ]
