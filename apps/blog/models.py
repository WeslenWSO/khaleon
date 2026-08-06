from django.db import models
from django.utils.text import slugify


class Category(models.Model):
    name = models.CharField("Nome", max_length=100)
    slug = models.SlugField("Slug", unique=True)

    class Meta:
        ordering = ["name"]
        verbose_name = "Categoria"
        verbose_name_plural = "Categorias"

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)


class Post(models.Model):
    title = models.CharField("Título", max_length=200)
    slug = models.SlugField("Slug", unique=True)
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="posts",
        verbose_name="Categoria",
    )
    excerpt = models.CharField("Resumo", max_length=300)
    content = models.TextField("Conteúdo")
    image = models.ImageField("Imagem", upload_to="blog/", blank=True)
    published = models.BooleanField("Publicado", default=False)
    published_at = models.DateTimeField("Data de publicação", null=True, blank=True)
    meta_title = models.CharField("Meta title", max_length=70, blank=True)
    meta_description = models.CharField("Meta description", max_length=160, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-published_at", "-created_at"]
        verbose_name = "Post"
        verbose_name_plural = "Posts"

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        from django.urls import reverse
        return reverse("blog:detail", kwargs={"slug": self.slug})

    @property
    def seo_title(self):
        return self.meta_title or self.title

    @property
    def seo_description(self):
        return self.meta_description or self.excerpt
