// =========================
// 1. DATOS DE SERVICIOS
// =========================
const services = [
    {
        name: "Limpieza Facial",
        description: "La Limpieza Facial es una técnica que limpia profundamente la piel, eliminando impurezas, células muertas, comedones, exceso de sebo y obstrucciones de los poros.",
        benefits: "Piel profundamente limpia, hidratada y rejuvenecida, con mayor luminosidad, reducción de puntos negros y una textura más suave.",
        sideEffects: "Puede causar enrojecimiento leve, irritación o sensibilidad temporal en la piel, que normalmente desaparecen en pocas horas.",
        whatsappMessage: "Me gustaría agendar una cita para Limpieza Facial.",
        image: "static/images/1. Limpieza Facial/2.jpg"
    },
    {
        name: "Hydrafacial",
        description: "El Hydrafacial es un tratamiento que hidrata profundamente la piel, exfoliando las células muertas y estimulando la producción de colágeno y elastina.",
        benefits: "Piel más hidratada, suave y luminosa, con reducción de líneas de expresión, poros menos visibles y una apariencia rejuvenecida.",
        sideEffects: "Puede causar enrojecimiento leve o sensibilidad temporal, pero generalmente desaparecen en pocas horas.",
        whatsappMessage: "Me gustaría agendar una cita para Hydrafacial.",
        image: "static/images/2. hydrafacial/Hydrafacial.jpg"
    },
    {
        name: "Mesoterapia",
        description: "La Mesoterapia es un tratamiento preventivo que utiliza microinfiltraciones de sustancias revitalizantes como ácido hialurónico, vitaminas, minerales y aminoácidos para mejorar la textura y luminosidad de la piel.",
        benefits: "Piel más tersa, luminosa e hidratada, con reducción de líneas de expresión, mejora en la flacidez y un tono más uniforme.",
        sideEffects: "Puede causar enrojecimiento, hinchazón o pequeños hematomas en la zona tratada, que suelen desaparecer en pocos días.",
        whatsappMessage: "Me gustaría agendar una cita para Mesoterapia.",
        image: "static/images/3. Mesoterapia/4.png"
    },
    {
        name: "Plasma Rico en Plaquetas",
        description: "El Plasma Rico en Plaquetas (PRP) es un tratamiento regenerativo que utiliza el plasma extraído de la sangre del propio paciente para estimular la producción de colágeno, elastina y promover la regeneración celular.",
        benefits: "Reducción de arrugas, mejora en la cicatrización, tratamiento del acné y manchas, y estimulación del crecimiento capilar.",
        sideEffects: "Puede causar hinchazón, enrojecimiento o pequeñas molestias en el área tratada, que desaparecen en pocos días.",
        whatsappMessage: "Me gustaría agendar una cita para PRP.",
        image: "static/images/4. Plasma Rico en Plaquetas/1.png"
    },
    {
        name: "Ácido Hialurónico",
        description: "El ácido hialurónico es una sustancia natural que retiene moléculas de agua, ayudando a mantener la hidratación, firmeza y volumen de la piel, disminuyendo los signos del envejecimiento.",
        benefits: "Hidrata profundamente la piel, reduce las arrugas, restaura el volumen perdido y mejora la firmeza, dando un aspecto más joven y radiante.",
        sideEffects: "Puede causar hinchazón, enrojecimiento o pequeños hematomas en las áreas tratadas, que suelen desaparecer en pocos días.",
        whatsappMessage: "Me gustaría agendar una cita para Botox.",
        image: "static/images/5. Acido Hialuronico/3.jpg"
    },
    {
        name: "Rinomodelación",
        description: "La rinomodelación es un procedimiento estético no invasivo que utiliza microinyecciones de rellenos dérmicos, como el ácido hialurónico, para modificar sutilmente la forma y el tamaño de la nariz, logrando una apariencia más armoniosa.",
        benefits: "Corrige pequeñas imperfecciones, mejora el perfil nasal, eleva la punta y suaviza el dorso de la nariz sin cirugía, obteniendo resultados rápidos y ajustables.",
        sideEffects: "Puede causar hinchazón, enrojecimiento o sensibilidad en el área tratada, que desaparecen en pocos días. Los resultados son temporales.",
        whatsappMessage: "Me gustaría agendar una cita para Rellenos Dérmicos.",
        image: "static/images/6. Rinomodelación/1.jpg"
    },
    {
        name: "Vitamina C E/V",
        description: "La vitamina C es esencial para la síntesis de colágeno y elastina, ayudando a fortalecer la piel y promover su regeneración.",
        benefits: "Mejora la firmeza y elasticidad de la piel, combate los radicales libres, reduce la inflamación y aclara las manchas, logrando una piel más luminosa y uniforme.",
        sideEffects: "Puede causar enrojecimiento o irritación leve en pieles sensibles, pero generalmente desaparece en pocas horas.",
        whatsappMessage: "Me gustaría agendar una cita para Depilación Láser.",
        image: "static/images/7. Vitamina C/Vitamica C.jpg"
    },
    {
        name: "Hilos Tensores",
        description: "Los Hilos Tensores son un tratamiento reafirmante que utiliza hilos biocompatibles para levantar y tensar los tejidos faciales, creando un efecto lifting inmediato y estimulando la producción de colágeno y elastina.",
        benefits: "Levanta y redefine el contorno facial, mejora la flacidez y promueve la producción de colágeno para lograr un aspecto rejuvenecido y natural.",
        sideEffects: "Puede causar hinchazón, hematomas o enrojecimiento temporal en el área tratada, que suelen desaparecer en pocos días.",
        whatsappMessage: "Me gustaría agendar una cita para Microdermoabrasión.",
        image: "static/images/8. Hilos Tensores/3.jpg"
    },
    {
        name: "Botox",
        description: "El Botox es una toxina botulínica que bloquea temporalmente las señales nerviosas que controlan los músculos, previniendo la contracción muscular y suavizando las arrugas y líneas de expresión.",
        benefits: "Suaviza las arrugas dinámicas, como las líneas de expresión y las patas de gallo, proporcionando un aspecto más joven y relajado durante varios meses.",
        sideEffects: "Puede causar hinchazón, enrojecimiento o hematomas leves en el área tratada, que generalmente desaparecen en pocos días.",
        precio: "100$",
        whatsappMessage: "Me gustaría agendar una cita para Peeling Químico.",
        image: "static/images/9. Botox/2.jpg"
    },
    {
        name: "Dermapen Facial",
        description: "El Dermapen es un tratamiento regenerativo que utiliza microagujas para crear microcanales en la piel, estimulando la producción natural de colágeno y elastina, y mejorando la textura y tono de la piel.",
        benefits: "Reduce arrugas, cicatrices de acné y poros dilatados, mejorando la textura, el tono y la apariencia general de la piel.",
        sideEffects: "Puede causar enrojecimiento, sensibilidad o hinchazón leve, que suelen desaparecer en pocos días.",
        whatsappMessage: "Me gustaría agendar una cita para RF para Reafirmar la Piel.",
        image: "static/images/10. Dermapen Facial/Dermapen.jpg"
    },
    {
        name: "Micropigmentación de Labios y efecto LIPS",
        description: "La Micropigmentación de Labios es una técnica de maquillaje semipermanente que implanta pigmentos biocompatibles en los labios, definiendo su contorno, corrigiendo asimetrías y proporcionando un color duradero con un efecto voluminoso.",
        benefits: "Labios más definidos, simétricos y voluminosos, con un color vibrante y duradero sin necesidad de retoques diarios.",
        sideEffects: "Puede causar hinchazón, enrojecimiento o sensibilidad temporal en los labios, que desaparecen en pocos días.",
        whatsappMessage: "Me gustaría agendar una cita para Crioterapia.",
        image: "static/images/11. Micropigmentación de Labios y efecto LIPS/1.jpg"
    },
    {
        name: "Micropigmentación de Cejas",
        description: "La Micropigmentación de Cejas es una técnica de maquillaje semipermanente que implanta pigmentos biocompatibles en la piel, creando la ilusión de vellos naturales y corrigiendo asimetrías para lograr unas cejas más densas y definidas.",
        benefits: "Cejas más pobladas, simétricas y definidas con un aspecto natural, eliminando la necesidad de retoques diarios y mejorando la apariencia general del rostro.",
        sideEffects: "Puede causar hinchazón, enrojecimiento o sensibilidad leve en el área tratada, los cuales suelen desaparecer en pocos días.",
        whatsappMessage: "Me gustaría agendar una cita para Contorno Corporal.",
        image: "static/images/12. Micropigmentación de Cejas/3.jpg"
    },
    {
        name: "Bioestimulador con Colágeno",
        description: "El Bioestimulador de Colágeno es un tratamiento estético que, mediante la inyección de sustancias biocompatibles, estimula la producción natural de colágeno en la piel, mejorando su firmeza y elasticidad.",
        benefits: "Rellena las arrugas desde el interior, mejora la firmeza y elasticidad de la piel, redensifica los contornos faciales y ofrece resultados naturales y progresivos.",
        sideEffects: "Puede causar hinchazón, enrojecimiento o pequeños hematomas en la zona tratada, que desaparecen en pocos días.",
        whatsappMessage: "Me gustaría agendar una cita para Eliminación de Tatuajes.",
        image: "static/images/13. Bioestimulador de Colageno/5.jpg"
    },
    {
        name: "Limpieza Facial para Adolescentes",
        description: "La Limpieza Facial para Adolescentes es un tratamiento personalizado que elimina impurezas, exceso de sebo y células muertas, ayudando a prevenir y reducir el acné, espinillas y puntos negros.",
        benefits: "Piel más limpia y equilibrada, con menos impurezas y reducción de la inflamación, contribuyendo a un aspecto más uniforme y saludable.",
        sideEffects: "Puede causar enrojecimiento o irritación leve, que suelen desaparecer rápidamente.",
        whatsappMessage: "Me gustaría agendar una cita para Reducción de Celulitis.",
        image: "static/images/14. Limpieza facial for TEENAGERS/2.jpg"
    },
    {
        name: "Cocktail de la Juventud",
        description: "El Cóctel de la Juventud es un tratamiento intravenoso que combina antioxidantes y nutrientes esenciales como la vitamina C, el glutatión, la coenzima Q10 y la biotina, estimulando la producción de colágeno y elastina para una piel más firme y rejuvenecida.",
        benefits: "Mejora la firmeza y luminosidad de la piel, combate los signos del envejecimiento, fortalece el sistema inmunológico y proporciona un aumento de energía y vitalidad.",
        sideEffects: "Puede causar leves mareos, molestias en el sitio de la infusión o reacciones alérgicas leves, que desaparecen rápidamente.",
        whatsappMessage: "Me gustaría agendar una cita para Tratamiento para el Acné.",
        image: "static/images/15. Cocktail de la Juventud/5.jpg"
    }
];


