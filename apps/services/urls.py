from django.urls import path

from apps.services import views

app_name = "services"

urlpatterns = [
    path("", views.service_list, name="list"),
    path("dashboard-conta-azul/painel/", views.conta_azul_dashboard, name="conta_azul_dashboard"),
    path("<slug:slug>/", views.service_detail, name="detail"),
]
