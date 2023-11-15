# Generated by Django 4.1.7 on 2023-11-13 04:15

import cloudinary_storage.storage
from django.conf import settings
from django.db import migrations, models
import django.db.models.expressions
import django_countries.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Technology',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name': 'Technology',
                'verbose_name_plural': 'Technologies',
            },
        ),
        migrations.CreateModel(
            name='Startup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_name', models.CharField(max_length=255, unique=True)),
                ('founding_date', models.DateField()),
                ('country', django_countries.fields.CountryField(default='Nigeria', max_length=255)),
                ('industry', models.CharField(choices=[('saas', 'SAAS'), ('edtech', 'EdTech'), ('proptech', 'PropTech'), ('fintech', 'Fintech'), ('others', 'Others')], max_length=255)),
                ('revenue', models.DecimalField(decimal_places=2, max_digits=12)),
                ('profit', models.DecimalField(decimal_places=2, max_digits=12)),
                ('valuation', models.DecimalField(decimal_places=2, max_digits=12)),
                ('description', models.TextField()),
                ('target_audience', models.TextField()),
                ('market_size', models.CharField(max_length=255)),
                ('competitors', models.TextField()),
                ('market_trends', models.TextField()),
                ('intellectual_property', models.TextField()),
                ('proprietary_assets', models.TextField()),
                ('total_user', models.PositiveIntegerField()),
                ('customer_demographics', models.TextField()),
                ('acquisition_retention_strategies', models.TextField()),
                ('monthly_active_users', models.PositiveIntegerField()),
                ('daily_active_users', models.PositiveIntegerField()),
                ('customer_engagement_metrics', models.TextField()),
                ('conversion_rates', models.TextField()),
                ('custom_tools', models.TextField()),
                ('legal_documents', models.FileField(storage=cloudinary_storage.storage.RawMediaCloudinaryStorage(), upload_to='legal_doc/')),
                ('legal_issues', models.BooleanField(default=False)),
                ('funds_raised', models.BooleanField(default=False)),
                ('supply_chain_info', models.TextField()),
                ('production_processes', models.TextField()),
                ('distribution_channels', models.TextField()),
                ('future_projections', models.TextField()),
                ('sale_motivation', models.TextField()),
                ('founders_after_sale', models.TextField()),
                ('sale_type', models.CharField(choices=[('full', 'Full'), ('partial', 'Partial')], max_length=255)),
                ('price_expectations', models.DecimalField(decimal_places=2, max_digits=12)),
                ('negotiable_terms', models.TextField()),
                ('customer_feedback', models.TextField()),
                ('exit_strategy', models.TextField()),
                ('exit_timeline', models.DateField()),
                ('due_diligence_documents', models.FileField(storage=cloudinary_storage.storage.RawMediaCloudinaryStorage(), upload_to='due_diligence_doc/')),
                ('require_ndas', models.BooleanField()),
                ('images', models.ImageField(upload_to='startup_images/')),
                ('founders', models.ForeignKey(on_delete=django.db.models.expressions.Case, to=settings.AUTH_USER_MODEL)),
                ('tag', models.ManyToManyField(max_length=50, to='marketplace.tag')),
                ('technology_used', models.ManyToManyField(max_length=50, to='marketplace.technology')),
            ],
        ),
    ]