// =========================
// 2. DESLIZADO AUTOMÁTICO DE SERVICIOS
// =========================

function displayService(service) {
    const cardContainer = document.getElementById('service-card-container');
    cardContainer.style.opacity = '0'; // Efecto de desvanecimiento

    setTimeout(() => {
        cardContainer.innerHTML = ''; // Limpiar el contenedor
        const card = document.createElement('div');
        card.className = 'service-card card shadow-lg mb-3';
        card.innerHTML = `
            <img src="${service.image}" class="card-img-top" alt="${service.name}">
            <div class="card-body">
                <h5 class="card-title">${service.name}</h5>
                <p class="card-text">${service.description}</p>
                <button class="btn btn-outline-primary btn-sm" onclick="openCalendarPopup('${service.name}')">
                    Reservar cita
                </button>
            </div>
        `;
        cardContainer.appendChild(card);
        cardContainer.style.opacity = '1'; // Efecto de aparición
    }, 500);
}

let currentServiceIndex = 0;
function showNextService() {
    currentServiceIndex = (currentServiceIndex + 1) % services.length;
    displayService(services[currentServiceIndex]);
}

setInterval(showNextService, 3000);
document.addEventListener("DOMContentLoaded", () => displayService(services[0]));


// =========================
// 3. LÓGICA DEL CHATBOT
// =========================

