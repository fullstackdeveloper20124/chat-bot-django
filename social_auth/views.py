from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from django.http import JsonResponse
import json, os, requests
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from .chat_manager import ChatSessionManager
from .models import ChatSession




def home(request):
    return render(request, 'home.html')

@login_required
def chat_interface_view(request):
    #  lógica adicional si es necesario
    return render(request, 'chat.html')  


@csrf_exempt  
@require_POST
def chatbot_api_view(request):
    data = json.loads(request.body.decode('utf-8'))
    user = request.user
    question = data.get('question', '')
    sessionId = data.get('sessionId', "0")
    session_manager = ChatSessionManager(user=user)   # Inicializa el gestor de sesiones de chat
    response_timestamp=timezone.now()
    
    # Determina si iniciar una nueva sesión o usar una existente
    session_id_int = int(sessionId)
    if session_id_int == 0:
        session = session_manager.start_new_session()
    else:
        try:
            # Asegúrate de que sessionId pueda convertirse a int
            session = session_manager.select_session(session_id_int)
        except ValueError:
            # sessionId no es ni 'new' ni un número válido
            return JsonResponse({"error": "SessionId inválido."}, status=400)
        except ChatSession.DoesNotExist:
            return JsonResponse({"error": "Sesión no válida o no encontrada."}, status=404)

    # Serializa la conversación actual de la sesión
    conversation = session_manager.serialize_conversation(session.id)
    history = conversation.get("history", [])
    
    # Prepara el payload para el servicio externo
    payload = {
        "question": question,
        "history": history  # Envía el historial de la conversación al servicio externo
    }


    ENDPOINT_LANGCHIAN = os.environ.get(
        'ENDPOINT_LANGCHIAN', 'default_value_if_not_set')
    url = ENDPOINT_LANGCHIAN
    TOKEN_LANGCHIAN = os.environ.get(
        'TOKEN_LANGCHIAN', 'default_value_if_not_set')
    token = TOKEN_LANGCHIAN

    # Envía la solicitud al servicio externo
    headers = {'Authorization': f'Bearer {token}'}
    response = requests.post(url, json=payload, headers=headers)

    if response.status_code == 200:
        response_data = response.json()
        bot_response = response_data.get('text', '')
        session_manager.add_message(
            session.id, question, bot_response, response_timestamp)
        # Prepara la respuesta para el cliente incluyendo tanto la respuesta del bot como el sessionId actualizado
        client_response = {
            'text': bot_response,
            'sessionId': session.id
        }
        return JsonResponse(client_response)
    else:
        return JsonResponse({"error": "Hubo un problema al procesar tu pregunta."}, status=500)
