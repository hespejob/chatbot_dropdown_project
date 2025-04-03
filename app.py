from flask import Flask, request, render_template, jsonify
from fuzzywuzzy import fuzz, process
import requests
import os

app = Flask(__name__)

# =========================
# 1. VERIFICAR TOKEN PARA WHATSAPP
# =========================
VERIFY_TOKEN = "tokenchatbot"

# =========================
# 2. SERVICIOS Y RESPUESTAS GENERALES
# =========================
services_data = [
    {"name": "Limpieza Facial", "description": "La limpieza facial ayuda a limpiar profundamente tu piel, eliminando la suciedad y el exceso de sebo para una piel más clara."},
    {"name": "Hydrafacial", "description": "Hydrafacial proporciona hidratación y exfoliación, dejando tu piel radiante y fresca."},
    {"name": "Mesoterapia", "description": "La mesoterapia es un tratamiento preventivo que enriquece la piel con vitaminas e hidratación."},
    {"name": "Plasma Rico en Plaquetas", "description": "El Plasma Rico en Plaquetas (PRP) revitaliza la piel utilizando los factores de crecimiento de tu propio cuerpo para promover la curación y el rejuvenecimiento."},
    {"name": "Botox", "description": "El Botox suaviza arrugas y líneas finas, proporcionando una apariencia más juvenil y fresca."},
    {"name": "Rellenos Dérmicos", "description": "Los rellenos dérmicos restauran el volumen facial y reducen las arrugas, realzando tu belleza natural."},
    {"name": "Depilación Láser", "description": "La depilación láser reduce permanentemente el vello no deseado para una piel suave y sin vello."},
    {"name": "Microdermoabrasión", "description": "La microdermoabrasión exfolia y renueva suavemente la superficie de la piel, mejorando su textura y tono."},
    {"name": "Peeling Químico", "description": "El peeling químico rejuvenece la piel eliminando las células muertas y revelando una complexión más suave."},
    {"name": "RF para Reafirmar la Piel", "description": "El tratamiento con radiofrecuencia reafirma y levanta la piel flácida sin necesidad de cirugía."},
    {"name": "Crioterapia", "description": "La crioterapia utiliza el frío para tonificar y reafirmar la piel, realzando su brillo natural."},
    {"name": "Contorno Corporal", "description": "El contorno corporal moldea y tonifica el cuerpo, ofreciéndote una apariencia más esculpida sin cirugía."},
    {"name": "Eliminación de Tatuajes", "description": "La eliminación de tatuajes desvanece de forma segura y eficaz los tatuajes no deseados mediante tecnología láser avanzada."},
    {"name": "Reducción de Celulitis", "description": "Los tratamientos para la reducción de celulitis se enfocan en suavizar la piel y reducir la apariencia de la celulitis."},
    {"name": "Tratamiento para el Acné", "description": "Nuestros tratamientos para el acné combaten las causas fundamentales del acné, dejando la piel limpia y sin imperfecciones."}
]

general_responses = {
    "hola": "¡Hola! ¿En qué puedo ayudarte hoy?",
    "saludo": "¡Hola! No dudes en preguntarme sobre cualquiera de nuestros servicios.",
    "contacto": "Puedes contactarnos al +51 981640627.",
    "ubicación": "Estamos ubicados en 123 Main Street, Lima, Perú.",
    "servicios": "Ofrecemos servicios como Limpieza Facial, Hydrafacial, Mesoterapia y más.",
    "precio": "Los precios varían según el servicio y la duración. Contáctanos para más detalles."
}

# =========================
# 3. INTEGRACIÓN CON LA API DE GEMINI
# =========================
GEMINI_API_KEY = "AIzaSyCocRQfyEnaKBB7bsHvgYO9hkeKSPN0pFI"

def get_gemini_response(prompt):
    # Añadir instrucción para que la respuesta sea en español
    prompt_in_spanish = prompt + "\n\nPor favor, responde en español."
    url = f"https://generativelanguage.googleapis.com/v1/models/gemini-1.5-flash:generateContent?key={GEMINI_API_KEY}"
    payload = {"contents": [{"parts": [{"text": prompt_in_spanish}]}]}
    headers = {"Content-Type": "application/json"}

    try:
        response = requests.post(url, json=payload, headers=headers)
        if response.status_code == 200:
            data = response.json()
            return data["candidates"][0]["content"]["parts"][0]["text"]
        else:
            print("Error en la API de Gemini:", response.status_code, response.text)
            return "Lo siento, ocurrió un error al obtener la respuesta de Gemini."
    except Exception as e:
        print("Error al llamar a la API de Gemini:", e)
        return "Lo siento, no puedo responder en este momento."

# =========================
# 4. AYUDAS CON FUZZY
# =========================
def detect_closest_service(user_message):
    service_names = [s['name'] for s in services_data]
    best_match, score = process.extractOne(user_message.lower(), service_names, scorer=fuzz.token_sort_ratio)
    if score > 60:
        for s in services_data:
            if s['name'].lower() == best_match.lower():
                return s
    return None

def detect_closest_general_response(user_message):
    best_match, score = process.extractOne(user_message.lower(), general_responses.keys(), scorer=fuzz.token_sort_ratio)
    if score > 60:
        return general_responses[best_match]
    return None

# =========================
# 5. RUTAS PARA EL CHATBOT + WHATSAPP
# =========================

@app.route('/')
def home():
    return render_template("index.html", services=services_data)

@app.route('/gemini-api', methods=['POST'])
def gemini_api():
    data = request.get_json()
    user_prompt = data.get("message", "").strip()
    if not user_prompt:
        return jsonify({"response": "No se recibió una entrada válida."})
    reply = get_gemini_response(user_prompt)
    return jsonify({"response": reply})

@app.route('/submit-appointment', methods=["POST"])
def submit_appointment():
    response = "¡Gracias! Ahora confirmaremos los detalles a través de WhatsApp."
    whatsapp_link = "https://api.whatsapp.com/send?phone=51981640627&text=Confirmación%20de%20cita"
    return jsonify({"response": response, "whatsapp_link": whatsapp_link})

@app.route('/webhook', methods=['GET', 'POST'])
def webhook():
    if request.method == 'GET':
        # Verificación desde el panel de Meta
        token = request.args.get('hub.verify_token')
        challenge = request.args.get('hub.challenge')
        if token == VERIFY_TOKEN:
            return challenge, 200
        return "Token de verificación inválido", 403

    if request.method == 'POST':
        data = request.get_json()
        print("Mensaje de WhatsApp recibido:", data)

        try:
            message_text = data['entry'][0]['changes'][0]['value']['messages'][0]['text']['body']
            sender_id = data['entry'][0]['changes'][0]['value']['messages'][0]['from']
            
            # Lógica del chatbot
            response_text = detect_closest_general_response(message_text)
            if not response_text:
                service = detect_closest_service(message_text)
                if service:
                    response_text = service["description"]
                else:
                    response_text = get_gemini_response(message_text)

            # Aquí puedes integrar el envío de la respuesta vía la API de WhatsApp
            print(f"Respondiendo a {sender_id}: {response_text}")
            # Para responder efectivamente, necesitarás usar la API de envío de mensajes de Meta.

        except Exception as e:
            print("Error al procesar el mensaje de WhatsApp:", e)

        return "OK", 200

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=True)
