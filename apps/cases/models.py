from django.db import models


class CaseStudy(models.Model):
    SECTOR_CHOICES = [
        ("financeiro", "Financeiro"),
        ("saude", "Saúde"),
        ("varejo", "Varejo"),
        ("industria", "Indústria"),
        ("tecnologia", "Tecnologia"),
        ("logistica", "Logística"),
    ]

    title = models.CharField("Título", max_length=200)
    slug = models.SlugField("Slug", unique=True)
    sector = models.CharField("Setor", max_length=20, choices=SECTOR_CHOICES)
    client = models.CharField("Cliente", max_length=150)
    challenge = models.TextField("Desafio")
    solution = models.TextField("Solução")
    results = models.TextField("Resultados")
    image = models.ImageField("Imagem", upload_to="cases/", blank=True)
    featured = models.BooleanField("Destaque", default=False)
    published = models.BooleanField("Publicado", default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]
        verbose_name = "Case"
        verbose_name_plural = "Cases"

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        from django.urls import reverse
        return reverse("cases:detail", kwargs={"slug": self.slug})

    def get_sector_display_name(self):
        return dict(self.SECTOR_CHOICES).get(self.sector, self.sector)
