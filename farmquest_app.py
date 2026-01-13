import streamlit as st
from reportlab.lib.pagesizes import A4
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_CENTER
from datetime import date

# -------------------------------------------------
# PAGE CONFIG (ONLY ONCE)
# -------------------------------------------------
st.set_page_config(
    page_title="FarmQuest 🌾",
    page_icon="🌱",
    layout="centered"
)

# -------------------------------------------------
# SESSION STATE INIT
# -------------------------------------------------
def reset_app():
    st.session_state.logged_in = False
    st.session_state.username = ""
    st.session_state.xp = 0
    st.session_state.level = 1

if "logged_in" not in st.session_state:
    reset_app()

# -------------------------------------------------
# CERTIFICATE FUNCTION
# -------------------------------------------------
def generate_certificate(username):
    file_path = f"/mnt/data/{username}_FarmQuest_Certificate.pdf"

    doc = SimpleDocTemplate(file_path, pagesize=A4)
    styles = getSampleStyleSheet()

    title = ParagraphStyle("title", fontSize=24, alignment=TA_CENTER)
    body = ParagraphStyle("body", fontSize=14, alignment=TA_CENTER)

    content = [
        Spacer(1, 40),
        Paragraph("🌾 FarmQuest Certificate of Completion 🌾", title),
        Spacer(1, 30),
        Paragraph(
            f"This certifies that <b>{username}</b><br/>"
            "has successfully completed all 10 levels of<br/>"
            "<b>FarmQuest – Learn Farming Like a Game</b>",
            body
        ),
        Spacer(1, 20),
        Paragraph(f"Date: {date.today().strftime('%d %B %Y')}", body),
        Spacer(1, 30),
        Paragraph("🏆 Title Awarded: <b>Smart Farmer</b>", body)
    ]

    doc.build(content)
    return file_path

# -------------------------------------------------
# LOGIN PAGE
# -------------------------------------------------
if not st.session_state.logged_in:
    st.title("🌾 FarmQuest")
    name = st.text_input("👤 Enter your name")

    if st.button("🚀 Start Game"):
        if name.strip():
            st.session_state.logged_in = True
            st.session_state.username = name
            st.balloons()
            st.rerun()
        else:
            st.warning("Please enter your name")
    st.stop()

# -------------------------------------------------
# SIDEBAR
# -------------------------------------------------
st.sidebar.title("🎯 Dashboard")
st.sidebar.write("👤", st.session_state.username)
st.sidebar.write("🌟 XP:", st.session_state.xp)
st.sidebar.write("🏆 Level:", st.session_state.level)

if st.sidebar.button("🔁 Logout"):
    reset_app()
    st.rerun()

# -------------------------------------------------
# TABS
# -------------------------------------------------
tab1, tab2, tab3, tab4 = st.tabs(
    ["🎮 Learn & Play", "🌾 Agri Guide", "🤖 AI Chatbot", "📜 Certificate"]
)

# -------------------------------------------------
# TAB 1: GAME LEVELS (1–10)
# -------------------------------------------------
levels = {
    1: ("What is farming?", ["Cooking", "Growing crops", "Mining"], "Growing crops"),
    2: ("What do crops need?", ["Plastic", "Water & Soil", "Stone"], "Water & Soil"),
    3: ("Which saves water?", ["Flood irrigation", "Drip irrigation", "Over watering"], "Drip irrigation"),
    4: ("Best soil for crops?", ["Sandy", "Clay", "Loamy"], "Loamy"),
    5: ("Which is organic fertilizer?", ["Urea", "DAP", "Compost"], "Compost"),
    6: ("Kharif crop?", ["Wheat", "Rice", "Mustard"], "Rice"),
    7: ("Natural pesticide?", ["Neem oil", "Chemical spray", "Plastic"], "Neem oil"),
    8: ("Why rotate crops?", ["Increase pests", "Improve soil", "Waste land"], "Improve soil"),
    9: ("Modern irrigation?", ["Bucket", "Canal", "Drip"], "Drip"),
    10: ("Eco-friendly farming?", ["Organic farming", "Burning crops", "Chemicals"], "Organic farming"),
}

