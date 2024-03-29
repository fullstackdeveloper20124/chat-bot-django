# Chatbot
Chatbot con mecanismo de gestión de usuarios

## Descripción
Chatbot es una aplicación de chatbot con interfaz web, diseñada para permitir a los usuarios autenticarse y, una vez autenticados, interactuar con un asistente digital a través de preguntas y respuestas. Este proyecto utiliza Django para el fordend y  Backend, PostgreSQL para la base de datos y se conteneriza con Docker para facilitar el despliegue y la escalabilidad.



## Características
- Autenticación de usuarios con Allauth.
- Interfaz web para interacción con el chatbot.
- Almacenamiento de sesiones e historial de interacciones.
- Contenerización con Docker para un despliegue consistente.

## Tecnologías Utilizadas
- **Backend**: Django (Python)
- **Frontend**: Django Templates
- **Base de Datos**: PostgreSQL

- **servidor de IA**: appserver usando langchain



### Instrucciones de Uso

1. **Construir y Ejecutar los Contenedores:**
   - Para construir las imágenes y ejecutar los contenedores, abre una terminal en el directorio del proyecto y ejecuta:
     ```
     docker-compose up --build
     ```
   - Esto iniciará tanto la aplicación Django como la base de datos PostgreSQL en contenedores separados.

2. **Acceder a la Aplicación:**
   - Una vez que los contenedores estén en ejecución, abre tu navegador y visita `http://localhost:8000/` para acceder a la aplicación Django.

3. **Detener los Contenedores:**
   - Para detener los contenedores, usa `Ctrl + C` en la terminal donde se están ejecutando.
   - Después, ejecuta:
     ```
     docker-compose down
     ```
   - Esto detendrá y eliminará los contenedores, pero no las imágenes ni los volúmenes de datos.



## Licencia
(Especifica la licencia bajo la cual se distribuye el proyecto. Si aún no has decidido, puedes mencionar "Licencia pendiente de definir" o elegir una licencia adecuada para tu proyecto.)

## Autores y Reconocimientos
Horacio Colina Fajardo y Novaer

## Estado del Proyecto
(Esta sección es para informar sobre el estado actual del proyecto, si está en desarrollo, en fase de prueba, etc.)
