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
    {
        "name": "Limpieza Facial",
        "description": "La limpieza facial ayuda a limpiar profundamente tu piel, eliminando la suciedad y el exceso de sebo para una piel más clara.",
        "benefits": "Piel limpia, hidratada y luminosa.",
        "sideEffects": "Puede causar enrojecimiento temporal.",
        "precio": "S/ 100"
    },
    {
        "name": "Hydrafacial",
        "description": "Hydrafacial proporciona hidratación y exfoliación, dejando tu piel radiante y fresca.",
        "benefits": "Hidratación profunda, piel más suave y luminosa.",
        "sideEffects": "Enrojecimiento leve o sensibilidad temporal.",
        "precio": "S/ 180"
    },
    {
        "name": "Mesoterapia",
        "description": "La mesoterapia es un tratamiento preventivo que enriquece la piel con vitaminas e hidratación.",
        "benefits": "Rejuvenecimiento facial, piel más firme y nutrida.",
        "sideEffects": "Enrojecimiento, picazón o hematomas leves.",
        "precio": "S/ 150"
    },
    {
        "name": "Plasma Rico en Plaquetas",
        "description": "El PRP revitaliza la piel utilizando los factores de crecimiento de tu propio cuerpo.",
        "benefits": "Regeneración celular, mejora de textura y brillo.",
        "sideEffects": "Hinchazón, sensibilidad temporal.",
        "precio": "S/ 250"
    },
    {
        "name": "Botox",
        "description": "El Botox suaviza arrugas y líneas finas, proporcionando una apariencia más juvenil y fresca.",
        "benefits": "Suaviza arrugas dinámicas y líneas de expresión.",
        "sideEffects": "Hinchazón o moretones leves en el área tratada.",
        "precio": "S/ 300"
    },
    {
        "name": "Rellenos Dérmicos",
        "description": "Los rellenos dérmicos restauran el volumen facial y reducen las arrugas.",
        "benefits": "Rostro más definido, reducción de arrugas profundas.",
        "sideEffects": "Inflamación o hematomas leves.",
        "precio": "S/ 350"
    },
    {
        "name": "Depilación Láser",
        "description": "La depilación láser reduce permanentemente el vello no deseado.",
        "benefits": "Piel suave y sin vello por más tiempo.",
        "sideEffects": "Irritación leve, enrojecimiento temporal.",
        "precio": "Desde S/ 90 por zona"
    },
    {
        "name": "Microdermoabrasión",
        "description": "Exfoliación mecánica que renueva la superficie de la piel.",
        "benefits": "Mejora la textura y el tono de la piel.",
        "sideEffects": "Enrojecimiento leve.",
        "precio": "S/ 120"
    },
    {
        "name": "Peeling Químico",
        "description": "Elimina las células muertas y revela una piel más suave.",
        "benefits": "Rejuvenecimiento cutáneo, reduce manchas.",
        "sideEffects": "Descamación, sensibilidad temporal.",
        "precio": "S/ 140"
    },
    {
        "name": "RF para Reafirmar la Piel",
        "description": "Radiofrecuencia que reafirma y levanta la piel sin cirugía.",
        "benefits": "Piel más firme, mejora de flacidez.",
        "sideEffects": "Calor leve o enrojecimiento.",
        "precio": "S/ 160"
    },
    {
        "name": "Crioterapia",
        "description": "Tratamiento con frío para tonificar y reafirmar la piel.",
        "benefits": "Efecto lifting inmediato, piel revitalizada.",
        "sideEffects": "Sensación de frío intenso temporal.",
        "precio": "S/ 110"
    },
    {
        "name": "Contorno Corporal",
        "description": "Moldea y tonifica el cuerpo sin cirugía.",
        "benefits": "Reduce grasa localizada, mejora firmeza.",
        "sideEffects": "Enrojecimiento leve, sensación de calor.",
        "precio": "Desde S/ 180"
    },
    {
        "name": "Eliminación de Tatuajes",
        "description": "Tecnología láser para eliminar tatuajes de manera segura.",
        "benefits": "Desvanecimiento progresivo del tatuaje.",
        "sideEffects": "Sensación de ardor, enrojecimiento temporal.",
        "precio": "Desde S/ 200 por sesión"
    },
    {
        "name": "Reducción de Celulitis",
        "description": "Tratamientos para suavizar la piel y reducir la celulitis.",
        "benefits": "Piel más lisa y firme.",
        "sideEffects": "Leve sensibilidad o enrojecimiento.",
        "precio": "S/ 150"
    },
    {
        "name": "Tratamiento para el Acné",
        "description": "Combate las causas fundamentales del acné.",
        "benefits": "Reducción de brotes y marcas.",
        "sideEffects": "Sensibilidad en pieles reactivas.",
        "precio": "S/ 130"
    }
]

