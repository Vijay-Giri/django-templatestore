# Generated by Django 3.0.7 on 2020-06-11 17:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("templatestore", "0002_templateconfig_attributes"),
    ]

    operations = [
        migrations.AddField(
            model_name="templateversion",
            name="version_alias",
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
