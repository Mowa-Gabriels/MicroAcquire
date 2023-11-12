# Generated by Django 4.1.7 on 2023-11-12 02:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('oauth2_provider', '0007_application_post_logout_redirect_uris'),
        ('admin', '0003_logentry_add_action_flag_choices'),
        ('socialaccount', '0006_alter_socialaccount_extra_data'),
        ('marketplace', '0007_alter_startup_due_diligence_documents_and_more'),
        ('drfpasswordless', '0005_auto_20201117_0410'),
        ('token_blacklist', '0012_alter_outstandingtoken_user'),
        ('account', '0005_emailaddress_idx_upper_email'),
        ('social_django', '0015_rename_extra_data_new_usersocialauth_extra_data'),
        ('authtoken', '0003_tokenproxy'),
        ('auth', '0012_alter_user_first_name_max_length'),
        ('authentication', '0005_remove_user_avatar_user_is_buyer_user_is_seller_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='User',
            new_name='CustomUser',
        ),
    ]
