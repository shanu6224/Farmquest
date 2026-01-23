import streamlit as st
from datetime import datetime, date
from reportlab.lib.pagesizes import A4
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_CENTER

# -------------------------------------------------
# PAGE CONFIG
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
    file_path = f"{username}_FarmQuest_Certificate.pdf"
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
# SIDEBAR SETTINGS
# -------------------------------------------------
st.sidebar.title("⚙️ Settings")
st.sidebar.write("👤", st.session_state.username)
st.sidebar.write("🌟 XP:", st.session_state.xp)
st.sidebar.write("🏆 Level:", st.session_state.level)

if st.sidebar.button("🔁 Logout"):
    reset_app()
    st.rerun()

language = st.sidebar.selectbox("🌐 Language / மொழி", ["English", "தமிழ்"])
mode = st.sidebar.radio("🌓 Mode", ["Day Mode", "Night Mode"])
hour = datetime.now().hour
time_status = "☀️ Day Mode Active" if mode == "Day Mode" else "🌙 Night Mode Active"
st.sidebar.info(time_status)

# -------------------------------------------------
# LANGUAGE CONTENT
# -------------------------------------------------
if language == "English":
    TITLE = "🌱 FarmQuest – Agriculture & Food Technology Guide"
    SUBTITLE = "Crop • Water • Soil • Climate • Rural Development"
    PROBLEM = [
        "Farmers lack scientific crop information",
        "Wrong crop selection causes loss",
        "Improper irrigation wastes water",
        "Beginners fear farming due to lack of guidance"
    ]
    SOLUTION = [
        "One platform for agriculture & food technology",
        "Crop-wise water, soil & climate info",
        "Beginner-friendly farming guide",
        "Supports rural development"
    ]
    GOV_SCHEMES = {
        "PMFBY – Crop Insurance": ["Covers losses from pre-sowing to post-harvest", "Low premium subsidized by government", "Technology-based yield estimation", "Link: https://pmfby.gov.in"],
        "PM-KISAN": ["Direct income support via DBT", "Helps buy seeds, fertilizers, pesticides", "Reduces debt and improves cash flow", "Link: https://pmkisan.gov.in"],
        "PMKSY – Micro Irrigation": ["Up to 100% subsidy for small farmers", "Saves 30–50% water", "Increases yield by 20–50%", "Link: https://pmksy.gov.in"],
        "Organic Farming Support": ["Improves soil health", "Produces chemical-free food", "Eco-friendly and climate resilient", "Link: https://pgsindia-ncof.gov.in"],
        "Farmer Training (TNAU)": ["Free expert guidance", "High-yield techniques", "Sustainable practices", "Link: https://www.tnau.ac.in/"]
    }
else:
    TITLE = "🌱 FarmQuest – வேளாண்மை மற்றும் உணவு தொழில்நுட்ப வழிகாட்டி"
    SUBTITLE = "பயிர் • நீர் • மண் • காலநிலை • ஊரக வளர்ச்சி"
    PROBLEM = [
        "விவசாயிகளுக்கு அறிவியல் தகவல் குறைவு",
        "தவறான பயிர் தேர்வு காரணமாக இழப்பு",
        "நீர் வீணாகிறது",
        "தொடக்க நிலை விவசாயிகளுக்கு வழிகாட்டல் இல்லை"
    ]
    SOLUTION = [
        "ஒருங்கிணைந்த வேளாண்மை தளம்",
        "பயிர் வாரியான தகவல்கள்",
        "தொடக்க நிலை விவசாயிகளுக்கு வழிகாட்டி",
        "ஊரக வளர்ச்சி ஆதரவு"
    ]
    GOV_SCHEMES = {
        "PMFBY – பயிர் காப்பீடு": ["விதைப்பு முதல் அறுவடை வரை பாதுகாப்பு", "குறைந்த காப்பீட்டு தொகை", "தொழில்நுட்ப அடிப்படையிலான இழப்பீடு", "Link: https://pmfby.gov.in"],
        "PM-KISAN": ["நேரடி வருமான உதவி", "விதை, உரம் வாங்க உதவி", "கடன் சார்பு குறைவு", "Link: https://pmkisan.gov.in"],
        "PMKSY – துளி நீர் பாசனம்": ["100% வரை மானியம்", "30–50% நீர் சேமிப்பு", "உற்பத்தி அதிகரிப்பு", "Link: https://pmksy.gov.in"],
        "இயற்கை வேளாண்மை": ["மண் வளம் மேம்பாடு", "ஆரோக்கியமான உணவு", "சுற்றுச்சூழல் பாதுகாப்பு", "Link: https://pgsindia-ncof.gov.in"],
        "TNAU பயிற்சிகள்": ["இலவச பயிற்சி", "உயர் விளைச்சல் முறைகள்", "நிலையான வேளாண்மை", "Link: https://www.tnau.ac.in/"]
    }

