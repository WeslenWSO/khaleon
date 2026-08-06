from types import SimpleNamespace

from django.db import OperationalError, ProgrammingError

from apps.core.models import Partner, SiteConfig

DEFAULT_SITE_CONFIG = SimpleNamespace(
    site_name="Khaleon IA",
    tagline="Inteligência Artificial Avançada",
    meta_description="Khaleon IA — BPO inteligente com tecnologia de ponta.",
    hero_title="Khaleon IA — BPO inteligente com tecnologia de ponta",
    hero_subtitle="Automatizamos operações, reduzimos custos e elevamos a eficiência do seu negócio.",
    hero_cta_text="Fale conosco",
    hero_cta_url="/contato/",
    about_title="Sobre a Khaleon IA",
    about_intro="",
    mission="",
    vision="",
    values="",
    phone="",
    email="",
    whatsapp="",
    address="",
    linkedin="",
    instagram="",
    system_active=False,
    system_url="",
    system_title="",
    system_description="",
)


def site_config(request):
    try:
        config = SiteConfig.load()
        partners = list(Partner.objects.filter(active=True))
    except (OperationalError, ProgrammingError):
        config = DEFAULT_SITE_CONFIG
        partners = []

    return {
        "site_config": config,
        "partners": partners,
    }
