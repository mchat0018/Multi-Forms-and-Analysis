# Generated by Django 3.0.8 on 2020-07-23 10:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('questionnaire', '0002_auto_20200723_1136'),
    ]

    operations = [
        migrations.RenameField(
            model_name='externalfactors',
            old_name='dyed_choices',
            new_name='dyed',
        ),
        migrations.RemoveField(
            model_name='externalfactors',
            name='volume',
        ),
    ]