# Generated by Django 2.2.4 on 2019-12-16 13:23

import phonenumbers
from django.db import migrations


def fill_owner_phone_pure(apps, schema_editor):
    Flat = apps.get_model("property", "Flat")
    for flat in Flat.objects.all():
        number = phonenumbers.parse(flat.owners_phonenumber, "RU")
        if phonenumbers.is_valid_number(number):
            raw = phonenumbers.format_number(number, 
                                             phonenumbers.PhoneNumberFormat.E164)
            flat.owners_phone_pure = raw
        flat.save()


def move_backward(apps, schema_editor):
    Flat = apps.get_model("property", "Flat")
    for flat in Flat.objects.all():
        flat.owners_phone_pure = None
        flat.save()


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0007_flat_owners_phone_pure'),
    ]

    operations = [
            migrations.RunPython(fill_owner_phone_pure, move_backward),
    ]
