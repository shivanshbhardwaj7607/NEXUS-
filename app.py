import streamlit as st

# ===============================
# PAGE CONFIG
# ===============================
st.set_page_config(
    page_title="School FAQ Chatbot",
    page_icon="🤖",
    layout="wide"
)

# ===============================
# SIDEBAR (COOL POP-UP)
# ===============================
with st.sidebar:
    st.title("🛰️ School AI Console")
    st.markdown("""
    **System Status:** 🟢 Online  
    **AI Mode:** School FAQ  
    **Security:** End-to-End Encrypted  
    **Network:** Satellite Connected  
    """)
    st.divider()
    st.markdown("📞 **School Office**")
    st.markdown("**Phone:** 7300723901")
    st.markdown("**Hours:** School Working Time")
    st.divider()
    st.caption("© School AI Assistant")

# ===============================
# MAIN UI
# ===============================
st.title("🤖 School FAQ Chatbot")
st.caption("Official School Information Assistant")

# ===============================
# SESSION STATE
# ===============================
if "chat" not in st.session_state:
    st.session_state.chat = []

if "fail_count" not in st.session_state:
    st.session_state.fail_count = 0

# ===============================
# FAQ DATA
# ===============================
FAQ = {
    "time": "School starts in the morning and ends in the afternoon as per schedule.",
    "bell": "The bell schedule is displayed on the school notice board.",
    "lunch": "The weekly lunch menu is shared by the school administration.",
    "holiday": "Please check the official school calendar for holidays.",
    "absence": "Parents should inform the class teacher or school office.",
    "pickup": "Early pickup requires written permission from parents.",
    "lost": "Lost and Found is located inside the school campus.",
    "dress": "Students must follow the prescribed school uniform.",
    "summer": "The school remains closed during summer vacations.",
    "library": "Library hours are announced by the school.",

    "admission": "Admissions are done through the school office.",
    "documents": "Documents include birth certificate and previous school records.",
    "fee": "Fee structure is provided during admission.",
    "scholarship": "Please contact the school office for scholarship details.",
    "age": "Age criteria follows school and board norms.",
    "transfer": "Mid-term transfers depend on seat availability.",

    "bus": "Transport facility is available through school registration.",
    "late": "If the bus is late, contact the transport department.",
    "visitor": "All visitors must register at the school gate.",
    "nurse": "The school nurse can be contacted via the office.",
    "bullying": "The school follows a strict anti-bullying policy.",

    "calendar": "The school calendar is available officially.",
    "teacher": "Teachers can be contacted via official channels.",
    "exam": "Students appear in school and board examinations.",
    "report": "Report cards are issued as per schedule.",
    "transcript": "Transcripts can be requested from the school office."
}

# ===============================
# RESPONSE ENGINE
# ===============================
def get_response(user_input):
    text = user_input.lower()

    for key in FAQ:
        if key in text:
            st.session_state.fail_count = 0
            return FAQ[key]

    st.session_state.fail_count += 1

    if st.session_state.fail_count >= 2:
        return (
            "🤝 **Talk to a Human**\n\n"
            "Please contact the school office directly.\n"
            "**📞 Phone:** 7300723901"
        )

    return "I’m not sure about that. Please rephrase your question."

# ===============================
# CHAT HISTORY
# ===============================
for role, msg in st.session_state.chat:
    with st.chat_message(role):
        st.markdown(msg)

# ===============================
# USER INPUT
# ===============================
user_input = st.chat_input("Ask your school-related question...")

if user_input:
    st.session_state.chat.append(("user", user_input))
    response = get_response(user_input)
    st.session_state.chat.append(("assistant", response))

    with st.chat_message("assistant"):
        st.markdown(response)