general_responses = {
    "hola": "¡Hola! ¿En qué puedo ayudarte hoy?",
    "saludo": "¡Hola! No dudes en preguntarme sobre cualquiera de nuestros servicios.",
    "contacto": "Puedes contactarnos al +51 981640627.",
    "ubicación": "Estamos ubicados en 123 Main Street, Lima, Perú.",
    "servicios": "Ofrecemos servicios como Limpieza Facial, Hydrafacial, Mesoterapia y más.",
    "precio": "Los precios varían según el servicio y la duración. Contáctanos para más detalles."
}
# Gemini API Config
GEMINI_API_KEY = "AIzaSyCocRQfyEnaKBB7bsHvgYO9hkeKSPN0pFI"

def get_gemini_response(prompt):
    prompt += "\n\nActua como un experto en Tratamiento facial, responde en español."
    url = f"https://generativelanguage.googleapis.com/v1/models/gemini-1.5-flash:generateContent?key={GEMINI_API_KEY}"
    headers = {"Content-Type": "application/json"}
    payload = {"contents": [{"parts": [{"text": prompt}]}]}
    try:
        r = requests.post(url, json=payload, headers=headers)
        return r.json()["candidates"][0]["content"]["parts"][0]["text"]
    except Exception as e:
        return "Lo siento, no puedo responder en este momento."

# Fuzzy logic
def detect_closest_service(msg):
    names = [s['name'] for s in services_data]
    best, score = process.extractOne(msg.lower(), names, scorer=fuzz.token_sort_ratio)
    if score > 60:
        return next(s for s in services_data if s['name'].lower() == best.lower())
    return None

def detect_closest_general_response(msg):
    best, score = process.extractOne(msg.lower(), general_responses.keys(), scorer=fuzz.token_sort_ratio)
    return general_responses[best] if score > 60 else None

# Nuevo: Generador de respuesta de servicio
def generate_service_response(user_msg, service):
    msg = user_msg.lower()
    if "benefits" in msg or "beneficios" in msg:
        return f"Los beneficios de {service['name']} son: {service.get('benefits', 'Información no disponible')}."
    elif "side effects" in msg or "efectos secundarios" in msg or "efectos-secundarios" in msg:
        return f"Los efectos secundarios de {service['name']} son: {service.get('sideEffects', 'Información no disponible')}."
    elif "precio" in msg or "price" in msg:
        return f"El precio de {service['name']} es: {service.get('precio', 'Por favor contáctanos para más detalles.')}."
    elif "qué es" in msg or "descripcion" in msg or "description" in msg:
        return f"Aquí tienes una descripción de {service['name']}: {service['description']}."
    else:
        return f"Has preguntado acerca de {service['name']}. Aquí una breve descripción: {service['description']}."

# Enviar mensaje a WhatsApp
def send_whatsapp_message(recipient_id, message_text):
    url = f"https://graph.facebook.com/v17.0/{PHONE_NUMBER_ID}/messages"
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
        response = requests.post(url, headers=headers, json=payload)
        print("Message sent:", response.status_code, response.text)
    except Exception as e:
        print("Sending error:", e)

# Rutas
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
    whatsapp_link = "https://api.whatsapp.com/send?phone=51981640627&text=Confirmación%20de%20cita"
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

            # First, try to detect if the query is about a specific service.
            service = detect_closest_service(message_text)
            if service:
                response_text = generate_service_response(message_text, service)
            else:
                # Next, check if there's a general response.
                general_response = detect_closest_general_response(message_text)
                if general_response:
                    response_text = general_response
                else:
                    # If none of the above, fall back to Gemini.
                    response_text = get_gemini_response(message_text)

            send_whatsapp_message(sender_id, response_text)
        except Exception as e:
            print("Webhook error:", e)
        return "OK", 200

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=True)