document.getElementById("send-button").addEventListener("click", sendMessage);
document.getElementById("user-input").addEventListener("keydown", function (event) {
    if (event.key === "Enter") {
        sendMessage();
    }
});

function displayMessage(message, className) {
    const chatBox = document.getElementById("chat-box");
    chatBox.style.display = "block";

    const messageDiv = document.createElement("div");
    messageDiv.className = `message ${className}`;
    messageDiv.textContent = message;

    chatBox.appendChild(messageDiv);
    chatBox.scrollTop = chatBox.scrollHeight;
}


// =========================
// 3A. MEJORA DE COINCIDENCIA FUZZY PARA FRASES
// =========================

function levenshtein(a, b) {
    const tmp = [];
    for (let i = 0; i <= b.length; i++) {
        tmp[i] = [i];
    }
    for (let j = 0; j <= a.length; j++) {
        tmp[0][j] = j;
    }
    for (let i = 1; i <= b.length; i++) {
        for (let j = 1; j <= a.length; j++) {
            if (b.charAt(i - 1) === a.charAt(j - 1)) {
                tmp[i][j] = tmp[i - 1][j - 1];
            } else {
                tmp[i][j] = Math.min(tmp[i - 1][j - 1] + 1, Math.min(tmp[i][j - 1] + 1, tmp[i - 1][j] + 1));
            }
        }
    }
    return tmp[b.length][a.length];
}

