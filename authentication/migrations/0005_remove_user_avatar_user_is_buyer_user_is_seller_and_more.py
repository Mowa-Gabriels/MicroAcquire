# Generated by Django 4.1.6 on 2023-10-19 22:32

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0004_alter_user_first_name_alter_user_is_staff_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='avatar',
        ),
        migrations.AddField(
            model_name='user',
            name='is_buyer',
            field=models.BooleanField(default=False, verbose_name='buyer'),
        ),
        migrations.AddField(
            model_name='user',
            name='is_seller',
            field=models.BooleanField(default=False, verbose_name='seller'),
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('linkedin_profile', models.URLField(blank=True, null=True)),
                ('twitter_profile', models.URLField(blank=True, null=True)),
                ('facebook_profile', models.URLField(blank=True, null=True)),
                ('phone_no', models.CharField(blank=True, max_length=14)),
                ('avatar', models.ImageField(blank=True, null=True, upload_to='avatars/')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='profile', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]