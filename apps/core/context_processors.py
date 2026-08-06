from apps.core.models import SiteConfig, Partner


def site_config(request):
    return {
        "site_config": SiteConfig.load(),
        "partners": Partner.objects.filter(active=True),
    }
