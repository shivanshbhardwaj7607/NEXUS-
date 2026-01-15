import streamlit as st

# ===============================
# PAGE CONFIG
# ===============================
st.set_page_config(
    page_title="School FAQ Chatbot",
    page_icon="🤖",
    layout="centered"
)

# ===============================
# BASIC UI
# ===============================
st.title("🤖 School FAQ Chatbot")
st.caption("Official School Information Assistant")

st.markdown("""
This chatbot answers common school-related questions.
If it cannot help, it will connect you to the school office.
""")

# ===============================
# SESSION STATE
# ===============================
if "chat" not in st.session_state:
    st.session_state.chat = []

if "fail_count" not in st.session_state:
    st.session_state.fail_count = 0

# ===============================
# FAQ DATA (GENERAL + SAFE)
# ===============================
FAQ = {
    "time": "School usually starts in the morning and ends in the afternoon. Exact timings are shared by the school office.",
    "bell": "The bell schedule is displayed on the school notice board and shared with students.",
    "lunch": "The weekly lunch menu is shared by the school administration.",
    "holiday": "Please check the official school calendar or contact the school office to confirm holidays.",
    "absence": "Parents should inform the class teacher or school office regarding absence or lateness.",
    "early pickup": "For early pickup, parents must submit a written request to the school office.",
    "lost": "The Lost and Found section is located inside the school campus.",
    "dress": "Students must follow the prescribed school uniform and dress code.",
    "summer": "The school remains closed during summer vacations as per the academic calendar.",
    "library": "Library hours are announced by the school and vary by class.",

    "admission": "Admissions are done through the school office as per availability of seats.",
    "documents": "Required documents generally include birth certificate, photographs, and previous school records.",
    "fee": "The fee structure is provided by the school office during admission.",
    "scholarship": "Please contact the school office for information regarding financial aid or scholarships.",
    "age": "The age requirement follows school and board guidelines.",
    "waiting": "Availability depends on seat vacancies in the requested class.",
    "tour": "School tours can be scheduled by contacting the school office.",
    "transfer": "Mid-term transfers are considered on a case-by-case basis.",
    "deadline": "Enrollment deadlines are announced by the school administration.",
    "sibling": "Sibling concessions are subject to school policy.",

    "bus": "Transport facility can be availed by registering with the transport department.",
    "bus stop": "Bus stop details are shared by the transport department.",
    "bus late": "In case of delay, parents should contact the transport office.",
    "weather": "Weather delays or closures are informed through official communication.",
    "emergency": "Emergency contact details can be updated through the school office.",
    "visitor": "All visitors must register at the school gate before entering.",
    "nurse": "The school nurse can be contacted through the school office.",
    "allergy": "The school takes necessary precautions for students with food allergies.",
    "bullying": "The school follows a strict anti-bullying policy.",
    "pickup": "Student drop-off and pick-up zones are designated by the school.",

    "calendar": "The school calendar is available on the notice board or official website.",
    "portal": "Login details for the parent/student portal are provided by the school.",
    "conference": "Parent-teacher meeting dates are announced by the school.",
    "homework": "Homework is assigned as per class requirements.",
    "teacher": "Parents can contact teachers through official school communication channels.",
    "tests": "Students appear for board and school-level assessments.",
    "report": "Report cards are distributed as per the academic schedule.",
    "esl": "Support programs depend on school facilities.",
    "iep": "Special support is provided as per school policy.",
    "transcript": "Official transcripts can be requested from the school office."
}

# ===============================
# RESPONSE FUNCTION
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
            "I’m unable to assist further.\n\n"
            "📞 **Talk to a Human:**\n"
            "Please contact the school office directly.\n"
            "**Phone:** 7300723901\n"
            "**Office Hours:** School working hours"
        )

    return "I’m not sure about that. Could you please rephrase your question?"

# ===============================
# CHAT DISPLAY
# ===============================
for role, msg in st.session_state.chat:
    with st.chat_message(role):
        st.markdown(msg)

# ===============================
# USER INPUT
# ===============================
user_input = st.chat_input("Ask your school-related question here...")

if user_input:
    st.session_state.chat.append(("user", user_input))

    response = get_response(user_input)

    st.session_state.chat.append(("assistant", response))

    with st.chat_message("assistant"):
        st.markdown(response)
