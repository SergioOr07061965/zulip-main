# Generated by Django 4.2.1 on 2023-05-27 03:13

from django.db import migrations, models

from zerver.models.linkifiers import url_template_validator


class Migration(migrations.Migration):
    dependencies = [
        ("zerver", "0463_backfill_realmplayground_url_template"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="realmplayground",
            name="url_prefix",
        ),
        migrations.AlterField(
            model_name="realmplayground",
            name="url_template",
            field=models.TextField(validators=[url_template_validator], null=False),
        ),
    ]
