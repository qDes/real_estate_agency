# Generated by Django 2.2.4 on 2019-12-16 13:47

from django.db import migrations

def connect_flats_to_owners(apps, schema_editor):
    Owner = apps.get_model("property", "Owner")
    Flat = apps.get_model("property", "Flat")
    for flat in Flat.objects.all():
        owner, created = Owner.objects.get_or_create(owner=flat.owner_depricated,
                owners_phonenumber=flat.owners_phonenumber)
        flat.owner.add(owner)
        flat.save()


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0012_flat_owner'),
    ]

    operations = [
            migrations.RunPython(connect_flats_to_owners)
    ]
