# Khaleon IA — Site Institucional

Site institucional da **Khaleon IA**, empresa de BPO com tecnologia. Desenvolvido em Django (Python).

## Funcionalidades

- **Home** com hero, diferenciais, serviços, cases, depoimentos e blog
- **Sobre** com missão, visão, valores e equipe
- **Serviços** com listagem e páginas de detalhe
- **Cases** com filtro por setor
- **Blog** com categorias e paginação
- **Contato** com formulário, persistência e envio por e-mail
- **CMS** completo via Django Admin
- **WhatsApp** flutuante configurável
- **SEO**: meta tags, sitemap.xml e robots.txt

## Requisitos

- Python 3.12+
- pip

## Instalação

```bash
# Clonar e entrar no diretório
cd Khaleon

# Criar ambiente virtual
python -m venv venv

# Ativar (Windows)
venv\Scripts\activate

# Ativar (Linux/Mac)
source venv/bin/activate

# Instalar dependências
pip install -r requirements.txt

# Configurar variáveis de ambiente
copy .env.example .env

# Migrar banco de dados
python manage.py migrate

# Popular com dados de demonstração
python manage.py seed_demo

# Criar superusuário para o admin
python manage.py createsuperuser

# Rodar servidor de desenvolvimento
python manage.py runserver
```

Acesse:
- Site: http://127.0.0.1:8000/
- Admin: http://127.0.0.1:8000/admin/

## Variáveis de ambiente

Copie `.env.example` para `.env` e configure:

| Variável | Descrição |
|----------|-----------|
| `SECRET_KEY` | Chave secreta do Django |
| `DEBUG` | `True` em dev, `False` em produção |
| `ALLOWED_HOSTS` | Hosts permitidos (separados por vírgula) |
| `DATABASE_URL` | URL PostgreSQL (opcional, usa SQLite se omitido) |
| `EMAIL_HOST` | Servidor SMTP |
| `EMAIL_PORT` | Porta SMTP (587) |
| `EMAIL_HOST_USER` | Usuário SMTP |
| `EMAIL_HOST_PASSWORD` | Senha SMTP |
| `CONTACT_RECIPIENT` | E-mail que recebe mensagens do formulário |

Sem credenciais SMTP, os e-mails são exibidos no console.

## Deploy em produção

```bash
export DJANGO_SETTINGS_MODULE=khaleon.settings.production
python manage.py collectstatic --noinput
python manage.py migrate
gunicorn khaleon.wsgi:application
```

Configure `DATABASE_URL` com PostgreSQL e defina `DEBUG=False` e uma `SECRET_KEY` segura.

## Estrutura

```
apps/
  core/       — Home, Sobre, config global, depoimentos, stats
  services/   — Serviços BPO
  blog/       — Blog e categorias
  cases/      — Cases de sucesso
  contact/    — Formulário de contato
templates/    — Templates HTML (Tailwind CSS)
static/       — CSS e JS
media/        — Uploads do CMS
```

## Licença

Projeto privado — Khaleon IA.
