from django.db import migrations


def add_consulta_car_service(apps, schema_editor):
    Service = apps.get_model("services", "Service")
    Service.objects.update_or_create(
        slug="consulta-car",
        defaults={
            "title": "Consulta CAR",
            "icon": "leaf",
            "summary": "Consulta e validação do Cadastro Ambiental Rural para imóveis rurais.",
            "description": (
                "O Cadastro Ambiental Rural (CAR) é obrigatório para imóveis rurais no Brasil. "
                "A Khaleon IA oferece consulta, validação e acompanhamento do status cadastral "
                "junto aos órgãos ambientais estaduais.\n\n"
                "Nosso serviço inclui:\n"
                "• Consulta de situação cadastral por CPF/CNPJ ou número do imóvel\n"
                "• Verificação de pendências e regularização ambiental\n"
                "• Relatórios consolidados para due diligence e compliance\n"
                "• Suporte na integração com sistemas de gestão rural\n\n"
                "Ideal para empresas do agronegócio, instituições financeiras, consultorias "
                "ambientais e produtores rurais que precisam de agilidade e confiabilidade "
                "nas consultas ao CAR."
            ),
            "order": 5,
            "active": True,
        },
    )


class Migration(migrations.Migration):

    dependencies = [
        ("services", "0001_initial"),
    ]

    operations = [
        migrations.RunPython(add_consulta_car_service, migrations.RunPython.noop),
    ]
