# Generated by Django 3.0.8 on 2020-07-31 16:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questionnaire', '0014_auto_20200731_2139'),
    ]

    operations = [
        migrations.AlterField(
            model_name='preferences',
            name='product_color',
            field=models.CharField(choices=[('1', 'Peach (with Apricot)'), ('2', 'Pink (with Strawberry'), ('3', 'Blue (with Blueberry'), ('4', 'Green (with Avocado)')], max_length=1),
        ),
    ]
