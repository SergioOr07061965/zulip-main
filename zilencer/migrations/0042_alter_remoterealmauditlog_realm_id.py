# Generated by Django 4.2.7 on 2023-11-30 11:24

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("zilencer", "0041_remotezulipserver_org_type"),
    ]

    operations = [
        migrations.AlterField(
            model_name="remoterealmauditlog",
            name="realm_id",
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
