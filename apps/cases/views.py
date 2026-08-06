from django.shortcuts import get_object_or_404, render

from apps.cases.models import CaseStudy


def case_list(request):
    cases = CaseStudy.objects.filter(published=True)
    sector = request.GET.get("setor")

    if sector:
        cases = cases.filter(sector=sector)

    context = {
        "cases": cases,
        "sectors": CaseStudy.SECTOR_CHOICES,
        "current_sector": sector,
        "page_title": "Cases — Khaleon IA",
        "meta_description": "Cases de sucesso em BPO com tecnologia: resultados reais para empresas de diversos setores.",
    }
    return render(request, "pages/cases/list.html", context)


def case_detail(request, slug):
    case = get_object_or_404(CaseStudy, slug=slug, published=True)
    context = {
        "case": case,
        "page_title": f"{case.title} — Khaleon IA",
        "meta_description": case.challenge[:160],
    }
    return render(request, "pages/cases/detail.html", context)
