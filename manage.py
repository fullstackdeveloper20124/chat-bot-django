#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys
from dotenv import load_dotenv
from django.core.management.utils import get_random_secret_key;

# Cargar variables de entorno desde '.env'



def main():
    """Run administrative tasks."""
    load_dotenv()
    env = os.environ.get('DJANGO_SETTINGS_MODULE', 'Desconocido')
    os.environ.setdefault('DJANGO_SETTINGS_MODULE',
    os.getenv(env, 'chatbotcerebro.development'))
                


    
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "No se pudo importar Django. ¿Estás seguro de que está instalado y "
            "disponible en su variable de entorno PYTHONPATH? Acaso tú "
            "¿Olvidaste activar un entorno virtual?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == "__main__":
    main()
