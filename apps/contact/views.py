from django.conf import settings
from django.contrib import messages
from django.core.mail import send_mail
from django.shortcuts import redirect, render

from apps.contact.forms import ContactForm


def contact(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            contact_message = form.save()
            send_mail(
                subject=f"[Khaleon IA] Contato de {contact_message.name}",
                message=(
                    f"Nome: {contact_message.name}\n"
                    f"E-mail: {contact_message.email}\n"
                    f"Telefone: {contact_message.phone}\n"
                    f"Empresa: {contact_message.company}\n\n"
                    f"Mensagem:\n{contact_message.message}"
                ),
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=[settings.CONTACT_RECIPIENT],
                fail_silently=False,
            )
            messages.success(request, "Mensagem enviada com sucesso! Entraremos em contato em breve.")
            return redirect("contact:contact")
    else:
        form = ContactForm()

    context = {
        "form": form,
        "page_title": "Contato — Khaleon IA",
        "meta_description": "Entre em contato com a Khaleon IA. Estamos prontos para transformar seus processos com BPO e tecnologia.",
    }
    return render(request, "pages/contact/contact.html", context)