function hasBookingIntent(message) {
    const bookingKeywords = ["book", "appointment", "cita", "reservar"];
    return bookingKeywords.some(keyword =>
        message.toLowerCase().includes(keyword)
    );
}

function findClosestService(userMessage) {
    let bestMatch = null;
    let bestScore = Infinity;

    const words = userMessage.toLowerCase().split(/\s+/);

    services.forEach(service => {
        const serviceName = service.name.toLowerCase();
        words.forEach(word => {
            const distance = levenshtein(word, serviceName);
            if (distance < bestScore) {
                bestScore = distance;
                bestMatch = service;
            }
        });
    });

    // If bestScore <= 3, we consider it "close enough"
    // Return both the matched service and the distance for extra logic if needed
    return { 
        service: bestScore <= 3 ? bestMatch : null,
        distance: bestScore
    };
}


function detectServiceInMessage(userMessage) {
    const lowerCaseMessage = userMessage.toLowerCase();
    
    // 1. Exact match check
    const exactMatch = services.find(service =>
        lowerCaseMessage.includes(service.name.toLowerCase())
    );
    if (exactMatch) {
        return { service: exactMatch, distance: 0 };
    }

    // 2. Check if user is just saying "book", "appointment", etc.
    const bookingKeywords = ["book", "appointment", "cita", "reservar"];
    const hasBooking = bookingKeywords.some(keyword =>
        lowerCaseMessage.includes(keyword)
    );
    if (hasBooking) {
        return { service: null, distance: Infinity };
    }

    // 3. Fuzzy match
    return findClosestService(userMessage);
}

function generateServiceResponse(userMessage, service) {
    const lowerCaseMessage = userMessage.toLowerCase();

    if (lowerCaseMessage.includes("benefits") || lowerCaseMessage.includes("beneficios")) {
        return `Los beneficios de ${service.name} son: ${service.benefits}`;
    }
    if (lowerCaseMessage.includes("side effects") || lowerCaseMessage.includes("efectos secundarios") || lowerCaseMessage.includes("efectos-secundarios")) {
        return `Los efectos secundarios de ${service.name} son: ${service.sideEffects}`;
    }
    if (lowerCaseMessage.includes("description") || lowerCaseMessage.includes("qué es") || lowerCaseMessage.includes("descripcion")) {
        return `Aquí tienes una descripción de ${service.name}: ${service.description}`;
    }
    if (lowerCaseMessage.includes("precio") || lowerCaseMessage.includes("price")) {
        return `El precio de ${service.name} es: ${service.precio || 'Por favor contáctanos para más detalles.'}`;
    }
    return `Has preguntado acerca de ${service.name}. Aquí una breve descripción: ${service.description}`;
}


