import requests
from flask import Flask, request, render_template, jsonify
from fuzzywuzzy import fuzz, process
import os

app = Flask(__name__)

# WhatsApp Config
ACCESS_TOKEN = "EAAZABMTzly0UBOZCwY69XvB6U1SSz4pC0VW5oaZC0PfGV5s4YuSV5cZBNE0UtlT2LLhi9H89gl7BKvPsXE2sHTZA4TwIjJNZA97rq92zKdcmrRXXQzf5tOROZAkj7r3XREhkGGihbsrOpohCPTxTo3xQv5BUcuPiZBhGOJ0ZBwmfpOD767P4Eumv1dtheD90mufylMJ4aUvw0MCo424vssgPfFNVsjQZDZD"
PHONE_NUMBER_ID = "622394210957095"
VERIFY_TOKEN = "tokenchatbot"

# Services Data
services_data = [
    {"name": "Limpieza Facial", "description": "La limpieza facial ayuda a limpiar profundamente tu piel, eliminando la suciedad y el exceso de sebo para una piel más clara."},
    {"name": "Hydrafacial", "description": "Hydrafacial proporciona hidratación y exfoliación, dejando tu piel radiante y fresca."},
    {"name": "Mesoterapia", "description": "La mesoterapia es un tratamiento preventivo que enriquece la piel con vitaminas e hidratación."},
    {"name": "Plasma Rico en Plaquetas", "description": "El PRP revitaliza la piel usando factores de crecimiento de tu propio cuerpo."},
    # (You can keep the rest of the services here)
]

general_responses = {
    "hola": "¡Hola! ¿En qué puedo ayudarte hoy?",
    "saludo": "¡Hola! No dudes en preguntarme sobre cualquiera de nuestros servicios.",
    "contacto": "Puedes contactarnos al ‪‪+51 981640627‬‬.",
    "ubicación": "Estamos ubicados en 123 Main Street, Lima, Perú.",
    "servicios": "Ofrecemos servicios como Limpieza Facial, Hydrafacial, Mesoterapia y más.",
    "precio": "Los precios varían según el servicio. Contáctanos para más detalles."
}

# Gemini Integration
GEMINI_API_KEY = "AIzaSyCocRQfyEnaKBB7bsHvgYO9hkeKSPN0pFI"

def get_gemini_response(prompt):
    prompt += "\n\nPor favor, responde en español."
    url = f"‪https://generativelanguage.googleapis.com/v1/models/gemini-1.5-flash:generateContent?key=‬{GEMINI_API_KEY}"
    headers = {"Content-Type": "application/json"}
    payload = {"contents": [{"parts": [{"text": prompt}]}]}
    try:
        r = ‪requests.post‬(url, json=payload, headers=headers)
        return r.json()["candidates"][0]["content"]["parts"][0]["text"]
    except Exception as e:
        print("Gemini error:", e)
        return "Lo siento, no puedo responder en este momento."

# Fuzzy Logic Helpers
def detect_closest_service(msg):
    names = [s['name'] for s in services_data]
    best, score = process.extractOne(msg.lower(), names, scorer=fuzz.token_sort_ratio)
    if score > 60:
        return next(s for s in services_data if s['name'].lower() == best.lower())
    return None

def detect_closest_general_response(msg):
    best, score = process.extractOne(msg.lower(), general_responses.keys(), scorer=fuzz.token_sort_ratio)
    return general_responses[best] if score > 60 else None

# ✅ WhatsApp message sender
def send_whatsapp_message(recipient_id, message_text):
    url = f"‪https://graph.facebook.com/v17.0/‬{PHONE_NUMBER_ID}/messages"
    headers = {
        "Authorization": f"Bearer {ACCESS_TOKEN}",
        "Content-Type": "application/json"
    }
    payload = {
        "messaging_product": "whatsapp",
        "to": recipient_id,
        "type": "text",
        "text": {"body": message_text}
    }
    try:
        response = ‪requests.post‬(url, headers=headers, json=payload)
        print("Message sent:", response.status_code, response.text)
    except Exception as e:
        print("Sending error:", e)

# Routes
@app.route('/')
def home():
    return render_template("index.html", services=services_data)

@app.route('/gemini-api', methods=['POST'])
def gemini_api():
    data = request.get_json()
    user_prompt = data.get("message", "").strip()
    reply = get_gemini_response(user_prompt)
    return jsonify({"response": reply or "No se pudo obtener respuesta."})

@app.route('/submit-appointment', methods=["POST"])
def submit_appointment():
    response = "¡Gracias! Ahora confirmaremos los detalles a través de WhatsApp."
    whatsapp_link = "‪https://api.whatsapp.com/send?phone=51981640627&text=Confirmación%20de%20cita‬"
    return jsonify({"response": response, "whatsapp_link": whatsapp_link})

@app.route('/webhook', methods=['GET', 'POST'])
def webhook():
    if request.method == 'GET':
        token = request.args.get('hub.verify_token')
        challenge = request.args.get('hub.challenge')
        return (challenge, 200) if token == VERIFY_TOKEN else ("Token inválido", 403)

    if request.method == 'POST':
        data = request.get_json()
        print("WhatsApp message received:", data)
        try:
            message_text = data['entry'][0]['changes'][0]['value']['messages'][0]['text']['body']
            sender_id = data['entry'][0]['changes'][0]['value']['messages'][0]['from']

            response_text = detect_closest_general_response(message_text)
            if not response_text:
                service = detect_closest_service(message_text)
                response_text = service["description"] if service else get_gemini_response(message_text)

            send_whatsapp_message(sender_id, response_text)
        except Exception as e:
            print("Webhook error:", e)
        return "OK", 200

if _name_ == '_main_':
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=True)
