from django.db import models


class ContactMessage(models.Model):
    name = models.CharField("Nome", max_length=150)
    email = models.EmailField("E-mail")
    phone = models.CharField("Telefone", max_length=20, blank=True)
    company = models.CharField("Empresa", max_length=150, blank=True)
    message = models.TextField("Mensagem")
    created_at = models.DateTimeField(auto_now_add=True)
    read = models.BooleanField("Lida", default=False)

    class Meta:
        ordering = ["-created_at"]
        verbose_name = "Mensagem de contato"
        verbose_name_plural = "Mensagens de contato"

    def __str__(self):
        return f"{self.name} — {self.email}"
