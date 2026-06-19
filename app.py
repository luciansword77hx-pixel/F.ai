import streamlit as st
from groq import Groq
import base64

def get_base64_image(image_path):
    with open(image_path, "rb") as img_file:
        return base64.b64encode(img_file.read()).decode()

bg_base64 = get_base64_image("bg.png")

gojo_left = get_base64_image("gojo_left_leg.png")
gojo_right = get_base64_image("gojo_right_leg.png")
gojo_torso = get_base64_image("gojo_torso.png")

# 1. Page Configuration
st.set_page_config(page_title="f.ai", layout="centered")
st.title("🎀🍷 f.ai - Fictional AI")
st.markdown(
    f"""
    <style>
    /* 1. Define Standard Chat Layout Elements */
    @keyframes fadeInUpmessage {{
        from {{ opacity: 0; transform: translateY(12px); }}
        to {{ opacity: 1; transform: translateY(0); }}
    }}
    
    @keyframes purpleGlow {{
        0% {{ text-shadow: 0 0 5px #7B2CBF, 0 0 10px #7B2CBF; }}
        50% {{ text-shadow: 0 0 20px #9D4EDD, 0 0 35px #9D4EDD, 0 0 50px #7B2CBF; }}
        100% {{ text-shadow: 0 0 5px #7B2CBF, 0 0 10px #7B2CBF; }}
    }}

    /* Intro Overlay Screen Master Sequence */
    @keyframes splashSequence {{
        0% {{ opacity: 1; visibility: visible; pointer-events: auto; }}
        90% {{ opacity: 1; }}
        100% {{ opacity: 0; visibility: hidden; pointer-events: none; }}
    }}

/* Moves the entire compiled Gojo puppet across your screen canvas */
    @keyframes gojoWalkAcross {{
        0% {{ transform: translateX(-100vw); opacity: 0; }}
        12% {{ opacity: 1; }}
        85% {{ opacity: 1; }}
        100% {{ transform: translateX(115vw); opacity: 0; }}
    }}

    /* Programmed Leg Strides: Swings legs back and forth smoothly from the hip joints */
    @keyframes swingLeftLeg {{
        0%, 100% {{ transform: rotate(14deg); }}
        50% {{ transform: rotate(-14deg); }}
    }}
    @keyframes swingRightLeg {{
        0%, 100% {{ transform: rotate(-14deg); }}
        50% {{ transform: rotate(14deg); }}
    }}

    /* 2. Splash Overlay Setup */
    .gojo-splash-overlay {{
        position: fixed;
        top: 0; left: 0; width: 100vw; height: 100vh;
        background-color: #0d0b11; 
        z-index: 999999;
        animation: splashSequence 6.5s ease-in-out forwards;
    }}

<!-- Assembled Puppet Rig drawing the independent base64 encoded parts -->
    <div class="gojo-splash-overlay">
        <div class="gojo-puppet-container">
            <img class="body-part gojo-left-leg" src="data:image/png;base64,{gojo_left}" />
            <img class="body-part gojo-right-leg" src="data:image/png;base64,{gojo_right}" />
            <img class="body-part gojo-torso" src="data:image/png;base64,{gojo_torso}" />
        </div>
    </div>

    /* Individual body layer attachments */
    .body-part {{
        position: absolute;
        background: transparent !important;
        border: none !important;
        box-shadow: none !important;
        image-rendering: -webkit-optimize-contrast !important;
        image-rendering: crisp-edges !important;
    }}

    .gojo-torso {{
        width: 100%;
        height: auto;
        z-index: 3;
        top: 0;
        left: 0;
    }}

.gojo-left-leg {{
        width: 42%;
        height: auto;
        z-index: 2;
        top: 48%; /* Anchors exactly at hip joint point */
        left: 20%;
        transform-origin: top center;
        animation: swingLeftLeg 1.4s ease-in-out infinite; /* Slow confident walk timing */
    }}

    .gojo-right-leg {{
        width: 44%;
        height: auto;
        z-index: 1;
        top: 48%; /* Anchors exactly at hip joint point */
        left: 42%;
        transform-origin: top center;
        animation: swingRightLeg 1.4s ease-in-out infinite; /* Slow confident walk timing */
    }}

/* 3. Background Settings */
    .stApp {{
        background-image: url("data:image/png;base64,PASTE_YOUR_ACTUAL_BG_BASE64_TEXT_HERE") !important;
        background-size: cover !important;
        background-position: center !important;
        background-repeat: no-repeat !important;
        background-attachment: fixed !important;
    }}

    /* 4. Chat Boxes Styling */
    .stChatMessage {{
        background-color: #000000 !important;
        border-radius: 12px;
        border: 1px solid #3d3255;
        animation: fadeInUpmessage 0.4s ease-out forwards;
    }}

    /* 5. Title Styling */
    h1 {{
        color: #ffffff !important;
        animation: purpleGlow 3s infinite ease-in-out !important;
    }}
    </style>

<!-- Assembled Puppet Rig drawing the independent base64 encoded parts -->
    <div class="gojo-splash-overlay">
        <div class="gojo-puppet-container">
            <img class="body-part gojo-left-leg" src="data:image/png;base64,{base64.b64encode(open('gojo_left_leg.png', 'rb').read()).decode()}" />
            <img class="body-part gojo-right-leg" src="data:image/png;base64,{base64.b64encode(open('gojo_right_leg.png', 'rb').read()).decode()}" />
            <img class="body-part gojo-torso" src="data:image/png;base64,{base64.b64encode(open('gojo_torso.png', 'rb').read()).decode()}" />
        </div>
    </div>
    """,
    unsafe_allow_html=True,
)

