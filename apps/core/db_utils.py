from django.db import OperationalError, ProgrammingError


def safe_query(queryset_fn, fallback=None):
    try:
        return queryset_fn()
    except (OperationalError, ProgrammingError):
        return fallback if fallback is not None else []


def table_exists(model):
    try:
        model.objects.exists()
        return True
    except (OperationalError, ProgrammingError):
        return False
