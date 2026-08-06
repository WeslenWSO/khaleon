import os


def run_render_boot():
    if not os.environ.get("RENDER"):
        return

    import django

    django.setup()

    from django.core.management import call_command
    from django.db import OperationalError, ProgrammingError

    call_command("migrate", "--noinput", verbosity=0)

    try:
        from apps.core.models import SiteConfig

        SiteConfig.objects.get(pk=1)
    except (SiteConfig.DoesNotExist, OperationalError, ProgrammingError):
        call_command("seed_demo", verbosity=0)
