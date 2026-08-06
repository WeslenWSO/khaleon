from django.db import migrations


def clear_public_email(apps, schema_editor):
    SiteConfig = apps.get_model("core", "SiteConfig")
    SiteConfig.objects.filter(pk=1).update(email="")


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0003_partner"),
    ]

    operations = [
        migrations.RunPython(clear_public_email, migrations.RunPython.noop),
    ]
