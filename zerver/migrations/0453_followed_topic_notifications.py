# Generated by Django 4.2.1 on 2023-05-24 11:09

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("zerver", "0452_realmauditlog_extra_data_json"),
    ]

    operations = [
        migrations.AddField(
            model_name="realmuserdefault",
            name="enable_followed_topic_audible_notifications",
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name="realmuserdefault",
            name="enable_followed_topic_desktop_notifications",
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name="realmuserdefault",
            name="enable_followed_topic_email_notifications",
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name="realmuserdefault",
            name="enable_followed_topic_push_notifications",
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name="realmuserdefault",
            name="enable_followed_topic_wildcard_mentions_notify",
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name="userprofile",
            name="enable_followed_topic_audible_notifications",
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name="userprofile",
            name="enable_followed_topic_desktop_notifications",
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name="userprofile",
            name="enable_followed_topic_email_notifications",
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name="userprofile",
            name="enable_followed_topic_push_notifications",
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name="userprofile",
            name="enable_followed_topic_wildcard_mentions_notify",
            field=models.BooleanField(default=True),
        ),
    ]
