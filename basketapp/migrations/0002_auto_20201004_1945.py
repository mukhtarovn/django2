# Generated by Django 2.1.5 on 2020-10-04 19:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('basketapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='basket',
            old_name='add_dateime',
            new_name='add_datetime',
        ),
    ]