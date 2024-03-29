# Generated by Django 4.2.5 on 2023-10-06 10:08

import uuid

from django.db import migrations, models

from zerver.models.realms import generate_realm_uuid_owner_secret


class Migration(migrations.Migration):
    dependencies = [
        ("zerver", "0480_realm_backfill_uuid_and_secret"),
    ]

    operations = [
        migrations.AlterField(
            model_name="realm",
            name="uuid",
            field=models.UUIDField(default=uuid.uuid4, unique=True),
        ),
        migrations.AlterField(
            model_name="realm",
            name="uuid_owner_secret",
            field=models.TextField(default=generate_realm_uuid_owner_secret),
        ),
    ]
