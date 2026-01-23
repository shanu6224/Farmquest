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
        "PM-KISAN": [
            "Direct Income Support: Provides financial assistance to small and marginal farmers, improving their purchasing power for essential agricultural inputs.",
            "Direct Benefit Transfer (DBT): Funds are transferred directly to the bank accounts of beneficiaries, ensuring transparency and reducing corruption or leakage.",
            "Assistance for Inputs: Helps farmers purchase seeds, fertilizers, and pesticides, especially during rising costs.",
            "Reduced Debt Reliance: Decreases dependency on high-interest loans from informal money lenders.",
            "Improved Cash Flow: The three-installment structure provides liquidity to farmers exactly when needed for cultivation cycles.",
            "Comprehensive Coverage: Designed to cover all landholding farmers' families, supporting both agricultural needs and domestic expenses.",
            "Source / Link: [PM-KISAN Official](https://share.google/jnXxl3n8oVdnkJe8I)"
        ],
        "PMFBY – Crop Insurance": [
            "Comprehensive Coverage: Protects against pre-sowing to post-harvest losses, including localized risks and post-harvest damages from cyclones, floods, etc.",
            "Low Premiums: Aims to increase penetration by keeping farmer premium shares low, subsidized by central and state governments.",
            "Voluntary for Non-Loanee Farmers: Compulsory for farmers with crop loans but optional for others.",
            "Technology Integration: Promotes using technology for yield estimation and efficient claim processing.",
            "Income Stabilization: Supports farmers' income to keep them in farming, promotes credit flow, and ensures food security.",
            "Source / Link: [PMFBY Official](https://share.google/jnXxl3n8oVdnkJe8I)"
        ],
        "PMKSY – Micro Irrigation": [
            "High Financial Assistance: Small and marginal farmers can receive up to 100% subsidy (often capped per hectare), while large farmers receive up to 75% for micro-irrigation systems.",
            "Water Conservation: Saves 30% to 50% more water compared to traditional flood irrigation methods.",
            "Increased Productivity: Boosts crop yields by 20% to 50% through precise, direct-to-root water and nutrient delivery (fertigation).",
            "Reduced Input Costs: Lowers expenditure on labor, fertilizers, and electricity for pumping.",
            "Improved Crop Quality: Ensures consistent moisture levels, leading to higher quality produce and better pest/disease control.",
            "Optimal Land Use: Highly suitable for diverse terrains and marginal lands.",
            "Source / Link: [PMKSY Official](https://share.google/MRCbNEjHRKQJaugRJ)"
        ],
        "Organic Farming Support": [
            "Environmental Sustainability: Reduces soil erosion, prevents groundwater pollution from chemical runoff, and promotes biodiversity by creating habitats for beneficial organisms.",
            "Soil Health Enhancement: Continuous use of organic manure and compost increases soil fertility and long-term productivity.",
            "Economic Benefits for Farmers: Organic farming reduces dependence on expensive synthetic inputs, leading to lower cultivation costs and higher income due to premium market prices.",
            "Healthier Food Production: Produces food free from harmful synthetic pesticide residues, often with higher nutritional value.",
            "Climate Change Mitigation: Organic methods typically require less energy and contribute to higher carbon sequestration in the soil.",
            "Source / Link: [TNAU Organic Farming](https://share.google/LcCgauk8WZlMffh6V)"
        ],
        "Farmer Training (TNAU)": [
            "Financial & Resource Accessibility: Eliminates cost barriers, making expert knowledge available to small and marginal farmers. Includes training on accessing government subsidies for machinery.",
            "Increased Yields and Quality: Covers high-yield techniques, integrated pest management (IPM), and improved irrigation, leading to higher productivity and better produce quality.",
            "Adoption of Sustainable Practices: Teaches efficient resource use, reduces reliance on chemical pesticides and fertilizers, improves soil health, and protects the ecosystem.",
            "Source / Link: [TNAU Agritech Portal](https://share.google/sek8t8VcUSNS31fRE)"
        ]
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
    "PM-KISAN": [
        "நேரடி வருமான உதவி: சிறிய மற்றும் புறநகர் விவசாயிகளுக்கு நிதி ஆதரவு, விதைகள், உரம், பூச்சிக் கொல்லிகள் வாங்க உதவுகிறது.",
        "நேரடி நன்மை பரிமாற்றம் (DBT): நிதி நேரடியாக வங்கி கணக்குகளில் செலுத்தப்படுகிறது, வெளிப்படைத்தன்மை மற்றும் ஊழலை குறைக்கிறது.",
        "வளங்களுக்கான உதவி: விதை, உரம், பூச்சிக் கொல்லிகள் வாங்க உதவி.",
        "கடன் சார்பு குறைவு: உயர்வான வட்டி கடன் தேவையில்லை.",
        "பணம் திரும்ப பெறுதல்: மூன்று நிலை தொகை விவசாயிகளுக்கு செறிவான நேரத்தில் கிடைக்கும்.",
        "முழுமையான வரம்பு: எல்லா விவசாயி குடும்பங்களையும் காப்பு செய்யும்.",
        "மூல / இணைப்பு: [PM-KISAN அதிகாரப்பூர்வம்](https://share.google/jnXxl3n8oVdnkJe8I)"
    ],
    "PMFBY – பயிர் காப்பீடு": [
        "முழுமையான காப்பீடு: விதைப்பு முதல் அறுவடை வரை, புயல், வெள்ளம் போன்ற இயற்கை நிபந்தனைகளில் ஏற்படும் இழப்புகளையும் பாதுகாக்கிறது.",
        "குறைந்த காப்பீட்டு தொகை: விவசாயி பங்கு குறைவு, மைய அரசு மற்றும் மாநில அரசு மானியம்.",
        "தன்னிச்சையான விவசாயிகளுக்கு விருப்ப: கடன் பெற்ற விவசாயிகளுக்கு கட்டாயம், மற்றவர்கள் விருப்பம்.",
        "தொழில்நுட்ப ஒருங்கிணைப்பு: விளைச்சல் மதிப்பீடு மற்றும் விரைவான கோரிக்கை செயலாக்கத்திற்கு தொழில்நுட்பம் பயன்படுத்தப்படுகிறது.",
        "வருமான நிலைத்தன்மை: விவசாயிகளை நிலைத்த வேளாண்மையில் வைக்கும், கடன் செல்லும் வழியை ஊக்குவிக்கும், உணவு பாதுகாப்பை உறுதி செய்கிறது.",
        "மூல / இணைப்பு: [PMFBY அதிகாரப்பூர்வம்](https://share.google/jnXxl3n8oVdnkJe8I)"
    ],
    "PMKSY – துளி நீர் பாசனம்": [
        "உயர் நிதி உதவி: சிறிய மற்றும் புறநகர் விவசாயிகள் 100% மானியம் பெறலாம்; பெரிய விவசாயிகள் 75% வரை பெறுவர்.",
        "நீர் சேமிப்பு: வழக்கமான வெள்ளம் பாசன முறைசெயலுக்கு 30–50% அதிக சேமிப்பு.",
        "உற்பத்தி அதிகரிப்பு: செடி வேரில் நேரடியாக நீர் மற்றும் உரங்களை அளிப்பதால் 20–50% விளைச்சல் அதிகரிப்பு.",
        "செலவுகள் குறைவு: உழவு, உரம் மற்றும் மின்சாரம் செலவைக் குறைக்கும்.",
        "பயிர் தரம் மேம்பாடு: நிலையான ஈரப்பதம், உயர் தரமுள்ள விளைச்சல், பூச்சி/நோய் கட்டுப்பாடு.",
        "சரியான நிலப்பயன்பாடு: பல்வேறு நிலத்துக்கு ஏற்றது, எல்லா நிலங்களுக்கும்.",
        "மூல / இணைப்பு: [PMKSY அதிகாரப்பூர்வம்](https://share.google/MRCbNEjHRKQJaugRJ)"
    ],
    "இயற்கை வேளாண்மை": [
        "சுற்றுச்சூழல் நிலைத்தன்மை: மண் அடர்த்தி குறைவு, இரசாயன நீர் மாசுபாடு குறைவு, பயனுள்ள உயிரினங்களுக்கு வாழிடம்.",
        "மண் வளம் மேம்பாடு: உரம் மற்றும் கம்போஸ்ட் பயன்படுத்தல் மூலம் நீண்டகால விளைச்சல்.",
        "விவசாயிகளுக்கு பொருளாதார நன்மை: குறைந்த செயற்கை செலவு, உயர் விலை சந்தை மூலம் அதிக வருமானம்.",
        "ஆரோக்கியமான உணவு: இரசாயன தடுப்பு இல்லாமல், அதிக ஊட்டச்சத்து கொண்ட உணவு.",
        "காலநிலை மாற்ற தடுப்பு: குறைந்த எரிசக்தி பயன்படுத்தல், நிலத்தில் கார்பன் அதிகம் சேர்க்கும்.",
        "மூல / இணைப்பு: [TNAU Organic Farming](https://share.google/LcCgauk8WZlMffh6V)"
    ],
    "TNAU பயிற்சிகள்": [
        "நிதி & வளங்கள்: சிறிய மற்றும் புறநகர் விவசாயிகளுக்கு விலை தடைகளை நீக்குகிறது, இயந்திர உதவி மற்றும் மானியம் பயன்படுத்த பயிற்சி.",
        "உயர் விளைச்சல் & தரம்: சிறந்த விதை தேர்வு, ஒருங்கிணைந்த பூச்சிக் கட்டுப்பாடு (IPM), மேம்பட்ட பாசனம் மூலம் உயர் விளைச்சல்.",
        "நிலையான நடைமுறை: வளங்களை திறம்பட பயன்படுத்துதல், இரசாயன பூச்சி/உரம் குறைப்பு, மண் நலம் மேம்பாடு, சுற்றுச்சூழல் பாதுகாப்பு.",
        "மூல / இணைப்பு: [TNAU Agritech Portal](https://share.google/sek8t8VcUSNS31fRE)"
    ]
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
# TAB 2: FULL CROP DATA
# -------------------------
crop_data = {
    "Tomato": {"water": "600–800 mm", "soil": "Loamy, well-drained", "climate": "20–30°C", "food": "Seeds, pulp (sauce, ketchup)"},
    "Brinjal": {"water": "500–700 mm", "soil": "Sandy loam", "climate": "22–35°C", "food": "Seeds"},
    "Chilli": {"water": "600–900 mm", "soil": "Well-drained loamy", "climate": "20–30°C", "food": "Dry chilli powder, seeds"},
    "Onion": {"water": "350–550 mm", "soil": "Sandy loam", "climate": "13–25°C", "food": "Onion skins (manure)"},
    "Ladies Finger": {"water": "500–800 mm", "soil": "Loamy", "climate": "22–35°C", "food": "Seeds"},
    "Spinach": {"water": "300–500 mm", "soil": "Fertile loamy", "climate": "15–25°C", "food": "Compost material"},
    "Cucumber": {"water": "700–1200 mm", "soil": "Sandy loam", "climate": "18–30°C", "food": "Seeds"},
    "Carrot": {"water": "350–550 mm", "soil": "Sandy soil", "climate": "15–25°C", "food": "Leaves (compost)"},
    "Coriander": {"water": "400–600 mm", "soil": "Loamy", "climate": "18–28°C", "food": "Seeds (spice)"},
    "Groundnut": {"water": "500–700 mm", "soil": "Sandy loam, well-drained", "climate": "20–30°C", "food": "Groundnut cake (cattle feed), shells"},
    "Mustard": {"water": "350–500 mm", "soil": "Loamy soil", "climate": "10–25°C", "food": "Mustard cake, leaves (vegetable)"},
    "Sunflower": {"water": "500–800 mm", "soil": "Loamy, well-drained", "climate": "20–30°C", "food": "Sunflower cake, husk"},
    "Sesame": {"water": "300–500 mm", "soil": "Sandy loam", "climate": "25–35°C", "food": "Sesame cake, stalks (fuel)"},
    "Soybean": {"water": "500–700 mm", "soil": "Loamy soil", "climate": "20–30°C", "food": "Soy cake, soy meal"},
    "Castor": {"water": "400–600 mm", "soil": "Sandy loam", "climate": "20–35°C", "food": "Castor cake (manure), stems"},
    "Linseed": {"water": "450–650 mm", "soil": "Loamy", "climate": "10–25°C", "food": "Linseed cake, fiber"},
    "Safflower": {"water": "400–600 mm", "soil": "Loamy, well-drained", "climate": "15–30°C", "food": "Safflower cake, petals (dye)"},
    "Niger": {"water": "500–800 mm", "soil": "Loamy", "climate": "20–30°C", "food": "Niger cake, bird feed"},
    "Coconut": {"water": "1300–2300 mm", "soil": "Sandy loam", "climate": "20–35°C", "food": "Copra, coir, shell charcoal"}
}

with tab2:
    crop = st.selectbox("Select Crop", list(crop_data.keys()))
    st.subheader("💧 Water Requirement"); st.write(crop_data[crop]["water"])
    st.subheader("🌱 Soil Requirement"); st.write(crop_data[crop]["soil"])
    st.subheader("☀️ Climate Requirement"); st.write(crop_data[crop]["climate"])
    st.subheader("🏭 By-product / Food Application"); st.write(crop_data[crop]["food"])


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

