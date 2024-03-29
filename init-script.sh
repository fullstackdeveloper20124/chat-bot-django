#!/bin/bash
# Esperar a que la base de datos esté lista (opcional)

# Ejecutar migraciones
python manage.py migrate --noinput

# Recolectar archivos estáticos
python manage.py collectstatic --noinput

# Iniciar el servidor de Django u otro comando principal
exec "$@"