// =========================
// 3B. DICCIONARIO LOCAL
// =========================
const generalResponses = {
    "hola": "👋 ¡Hola! Soy el chatbot LOOKATME 🤖 ¿En qué puedo ayudarte hoy?",
    "saludo": "👋 ¡Hola! Soy el chatbot LOOKATME 🤖 Pregúntame sobre cualquiera de nuestros servicios o tratamientos.",
    "contacto": "📞 Puedes contactarnos al +51 981640627 para más información.",
    "ubicación": "📍 Estamos ubicados en la Calle Principal 123, Lima, Perú. ¡Ven a visitarnos!",
    "ubicacion": "📍 Estamos ubicados en la Calle Principal 123, Lima, Perú. ¡Ven a visitarnos!",
    "si": "😊 Pregunta por cualquier servicio que quieras reservar",
    "servicios": "💆‍♀️ Ofrecemos una variedad de servicios como limpieza facial, Hydrafacial, mesoterapia y más. ¿En qué puedo ayudarte hoy?",
    "precio": "💰 El precio de cada servicio depende del tipo y duración. Contáctanos para obtener más información detallada.",
    "gracias": "😊 ¡De nada! No dudes en preguntar si tienes más preguntas.",
    "email": "😊 Puedes contactarnos en el correo electrónico estetic-lookatme@gmail.com. ✉️",
    "whatsapp": "😊 Puedes contactarnos a través de nuestro número de WhatsApp: +51 981640627.",
    "oferta": "🌟 Ofrecemos tratamientos como Botox, Hydrafacial, PRP y más. ¿En qué puedo ayudarte?",
    "reservar": "🗓️ Puedes reservar una cita contactándonos al +51 981640627 o a través de nuestro sitio web.",
    "horario": "⏰ Estamos abiertos de lunes a sábado, de 9 AM a 6 PM. ¿En qué podemos ayudarte?",
    "estacionamiento": "🚗 Sí, ofrecemos estacionamiento gratuito para todos nuestros clientes.",
    "caminar": "🚶‍♀️ Aceptamos visitas sin cita previa según disponibilidad, pero recomendamos reservar con anticipación.",
    "botox": "💉 El precio del Botox depende de la cantidad de unidades necesarias. Contáctanos para obtener más información.",
    "promociones": "🎉 ¡Sí! A menudo tenemos promociones de temporada. ¡Contáctanos para conocer nuestras ofertas actuales!",
    "duración": "⏳ La duración de los tratamientos varía, pero la mayoría duran entre 30-90 minutos. Haznos saber en qué estás interesado y te guiaremos.",
    "cancelar": "❌ Puedes cancelar tu cita con 24 horas de anticipación. Contáctanos para hacer cambios.",
    "tarjeta de regalo": "🎁 ¡Sí! Ofrecemos tarjetas de regalo para todos nuestros servicios. ¡Son un excelente regalo!",
    "preparar": "✨ Lo mejor es venir con la piel limpia para la mayoría de los tratamientos. Te daremos instrucciones específicas antes de tu cita.",
    "cuerpo": "🧖‍♀️ Sí, ofrecemos tratamientos de contorno corporal, exfoliaciones y otros tratamientos rejuvenecedores.",
    "amigo": "👫 ¡Por supuesto! Puedes traer a un amigo o familiar contigo.",
    "pago": "💳 Aceptamos efectivo, tarjetas de crédito y pagos móviles para tu comodidad.",
    "consulta": "👩‍⚕️ Sí, ofrecemos consultas personalizadas para discutir tus necesidades de cuidado de la piel y recomendarte los mejores tratamientos.",
    "acné": "🔬 Nuestros tratamientos para el acné incluyen peelings químicos, faciales y más para reducir cicatrices. ¿Te gustaría saber más?",
    "piel sensible": "🌸 ¡Sí! Ofrecemos faciales suaves diseñados específicamente para pieles sensibles.",
    "arrugas": "👵 Tratamientos como Botox, rellenos y tratamientos reafirmantes son ideales para reducir las arrugas.",
    "depilación": "🧖‍♀️ Sí, ofrecemos depilación láser y depilación con cera. Avísame si quieres saber más.",
    "hidratación": "💦 Hydrafacial es un tratamiento no invasivo que limpia, exfolia e hidrata tu piel. ¡Es el favorito para una piel radiante!",
    "anti-edad": "🌟 Recomendamos tratamientos como Botox, PRP y radiofrecuencia para resultados anti-edad efectivos.",
    "embarazo": "🤰 Generalmente se recomienda evitar el Botox durante el embarazo. Consulta con un profesional de salud antes de proceder.",
    "microneedling": "🔬 El microneedling utiliza agujas diminutas para estimular la producción de colágeno, mejorando la textura de la piel y reduciendo cicatrices.",
    "peeling químico": "🧴 Un peeling químico utiliza ácidos para exfoliar y rejuvenecer la piel, dejándola más suave y brillante.",
    "cuidado posterior": "🌿 Después de un facial, es mejor evitar el maquillaje durante 24 horas y seguir nuestras instrucciones de cuidado posterior para obtener resultados brillantes.",
    "combinar tratamientos": "🤝 ¡Por supuesto! Muchos de nuestros tratamientos se pueden combinar para un enfoque más integral.",
    "membresía": "👑 Sí, ofrecemos planes de membresía con descuentos exclusivos para nuestros clientes leales.",
    "poros": "🔍 Tratamientos como microdermoabrasión y peelings químicos pueden ayudar a minimizar la apariencia de los poros grandes.",
    "corporativo": "💼 Sí, ofrecemos paquetes de bienestar corporativo. Contáctanos para conocer más sobre nuestras ofertas para equipos.",
    "recuperación láser": "⏳ Algunos tratamientos láser tienen un tiempo de recuperación mínimo, pero proporcionaremos instrucciones detalladas de cuidado posterior.",
    "prp": "💉 PRP utiliza los factores de crecimiento de tu cuerpo para rejuvenecer la piel, reducir arrugas y promover la curación.",
    "manchas oscuras": "🌟 Tratamientos como peelings químicos y terapia láser pueden ayudar a desvanecer las manchas oscuras con el tiempo.",
    "efectos secundarios del botox": "🤔 Los efectos secundarios pueden incluir moretones leves o hinchazón, pero generalmente desaparecen en pocos días.",
    "contorneado corporal": "💪 Sí, ofrecemos tratamientos de contorno corporal para ayudarte a moldear y tonificar tu cuerpo sin cirugía.",
    "pago en línea": "💻 Sí, ofrecemos opciones de pago en línea seguras cuando reservas tu cita.",
    "piel seca": "💧 Los faciales hidratantes y tratamientos hidratantes son ideales para tratar la piel seca.",
    "frecuencia del botox": "📅 El Botox generalmente dura de 3 a 6 meses. Para mejores resultados, recomendamos tratamientos de mantenimiento cada pocos meses.",
    "reafirmación rf": "📡 La reafirmación con radiofrecuencia utiliza energía para tensar y levantar la piel, dándote una apariencia más firme y juvenil.",
    "cuidado de la piel": "🧴 Sí, ofrecemos una gama de productos profesionales para el cuidado de la piel para todo tipo de pieles.",
    "promociones": "🎉 ¡Sí! Ofrecemos ofertas de temporada. Contáctanos o sigue nuestras redes sociales para obtener más información.",
    "depilación láser": "🔦 La depilación láser puede resultar en una reducción permanente del vello después de varias sesiones.",
    "cicatrices de acné": "✨ Tratamientos como el microneedling y los peelings químicos son efectivos para reducir las cicatrices del acné.",
    "maquillaje después del facial": "💄 Recomendamos esperar 24 horas antes de aplicar maquillaje después de un facial para permitir que tu piel respire.",
    "piel radiante": "🌟 Los Hydrafacials, peelings químicos y una buena hidratación pueden ayudarte a lograr una piel radiante.",
    "reprogramar": "🔄 Puedes reprogramar contactándonos. Recomendamos hacerlo con 24 horas de anticipación.",
    "múltiples citas": "🗓️ ¡Sí, puedes reservar varias citas a la vez! Haznos saber cómo podemos ayudarte.",
    "bienvenida": "🎉 ¡Bienvenido! ¿En qué puedo ayudarte hoy?",
    "cita": "📅 ¿Necesitas reservar una cita? ¡Déjame saber el servicio!",
    "consulta": "👩‍⚕️ Ofrecemos consultas gratuitas. ¿Te gustaría reservar una?",
    "disponibilidad": "🕒 Tenemos disponibilidad esta semana. ¿Qué día te conviene?",
    "especial": "🎊 ¡Pregúntanos sobre nuestras promociones especiales para nuevos clientes!",
    "promoción": "💸 ¡Consulta nuestras promociones y descuentos de temporada!",
    "resultados": "📈 Los resultados de los tratamientos pueden variar, pero la mayoría se notan dentro de 2 a 4 semanas.",
    "brillar": "💫 ¡Los Hydrafacials y los peelings químicos son ideales para una piel radiante!",
    "resplandor": "✨ Nuestros faciales dejarán tu piel radiante. ¿Quieres reservar?",
    "rejuvenecimiento": "🌿 Tratamientos rejuvenecedores disponibles. ¿Te gustaría más información?",
    "tratamiento": "💆 Ofrecemos varios tratamientos. ¿Qué tipo te interesa?",
    "láser": "🔦 Nuestros tratamientos láser pueden reducir el vello y rejuvenecer tu piel.",
    "prp": "💉 La terapia PRP es ideal para el rejuvenecimiento de la piel y el crecimiento capilar.",
    "facial": "🧖‍♀️ Los faciales están disponibles para darte una piel fresca e hidratada.",
    "hidratación": "💦 ¡Mantén tu piel hidratada con nuestro Hydrafacial! ¿Lo reservamos?",
    "peeling": "🧴 Los peelings químicos ayudan a refrescar y suavizar tu piel.",
    "spa": "🧖‍♀️ Relájate y disfruta con nuestros tratamientos de spa de lujo.",
    "acné": "🔬 Nuestros tratamientos para el acné pueden reducir las imperfecciones y cicatrices de manera efectiva.",
    "masaje": "💆 ¿Necesitas un masaje? ¡Déjame reservarlo para ti!",
    "colágeno": "💉 Aumenta tu colágeno con nuestros tratamientos reafirmantes para la piel.",
    "sol": "☀️ ¡No olvides tu protector solar! ¿Te gustaría recomendaciones de productos?",
    "arrugas": "👵 Los tratamientos para reducir arrugas como Botox y rellenos están disponibles.",
    "cicatrices": "✨ Reduce cicatrices con microneedling y peelings químicos.",
    "reafirmante": "💪 Los tratamientos reafirmantes de la piel pueden ayudar a levantar y tensar tu piel.",
    "suero": "🧴 ¿Te gustaría saber más sobre nuestros sueros para la piel?",
    "relleno": "💉 Los rellenos pueden restaurar el volumen y reducir las arrugas. ¿Te interesa?",
    "inyectable": "💉 Ofrecemos inyectables tanto para belleza como para tratamientos de salud.",
    "dermapen": "🔬 El Dermapen ayuda con cicatrices, textura y líneas finas.",
    "anti-edad": "🌟 Nuestros tratamientos anti-edad son muy efectivos. ¿Te gustaría más información?",
    "recuperación": "⏳ Los tiempos de recuperación dependen del tratamiento, pero la mayoría son rápidos.",
    "volumen": "💉 Los rellenos ayudan a restaurar el volumen perdido y dan un aspecto juvenil."
};

