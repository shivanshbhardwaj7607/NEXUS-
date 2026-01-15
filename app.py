import streamlit as st

# ===============================
# PAGE CONFIG
# ===============================
st.set_page_config(
    page_title="PRAGYAN AI • School Intelligence",
    page_icon="🛰️",
    layout="wide"
)

# ===============================
# SCI-FI CSS
# ===============================
st.markdown("""
<style>
.stApp {
    background: radial-gradient(circle at top, #020617, #000000);
    color: #e5e7eb;
    font-family: 'Orbitron', sans-serif;
}

h1 {
    text-align: center;
    color: #38bdf8;
    text-shadow: 0 0 20px #38bdf8;
    letter-spacing: 4px;
}

.stChatMessage {
    background: rgba(2, 6, 23, 0.85);
    border: 1px solid rgba(56,189,248,0.4);
    border-radius: 18px;
    padding: 22px;
    box-shadow: 0 0 25px rgba(56,189,248,0.25);
}

[data-testid="stSidebar"] {
    background: linear-gradient(180deg, #020617, #020617);
    border-right: 2px solid #38bdf8;
}

.badge {
    display:inline-block;
    padding:6px 16px;
    border-radius:50px;
    border:1px solid #38bdf8;
    color:#38bdf8;
    margin:4px;
    font-size:12px;
    box-shadow:0 0 10px rgba(56,189,248,0.6);
}
</style>
""", unsafe_allow_html=True)

# ===============================
# SIDEBAR (COMMAND PANEL)
# ===============================
with st.sidebar:
    st.markdown("## 🛰️ AI COMMAND CORE")
    st.markdown("**Status:** 🟢 ONLINE")
    st.markdown("**Security:** 🔐 End-to-End Encrypted")
    st.markdown("**Network:** 🛰️ Satellite Linked")
    st.markdown("**Mode:** 🎓 School Intelligence")
    st.divider()
    st.markdown("📞 **Human Support**")
    st.markdown("**Office:** 7300723901")
    st.caption("© PRAGYAN AI SYSTEM")

# ===============================
# HEADER
# ===============================
st.markdown("<h1>PRAGYAN AI</h1>", unsafe_allow_html=True)
st.markdown("""
<div class="badge">INSTITUTIONAL AI</div>
<div class="badge">REAL-TIME RESPONSE</div>
<div class="badge">DOMAIN-LOCKED</div>
<div class="badge">SCI-FI INTERFACE</div>
""", unsafe_allow_html=True)

# ===============================
# SESSION STATE
# ===============================
if "chat" not in st.session_state:
    st.session_state.chat = []

if "fail" not in st.session_state:
    st.session_state.fail = 0

# ===============================
# FAQ DATA
# ===============================
FAQ = {
    "time": "School operates during official academic hours as notified.",
    "bell": "Bell schedule is displayed on the school notice board.",
    "lunch": "Lunch menu is shared weekly by the school.",
    "holiday": "Please refer to the official school calendar.",
    "absence": "Parents must inform the school for absence or late arrival.",
    "pickup": "Early pickup requires prior permission.",
    "lost": "Lost and Found is available inside the campus.",
    "dress": "Students must strictly follow the uniform policy.",
    "summer": "School remains closed during summer vacation.",
    "library": "Library timings are announced by the administration.",

    "admission": "Admissions are processed through the school office.",
    "documents": "Documents include birth certificate and school records.",
    "fee": "Fee structure is available at the school office.",
    "scholarship": "Scholarship details are provided by the administration.",

    "bus": "School transport is available upon registration.",
    "late": "Contact the transport office if the bus is delayed.",
    "visitor": "All visitors must register at the entry gate.",
    "bullying": "The school follows a zero-tolerance anti-bullying policy.",

    "calendar": "School calendar is officially published.",
    "teacher": "Teachers can be contacted via official channels.",
    "exam": "Students appear in school and board examinations.",
    "report": "Report cards are released as per schedule.",
    "transcript": "Transcripts can be requested from the school office."
}

# ===============================
# RESPONSE ENGINE
# ===============================
def respond(q):
    q = q.lower()
    for k in FAQ:
        if k in q:
            st.session_state.fail = 0
            return FAQ[k]

    st.session_state.fail += 1
    if st.session_state.fail >= 2:
        return "🤝 **Talk to a Human**\n\n📞 School Office: **7300723901**"

    return "⚠️ Query not recognized. Please rephrase."

# ===============================
# CHAT HISTORY
# ===============================
for r, m in st.session_state.chat:
    with st.chat_message(r):
        st.markdown(m)

# ===============================
# INPUT
# ===============================
user = st.chat_input("🔍 Ask School Intelligence Query...")

if user:
    st.session_state.chat.append(("user", user))
    ans = respond(user)
    st.session_state.chat.append(("assistant", ans))
    with st.chat_message("assistant"):
        st.markdown(ans)
