# Generated by Django 3.0.8 on 2020-07-24 09:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questionnaire', '0005_auto_20200724_1503'),
    ]

    operations = [
        migrations.AlterField(
            model_name='externalfactors',
            name='appliances',
            field=models.CharField(choices=[('HD', 'Hair Dryer'), ('HS', 'Hair Straightner'), ('CI', 'Curling Iron'), ('None', 'None')], max_length=4),
        ),
        migrations.AlterField(
            model_name='externalfactors',
            name='style',
            field=models.CharField(choices=[('HO', 'Hair Oil'), ('GP', 'Gel or Paste'), ('DS', 'Dry Shampoo'), ('HS', 'Hair Spray'), ('MS', 'Mousse'), ('None', 'None')], max_length=4),
        ),
    ]
