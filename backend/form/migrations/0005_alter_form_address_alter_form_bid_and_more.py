# Generated by Django 4.0.2 on 2022-02-25 21:40

import django.core.validators
from django.db import migrations, models
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('form', '0004_alter_form_address_alter_form_bid_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='form',
            name='address',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='form',
            name='bid',
            field=models.CharField(choices=[('high', 'HIGH'), ('medium', 'MEDIUM'), ('low', 'LOW')], max_length=6),
        ),
        migrations.AlterField(
            model_name='form',
            name='company_name',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='form',
            name='dob',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='form',
            name='first_name',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='form',
            name='google_id',
            field=models.BigIntegerField(),
        ),
        migrations.AlterField(
            model_name='form',
            name='surname',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='form',
            name='telephone',
            field=phonenumber_field.modelfields.PhoneNumberField(max_length=17, region=None, unique=True, validators=[django.core.validators.RegexValidator(message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.", regex='^\\+?1?\\d{9,15}$')]),
        ),
        migrations.AlterField(
            model_name='form',
            name='title',
            field=models.CharField(max_length=20),
        ),
    ]
