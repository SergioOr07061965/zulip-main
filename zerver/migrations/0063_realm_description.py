# Generated by Django 1.10.5 on 2017-03-19 19:06
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("zerver", "0062_default_timezone"),
    ]

    operations = [
        migrations.AddField(
            model_name="realm",
            name="description",
            field=models.TextField(max_length=100, null=True),
        ),
    ]
