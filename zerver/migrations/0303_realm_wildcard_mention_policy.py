# Generated by Django 2.2.14 on 2020-09-04 16:28

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("zerver", "0302_case_insensitive_stream_name_index"),
    ]

    operations = [
        migrations.AddField(
            model_name="realm",
            name="wildcard_mention_policy",
            field=models.PositiveSmallIntegerField(default=4),
        ),
    ]
