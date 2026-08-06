from django.shortcuts import get_object_or_404, render

from apps.services.conta_azul import get_dashboard_data
from apps.services.models import Service


def service_list(request):
    services = Service.objects.filter(active=True)
    context = {
        "services": services,
        "page_title": "Serviços — Khaleon IA",
        "meta_description": "Conheça nossos serviços de BPO com tecnologia, dashboard Conta Azul, analytics e compliance.",
    }
    return render(request, "pages/services/list.html", context)


def service_detail(request, slug):
    service = get_object_or_404(Service, slug=slug, active=True)
    context = {
        "service": service,
        "page_title": f"{service.title} — Khaleon IA",
        "meta_description": service.summary,
        "is_conta_azul": slug == "dashboard-conta-azul",
    }
    return render(request, "pages/services/detail.html", context)


def conta_azul_dashboard(request):
    service = get_object_or_404(Service, slug="dashboard-conta-azul", active=True)
    data = get_dashboard_data()
    context = {
        "service": service,
        "data": data,
        "page_title": f"Painel Conta Azul — {service.title}",
        "meta_description": service.summary,
    }
    return render(request, "pages/services/dashboard_conta_azul.html", context)