# -------------------------------------------------
# TITLE
# -------------------------------------------------
st.title(TITLE)
st.subheader(SUBTITLE)
st.divider()
st.header("🌾 Welcome")
st.write("Farming is the backbone of our nation 🇮🇳. Even beginners can become successful farmers with the right guidance.")

# -------------------------------------------------
# TABS
# -------------------------------------------------
tab1, tab2, tab3, tab4 = st.tabs(
    ["🎮 Game Levels", "🌾 Crop Info", "📘 Guide + AI Chatbot", "📜 Knowledge & Certificate"]
)

# -------------------------
# TAB 1: GAME LEVELS
# -------------------------
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

# -------------------------
# TAB 2: CROP DATA
# -------------------------
crop_data = {
    "Tomato": {"water": "600–800 mm", "soil": "Loamy", "climate": "20–30°C", "food": "Sauce/Ketchup"},
    "Brinjal": {"water": "500–700 mm", "soil": "Sandy loam", "climate": "22–35°C", "food": "Curry"},
    "Onion": {"water": "350–550 mm", "soil": "Sandy loam", "climate": "13–25°C", "food": "Flakes"},
    "Groundnut": {"water": "500–700 mm", "soil": "Sandy loam", "climate": "20–30°C", "food": "Oil"},
    "Coconut": {"water": "1300–2300 mm", "soil": "Sandy loam", "climate": "20–35°C", "food": "Copra/Coconut oil"},
}
with tab2:
    crop = st.selectbox("Select Crop", list(crop_data.keys()))
    st.subheader("💧 Water Requirement"); st.write(crop_data[crop]["water"])
    st.subheader("🌱 Soil Requirement"); st.write(crop_data[crop]["soil"])
    st.subheader("☀️ Climate Requirement"); st.write(crop_data[crop]["climate"])
    st.subheader("🏭 Food Technology Application"); st.write(crop_data[crop]["food"])

# -------------------------
# TAB 3: GUIDE + AI CHATBOT
# -------------------------
with tab3:
    st.subheader("📘 Beginner Guide")
    st.write("🌱 Step 1: Understand soil & water")
    st.write("🌾 Step 2: Select suitable crops")
    st.write("💧 Step 3: Efficient irrigation")
    st.write("🌿 Step 4: Prefer organic methods")
    st.write("🧺 Step 5: Harvest & store properly")
    st.subheader("✅ Do’s"); st.write("• Soil testing\n• Crop rotation\n• Use organic manure")
    st.subheader("❌ Don’ts"); st.write("• Don't waste water\n• Don't overuse chemicals\n• Don't lose confidence")

    st.subheader("🤖 Smart Farming AI Assistant")
    question = st.text_input("💬 Ask your farming question")

    def farming_ai(q):
        q_lower = q.lower()
        if "rice" in q_lower: return "🌾 Rice needs clay soil, high water, warm climate."
        if "wheat" in q_lower: return "🌾 Wheat grows well in loamy soil, moderate water, cool climate."
        if "millet" in q_lower: return "🌾 Millets require low water, dry regions."
        if "soil" in q_lower: return "🌍 Healthy soil contains nutrients, organic matter, and good drainage."
        if "water" in q_lower or "irrigation" in q_lower: return "💧 Drip irrigation saves water and improves yield."
        if "fertilizer" in q_lower: return "🌱 Organic fertilizers improve soil health."
        if "pest" in q_lower or "insect" in q_lower: return "🐛 Neem oil is natural & safe."
        if "disease" in q_lower: return "🦠 Crop rotation & healthy soil prevent diseases."
        if "scheme" in q_lower or "government" in q_lower:
            text = "🌾 **Government Schemes:**\n"
            for scheme, points in GOV_SCHEMES.items():
                text += f"• **{scheme}**\n"
                for p in points:
                    text += f"  - {p}\n"
            return text
        return "🌱 Tip: Choose crops by soil/climate, use organic fertilizer, save water, rotate crops, check gov schemes."

    if st.button("💬 Ask AI"):
        if question.strip(): st.markdown(farming_ai(question))
        else: st.warning("Type a question")

# -------------------------
# TAB 4: KNOWLEDGE & CERTIFICATE
# -------------------------
with tab4:
    st.header("❗ Problems")
    for p in PROBLEM: st.write("•", p)
    st.header("🤝 Government Schemes")
    for scheme, points in GOV_SCHEMES.items():
        st.write(f"• {scheme} — {points[-1]}")  # show link

    st.divider()
    if st.session_state.level > 10:
        if st.button("📄 Download Certificate"):
            path = generate_certificate(st.session_state.username)
            with open(path, "rb") as f:
                st.download_button("⬇️ Download PDF", f, file_name="FarmQuest_Certificate.pdf")
    else:
        st.warning("❌ Complete all 10 levels to unlock certificate")