function detectGeneralResponse(userMessage) {
    const lowerCaseMessage = userMessage.toLowerCase();
    for (let keyword in generalResponses) {
        if (lowerCaseMessage.includes(keyword)) {
            return generalResponses[keyword];
        }
    }
    return null;
}


// =========================
// 4. RESPALDO CON GEMINI
// =========================

function callGeminiAPI(userMessage) {
    return new Promise((resolve, reject) => {
        fetch("/gemini-api", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ message: userMessage })
        })
        .then(response => response.json())
        .then(data => {
            if (data.response) {
                resolve(data.response);
            } else {
                resolve("Lo siento, no pude obtener una respuesta de Gemini.");
            }
        })
        .catch(err => {
            console.error("Error al llamar a /gemini-api:", err);
            reject("Lo siento, hubo un error al obtener la respuesta.");
        });
    });
}


// =========================
// 5. ENVÍO PRINCIPAL DE MENSAJE
// =========================

function sendMessage() {
    const userInput = document.getElementById("user-input").value;
    if (userInput.trim() === "") return;

    displayMessage(userInput, "user-message");
    const typingDiv = showTypingAnimation();

    const detectionResult = detectServiceInMessage(userInput);
    const detectedService = detectionResult.service;
    const bestDistance = detectionResult.distance;
    const generalResponse = detectGeneralResponse(userInput);

    if (detectedService) {
        // The user typed something close to one of your services
        const response = generateServiceResponse(userInput, detectedService);
        finalizeResponse(response, detectedService, typingDiv);
    } 
    else if (generalResponse) {
        // A generic response was detected
        finalizeResponse(generalResponse, null, typingDiv);
    } 
    else if (hasBookingIntent(userInput)) {
        // The user is asking to book an appointment but didn't mention a specific service
        const response = "🗓️ ¡Entiendo que deseas agendar una cita! ¿Podrías indicarme el tratamiento que te interesa?";
        finalizeResponse(response, null, typingDiv);
    }
    else {
        // Fallback to Gemini or your default reply
        callGeminiAPI(userInput)
            .then(geminiResponse => {
                finalizeResponse(geminiResponse, null, typingDiv);
            })
            .catch(() => {
                finalizeResponse("Lo siento, hubo un error al obtener la respuesta.", null, typingDiv);
            });
    }

    document.getElementById("user-input").value = "";
}
if (detectedService) {
    // If distance is > 0, user spelled it incorrectly
    if (bestDistance > 0) {
        displayMessage(`¿Quizás quisiste decir "${detectedService.name}"?`, "bot-response");
    }
    const response = generateServiceResponse(userInput, detectedService);
    finalizeResponse(response, detectedService, typingDiv);
}


