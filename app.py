import streamlit as st

st.set_page_config(
    page_title="PRAGYAN AI – School Assistant",
    page_icon="🤖",
    layout="wide"
)

# ================== STYLE ==================
st.markdown("""
<style>
body { background-color:#020617; color:#e6f1ff; }
.chat { border:1px solid #00eaff; border-radius:14px; padding:14px; margin:10px 0; }
.user { border-left:5px solid #ff4b4b; }
.bot { border-left:5px solid #00eaff; }
.sidebar-box { border:1px solid #00eaff; padding:15px; border-radius:12px; }
</style>
""", unsafe_allow_html=True)

# ================== SIDEBAR ==================
with st.sidebar:
    st.markdown("<div class='sidebar-box'>", unsafe_allow_html=True)
    st.markdown("### 🛰 PRAGYAN AI SYSTEM")
    st.markdown("""
    • Institutional AI  
    • Domain Locked  
    • Secure & Reliable  
    • Human Escalation Enabled  
    """)
    st.markdown("📞 **School Office:** +91-XXXXXXXXXX")
    st.markdown("</div>", unsafe_allow_html=True)

# ================== ANSWERS ==================
ANSWERS = {
    "contact teacher": "You can contact your child’s teacher through the school diary, official school phone number, or during scheduled parent-teacher meetings.",
    "teacher": "Teachers can be contacted via the school office or during parent-teacher conferences.",
    "school start": "The school day usually starts at 8:00 AM with morning assembly.",
    "school end": "The school day generally ends around 2:00 PM after all periods are completed.",
    "bell": "The bell schedule includes morning assembly, subject periods, a lunch break, and dispersal.",
    "absence": "Parents should inform the school or class teacher in case of absence or late arrival.",
    "uniform": "Students must wear the prescribed school uniform as per school guidelines.",
    "library": "The school library is open during school hours as per class schedule.",
    "fees": "The fee structure varies by class. Parents should contact the school office for exact details."
}

# ================== SESSION ==================
if "chat" not in st.session_state:
    st.session_state.chat = []

if "fail" not in st.session_state:
    st.session_state.fail = 0

# ================== UI ==================
st.markdown("## 🤖 PRAGYAN AI – School Assistant")

for role, msg in st.session_state.chat:
    css = "user" if role == "user" else "bot"
    st.markdown(f"<div class='chat {css}'>{msg}</div>", unsafe_allow_html=True)

query = st.text_input("Ask your question:")

def get_answer(q):
    q = q.lower()
    for key in ANSWERS:
        if key in q:
            return ANSWERS[key]
    return None

if query:
    st.session_state.chat.append(("user", query))
    answer = get_answer(query)

    if answer:
        st.session_state.chat.append(("bot", answer))
        st.session_state.fail = 0
    else:
        st.session_state.fail += 1
        if st.session_state.fail >= 2:
            st.session_state.chat.append(
                ("bot", "I’m unable to answer this accurately. Please contact the school office at +91-XXXXXXXXXX.")
            )
            st.session_state.fail = 0
        else:
            st.session_state.chat.append(
                ("bot", "Could you please rephrase or give more details?")
            )

    st.rerun()
