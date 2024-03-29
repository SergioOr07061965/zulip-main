# Generated by Django 4.2.1 on 2023-05-27 00:06

from django.db import migrations, models

from zerver.models.linkifiers import url_template_validator


class Migration(migrations.Migration):
    dependencies = [
        ("zerver", "0461_alter_realm_default_code_block_language"),
    ]

    operations = [
        migrations.AddField(
            model_name="realmplayground",
            name="url_template",
            field=models.TextField(null=True, validators=[url_template_validator]),
        ),
    ]
