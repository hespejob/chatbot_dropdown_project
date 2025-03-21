from flask import Flask, render_template, jsonify, request
from fuzzywuzzy import fuzz, process
import requests
import os

app = Flask(__name__)

# =========================
# 1. DATA & CONFIG
# =========================

# Service data for chatbot and cards
services_data = [
    {"name": "Facial Cleansing", "description": "Facial Cleansing helps deeply clean your skin, removing dirt and oils for clearer skin."},
    {"name": "Hydrafacial", "description": "Hydrafacial provides hydration and exfoliation, leaving your skin glowing and refreshed."},
    {"name": "Mesotherapy", "description": "Mesotherapy is a preventative treatment that enriches the skin with vitamins and hydration."},
    {"name": "Platelet Rich Plasma", "description": "PRP revitalizes the skin by using your body’s own growth factors for healing and rejuvenation."},
    {"name": "Botox", "description": "Botox smooths wrinkles and fine lines, giving you a more youthful and refreshed appearance."},
    {"name": "Dermal Fillers", "description": "Dermal fillers restore facial volume and reduce wrinkles, enhancing your natural beauty."},
    {"name": "Laser Hair Removal", "description": "Laser Hair Removal permanently reduces unwanted hair for smooth, hair-free skin."},
    {"name": "Microdermabrasion", "description": "Microdermabrasion gently exfoliates and renews the skin’s surface, improving texture and tone."},
    {"name": "Chemical Peel", "description": "Chemical peels rejuvenate the skin by removing dead skin cells and revealing a smoother complexion."},
    {"name": "RF Skin Tightening", "description": "RF Skin Tightening is a non-invasive treatment to lift and firm sagging skin without surgery."},
    {"name": "Cryotherapy", "description": "Cryotherapy uses cooling to tone and tighten the skin, enhancing its natural glow."},
    {"name": "Body Contouring", "description": "Body Contouring shapes and tones the body, giving you a more sculpted appearance without surgery."},
    {"name": "Tattoo Removal", "description": "Tattoo removal safely and effectively fades unwanted tattoos with advanced laser technology."},
    {"name": "Cellulite Reduction", "description": "Cellulite reduction treatments target cellulite, leaving the skin smoother and firmer."},
    {"name": "Acne Treatment", "description": "Our acne treatments target the root causes of acne, leaving your skin clear and blemish-free."}
]

# You can still keep or remove this dictionary if you wish.
general_responses = {
    "hi": "Hello! How can I assist you today?",
    "hello": "Hi there! Feel free to ask me about any of our services.",
    "contact": "You can contact us at +51 981640627.",
    "location": "We are located at 123 Main Street, Lima, Peru.",
    "services": "We offer a range of services such as Facial Cleansing, Hydrafacial, Mesotherapy, and more.",
    "price": "The price for each service depends on the type and session duration. Please contact us for more details."
}

# =========================
# 2. GEMINI CONFIG & HELPER
# =========================

GEMINI_API_URL = "https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent"
GEMINI_API_KEY = "AIzaSyCocRQfyEnaKBB7bsHvgYO9hkeKSPN0pFI"  # Reemplaza con tu clave real

def get_gemini_response(prompt):
    """
    Send the prompt to Gemini API and return the AI-generated response.
    """
    url = f"https://generativelanguage.googleapis.com/v1/models/gemini-1.5-flash:generateContent?key={GEMINI_API_KEY}"
    
    payload = {
        "contents": [{"parts": [{"text": prompt}]}]  # Correct payload format
    }

    headers = {
        "Content-Type": "application/json"
    }
    
    try:
        response = requests.post(url, json=payload, headers=headers)
        if response.status_code == 200:
            data = response.json()
            return data["candidates"][0]["content"]["parts"][0]["text"]  # Extract response
        else:
            print("Gemini API error:", response.status_code, response.text)
            return "Lo siento, algo salió mal al obtener la respuesta de Gemini."
    except Exception as e:
        print("Error calling Gemini API:", e)
        return "Lo siento, actualmente no puedo responder esa pregunta."

# =========================
# 3. FUZZY MATCHING HELPERS
# =========================

def detect_closest_service(user_message):
    """
    Use fuzzy matching to find if the user's message references a known service.
    """
    user_message_lower = user_message.lower()
    service_names = [service['name'] for service in services_data]
    best_match, match_score = process.extractOne(user_message_lower, service_names, scorer=fuzz.token_sort_ratio)
    if match_score > 60:  # threshold
        for service in services_data:
            if service['name'].lower() == best_match.lower():
                return service
    return None

def detect_closest_general_response(user_message):
    """
    Use fuzzy matching to find if the user's message references a known general question/response.
    """
    user_message_lower = user_message.lower()
    best_match, match_score = process.extractOne(user_message_lower, general_responses.keys(), scorer=fuzz.token_sort_ratio)
    if match_score > 60:
        return general_responses[best_match]
    return None

# =========================
# 4. ROUTES
# =========================

@app.route("/")
def home():
    """
    Render the main page (index.html) which loads your chatbot UI and service cards.
    """
    return render_template("index.html", services=services_data)

@app.route("/gemini-api", methods=["POST"])
def gemini_api():
    """
    Handles chatbot fallback requests to Gemini API.
    """
    try:
        data = request.get_json()
        user_prompt = data.get("message", "").strip()
        if not user_prompt:
            return jsonify({"response": "Lo siento, no recibí una pregunta válida."})

        gemini_resp = get_gemini_response(user_prompt)
        return jsonify({"response": gemini_resp})

    except Exception as e:
        print("Flask API Error:", e)
        return jsonify({"response": "Lo siento, algo salió mal en el servidor."})


@app.route("/submit-appointment", methods=["POST"])
def submit_appointment():
    """
    Example endpoint if you want to handle a booking flow in the back end.
    """
    user_message = request.json.get("message", "").lower()
    # For example, you can store the user's chosen date, etc.
    # Then build a response or link to WhatsApp.
    response = "Thank you! I will now confirm the details via WhatsApp."
    whatsapp_link = "https://api.whatsapp.com/send?phone=51981640627&text=Booking%20confirmation"
    return jsonify({"response": response, "whatsapp_link": whatsapp_link})

if __name__ == "__main__":
    # Bind to the appropriate host and port for Render
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=True)
