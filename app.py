import streamlit as st

st.set_page_config(
    page_title="PRAGYAN AI • School Assistant",
    page_icon="🤖",
    layout="wide"
)

# ------------------ SCI-FI UI ------------------
st.markdown("""
<style>
body { background: #020617; color:#e6f1ff; }
.chat { border:1px solid #00eaff; border-radius:14px; padding:14px; margin:8px 0; }
.user { border-left:5px solid #ff4b4b; }
.bot { border-left:5px solid #00eaff; }
.sidebar-box { border:1px solid #00eaff; padding:15px; border-radius:12px; }
</style>
""", unsafe_allow_html=True)

# ------------------ SIDEBAR ------------------
with st.sidebar:
    st.markdown("<div class='sidebar-box'>", unsafe_allow_html=True)
    st.markdown("### 🛰 PRAGYAN AI SYSTEM")
    st.markdown("""
    • Institutional AI  
    • Domain Locked  
    • Secure Communication  
    • Human Escalation Enabled  
    """)
    st.markdown("📞 **School Office:** +91-XXXXXXXXXX")
    st.markdown("</div>", unsafe_allow_html=True)

# ------------------ FAQ ANSWERS (HUMAN-LIKE) ------------------
ANSWERS = {
    "start": "The school day usually begins at **8:00 AM** with morning assembly and ends around **2:00 PM**. Timings may vary slightly for different classes.",
    "end": "The school day generally concludes by **2:00 PM**, after completion of all academic periods.",
    "bell": "The regular bell schedule includes morning assembly, subject periods of around 40 minutes, a lunch break in the middle of the day, and dispersal in the afternoon.",
    "lunch": "The weekly lunch menu is planned by the school and shared through circulars or the notice board. Students may also bring home-packed meals.",
    "holiday": "School holidays follow the official academic calendar. If today is a holiday, students are informed in advance through notice or circular.",
    "absence": "To report an absence, parents should inform the class teacher or school office through a written note or phone call.",
    "early pickup": "For early pickup, parents must submit a request at the school office and show valid identification.",
    "lost": "The Lost and Found section is usually maintained near the school office where students can check for misplaced items.",
    "uniform": "The school follows a strict uniform and dress code policy. Students are expected to wear the prescribed uniform on all working days.",
    "library": "The school library is open during school hours and students can visit as per their class schedule or teacher’s permission.",
    "admission": "Admissions are processed by the school office. Application forms and guidance are provided during the admission period.",
    "fees": "The fee structure varies by class and includes tuition and other charges. Parents are advised to contact the school office for exact details.",
    "bus": "School transport is available on selected routes. Registration is done through the transport office.",
    "nurse": "A trained school nurse is available during school hours to handle minor injuries and health concerns.",
    "bullying": "The school follows a zero-tolerance anti-bullying policy to ensure a safe and respectful environment.",
    "calendar": "The academic calendar is issued by the school at the start of the session and shared with parents.",
    "teacher": "Parents can contact teachers through official school communication channels or during parent-teacher meetings."
}

# ------------------ SESSION ------------------
if "chat" not in st.session_state:
    st.session_state.chat = []

if "fail" not in st.session_state:
    st.session_state.fail = 0

# ------------------ DISPLAY ------------------
st.markdown("## 🤖 PRAGYAN AI – School Assistant")

for role, msg in st.session_state.chat:
    cls = "user" if role == "user" else "bot"
    st.markdown(f"<div class='chat {cls}'>{msg}</div>", unsafe_allow_html=True)

# ------------------ INPUT ------------------
query = st.text_input("Ask your question:")

def intelligent_reply(q):
    q = q.lower()
    for k in ANSWERS:
        if k in q:
            return ANSWERS[k]
    return None

if query:
    st.session_state.chat.append(("user", query))
    reply = intelligent_reply(query)

    if reply:
        st.session_state.chat.append(("bot", reply))
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
                ("bot", "Could you please clarify your question? I want to assist you accurately.")
            )

    st.experimental_rerun()
