import json
import os
from pathlib import Path

from django.conf import settings
from django.core.management import call_command
from django.core.management.base import BaseCommand, CommandError


class Command(BaseCommand):
    help = "Exporta dados do SQLite e importa no PostgreSQL definido em DATABASE_URL"

    def add_arguments(self, parser):
        parser.add_argument(
            "--sqlite-path",
            default=str(settings.BASE_DIR / "db.sqlite3"),
            help="Caminho do arquivo SQLite de origem",
        )
        parser.add_argument(
            "--export-only",
            action="store_true",
            help="Apenas exporta para fixtures/khaleon_export.json",
        )
        parser.add_argument(
            "--input",
            default="",
            help="Arquivo JSON para importar (pula exportação do SQLite)",
        )

    def handle(self, *args, **options):
        export_path = Path(settings.BASE_DIR / "fixtures" / "khaleon_export.json")
        export_path.parent.mkdir(exist_ok=True)

        if options["input"]:
            export_path = Path(options["input"])
            if not export_path.exists():
                raise CommandError(f"Arquivo não encontrado: {export_path}")
            self.stdout.write(f"Usando export existente: {export_path}")
        elif not options["export_only"]:
            sqlite_path = Path(options["sqlite_path"])
            if not sqlite_path.exists():
                raise CommandError(f"SQLite não encontrado: {sqlite_path}")

            self.stdout.write("Exportando dados do SQLite...")
            self._export_from_sqlite(sqlite_path, export_path)
        else:
            sqlite_path = Path(options["sqlite_path"])
            self._export_from_sqlite(sqlite_path, export_path)
            self.stdout.write(self.style.SUCCESS(f"Export concluído: {export_path}"))
            return

        if not os.environ.get("DATABASE_URL"):
            raise CommandError(
                "DATABASE_URL não definida. Configure a URL do PostgreSQL antes de importar."
            )

        if "sqlite" in os.environ["DATABASE_URL"]:
            raise CommandError("DATABASE_URL aponta para SQLite. Use a URL do PostgreSQL.")

        engine = settings.DATABASES["default"]["ENGINE"]
        if "postgresql" not in engine:
            raise CommandError(f"Banco default não é PostgreSQL: {engine}")

        self.stdout.write("Preparando PostgreSQL (migrate)...")
        call_command("migrate", "--noinput")

        self.stdout.write("Importando dados no PostgreSQL...")
        call_command("loaddata", str(export_path))
        self.stdout.write(self.style.SUCCESS("Migração SQLite → PostgreSQL concluída."))

    def _export_from_sqlite(self, sqlite_path, export_path):
        sqlite_config = {
            "ENGINE": "django.db.backends.sqlite3",
            "NAME": sqlite_path,
        }
        original = settings.DATABASES["default"]
        settings.DATABASES["default"] = sqlite_config

        try:
            with export_path.open("w", encoding="utf-8") as handle:
                call_command(
                    "dumpdata",
                    natural_foreign=True,
                    natural_primary=True,
                    exclude=["contenttypes", "auth.permission", "sessions"],
                    stdout=handle,
                )
        finally:
            settings.DATABASES["default"] = original

        count = len(json.loads(export_path.read_text(encoding="utf-8")))
        self.stdout.write(f"Registros exportados: {count}")
