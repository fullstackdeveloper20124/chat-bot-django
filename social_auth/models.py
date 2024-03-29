from django.db import models

from django.contrib.auth.models import User
from django.contrib.auth import get_user_model

# Obtiene el modelo de usuario actualmente activo en el proyecto Django.
User = get_user_model()


class ChatSession(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='chat_sessions')
    start_timestamp = models.DateTimeField(auto_now_add=True)
    
    # Este modelo almacena información sobre las sesiones de chat.
    # Cada sesión está vinculada a un usuario específico y registra cuándo se inició.


class ChatMessage(models.Model):
    chat_session = models.ForeignKey(
        ChatSession, on_delete=models.CASCADE, related_name='messages')
    user_question = models.TextField()
    question_received_timestamp = models.DateTimeField(auto_now_add=True)
    bot_response = models.TextField()
    # Este campo debe establecerse manualmente en el momento de enviar la respuesta.
    response_sent_timestamp = models.DateTimeField()
    rating = models.IntegerField(
        default=0,
        choices=[(0, 'Sin calificar'), (1, 'Baja calidad'), (2, 'Regular'),
                 (3, 'Buena'), (4, 'Muy buena'), (5, 'Excelente')],
        help_text="Calificación de la respuesta del chatbot en una escala de 1 a 5."
    )
    feedback = models.TextField(
        null=True,
        blank=True,
        max_length=500,
        help_text="Comentarios adicionales sobre la respuesta del chatbot. Máximo 500 caracteres."
    )

    # Este modelo almacena los mensajes entre el usuario y el chatbot dentro de una sesión de chat.
    # Incluye tanto la pregunta del usuario como la respuesta del bot, junto con timestamps para ambos eventos.
        # También permite a los usuarios calificar y proporcionar comentarios sobre las respuestas del bot.

