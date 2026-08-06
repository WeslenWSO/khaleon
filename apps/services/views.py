from django.db import OperationalError, ProgrammingError
from django.http import Http404
from django.shortcuts import get_object_or_404, render

from apps.core.db_utils import safe_query
from apps.services.conta_azul import get_dashboard_data
from apps.services.models import Service


def service_list(request):
    services = safe_query(lambda: list(Service.objects.filter(active=True)))
    context = {
        "services": services,
        "page_title": "Serviços — Khaleon IA",
        "meta_description": "Conheça nossos serviços de BPO com tecnologia, dashboard Conta Azul, analytics e compliance.",
    }
    return render(request, "pages/services/list.html", context)


def service_detail(request, slug):
    try:
        service = get_object_or_404(Service, slug=slug, active=True)
    except (OperationalError, ProgrammingError):
        raise Http404("Serviço não encontrado") from None

    context = {
        "service": service,
        "page_title": f"{service.title} — Khaleon IA",
        "meta_description": service.summary,
        "is_conta_azul": slug == "dashboard-conta-azul",
    }
    return render(request, "pages/services/detail.html", context)


def conta_azul_dashboard(request):
    try:
        service = get_object_or_404(Service, slug="dashboard-conta-azul", active=True)
    except (OperationalError, ProgrammingError):
        raise Http404("Serviço não encontrado") from None

    data = get_dashboard_data()
    context = {
        "service": service,
        "data": data,
        "page_title": f"Painel Conta Azul — {service.title}",
        "meta_description": service.summary,
    }
    return render(request, "pages/services/dashboard_conta_azul.html", context)