with tab1:
    st.header(f"🌱 Level {st.session_state.level}")

    if st.session_state.level <= 10:
        q, options, correct = levels[st.session_state.level]
        ans = st.radio(q, options, key=f"lvl{st.session_state.level}")

        if st.button("✅ Submit"):
            if ans == correct:
                st.success("Correct! +20 XP 🎉")
                st.session_state.xp += 20
                st.session_state.level += 1
                st.rerun()
            else:
                st.error("❌ Wrong answer. Try again!")
    else:
        st.success("🎉 All levels completed!")

# -------------------------------------------------
# TAB 2: SMART AGRI GUIDE WITH PLANT CARE TIPS
# -------------------------------------------------
with tab2:
    st.title("🌱 Agriculture & Gardening Guide")

    # -------------------------------
    # USER INPUTS
    # -------------------------------
    soil = st.selectbox("🪨 Soil Type", [
        "Clay","Sandy","Loamy","Red Soil","Black Soil",
        "Alluvial","Silt","Peaty","Chalky","Laterite"
    ])

    water = st.selectbox("💧 Water Facility", [
        "Low","Medium","High",
        "Salty Water","Survey Water","Rainfed Land"
    ])

    sun = st.selectbox("☀️ Sunlight", ["Low","Medium","High"])

    climate = st.selectbox("🌍 Climate", [
        "Plains","Hills","Desert","Coastal",
        "Tropical","Temperate","Cold","Rainforest","Polar"
    ])

    purpose = st.selectbox("🎯 Purpose", [
        "Vegetables","Fruits","Flowers","Medicinal",
        "Holy Plants","Money Plants","Decorative Plants",
        "Succulents","Water Plants","Dry Plants"
    ])

    # -------------------------------
    # COMBINED PLANT DATABASE
    # -------------------------------
    plant_db = {
        "Rice": {
            "soil": ["Clay"],
            "water": ["High", "Survey Water"],
            "sun": ["High"],
            "climate": ["Plains", "Tropical"],
            "purpose": ["Vegetables"],
            "care": "💧 Standing water | 🌱 Clay soil | ☀️ Full sun | 🌿 High nitrogen fertilizer | 📏 Close spacing"
        },
        "Wheat": {
            "soil": ["Loamy"],
            "water": ["Medium"],
            "sun": ["High"],
            "climate": ["Plains", "Temperate"],
            "purpose": ["Vegetables"],
            "care": "💧 Moderate water | 🌱 Loamy soil | ☀️ Full sun | 🌿 Balanced fertilizer | ✂️ No pruning"
        },
        "Millets": {
            "soil": ["Sandy", "Red Soil"],
            "water": ["Low", "Rainfed Land"],
            "sun": ["High"],
            "climate": ["Plains"],
            "purpose": ["Vegetables", "Dry Plants"],
            "care": "💧 Low water | 🌱 Dry soil | ☀️ Full sun | 🌿 Organic compost | 📏 Wide spacing"
        },
        "Pulses": {
            "soil": ["Loamy"],
            "water": ["Low", "Rainfed Land"],
            "sun": ["High"],
            "climate": ["Plains"],
            "purpose": ["Vegetables"],
            "care": "💧 Low water | 🌱 Well-drained soil | ☀️ Full sun | 🌿 Phosphorus-rich fertilizer | ✂️ Light pruning"
        },
        "Cotton": {
            "soil": ["Black Soil"],
            "water": ["Medium", "Rainfed Land"],
            "sun": ["High"],
            "climate": ["Plains"],
            "purpose": ["Dry Plants"],
            "care": "💧 Medium water | 🌱 Black soil | ☀️ Full sun | 🌿 Potassium fertilizer | ✂️ Regular pruning"
        },
        "Coconut": {
            "soil": ["Sandy", "Laterite"],
            "water": ["High", "Salty Water"],
            "sun": ["High"],
            "climate": ["Coastal", "Tropical"],
            "purpose": ["Fruits"],
            "care": "💧 High water | 🌱 Sandy soil | ☀️ Full sun | 🌿 Organic manure | 📏 Wide spacing"
        },
        "Date Palm": {
            "soil": ["Sandy"],
            "water": ["Low", "Salty Water"],
            "sun": ["High"],
            "climate": ["Desert"],
            "purpose": ["Fruits"],
            "care": "💧 Low water | 🌱 Sandy soil | ☀️ Hot sun | 🌿 Compost | ✂️ Old leaf removal"
        },
        "Banana": {
            "soil": ["Alluvial", "Loamy"],
            "water": ["High"],
            "sun": ["High"],
            "climate": ["Tropical"],
            "purpose": ["Fruits"],
            "care": "💧 High water | 🌱 Rich soil | ☀️ Full sun | 🌿 Nitrogen-rich fertilizer | 📏 Wide spacing"
        },
        "Papaya": {
            "soil": ["Loamy"],
            "water": ["Medium"],
            "sun": ["High"],
            "climate": ["Tropical"],
            "purpose": ["Fruits"],
            "care": "💧 Medium water | 🌱 Loamy soil | ☀️ Full sun | 🌿 Compost | ✂️ Remove weak shoots"
        },
        "Mango": {
            "soil": ["Red Soil", "Loamy"],
            "water": ["Medium"],
            "sun": ["High"],
            "climate": ["Tropical"],
            "purpose": ["Fruits"],
            "care": "💧 Medium water | 🌱 Red soil | ☀️ Full sun | 🌿 Potassium fertilizer | ✂️ Annual pruning"
        },
        "Cashew": {
            "soil": ["Laterite"],
            "water": ["Medium"],
            "sun": ["High"],
            "climate": ["Hills", "Tropical"],
            "purpose": ["Fruits"],
            "care": "💧 Medium water | 🌱 Laterite soil | ☀️ Full sun | 🌿 Organic manure | 📏 Wide spacing"
        },
        "Tea": {
            "soil": ["Laterite"],
            "water": ["High"],
            "sun": ["Medium"],
            "climate": ["Hills"],
            "purpose": ["Medicinal"],
            "care": "💧 High water | 🌱 Acidic soil | ☀️ Partial sun | 🌿 Nitrogen fertilizer | ✂️ Regular pruning"
        },
        "Coffee": {
            "soil": ["Laterite"],
            "water": ["Medium"],
            "sun": ["Low"],
            "climate": ["Hills"],
            "purpose": ["Medicinal"],
            "care": "💧 Medium water | 🌱 Well-drained soil | ☀️ Shade | 🌿 Organic compost | ✂️ Shape pruning"
        },
        "Rubber": {
            "soil": ["Laterite"],
            "water": ["High"],
            "sun": ["Medium"],
            "climate": ["Tropical"],
            "purpose": ["Decorative Plants"],
            "care": "💧 High water | 🌱 Laterite soil | ☀️ Partial sun | 🌿 Organic manure | ✂️ Minimal pruning"
        },
        "Cactus": {
            "soil": ["Sandy"],
            "water": ["Low"],
            "sun": ["High"],
            "climate": ["Desert"],
            "purpose": ["Dry Plants"],
            "care": "💧 Very low water | 🌱 Sandy soil | ☀️ Bright sunlight | 🌿 No fertilizer | ✂️ No pruning"
        },
        "Aloe Vera": {
            "soil": ["Sandy", "Loamy"],
            "water": ["Low"],
            "sun": ["Medium"],
            "climate": ["Desert", "Plains"],
            "purpose": ["Medicinal", "Dry Plants"],
            "care": "💧 Low water | 🌱 Well-drained soil | ☀️ Medium sunlight | 🌿 Organic compost | ✂️ Remove old leaves"
        },
        "Moss": {
            "soil": ["Peaty"],
            "water": ["High"],
            "sun": ["Low"],
            "climate": ["Polar", "Cold"],
            "purpose": ["Decorative Plants"],
            "care": "💧 Moist | 🌱 Rocks/soil | ☀️ Low light | 🌿 No fertilizer | ✂️ No pruning"
        },
        "Lichen": {
            "soil": ["Chalky"],
            "water": ["Low"],
            "sun": ["Low"],
            "climate": ["Polar"],
            "purpose": ["Decorative Plants"],
            "care": "💧 Minimal | 🌱 Rocks | ☀️ Low sun | 🌿 No fertilizer | ✂️ No pruning"
        }
    }

    # -------------------------------
    # SMART SUGGESTION LOGIC
    # -------------------------------
    if st.button("🌿 Get Suggestions"):
        results = []

        for plant, data in plant_db.items():
            if (
                soil in data["soil"] and
                water in data["water"] and
                sun in data["sun"] and
                climate in data["climate"] and
                purpose in data["purpose"]
            ):
                results.append(plant)

        if results:
            st.success("🌾 Recommended Plants & Care Tips")
            for plant in results:
                st.markdown(f"### 🌱 {plant}")
                st.info(plant_db[plant]["care"])
        else:
            st.warning("⚠️ No plants match ALL selected conditions.")
       

