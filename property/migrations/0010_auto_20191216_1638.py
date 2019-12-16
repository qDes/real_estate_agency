# Generated by Django 2.2.4 on 2019-12-16 13:38

from django.db import migrations

def fill_owners(apps, schema_editor):
    Flat = apps.get_model("property", "Flat")
    Owner = apps.get_model("property", "Owner")
    for flat in Flat.objects.all():
        obj, created = Owner.objects.get_or_create(owner=flat.owner,
                owners_phonenumber=flat.owners_phonenumber,
                owners_phone_pure=flat.owners_phone_pure)
        obj.owners_flats.add(flat)
        obj.save()

class Migration(migrations.Migration):

    dependencies = [
        ('property', '0009_owner'),
    ]

    operations = [
            migrations.RunPython(fill_owners),
    ]
