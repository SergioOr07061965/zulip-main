# Generated by Django 4.2.6 on 2023-10-25 14:49

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("zerver", "0482_automatically_follow_unmute_topics_policy_defaults"),
    ]

    operations = [
        migrations.RenameField(
            model_name="realmuserdefault",
            old_name="escape_navigates_to_default_view",
            new_name="web_escape_navigates_to_home_view",
        ),
        migrations.RenameField(
            model_name="realmuserdefault",
            old_name="default_view",
            new_name="web_home_view",
        ),
        migrations.RenameField(
            model_name="userprofile",
            old_name="escape_navigates_to_default_view",
            new_name="web_escape_navigates_to_home_view",
        ),
        migrations.RenameField(
            model_name="userprofile",
            old_name="default_view",
            new_name="web_home_view",
        ),
    ]
