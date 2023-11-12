# Generated by Django 4.1.6 on 2023-10-24 08:15

from django.db import migrations
import django_countries.fields


class Migration(migrations.Migration):

    dependencies = [
        ('marketplace', '0003_alter_technology_options'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='startup',
            name='location',
        ),
        migrations.AddField(
            model_name='startup',
            name='country',
            field=django_countries.fields.CountryField(default='Nigeria', max_length=225),
        ),
    ]
