from django.urls import path

from apps.cases import views

app_name = "cases"

urlpatterns = [
    path("", views.case_list, name="list"),
    path("<slug:slug>/", views.case_detail, name="detail"),
]
