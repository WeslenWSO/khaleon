from django.db import migrations


def remove_clientes_ativos_stat(apps, schema_editor):
    Stat = apps.get_model("core", "Stat")
    Stat.objects.filter(label="Clientes ativos").delete()


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0004_clear_siteconfig_email"),
    ]

    operations = [
        migrations.RunPython(remove_clientes_ativos_stat, migrations.RunPython.noop),
    ]
