from flask import Flask, render_template, jsonify, request
from fuzzywuzzy import fuzz, process
import os

app = Flask(__name__)

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

# General responses/questions
general_responses = {
    "hi": "Hello! How can I assist you today? 😊",
    "hello": "Hi there! Feel free to ask me about any of our services. 🌟",
    "contact": "📞 You can contact us at +51 987 632 686.",
    "location": "📍 We are located at 123 Main Street, Lima, Peru.",
    "services": "💆 We offer a range of services such as Facial Cleansing, Hydrafacial, Mesotherapy, and more.",
    "price": "💵 The price for each service depends on the type and session duration. Please contact us for more details."
}

# Store user conversation state
user_conversations = {}

# Function to detect the closest general response based on fuzzy matching
def detect_closest_general_response(user_message):
    user_message_lower = user_message.lower()
    # Use fuzzy matching to find the best match from the general responses
    best_match, match_score = process.extractOne(user_message_lower, general_responses.keys(), scorer=fuzz.token_sort_ratio)

    # Set a threshold score for how "close" the match needs to be
    if match_score > 60:  # Lowered threshold for better typo tolerance
        return general_responses[best_match]
    return None

# Function to detect the closest service based on fuzzy matching
def detect_closest_service(user_message):
    user_message_lower = user_message.lower()
    service_names = [service['name'] for service in services_data]
    best_match, match_score = process.extractOne(user_message_lower, service_names, scorer=fuzz.token_sort_ratio)

    if match_score > 60:  # Lowered threshold
        for service in services_data:
            if service['name'].lower() == best_match.lower():
                return service
    return None

@app.route("/")
def home():
    return render_template("index.html", services=services_data)

@app.route("/get-response", methods=["POST"])
def get_response():
    user_message = request.json.get("message", "").lower()  # Get the user's message and convert it to lowercase
    user_id = request.remote_addr  # Using the user's IP as a temporary user identifier

    if user_id not in user_conversations:
        user_conversations[user_id] = {"state": "initial", "service": None, "date": None}

    conversation = user_conversations[user_id]

    # First check for service-related queries using fuzzy matching
    detected_service = detect_closest_service(user_message)
    if detected_service:
        conversation["service"] = detected_service['name']
        response = f"Great! You have selected {detected_service['name']}. Please select a date for the appointment using the calendar below. 📅"
        conversation["state"] = "awaiting_date"
        return jsonify({"response": response})

    # If no service match, check for general responses using fuzzy matching
    general_response = detect_closest_general_response(user_message)
    if general_response:
        conversation["state"] = "service_info"
        return jsonify({"response": general_response})

    # Default response if no match
    return jsonify({"response": "🤔 I didn't quite get that. Could you ask again or select a service?"})

@app.route("/submit-appointment", methods=["POST"])
def submit_appointment():
    user_message = request.json.get("message", "").lower()
    user_id = request.remote_addr  # Using the user's IP as a temporary user identifier
    conversation = user_conversations.get(user_id, None)

    if conversation and conversation["state"] == "awaiting_date":
        conversation["date"] = user_message
        response = f"Thank you! 🙏 You are booking {conversation['service']} on {conversation['date']}. I will now confirm the details via WhatsApp."

        # Send WhatsApp booking message link
        whatsapp_message = f"I would like to book an appointment for {conversation['service']} on {conversation['date']}."
        whatsapp_link = f"https://api.whatsapp.com/send?phone=51987632686&text={whatsapp_message}"

        conversation["state"] = "completed"
        return jsonify({"response": response, "whatsapp_link": whatsapp_link})

    return jsonify({"response": "⚠️ Please enter a valid date for the appointment."})

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))  # Use the PORT environment variable or default to 5000
    app.run(host="0.0.0.0", port=port, debug=True)
