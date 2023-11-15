from django.db import models
from authentication.models import User
from django_countries.fields import CountryField
from cloudinary_storage.storage import RawMediaCloudinaryStorage
import random
from django.utils.text import slugify



class Tag(models.Model):
    name = models.CharField(max_length=100)
 
    def __str__(self):
        return self.name
    
class Technology(models.Model):
    name = models.CharField(max_length=100)
 
    def __str__(self):
        return self.name
    class Meta:

        verbose_name =('Technology')
        verbose_name_plural = ('Technologies')
    


Industry_options = [
        ('saas', 'SAAS'),
        ('edtech', 'EdTech'),
        ('proptech', 'PropTech'),
        ('fintech', 'Fintech'),
        ('others', 'Others')
        
    ]

Sale_options = [
        ('full', 'Full'),
        ('partial', 'Partial')
        
    ]

class Startup(models.Model):
    # Basic Company Information

      # Team Details
    founders = models.ForeignKey(User, on_delete=models.Case)
    
    company_name = models.CharField(max_length=255, unique=True)
    founding_date = models.DateField()
    country = CountryField(default='Nigeria',max_length=255)
    industry = models.CharField(max_length=255, choices=Industry_options)
    tag = models.ManyToManyField(to=Tag, max_length=50)
    slug = models.SlugField(unique=True, blank=True,null=True)
    # Financial Information
    revenue = models.DecimalField(max_digits=12, decimal_places=2)
    profit = models.DecimalField(max_digits=12, decimal_places=2)
    valuation = models.DecimalField(max_digits=12, decimal_places=2)
    

    # Product/Service Description
    description = models.TextField()

    # Market Information
    target_audience = models.TextField()
    market_size = models.CharField(max_length=255)
    competitors = models.TextField()
    market_trends = models.TextField()


    # Intellectual Property and Assets
    intellectual_property = models.TextField()
    proprietary_assets = models.TextField()

    # Customer Base
    total_user = models.PositiveIntegerField()
    customer_demographics = models.TextField()
    acquisition_retention_strategies = models.TextField()

    # User Metrics
    monthly_active_users = models.PositiveIntegerField()
    daily_active_users = models.PositiveIntegerField()
    customer_engagement_metrics = models.TextField()
    conversion_rates = models.TextField()

    # Technology Stack
    technology_used = models.ManyToManyField(to= Technology, max_length=50)
    custom_tools = models.TextField()

    # Legal and Compliance
    legal_documents = models.FileField(upload_to='legal_doc/', storage=RawMediaCloudinaryStorage())
    legal_issues = models.BooleanField(default=False)
    funds_raised = models.BooleanField(default=False)

    # Operational Details
    supply_chain_info = models.TextField()
    production_processes = models.TextField()
    distribution_channels = models.TextField()

    # Financial Projections
    future_projections = models.TextField()

    # Reason for Sale
    sale_motivation = models.TextField()
    founders_after_sale = models.TextField()

    # Terms of Sale
    sale_type = models.CharField(max_length=255, choices=Sale_options)
    price_expectations = models.DecimalField(max_digits=12, decimal_places=2)
    negotiable_terms = models.TextField()

    # Customer Feedback and Reviews
    customer_feedback = models.TextField()

    # Exit Strategy
    exit_strategy = models.TextField()
    exit_timeline = models.DateField()

    # Due Diligence Documents
    due_diligence_documents = models.FileField(upload_to='due_diligence_doc/', storage=RawMediaCloudinaryStorage())

    # NDAs
    require_ndas = models.BooleanField()

    # Images and Media
    images = models.ImageField(upload_to='startup_images/')

    def __str__(self):
        return self.company_name
    
    def save(self, *args, **kwargs):
        # Combine last name and random 6 numbers
        random_numbers = ''.join([str(random.randint(0, 9)) for _ in range(2)])
        combined_slug = f"{slugify(self.description)}-{random_numbers}"

        # Assign the generated slug to the slug field
        self.slug = combined_slug

        super().save(*args, **kwargs)
