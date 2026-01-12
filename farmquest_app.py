import streamlit as st


# ---------- Page Setup ----------
st.set_page_config(
    page_title="FarmQuest 🌾",
    page_icon="🌱",
    layout="centered"
)

# ---------- Session State ----------
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False
if "username" not in st.session_state:
    st.session_state.username = ""
if "xp" not in st.session_state:
    st.session_state.xp = 0
if "level" not in st.session_state:
    st.session_state.level = 1

# ---------- Login ----------
if not st.session_state.logged_in:
    st.markdown("## 🌾 FarmQuest")
    st.markdown("### Learn Farming Like a Game 🎮")

    name = st.text_input("👤 Enter your name")

    if st.button("🚀 Start"):
        if name:
            st.session_state.logged_in = True
            st.session_state.username = name
            st.balloons()
        else:
            st.warning("Please enter your name")
    st.stop()

# ---------- Sidebar ----------
st.sidebar.title("🎯 Dashboard")
st.sidebar.write("👤", st.session_state.username)
st.sidebar.write("🌟 XP:", st.session_state.xp)
st.sidebar.write("🏆 Level:", st.session_state.level)
st.sidebar.progress((st.session_state.xp % 100) / 100)

# ---------- Logout ----------
st.sidebar.markdown("---")
if st.sidebar.button("🚪 Logout"):
    st.session_state.logged_in = False
    st.session_state.username = ""
    st.session_state.level = 1
    st.session_state.xp = 0
    st.rerun()


# ---------- Tabs ----------
tab1, tab2, tab3 = st.tabs(["🎮 Learn & Play", "🧾 Crop Survey", "🤖 AI Chatbot"])

# ---------- TAB 1: Game Levels ----------
levels = {
    1: {
        "lesson": "Farming is the practice of growing crops.",
        "question": "What is farming?",
        "options": ["Cooking", "Growing crops", "Mining"],
        "answer": "Growing crops"
    },
    2: {
        "lesson": "Different crops need different soil and water.",
        "question": "What do crops need?",
        "options": ["Water & Soil", "Plastic", "Stone"],
        "answer": "Water & Soil"
    }
}

with tab1:
    st.markdown(f"## 🌱 Level {st.session_state.level}")
    current = levels.get(st.session_state.level)

    if current:
        st.info(current["lesson"])
        ans = st.radio(current["question"], current["options"])

        if st.button("✅ Submit Answer"):
            if ans == current["answer"]:
                st.success("Correct! +20 XP 🎉")
                st.session_state.xp += 20
                st.session_state.level += 1
                st.balloons()
            else:
                st.error("Try again 😄")
    else:
        st.success("🎉 All levels completed!")

# ---------- TAB 2: Crop Survey ----------
with tab2:
    st.markdown("## 🧾 Farming Survey")
    st.markdown("Answer these to get crop suggestion 🌾")

    water = st.selectbox(
        "💧 Water Availability",
        ["High", "Medium", "Low"]
    )

    soil = st.selectbox(
        "🌍 Soil Type",
        ["Clay", "Loamy", "Sandy"]
    )

    crop_type = st.selectbox(
        "🌱 Crop Preference",
        ["Food Crop", "Cash Crop", "Vegetable"]
    )

    if st.button("🌾 Get Crop Recommendation"):
        if water == "High" and soil == "Clay":
            crop = "Rice 🌾"
        elif water == "Medium" and soil == "Loamy":
            crop = "Wheat 🌾"
        elif water == "Low" and soil == "Sandy":
            crop = "Millets 🌾"
        elif crop_type == "Vegetable":
            crop = "Tomato 🍅"
        else:
            crop = "Groundnut 🥜"

        st.success(f"✅ Recommended Crop: **{crop}**")
        st.info("This crop matches your water & soil conditions")
        st.session_state.xp += 30
        st.balloons()

# ---------- TAB 3: AI Chatbot ----------
with tab3:
    st.markdown("## 🤖 Farming AI Chatbot")

    q = st.text_input("Ask your farming doubt")

    def bot(q):
        q = q.lower()
        if "rice" in q:
            return "Rice needs high water and clay soil 🌾"
        if "millet" in q:
            return "Millets need less water and grow in dry areas 🌾"
        if "fertilizer" in q:
            return "Organic fertilizers improve soil health 🌱"
        if "irrigation" in q:
            return "Drip irrigation saves water 💧"
        return "I'm still learning 🌱 Ask basic farming questions."

    if st.button("💬 Ask"):
        if q:
            st.write("🤖:", bot(q))
        else:
            st.warning("Please type a question")
            
            # ---------- Restart Game ----------
st.markdown("### 🔄 Restart Game")

if st.button("Restart from Beginning"):
    st.session_state.level = 1
    st.session_state.xp = 0
    st.success("Game restarted! 🌱")
    st.rerun()

# ---------- Footer ----------
st.markdown("---")
st.markdown("💚 Encouraging youngsters to love farming 🌾")
