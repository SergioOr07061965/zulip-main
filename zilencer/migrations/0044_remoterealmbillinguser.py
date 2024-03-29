# Generated by Django 4.2.7 on 2023-12-05 01:15

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("zilencer", "0043_remotepushdevicetoken_remote_realm"),
    ]

    operations = [
        migrations.CreateModel(
            name="RemoteRealmBillingUser",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True, primary_key=True, serialize=False, verbose_name="ID"
                    ),
                ),
                ("user_uuid", models.UUIDField()),
                ("full_name", models.TextField(default="")),
                ("email", models.EmailField(max_length=254)),
                ("tos_version", models.TextField(default="-1")),
                (
                    "remote_realm",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="zilencer.remoterealm"
                    ),
                ),
            ],
        ),
    ]
