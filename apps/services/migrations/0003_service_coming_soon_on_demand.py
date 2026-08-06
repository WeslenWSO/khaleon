from django.db import migrations, models


def set_car_badges(apps, schema_editor):
    Service = apps.get_model("services", "Service")
    Service.objects.filter(slug="consulta-car").update(coming_soon=True, on_demand=True)


class Migration(migrations.Migration):

    dependencies = [
        ("services", "0002_add_consulta_car_service"),
    ]

    operations = [
        migrations.AddField(
            model_name="service",
            name="coming_soon",
            field=models.BooleanField(default=False, verbose_name="Em breve"),
        ),
        migrations.AddField(
            model_name="service",
            name="on_demand",
            field=models.BooleanField(default=False, verbose_name="Sob demanda"),
        ),
        migrations.RunPython(set_car_badges, migrations.RunPython.noop),
    ]