function finalizeResponse(botResponse, detectedService, typingDiv) {
    setTimeout(() => {
        hideTypingAnimation(typingDiv);
        displayMessage(botResponse, "bot-response");

        if (detectedService) {
            displayBookAppointmentButtonInChat(detectedService);
        }

        const options = [
            { label: "Asistente virtual LOOKATME", value: "virtual-assistant" },
            { label: "Personal (WhatsApp)", value: "personal-whatsapp" },
            { label: "Email (estetic-lookatme@gmail.com)", value: "email-lookatme" }
        ];
        displayOptions(options);

    }, 3000);
}


// =========================
// 6. INDICADOR DE ESCRITURA
// =========================

function showTypingAnimation() {
    const chatBox = document.getElementById("chat-box");
    const typingDiv = document.createElement("div");
    typingDiv.className = "message bot-response";
    typingDiv.innerHTML = `
        <div class="typing-indicator">
            <span></span>
            <span></span>
            <span></span>
        </div>
    `;
    chatBox.appendChild(typingDiv);
    chatBox.scrollTop = chatBox.scrollHeight;
    return typingDiv;
}

function hideTypingAnimation(typingDiv) {
    if (typingDiv && typingDiv.parentNode) {
        typingDiv.parentNode.removeChild(typingDiv);
    }
}


