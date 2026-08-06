from datetime import timedelta

from django.core.management.base import BaseCommand
from django.utils import timezone

from apps.blog.models import Category, Post
from apps.core.models import SiteConfig, Stat
from apps.services.models import Service


class Command(BaseCommand):
    help = "Popula o banco com dados de demonstração para o site Khaleon IA"

    def handle(self, *args, **options):
        self.stdout.write("Criando configuração do site...")
        config, _ = SiteConfig.objects.update_or_create(
            pk=1,
            defaults={
                "site_name": "Khaleon IA",
                "tagline": "Inteligência Artificial Avançada",
                "hero_title": "Khaleon IA — BPO inteligente com tecnologia de ponta",
                "hero_subtitle": (
                    "Automatizamos operações, reduzimos custos e elevamos a eficiência "
                    "do seu negócio com soluções BPO integradas à tecnologia de ponta."
                ),
                "about_title": "Sobre a Khaleon IA",
                "about_intro": (
                    "Somos uma empresa de BPO que une expertise operacional com tecnologia "
                    "de ponta. Nossa missão é transformar processos empresariais através da "
                    "automação inteligente, entregando resultados mensuráveis e sustentáveis."
                ),
                "mission": (
                    "Democratizar o acesso a soluções de BPO de alta performance, "
                    "integrando tecnologia e inteligência artificial para otimizar "
                    "processos empresariais de qualquer porte."
                ),
                "vision": (
                    "Ser referência nacional em BPO tecnológico, reconhecida pela "
                    "inovação, excelência operacional e impacto positivo nos negócios "
                    "de nossos clientes."
                ),
                "values": (
                    "Inovação contínua\nExcelência operacional\nTransparência e ética\n"
                    "Foco no cliente\nSegurança e compliance"
                ),
                "phone": "(68) 99907-3217",
                "email": "",
                "whatsapp": "5568999073217",
                "address": "",
                "linkedin": "",
                "instagram": "",
                "facebook": "",
                "meta_description": (
                    "Khaleon IA — Inteligência Artificial Avançada. "
                    "BPO inteligente com automação, IA e excelência operacional."
                ),
                "system_title": "Finanças Pessoais",
                "system_description": (
                    "Acesse sua plataforma de gestão financeira e acompanhe "
                    "receitas, despesas e metas em tempo real."
                ),
                "system_url": "https://financaspessoais-eloo.onrender.com/",
                "system_active": True,
            },
        )

        self.stdout.write("Criando estatísticas...")
        stats_data = [
            ("40%", "Redução de custos média", 1),
            ("2M+", "Processos automatizados", 2),
            ("99.8%", "SLA de qualidade", 3),
        ]
        Stat.objects.all().delete()
        for value, label, order in stats_data:
            Stat.objects.create(value=value, label=label, order=order)

        self.stdout.write("Criando serviços...")
        services_data = [
            {
                "title": "Back-office Financeiro",
                "slug": "back-office-financeiro",
                "icon": "chart",
                "summary": "Gestão completa de contas a pagar, receber, conciliação e fechamento contábil.",
                "description": (
                    "Nossa solução de back-office financeiro automatiza todo o ciclo financeiro "
                    "da sua empresa. Desde a captura de documentos fiscais até a conciliação bancária "
                    "e fechamento contábil, utilizamos RPA e IA para garantir precisão, agilidade "
                    "e compliance fiscal.\n\nBenefícios: redução de 40% nos custos operacionais, "
                    "eliminação de erros manuais e visibilidade em tempo real dos indicadores financeiros."
                ),
                "order": 1,
            },
            {
                "title": "Dashboard Conta Azul",
                "slug": "dashboard-conta-azul",
                "icon": "chart",
                "summary": "Painel financeiro integrado com os dados da sua conta Conta Azul em tempo real.",
                "description": (
                    "Desenvolvemos dashboards personalizados conectados à Conta Azul para centralizar "
                    "a gestão financeira do seu negócio.\n\n"
                    "Acompanhe receitas, despesas, saldo, contas a pagar e a receber em um painel "
                    "visual e intuitivo, com lançamentos atualizados e indicadores para tomada de decisão.\n\n"
                    "Ideal para empresas que já utilizam Conta Azul e precisam de visibilidade "
                    "operacional integrada ao BPO da Khaleon IA."
                ),
                "order": 2,
            },
            {
                "title": "Analytics & BI",
                "slug": "analytics-bi",
                "icon": "brain",
                "summary": "Business Intelligence e análise preditiva para decisões data-driven.",
                "description": (
                    "Transforme dados em insights acionáveis com nossas soluções de Analytics e BI. "
                    "Criamos dashboards personalizados, modelos preditivos e relatórios automatizados "
                    "que empoderam a tomada de decisão.\n\nIntegração com ERPs, CRMs e fontes de dados "
                    "diversas para uma visão 360° do seu negócio."
                ),
                "order": 3,
            },
            {
                "title": "Compliance & LGPD",
                "slug": "compliance-lgpd",
                "icon": "shield",
                "summary": "Gestão de conformidade regulatória e proteção de dados pessoais.",
                "description": (
                    "Garanta conformidade total com LGPD, SOX, ISO 27001 e regulamentações do seu setor. "
                    "Nossa equipe especializada implementa controles, auditorias e processos de "
                    "governança de dados.\n\nInclui: mapeamento de dados, DPIA, gestão de consentimento, "
                    "resposta a incidentes e treinamento de equipes."
                ),
                "order": 4,
            },
            {
                "title": "Consulta CAR",
                "slug": "consulta-car",
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
            },
        ]
        for data in services_data:
            Service.objects.update_or_create(slug=data["slug"], defaults={**data, "active": True})
        Service.objects.filter(
            slug__in=["rh-digital", "atendimento-omnichannel", "automacao-rpa"]
        ).delete()

        self.stdout.write("Criando blog...")
        categories = {
            "bpo": "BPO",
            "automacao": "Automação",
            "ia": "Inteligência Artificial",
        }
        cat_objects = {}
        for slug, name in categories.items():
            cat_objects[slug], _ = Category.objects.get_or_create(slug=slug, defaults={"name": name})

        now = timezone.now()
        posts_data = [
            {
                "title": "Como a IA está transformando o BPO em 2026",
                "slug": "ia-transformando-bpo-2026",
                "category": cat_objects["ia"],
                "excerpt": "Descubra as principais tendências de inteligência artificial aplicadas ao outsourcing de processos.",
                "content": (
                    "A inteligência artificial revolucionou o setor de BPO nos últimos anos. "
                    "De chatbots avançados a modelos preditivos, a IA permite automatizar tarefas "
                    "complexas que antes exigiam intervenção humana.\n\n"
                    "Neste artigo, exploramos as tendências que moldam o futuro do BPO: "
                    "automação cognitiva, processamento de linguagem natural, análise preditiva "
                    "e a integração de agentes autônomos nos fluxos operacionais.\n\n"
                    "Empresas que adotam BPO com IA reportam reduções de até 50% nos custos "
                    "operacionais e melhorias significativas na qualidade e velocidade dos processos."
                ),
                "published_at": now - timedelta(days=5),
            },
            {
                "title": "5 sinais de que sua empresa precisa de automação RPA",
                "slug": "5-sinais-automacao-rpa",
                "category": cat_objects["automacao"],
                "excerpt": "Identifique os indicadores que mostram que é hora de automatizar seus processos manuais.",
                "content": (
                    "Muitas empresas ainda dependem de processos manuais repetitivos que consomem "
                    "tempo e recursos valiosos. Mas como saber quando é o momento certo para investir "
                    "em automação RPA?\n\n"
                    "1. Equipes sobrecarregadas com tarefas repetitivas\n"
                    "2. Altos índices de erro em processos manuais\n"
                    "3. Dificuldade em escalar operações\n"
                    "4. Integração complexa entre sistemas legados\n"
                    "5. Custos operacionais crescentes\n\n"
                    "Se sua empresa se identifica com dois ou mais desses sinais, "
                    "a automação RPA pode ser a solução ideal."
                ),
                "published_at": now - timedelta(days=12),
            },
            {
                "title": "LGPD e BPO: como garantir compliance na terceirização",
                "slug": "lgpd-bpo-compliance",
                "category": cat_objects["bpo"],
                "excerpt": "Guia prático para manter a conformidade com a LGPD ao terceirizar processos com dados pessoais.",
                "content": (
                    "A Lei Geral de Proteção de Dados (LGPD) impõe responsabilidades específicas "
                    "quando empresas terceirizam processos que envolvem dados pessoais.\n\n"
                    "Neste guia, abordamos: papéis de controlador e operador, cláusulas contratuais "
                    "obrigatórias, mapeamento de dados, gestão de consentimento e resposta a incidentes.\n\n"
                    "Um parceiro de BPO adequado deve demonstrar certificações, políticas de segurança "
                    "robustas e processos auditáveis de governança de dados."
                ),
                "published_at": now - timedelta(days=20),
            },
        ]
        for data in posts_data:
            Post.objects.update_or_create(
                slug=data["slug"],
                defaults={**data, "published": True},
            )

        self.stdout.write("Criando parceiros...")
        from apps.core.models import Partner

        Partner.objects.all().delete()
        Partner.objects.create(
            name="WMAN",
            url="https://wman.com.br",
            order=1,
            active=True,
        )

        self.stdout.write(self.style.SUCCESS("Dados de demonstração criados com sucesso!"))
