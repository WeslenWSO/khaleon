from django.db import models


class SiteConfig(models.Model):
    site_name = models.CharField("Nome do site", max_length=100, default="Khaleon IA")
    tagline = models.CharField("Slogan", max_length=200, default="BPO inteligente com tecnologia de ponta")
    hero_title = models.CharField("Título do hero", max_length=200)
    hero_subtitle = models.TextField("Subtítulo do hero")
    hero_cta_text = models.CharField("Texto do botão hero", max_length=50, default="Fale conosco")
    hero_cta_url = models.CharField("URL do botão hero", max_length=200, default="/contato/")

    about_title = models.CharField("Título sobre", max_length=200, default="Sobre a Khaleon IA")
    about_intro = models.TextField("Introdução sobre")
    mission = models.TextField("Missão")
    vision = models.TextField("Visão")
    values = models.TextField("Valores")

    phone = models.CharField("Telefone", max_length=20, blank=True)
    email = models.EmailField("E-mail", blank=True)
    whatsapp = models.CharField("WhatsApp (apenas números)", max_length=20, blank=True)
    address = models.TextField("Endereço", blank=True)
    map_embed = models.TextField("Embed do mapa (iframe)", blank=True)

    linkedin = models.URLField("LinkedIn", blank=True)
    instagram = models.URLField("Instagram", blank=True)
    facebook = models.URLField("Facebook", blank=True)

    meta_description = models.CharField("Meta description padrão", max_length=160, blank=True)

    system_title = models.CharField("Título do sistema", max_length=100, default="Finanças Pessoais")
    system_description = models.CharField(
        "Descrição do sistema",
        max_length=300,
        default="Acesse sua plataforma de gestão financeira e acompanhe suas finanças em tempo real.",
        blank=True,
    )
    system_url = models.URLField("URL do sistema", blank=True)
    system_active = models.BooleanField("Exibir card do sistema", default=True)

    class Meta:
        verbose_name = "Configuração do site"
        verbose_name_plural = "Configuração do site"

    def __str__(self):
        return self.site_name

    def save(self, *args, **kwargs):
        self.pk = 1
        super().save(*args, **kwargs)

    @classmethod
    def load(cls):
        defaults = {
            "hero_title": "Khaleon IA — BPO inteligente com tecnologia de ponta",
            "hero_subtitle": (
                "Automatizamos operações, reduzimos custos e elevamos a eficiência "
                "do seu negócio com soluções BPO integradas à tecnologia de ponta."
            ),
            "about_intro": "",
            "mission": "",
            "vision": "",
            "values": "",
        }
        obj, _ = cls.objects.get_or_create(pk=1, defaults=defaults)
        return obj


class Stat(models.Model):
    label = models.CharField("Rótulo", max_length=100)
    value = models.CharField("Valor", max_length=50)
    order = models.PositiveIntegerField("Ordem", default=0)

    class Meta:
        ordering = ["order"]
        verbose_name = "Estatística"
        verbose_name_plural = "Estatísticas"

    def __str__(self):
        return f"{self.value} — {self.label}"


class Testimonial(models.Model):
    name = models.CharField("Nome", max_length=100)
    company = models.CharField("Empresa", max_length=100)
    text = models.TextField("Depoimento")
    photo = models.ImageField("Foto", upload_to="testimonials/", blank=True)
    order = models.PositiveIntegerField("Ordem", default=0)
    active = models.BooleanField("Ativo", default=True)

    class Meta:
        ordering = ["order"]
        verbose_name = "Depoimento"
        verbose_name_plural = "Depoimentos"

    def __str__(self):
        return f"{self.name} — {self.company}"


class TeamMember(models.Model):
    name = models.CharField("Nome", max_length=100)
    role = models.CharField("Cargo", max_length=100)
    bio = models.TextField("Bio", blank=True)
    photo = models.ImageField("Foto", upload_to="team/", blank=True)
    order = models.PositiveIntegerField("Ordem", default=0)
    active = models.BooleanField("Ativo", default=True)

    class Meta:
        ordering = ["order"]
        verbose_name = "Membro da equipe"
        verbose_name_plural = "Equipe"

    def __str__(self):
        return self.name


class Partner(models.Model):
    name = models.CharField("Nome", max_length=100)
    url = models.URLField("Site")
    logo = models.ImageField("Logo", upload_to="partners/", blank=True)
    order = models.PositiveIntegerField("Ordem", default=0)
    active = models.BooleanField("Ativo", default=True)

    class Meta:
        ordering = ["order"]
        verbose_name = "Parceiro"
        verbose_name_plural = "Parceiros"

    def __str__(self):
        return self.name
