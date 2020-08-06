# Generated by Django 3.0.7 on 2020-07-29 23:07

from django.db import migrations


def update_config_attributes(apps, schema_editor):
    TemplateConfig = apps.get_model("templatestore", "TemplateConfig")

    for config in TemplateConfig.objects.all():
        updated_attributes = {}
        for key in config.attributes.keys():
            if config.attributes[key]:
                ls = list()
                ls.append(config.attributes[key])
                updated_attributes[key] = {"allowed_values": ls}
            else:
                updated_attributes = {}
        config.attributes = updated_attributes
        config.save(update_fields=["attributes"])


class Migration(migrations.Migration):
    dependencies = [
        ("templatestore", "0004_merge_20200624_1240"),
    ]

    operations = [migrations.RunPython(update_config_attributes)]