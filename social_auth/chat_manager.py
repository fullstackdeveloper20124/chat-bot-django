from django.utils import timezone
from .models import ChatSession, ChatMessage

class ChatSessionManager:
    def __init__(self, user):
        self.user = user
        self.session = None

    def start_new_session(self):
        """
        Crea y retorna una nueva sesión de chat para el usuario.
        """
        new_session = ChatSession.objects.create(user=self.user)
        return new_session
    
    def select_session(self, session_id):
        """
        Selecciona una sesión de chat existente basada en su ID.
        Retorna la sesión si pertenece al usuario, de lo contrario None.
        """
        try:
            session = ChatSession.objects.get(id=session_id, user=self.user)
            return session
        except ChatSession.DoesNotExist:
            return None

    
    def add_message(self, session_id, user_question, bot_response, response_sent_timestamp):
        """
        Añade un nuevo par de pregunta-respuesta a la sesión especificada por session_id.
        """
        # Asegurarse de que la sesión pertenezca al usuario para evitar modificaciones no autorizadas
        try:
            session = ChatSession.objects.get(id=session_id, user=self.user)
        except ChatSession.DoesNotExist:
            raise ValueError("La sesión especificada no existe o no pertenece al usuario actual.")
        
        # Crear el mensaje en la base de datos
        ChatMessage.objects.create(
            chat_session=session,
            user_question=user_question,
            question_received_timestamp=timezone.now(),
            bot_response=bot_response,
            response_sent_timestamp=response_sent_timestamp
        )

    def serialize_conversation(self, session_id):
        """
        Recopila y serializa la conversación de una sesión de chat específica.
        """
        try:
            session = ChatSession.objects.get(id=session_id, user=self.user)
        except ChatSession.DoesNotExist:
            raise ValueError("La sesión especificada no existe o no pertenece al usuario actual.")
        
        # Recuperar todos los mensajes asociados a la sesión
        messages = ChatMessage.objects.filter(chat_session=session).order_by('question_received_timestamp')
        
        # Organizar los mensajes en una estructura serializable
        conversation = {
            "session": str(session.id),
            "history": []
        }

        for message in messages:
            conversation["history"].append({
                "type": "userMessage",
                "message": message.user_question
                
            })
            conversation["history"].append({
                "type": "apiMessage",
                "message": message.bot_response
            })
        
        return conversation