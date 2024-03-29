
// Función para obtener el valor de una cookie por su nombre (necesario para el CSRF token)
function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}


function enviarMensaje() {
    var userInput = document.getElementById("user-input").value.trim();
    var chatbotWindow = document.getElementById("chatbot");

    // Verifica si el userInput está vacío
    if(userInput === '') {
        return; // No hace nada si el input está vacío
    }

    // Mostrar el mensaje del usuario en la ventana del chatbot
    chatbotWindow.innerHTML += `
        <div class="card-text">
            <strong>Tú:</strong> ${userInput}
        </div>
    `;

    // Configuración de la solicitud AJAX
    fetch('/api/chatbot/', {  // Asegúrate de que esta URL coincida con la configurada en urls.py
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': getCookie('csrftoken'), // Asegúrate de manejar el CSRF token correctamente
        },
        body: JSON.stringify({ question: userInput })
    })
    .then(response => response.json())
    .then(data => {
        // Procesa la respuesta del servidor y actualiza el chatbotWindow
        const respuestaBot = data.text || "Lo siento, no puedo responder a eso en este momento.";
        chatbotWindow.innerHTML += `<div class="card-text"><strong>Bot:</strong> ${respuestaBot}</div>`;

        // Desplázate automáticamente hacia la parte inferior de la ventana del chatbot
        chatbotWindow.scrollTop = chatbotWindow.scrollHeight;
    })
    .catch(error => {
        console.error('Error:', error);
        chatbotWindow.innerHTML += `<div class="card-text"><strong>Bot:</strong> Hubo un error al procesar tu mensaje.</div>`;
    });

    // Limpia el campo de entrada de texto después de enviar el mensaje
    document.getElementById("user-input").value = "";
}
