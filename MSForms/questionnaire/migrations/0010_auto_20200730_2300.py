# Generated by Django 3.0.8 on 2020-07-30 17:30

from django.db import migrations
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('questionnaire', '0009_auto_20200725_1122'),
    ]

    operations = [
        migrations.AlterField(
            model_name='preferences',
            name='hair_goals',
            field=multiselectfield.db.fields.MultiSelectField(choices=[('1', 'Shine'), ('2', 'Smoothness'), ('3', 'Lengthen'), ('4', 'Volume'), ('5', 'Thickness'), ('6', 'Strengthen'), ('7', 'Fix split ends'), ('8', 'Anti-Dryness'), ('9', 'Oil COntrol'), ('10', 'Anti-Frizz'), ('11', 'Damage Repair'), ('12', 'Anti-dandruff'), ('13', 'Color Protection'), ('14', 'Thermal Protection')], max_length=2),
        ),
        migrations.AlterField(
            model_name='preferences',
            name='product_color',
            field=multiselectfield.db.fields.MultiSelectField(choices=[('1', 'Peach (with Apricot)'), ('2', 'Pink (with Strawberry'), ('3', 'Blue (with Blueberry'), ('4', 'Green (with Avocado)')], max_length=1),
        ),
    ]