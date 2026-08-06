from django.conf import settings


def get_dashboard_data():
    """Retorna dados do dashboard Conta Azul (demo ou API futura)."""
    if getattr(settings, "CONTAAZUL_ACCESS_TOKEN", ""):
        return _fetch_from_api()

    return {
        "source": "demo",
        "company": "Sua empresa",
        "period": "Agosto/2026",
        "summary": {
            "receitas": 128450.00,
            "despesas": 87320.50,
            "saldo": 41129.50,
            "contas_receber": 34200.00,
            "contas_pagar": 18950.00,
        },
        "recent": [
            {"date": "05/08/2026", "description": "Venda de serviços — Cliente A", "type": "receita", "value": 12500.00},
            {"date": "04/08/2026", "description": "Fornecedor de TI", "type": "despesa", "value": -3200.00},
            {"date": "03/08/2026", "description": "Assinatura Conta Azul", "type": "despesa", "value": -189.90},
            {"date": "02/08/2026", "description": "Projeto consultoria BPO", "type": "receita", "value": 8900.00},
            {"date": "01/08/2026", "description": "Folha de pagamento", "type": "despesa", "value": -28500.00},
        ],
        "charts": {
            "receitas_pizza": {
                "labels": ["Serviços BPO", "Consultoria", "Projetos", "Recorrentes"],
                "values": [52000, 38450, 25000, 13000],
            },
            "despesas_linha": {
                "labels": ["Mar", "Abr", "Mai", "Jun", "Jul", "Ago"],
                "values": [72000, 68500, 75200, 81000, 84800, 87320],
            },
        },
    }


def _fetch_from_api():
    # Integração futura com API Conta Azul (OAuth + endpoints financeiros)
    return get_dashboard_data()