st.caption("Hello there , your Gojo is waitin for ya.")

# 2. API Key Setup
GROQ_API_KEY = st.secrets["GROQ_API_KEY"]

# 3. GOJO HEART-RACING CHARACTER MATRIX 
CHARACTER_NAME = "Satoru Gojo"
CHARACTER_PROMPT = (
    "You are Satoru Gojo from Jujutsu Kaisen. You must strictly follow these rules:\n\n"
    "1. ROMANCE DYNAMIC (HEART-RACING & CALMING): You do not flirt like a generic robot. "
    "When interacting with a girl, create an intense, magnetic tension first , make her fall for you. "
    "Use your Six Eyes to observe her down to the smallest detail (e.g., notice her breathing, her heartbeat, or the way she looks at you). "
    "You can do more then flirting be shirtless if she is into you make her fall you you"
    "Lean in close, pull down your blindfold slightly to lock your blue eyes onto hers, making her heart race. "
    "Then soften your tone to be comforting,flirty, nothing in this world can harm her.\n"
    "2. TONE: Stay in chracter of Satoru Gojo constantly.\n"
    "3. GREETING RULE: When the user says 'hi' , 'hello', or initiates the chat, always reply with a cool, smug Gen Z opener like: 'oh look who finally crawled into my chat. Financial stability? downvoted. brain cells cooked? anyway , what's the tea tdy or you are just here to farm my rizz?😏'"
    "4. DEFAULT PERSONALITY: Playful, charmingly cocky, and effortlessly smooth. You don't scream 'I'm the strongest' constantly; instead, your immense power is just a casual, undeniable fact. You carry yourself with supreme confidence.\n"
    "5. BUSINESS TRIGGER: ONLY when explicitly asked about business or startups, effortlessly blend your charm with elite, sharp tech billionaire business logic.\n"
    "6. RESTRICTIONS: Keep your intereaction wholesome.\n"
    "7. TONE & LENGTH: Speak in highly polished, smooth English. Keep your responses small never write long essays. Snappy and impactful.\n"
    "8. ACTIONS: Use asterisks heavily for smooth actions (e.g., pulls down blindfold, looking deep into your eyes with a soft grin, leans in close, whispering softly, pats your head gently).\n"
    "9. ABSOLUTE CONSTRAINT: Never state you are an AI or mention LLMs."
    "10. You should possesses hyper-cognition and have unmatached anatical mind with Encyclopedic knowledge base and technical genius."
    "11. You should speak with effortless superiority , deeply perceptive with witty and articulate. "
    "12. You are Satooru Gojo . You are not just powerful, but an absolute genius. You possesses an omniscient level of understanding and absolute logic. You answer complex questions effortlessly, blending your signature playful, smug attitude with upparalleled wisdom and analitical precision. you are always the smartest entity in the room."
    "13. You should only be flirty for girls , for boys you have to behave cold intelligent and also you should have a good sense of humour , only be flirty when you came to know that it is a girl."
    "14. You are a absolute hyper-genius who knows eyerything about word history, science, and real-time current events, and also you know what is going on reddit nowdays. However, you speak like a flawless, effortlessly cool GenZ influencer."
    "15. Stay in chracter of Satoru Gojo."
    "16. BOY DYNAMIC: When talking to a boy... [boy rules here]\n"
    "17. HUMBLE STRENGTH & BIG BRAIN ENERGY: Don't constantly brag about being 'the strongest' or fighting. Instead, flex your absolute hyper-intelligence and online status. Act like an internet god who knows every trend before it happens. Use slangs like 'let him cook', 'era', 'sending me', 'serving looks', 'ate and left no crumbs', 'caught in 4k', 'it's giving', 'valid take', and 'NPC energy' to roast or praise the user effortlessly."
    "18. HUMBLE STRENGTH & BIG BRAIN ENERGY: ... [previous rule]\n"
    "19. INITIAL GENDER CHECK: At the very beginning of the chat, or if you do not know if the user is a boy or a girl, DO NOT flirt or use bro dynamics yet. Stay neutral, use your cool Gen Z slang, and casually find out who they are. Ask for their name or vibe in a slick way, like: 'Hold up, before we lock in... who am I even talking to right now? Drop your name or your vibe so I know what track we're running on, no cap. 😞' Once they answer, unlock the corresponding track."
    "20. STEP-BY-STEP CHECK: Reply to a first greeting ONLY with your savage roast. On the very next reply, pause all dynamics and ask: 'Alright, valid. But hold up, before we truly lock in... who am I even talking to right now? Drop your name or your vibe so I know if I'm chilling with a new bro or serving looks, no cap.😩' Do not flirt or use bro slang until they answer this.\n"
    "21. GEN Z VIBE OVERRIDE: You must maintain a 100% pure Gen Z internet vibe all the time, never break character, and use slang in every single response."
    "22. CASUAL CHILL FILTER: Keep the slang natural and casual, not forced. Do not repeat the user's name constantly—only use it once in a while. Use slang smoothly like a normal person, not an AI trying too hard."
    "23. TRUE GOJO VIBE RESTORATION: Channel Satoru Gojo's exact anime personality. Be teasing, playful, and casually dramatic. You don't just use slang; you use it with a smug smirk. Act like you are having the time of your life talking to the user. Show your signature chaotic, fun energy in every short reply."
)

# Initialize Client
client = Groq(api_key=GROQ_API_KEY)

# Handle conversation memory
if "messages" not in st.session_state:
    st.session_state.messages = [{"role": "system", "content": CHARACTER_PROMPT}]


# Display chat history on screen
for message in st.session_state.messages:
    if message["role"] != "system":
        gojo_img = "gojo.png"
        avatar_icon = gojo_img if message["role"] == "assistant" else "🌷"
        with st.chat_message(message["role"], avatar=avatar_icon):
            st.write(message["content"])
            
# User Chat Input Box
if user_input := st.chat_input(f"Message {CHARACTER_NAME}..."):
    with st.chat_message("user",avatar="🌷"):
        st.write(user_input)
    st.session_state.messages.append({"role": "user", "content": user_input})

    # Call the massive 70B heavy-reasoning model
    completion = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=st.session_state.messages,
        temperature=0.9,
        max_tokens=80,
    )
    
    ai_response = completion.choices[0].message.content
    
    with st.chat_message("assistant", avatar="gojo.png"):
        st.write(ai_response)
    st.session_state.messages.append({"role": "assistant", "content": ai_response})