# -------------------------------------------------
# TAB 3: SMART AI FARMING CHATBOT
# -------------------------------------------------
with tab3:
    st.title("🤖 Smart Farming AI Assistant")
    st.write("Ask me anything about crops, soil, water, fertilizer, pests 🌱")

    question = st.text_input("💬 Ask your farming question")

    def farming_ai(q):
        q = q.lower()

        # CROPS
        if "rice" in q:
            return "🌾 Rice needs clay soil, high water availability, and warm climate."
        if "wheat" in q:
            return "🌾 Wheat grows well in loamy soil with moderate water and cool climate."
        if "millet" in q:
            return "🌾 Millets require low water and grow well in dry regions."
        # SOIL
        if "soil" in q:
            return "🌍 Healthy soil contains nutrients, organic matter, and good drainage."

        # WATER
        if "irrigation" in q or "water" in q:
            return "💧 Drip irrigation saves water and improves crop yield."

        # FERTILIZER
        if "fertilizer" in q:
            return "🌱 Organic fertilizers like compost and vermicompost improve soil health."

        # PESTS
        if "pest" in q or "insect" in q:
            return "🐛 Neem oil is a natural pesticide and safe for crops."

        # DISEASE
        if "disease" in q:
            return "🦠 Crop diseases can be reduced by crop rotation and healthy soil."
        
        # SEASONS
        if "kharif" in q:
            return "🌦️ Kharif crops are grown in rainy season like rice and maize."
        if "rabi" in q:
            return "❄️ Rabi crops grow in winter like wheat and mustard."

        # DEFAULT AI RESPONSE
        return (
            "🌱 Farming AI Tip:\n"
            "- Choose crop based on soil & climate\n"
            "- Use organic fertilizer\n"
            "- Save water using drip irrigation\n"
            "- Rotate crops to maintain soil fertility"
        )

    if st.button("💬 Ask AI"):
        if question.strip():
            st.success(farming_ai(question))
        else:
            st.warning("Please type a question")

# -------------------------------------------------
# TAB 4: CERTIFICATE
# -------------------------------------------------
with tab4:
    if st.session_state.level > 10:
        if st.button("📄 Download Certificate"):
            path = generate_certificate(st.session_state.username)
            with open(path, "rb") as f:
                st.download_button(
                    "⬇️ Download PDF",
                    f,
                    file_name="FarmQuest_Certificate.pdf"
                )
    else:
        st.warning("❌ Complete all 10 levels to unlock certificate")
