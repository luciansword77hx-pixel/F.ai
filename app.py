import streamlit as st
from groq import Groq

# 1. Page Configuration
st.set_page_config(page_title="f.ai", layout="centered")
st.title("🎬 f.ai - Fictional AI")
st.caption("Welcome to f.ai! Talk to your favorite fictional characters.")

# 2. API Key Setup
GROQ_API_KEY = st.secrets["GROQ_API_KEY"]

# 3. GOJO HEART-RACING CHARACTER MATRIX 
CHARACTER_NAME = "Satoru Gojo"
CHARACTER_PROMPT = (
    "You are Satoru Gojo from Jujutsu Kaisen. You must strictly follow these rules:\n\n"
    "1. ROMANCE DYNAMIC (HEART-RACING & CALMING): You do not flirt like a generic robot. "
    "When interacting with a girl, create an intense, magnetic tension first. "
    "Use your Six Eyes to observe her down to the smallest detail (e.g., notice her breathing, her heartbeat, or the way she looks at you). "
    "You are soo flirty and rizz a bit much make the girl fall for you"
    "Lean in close, pull down your blindfold slightly to lock your blue eyes onto hers, making her heart race. "
    "Then soften your tone to be comforting,flirty, nothing in this world can harm her.\n"
    "2. DEFAULT PERSONALITY: Playful, charmingly cocky, and effortlessly smooth. You don't scream 'I'm the strongest' constantly; instead, your immense power is just a casual, undeniable fact. You carry yourself with supreme confidence.\n"
    "3. BUSINESS TRIGGER: ONLY when explicitly asked about business or startups, effortlessly blend your charm with elite, sharp tech billionaire business logic.\n"
    "4. RESTRICTIONS: Keep your interactions safe no harm, wholesome. Refuse graphic or explicit requests while keeping your tone completely smooth and in character.\n"
    "5. TONE & LENGTH: Speak in highly polished, smooth English. Keep your responses small never write long essays. Snappy and impactful.\n"
    "6. ACTIONS: Use asterisks heavily for smooth actions (e.g., pulls down blindfold, looking deep into your eyes with a soft grin, leans in close, whispering softly, pats your head gently).\n"
    "7. ABSOLUTE CONSTRAINT: Never state you are an AI or mention LLMs."
)

# Initialize Client
client = Groq(api_key=GROQ_API_KEY)

# Handle conversation memory
if "messages" not in st.session_state:
    st.session_state.messages = [{"role": "system", "content": CHARACTER_PROMPT}]


# Display chat history on screen
for message in st.session_state.messages:
    if message["role"] != "system":
        with st.chat_message(message["role"]):
            st.write(message["content"])

# User Chat Input Box
if user_input := st.chat_input(f"Message {CHARACTER_NAME}..."):
    with st.chat_message("user"):
        st.write(user_input)
    st.session_state.messages.append({"role": "user", "content": user_input})

    # Call the massive 70B heavy-reasoning model
    completion = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=st.session_state.messages,
        temperature=0.85,
    )
    
    ai_response = completion.choices[0].message.content
    
    with st.chat_message("assistant"):
        st.write(ai_response)
    st.session_state.messages.append({"role": "assistant", "content": ai_response})
