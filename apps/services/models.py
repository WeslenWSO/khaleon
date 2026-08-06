from django.db import models


class Service(models.Model):
    ICON_CHOICES = [
        ("chart", "Gráfico"),
        ("users", "Usuários"),
        ("headset", "Atendimento"),
        ("robot", "Automação"),
        ("shield", "Compliance"),
        ("brain", "Inteligência"),
        ("leaf", "Ambiental"),
    ]

    title = models.CharField("Título", max_length=150)
    slug = models.SlugField("Slug", unique=True)
    icon = models.CharField("Ícone", max_length=20, choices=ICON_CHOICES, default="chart")
    summary = models.CharField("Resumo", max_length=300)
    description = models.TextField("Descrição")
    order = models.PositiveIntegerField("Ordem", default=0)
    active = models.BooleanField("Ativo", default=True)
    coming_soon = models.BooleanField("Em breve", default=False)
    on_demand = models.BooleanField("Sob demanda", default=False)

    class Meta:
        ordering = ["order"]
        verbose_name = "Serviço"
        verbose_name_plural = "Serviços"

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        from django.urls import reverse
        return reverse("services:detail", kwargs={"slug": self.slug})