// =========================
// 7. BOTÓN PARA RESERVAR CITA
// =========================

function displayBookAppointmentButtonInChat(service) {
    const chatBox = document.getElementById("chat-box");
    const bookButton = document.createElement("button");
    bookButton.textContent = `Reservar cita para ${service.name}`;
    bookButton.className = "btn btn-outline-primary btn-sm mt-3";

    bookButton.addEventListener("click", function () {
        openCalendarPopup(service.name);
    });
    chatBox.appendChild(bookButton);
}


// =========================
// 8. OPCIONES DE CONTACTO
// =========================

function displayOptions(options) {
    const chatBox = document.getElementById("chat-box");
    if (document.querySelector('.options-container')) return;

    const optionsContainer = document.createElement("div");
    optionsContainer.className = "options-container mt-3";

    options.forEach(option => {
        const optionButton = document.createElement("button");
        optionButton.className = "btn btn-outline-primary option-btn btn-sm";
        optionButton.textContent = option.label;
        optionButton.onclick = function () {
            handleOptionSelection(option.value);
        };
        optionsContainer.appendChild(optionButton);
    });

    chatBox.appendChild(optionsContainer);
    chatBox.scrollTop = chatBox.scrollHeight;
}

function handleOptionSelection(optionValue) {
    const optionsContainer = document.querySelector('.options-container');
    if (optionsContainer) {
        optionsContainer.remove();
    }

    if (optionValue === 'virtual-assistant') {
        displayMessage("¿Qué servicio le gustaría seleccionar?", "bot-response");
        displayImage('static/images/fotor-ai-2024100710376.jpg');
    } else if (optionValue === 'personal-whatsapp') {
        const whatsappURL = "https://wa.me/51981640627?text=Hola%2C%20me%20gustaría%20consultar%20sobre%20sus%20servicios.";
        window.open(whatsappURL, '_blank');
    } else if (optionValue === 'email-lookatme') {
        window.location.href = "mailto:estetic-lookatme@gmail.com?subject=Consulta%20de%20Servicios&body=Hola,%20me%20gustaría%20preguntar%20sobre%20sus%20servicios.";
    }
}


// =========================
// 9. POPUP DE CALENDARIO
// =========================

function openCalendarPopup(serviceName) {
    window.open('https://calendar.app.google/DiFczsWq41uW7TnG6', '_blank');
}

function displayImage(imageSrc) {
    const chatBox = document.getElementById("chat-box");
    const imageElement = document.createElement("img");
    imageElement.src = imageSrc;
    imageElement.className = "assistant-image";
    chatBox.appendChild(imageElement);
    chatBox.scrollTop = chatBox.scrollHeight;
}
