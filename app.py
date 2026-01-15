import streamlit as st

# ------------------ PAGE CONFIG ------------------
st.set_page_config(
    page_title="PRAGYAN AI • School Assistant",
    page_icon="🤖",
    layout="wide"
)

# ------------------ CUSTOM CSS ------------------
st.markdown("""
<style>
body {
    background: radial-gradient(circle at top, #050b18, #000000);
    color: #e6f1ff;
}
.chat-box {
    background: linear-gradient(145deg, #050b18, #020617);
    border: 1px solid #00eaff;
    border-radius: 14px;
    padding: 14px;
    margin-bottom: 10px;
    box-shadow: 0 0 12px rgba(0,234,255,0.15);
}
.user {
    border-left: 5px solid #ff4b4b;
}
.bot {
    border-left: 5px solid #00eaff;
}
.sidebar-box {
    background: #020617;
    border: 1px solid #00eaff;
    padding: 15px;
    border-radius: 12px;
}
</style>
""", unsafe_allow_html=True)

# ------------------ SIDEBAR (SCI-FI POPUP) ------------------
with st.sidebar:
    st.markdown("<div class='sidebar-box'>", unsafe_allow_html=True)
    st.markdown("### 🛰 PRAGYAN AI CORE")
    st.markdown("""
    - 🔐 End-to-End Encrypted  
    - 🧠 Domain-Locked Intelligence  
    - ⚡ Real-Time Responses  
    - ☎ Human Escalation Ready  
    """)
    st.markdown("📞 **School Office:** +91-XXXXXXXXXX")
    st.markdown("</div>", unsafe_allow_html=True)

# ------------------ DATA ------------------
FAQ_DATA = {
    "school timing": "School usually starts at **8:00 AM** and ends at **2:00 PM**. Timings may vary on special days.",
    "bell schedule": "The bell schedule includes period-wise classes, short breaks, and a lunch break. Please confirm from the notice board for today.",
    "lunch menu": "The weekly lunch menu is shared by the school office or displayed on the notice board.",
    "holiday": "School holidays follow the official academic calendar issued by the school.",
    "absence": "Parents should inform the school office through a written note or phone call for any absence or late arrival.",
    "early pickup": "For early pickup, parents must submit a request at the school office with valid identification.",
    "lost and found": "The Lost & Found section is located near the school office.",
    "dress code": "The school follows a prescribed uniform and dress code as per school guidelines.",
    "summer": "The school remains closed during summer vacations except for notified activities.",
    "library": "Library hours are generally during school hours and as per class schedule.",
    "admission": "Admissions are handled by the school office. Application forms and guidelines are available there.",
    "documents": "Required documents include birth certificate, previous report card, transfer certificate, and ID proof.",
    "fees": "Fee structure varies by class. Please contact the school office for exact details.",
    "scholarship": "Scholarships or fee concessions are offered as per school policy.",
    "bus": "School bus registration is available through the transport office.",
    "visitor": "All visitors must register at the school gate and carry valid ID.",
    "nurse": "The school nurse is available during school hours for medical assistance.",
    "bullying": "The school follows a strict anti-bullying policy to ensure student safety.",
    "calendar": "The academic calendar is available from the school office or official communication.",
    "portal": "Parents can access student information through the official school portal.",
    "contact teacher": "Teachers can be contacted via official school communication channels."
}

OFFICE_CONTACT = "📞 School Office: +91-XXXXXXXXXX"

# ------------------ SESSION STATE ------------------
if "chat" not in st.session_state:
    st.session_state.chat = []

if "fail_count" not in st.session_state:
    st.session_state.fail_count = 0

# ------------------ CHAT TITLE ------------------
st.markdown("## 🤖 PRAGYAN AI – School Information Assistant")
st.markdown("Ask about timings, fees, admissions, transport, rules, academics, and more.")

# ------------------ DISPLAY CHAT ------------------
for role, msg in st.session_state.chat:
    css_class = "user" if role == "user" else "bot"
    st.markdown(f"<div class='chat-box {css_class}'>{msg}</div>", unsafe_allow_html=True)

# ------------------ USER INPUT ------------------
user_input = st.text_input("💬 Ask your question here:")

# ------------------ RESPONSE LOGIC ------------------
def get_answer(query):
    query = query.lower()
    for key in FAQ_DATA:
        if key in query:
            return FAQ_DATA[key]
    return None

if user_input:
    st.session_state.chat.append(("user", user_input))
    answer = get_answer(user_input)

    if answer:
        st.session_state.chat.append(("bot", answer))
        st.session_state.fail_count = 0
    else:
        st.session_state.fail_count += 1
        if st.session_state.fail_count >= 2:
            st.session_state.chat.append(
                ("bot", f"I’m unable to answer this accurately. Please contact a human representative.\n\n{OFFICE_CONTACT}")
            )
            st.session_state.fail_count = 0
        else:
            st.session_state.chat.append(
                ("bot", "I’m not completely sure about that. Could you please rephrase your question?")
            )

    st.experimental_rerun()
