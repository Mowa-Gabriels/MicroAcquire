# Generated by Django 4.1.6 on 2023-10-24 10:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('marketplace', '0005_alter_startup_tag_alter_startup_technology_used'),
    ]

    operations = [
        migrations.AlterField(
            model_name='startup',
            name='company_name',
            field=models.CharField(max_length=255, unique=True),
        ),
        migrations.AlterField(
            model_name='startup',
            name='tag',
            field=models.ManyToManyField(max_length=50, to='marketplace.tag'),
        ),
        migrations.AlterField(
            model_name='startup',
            name='technology_used',
            field=models.ManyToManyField(max_length=50, to='marketplace.technology'),
        ),
    ]