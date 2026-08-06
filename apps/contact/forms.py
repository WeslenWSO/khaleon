from django import forms

from apps.contact.models import ContactMessage


class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = ["name", "email", "phone", "company", "message"]
        widgets = {
            "name": forms.TextInput(attrs={
                "class": "w-full px-4 py-3 rounded-lg border border-slate-300 focus:ring-2 focus:ring-cyan-500 focus:border-cyan-500 outline-none",
                "placeholder": "Seu nome completo",
            }),
            "email": forms.EmailInput(attrs={
                "class": "w-full px-4 py-3 rounded-lg border border-slate-300 focus:ring-2 focus:ring-cyan-500 focus:border-cyan-500 outline-none",
                "placeholder": "seu@email.com",
            }),
            "phone": forms.TextInput(attrs={
                "class": "w-full px-4 py-3 rounded-lg border border-slate-300 focus:ring-2 focus:ring-cyan-500 focus:border-cyan-500 outline-none",
                "placeholder": "(11) 99999-9999",
            }),
            "company": forms.TextInput(attrs={
                "class": "w-full px-4 py-3 rounded-lg border border-slate-300 focus:ring-2 focus:ring-cyan-500 focus:border-cyan-500 outline-none",
                "placeholder": "Nome da empresa",
            }),
            "message": forms.Textarea(attrs={
                "class": "w-full px-4 py-3 rounded-lg border border-slate-300 focus:ring-2 focus:ring-cyan-500 focus:border-cyan-500 outline-none",
                "placeholder": "Como podemos ajudar?",
                "rows": 5,
            }),
        }
        labels = {
            "name": "Nome",
            "email": "E-mail",
            "phone": "Telefone",
            "company": "Empresa",
            "message": "Mensagem",
        }
