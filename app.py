from flask import Flask, request, render_template, jsonify
from fuzzywuzzy import fuzz, process
import requests
import os

app = Flask(__name__)

# =========================
# 1. VERIFY TOKEN FOR WHATSAPP
# =========================
VERIFY_TOKEN = "tokenchatbot"

# =========================
# 2. SERVICES & GENERAL RESPONSES
# =========================
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

general_responses = {
    "hi": "Hello! How can I assist you today?",
    "hello": "Hi there! Feel free to ask me about any of our services.",
    "contact": "You can contact us at +51 981640627.",
    "location": "We are located at 123 Main Street, Lima, Peru.",
    "services": "We offer services like Facial Cleansing, Hydrafacial, Mesotherapy, and more.",
    "price": "Prices vary by service and duration. Contact us for full details."
}

# =========================
# 3. GEMINI API INTEGRATION
# =========================
GEMINI_API_KEY = "AIzaSyCocRQfyEnaKBB7bsHvgYO9hkeKSPN0pFI"

def get_gemini_response(prompt):
    url = f"https://generativelanguage.googleapis.com/v1/models/gemini-1.5-flash:generateContent?key={GEMINI_API_KEY}"
    payload = {"contents": [{"parts": [{"text": prompt}]}]}
    headers = {"Content-Type": "application/json"}

    try:
        response = requests.post(url, json=payload, headers=headers)
        if response.status_code == 200:
            data = response.json()
            return data["candidates"][0]["content"]["parts"][0]["text"]
        else:
            print("Gemini API error:", response.status_code, response.text)
            return "Sorry, an error occurred while fetching Gemini response."
    except Exception as e:
        print("Error calling Gemini API:", e)
        return "Sorry, I can't respond at the moment."

# =========================
# 4. FUZZY HELPERS
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
# 5. ROUTES FOR CHATBOT + WHATSAPP
# =========================

@app.route('/')
def home():
    return render_template("index.html", services=services_data)

@app.route('/gemini-api', methods=['POST'])
def gemini_api():
    data = request.get_json()
    user_prompt = data.get("message", "").strip()
    if not user_prompt:
        return jsonify({"response": "No valid input received."})
    reply = get_gemini_response(user_prompt)
    return jsonify({"response": reply})

@app.route('/submit-appointment', methods=["POST"])
def submit_appointment():
    response = "Thank you! I will now confirm the details via WhatsApp."
    whatsapp_link = "https://api.whatsapp.com/send?phone=51981640627&text=Booking%20confirmation"
    return jsonify({"response": response, "whatsapp_link": whatsapp_link})

@app.route('/webhook', methods=['GET', 'POST'])
def webhook():
    if request.method == 'GET':
        # Verification from Meta dashboard
        token = request.args.get('hub.verify_token')
        challenge = request.args.get('hub.challenge')
        if token == VERIFY_TOKEN:
            return challenge, 200
        return "Invalid verification token", 403

    if request.method == 'POST':
        data = request.get_json()
        print("Received WhatsApp message:", data)

        try:
            message_text = data['entry'][0]['changes'][0]['value']['messages'][0]['text']['body']
            sender_id = data['entry'][0]['changes'][0]['value']['messages'][0]['from']
            
            # Chatbot logic
            response_text = detect_closest_general_response(message_text)
            if not response_text:
                service = detect_closest_service(message_text)
                if service:
                    response_text = service["description"]
                else:
                    response_text = get_gemini_response(message_text)

            # Here you can integrate sending a response via WhatsApp API (using message templates or session messages)
            print(f"Responding to {sender_id}: {response_text}")
            # To actually respond, you'll need to use Meta's send message API here.

        except Exception as e:
            print("Error handling WhatsApp message:", e)

        return "OK", 200

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=True)
