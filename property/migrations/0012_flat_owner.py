# Generated by Django 2.2.4 on 2019-12-16 13:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0011_auto_20191216_1646'),
    ]

    operations = [
        migrations.AddField(
            model_name='flat',
            name='owner',
            field=models.ManyToManyField(to='property.Owner', verbose_name='Владелец'),
        ),
    ]
