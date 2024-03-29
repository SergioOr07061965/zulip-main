# Generated by Django 4.2.7 on 2023-11-29 05:16

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("zilencer", "0040_remoterealm_authentication_methods_remoterealm_name"),
    ]

    operations = [
        migrations.AddField(
            model_name="remotezulipserver",
            name="org_type",
            field=models.PositiveSmallIntegerField(
                choices=[
                    (0, "Unspecified"),
                    (10, "Business"),
                    (20, "Open-source project"),
                    (30, "Education (non-profit)"),
                    (35, "Education (for-profit)"),
                    (40, "Research"),
                    (50, "Event or conference"),
                    (60, "Non-profit (registered)"),
                    (70, "Government"),
                    (80, "Political group"),
                    (90, "Community"),
                    (100, "Personal"),
                    (1000, "Other"),
                ],
                default=0,
            ),
        ),
    ]
