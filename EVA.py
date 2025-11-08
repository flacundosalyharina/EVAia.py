# E.V.A.: Experimental Virtual Assistant

import streamlit as st
from groq import Groq

st.set_page_config(page_title="EVA.ia", page_icon="👍✨🤖")

# Fuentes personalizadas
st.markdown("""
    <link href="https://fonts.googleapis.com/css2?family=Orbitron:wght@600&family=Rajdhani:wght@400;500&display=swap" rel="stylesheet">
    <link href="https://fonts.googleapis.com/css2?family=Exo+2:ital,wght@0,100..900;1,100..900&display=swap" rel="stylesheet">
    <style>
    html, body, [class*="st-"] {
        font-family: 'Exo 2', sans-serif;
        color: #f3f3f3;
    }
    h1, h2, h3, .stMarkdown h1 {
        font-family: 'Orbitron', sans-serif;
        letter-spacing: 2px;
    }
    </style>
""", unsafe_allow_html=True)

# #CBA6F7

# TÍTULO

st.markdown("""
    <h1 style="
        text-align:center;
        font-family:'Orbitron', sans-serif;
        color:#ffffff;
        margin: 10px;
        padding: 0;
        text-shadow:0px 0px 20px #9b5de5;
        letter-spacing:3px;
        animation: glow 2s ease-in-out infinite alternate;
    ">
    E.V.A.
    </h1>
            
    <h3 style="
        text-align:center;
        font-family:'Orbitron', sans-serif;
        color:#CBA6F7;
        margin: 0;
        padding: 0;
        letter-spacing:3px;
        animation: glow 2s ease-in-out infinite alternate;
    ">
    Experimental Virtual Assistant
    </h3>
""", unsafe_allow_html=True)

st.markdown("<link href='https://fonts.googleapis.com/css2?family=Orbitron:wght@600&display=swap' rel='stylesheet'>", unsafe_allow_html=True)

st.caption("by Facundo Salinas de Lima")

#linear-gradient(180deg, #1f1c2c, #928DAB);

# CSS
st.markdown("""
    <style>
    /*Fondo general*/
    .stApp{
        background: linear-gradient(135deg, #2A0845, #6441A5);
        color: white;
    }

    /*Sidebar con otro degradado*/
    section[data-testid="stSidebar"] {
        background: #2A0845;
        color: #f5f5f5;
    }

    /*Ajustes del título principal*/
    h1 {
        color: #ffffff;
        text-shadow: 2px 2px 8px rgba(0,0,0,0.5);
    }

    /*Botones*/
    button[kind="secondary"] {
        background-color: #a855f7 !important;
        color: white !important;
        border-radius: 10px !important;
        transition: all 0.3s ease-in-out;
    }

    button[kind="secondary"]:hover {
        background-color: #c084fc !important;
        transform: scale(1.05);
    }

    /*Chat bubbles*/
    [data-testid="stChatMessageUser"] {
        background: rgba(255,255,255,0.1);
        border-radius: 10px;
        padding: 10px;
        margin-bottom: 5px;
    }

    [data-testid="stChatMessageAssistant"] {
        background: rgba(255,255,255,0.15);
        border-radius: 10px;
        padding: 10px;
        margin-bottom: 5px;
    }

    /*Scrollbar estética*/
    ::-webkit-scrollbar {
        width: 10px;
    }
    ::-webkit-scrollbar-thumb {
        background: #a855f7;
        border-radius: 10px;
    }
    </style>
""", unsafe_allow_html=True)

#PARA ICONO FLECHITA 

st.markdown("""
    <style>
    [data-testid="stSidebarCollapseButton"] svg {
        color: white !important;
        width: 1.2em !important;
        height: 1.2em !important;
    }
    </style>
""", unsafe_allow_html=True)

# CONFIGURACIÓN
MODELOS = ['llama-3.1-8b-instant', 'llama-3.3-70b-versatile', 'deepseek-r1-distill-llama-70b']

def configurar_pagina():

    st.sidebar.markdown("""
        <link href="https://fonts.googleapis.com/css2?family=Exo+2:ital,wght@0,100..900;1,100..900&display=swap" rel="stylesheet">
        <div style="
            background: rgba(255,255,255,0.1);
            border: 1px solid rgba(255,255,255,0.2);
            border-radius: 12px;
            padding: 5px;
            margin: 15px 0px;
            text-align: center;
            box-shadow: 0 0 10px rgba(155,93,229,0.3);
        ">
            <h3 style="color:#E3DAFF; font-family: 'Exo 2', sans-serif;">
                Configuración IA    
            </h3>
        </div>
    """, unsafe_allow_html=True)

    elegirModelo = st.sidebar.selectbox(
        "MODELOS",
        options = tuple(MODELOS),
        index = 0,
        key="selector_modelo"
    )
    return elegirModelo

st.markdown("""
    <style>
    div[data-baseweb="select"] input {
        pointer-events: none;
    }
    </style>
""", unsafe_allow_html=True)

def crear_usuario_groq():
    clave_secreta = st.secrets["CLAVE_API"]
    return Groq(api_key=clave_secreta)

def configurar_modelo(historial, modelo):
    respuesta = clienteUsuario.chat.completions.create(
        model=modelo,
        messages=historial
    )
    return respuesta.choices[0].message.content

def inicializar_estado():
    if "mensajes" not in st.session_state:
        st.session_state.mensajes = []
    if "nombre" not in st.session_state:
        st.session_state.nombre = None

# INICIO
inicializar_estado()
clienteUsuario = crear_usuario_groq()
modelo = configurar_pagina()

# # PEDIR NOMBRE
# if not st.session_state.nombre:
#     nombre = st.text_input("¿Cuál es tu nombre?")

#     if st.button("Saludar!"):
#         print("apretó saludar")
#         if nombre.strip():
#             print("tenía nombre")
#             st.session_state.nombre = nombre.strip()

#             # Insertar mensaje de sistema (solo una vez)
#             if not any(m["role"] == "system" for m in st.session_state.mensajes):
#                 st.session_state.mensajes.insert(0, {
#                     "role": "system",
#                     "content": f"Sos EVA, una IA experimental creada por Facundo. "
#                             f"El usuario se llama <{st.session_state.nombre}>. "
#                             f"Tu estilo debe ser cálido, profesional y natural."
#                 })

#             # Saludo visible
#             saludo = f"¡Hola {nombre}! Bienvenid@ a la experiencia E.V.A. 🤖 ¿En qué te puedo ayudar hoy?"
#             st.session_state.mensajes.append({"role": "assistant", "content": saludo})

#             st.rerun()
#         else:
#             st.warning("Por favor, ingresá tu nombre antes de continuar.")
# else:
#     # CHAT
#     #st.subheader(f"Tu chat con EVA") 💬👩‍💻

#     st.markdown("""
#         <link href="https://fonts.googleapis.com/css2?family=Exo+2:ital,wght@0,100..900;1,100..900&display=swap" rel="stylesheet">
#         <div style="
#             background: rgba(255,255,255,0.1);
#             border: 1px solid rgba(255,255,255,0.2);
#             border-radius: 12px;
#             padding: 0px;
#             margin-top: 5px;
#             text-align: center;
#             box-shadow: 0 0 10px rgba(155,93,229,0.3);
#         ">
#             <h3 style="color:#E3DAFF; font-family: 'Exo 2', sans-serif;"> Tu chat con EVA </h3>
#         </div>
#     """, unsafe_allow_html=True)

#     # Historial
#     for msg in st.session_state.mensajes:
#         with st.chat_message(msg["role"]):
#             st.markdown(f"""
#                 <div style="
#                     margin: 0 !important;
#                     padding: 10px;
#                     text-indent: 0;
#                     line-height: 1.4;
#                     background-color: #18181b;
#                     color: #00FFB7;
#                     font-family: 'Courier New', monospace;
#                     border-radius: 8px;
#                     border-left: 3px solid #9b5de5;
#                     box-shadow: 0 0 8px rgba(155,93,229,0.5);
#                     display: inline-block;
#                     max-width: 95%;
#                 ">
#                     {msg["content"].strip()}
#                 </div>
#             """, unsafe_allow_html=True)

#     mensaje = st.chat_input("Escribí tu mensaje:")

#     if mensaje:
#         st.session_state.mensajes.append({"role": "user", "content": mensaje})

#         with st.chat_message("user"):
#             st.markdown(mensaje)

#         with st.spinner("🤖 EVA está pensando..."):
#             respuesta = configurar_modelo(st.session_state.mensajes, modelo)

#         st.session_state.mensajes.append({"role": "assistant", "content": respuesta})

#         with st.chat_message("assistant"):
#             st.markdown(f"""
#                 <div style="
#                     margin: 0 !important;
#                     padding: 10px;
#                     text-indent: 0;
#                     line-height: 1.4;
#                     background-color: #18181b;
#                     color: #00FFB7;
#                     font-family: 'Courier New', monospace;
#                     border-radius: 8px;
#                     border-left: 3px solid #9b5de5;
#                     box-shadow: 0 0 8px rgba(155,93,229,0.5);
#                     display: inline-block;
#                     max-width: 95%;
#                 ">
#                     {msg["content"].strip()}
#                 </div>
#             """, unsafe_allow_html=True)

# PEDIR NOMBRE
if not st.session_state.nombre:
    nombre = st.text_input("¿Cuál es tu nombre?")

    if st.button("Saludar!"):
        print("apretó saludar")
        if nombre.strip():
            print("tenía nombre")
            st.session_state.nombre = nombre.strip()

            # Saludo visible (solo una vez)
            saludo = f"¡Hola {nombre}! Bienvenid@ a la experiencia E.V.A. 🤖 ¿En qué te puedo ayudar hoy?"
            st.session_state.mensajes = [  # Reinicia el historial limpio
                {"role": "assistant", "content": saludo}
            ]

            st.rerun()
        else:
            st.warning("Por favor, ingresá tu nombre antes de continuar.")

else:
    # CHAT
    st.markdown("""
        <link href="https://fonts.googleapis.com/css2?family=Exo+2:ital,wght@0,100..900;1,100..900&display=swap" rel="stylesheet">
        <div style="
            background: rgba(255,255,255,0.1);
            border: 1px solid rgba(255,255,255,0.2);
            border-radius: 12px;
            padding: 0px;
            margin-top: 5px;
            text-align: center;
            box-shadow: 0 0 10px rgba(155,93,229,0.3);
        ">
            <h3 style="color:#E3DAFF; font-family: 'Exo 2', sans-serif;"> Tu chat con EVA </h3>
        </div>
    """, unsafe_allow_html=True)

    # HISTORIAL
    for msg in st.session_state.mensajes:
        with st.chat_message(msg["role"]):
            st.markdown(f"""
                <div style="
                    margin: 0 !important;
                    padding: 10px;
                    line-height: 1.4;
                    background-color: #18181b;
                    color: #00FFB7;
                    font-family: 'Courier New', monospace;
                    border-radius: 8px;
                    border-left: 3px solid #9b5de5;
                    box-shadow: 0 0 8px rgba(155,93,229,0.5);
                    display: inline-block;
                    max-width: 95%;
                ">
                    {msg["content"].strip()}
                </div>
            """, unsafe_allow_html=True)

    # INPUT DEL USUARIO
    mensaje = st.chat_input("Escribí tu mensaje:")

    if mensaje:
        st.session_state.mensajes.append({"role": "user", "content": mensaje})

        with st.chat_message("user"):
            st.markdown(mensaje)

        with st.spinner("🤖 EVA está pensando..."):
            # Pasamos todo el historial (incluyendo el saludo) al modelo
            respuesta = configurar_modelo(st.session_state.mensajes, modelo)

        st.session_state.mensajes.append({"role": "assistant", "content": respuesta})

        with st.chat_message("assistant"):
            st.markdown(f"""
                <div style="
                    margin: 0 !important;
                    padding: 10px;
                    line-height: 1.4;
                    background-color: #18181b;
                    color: #00FFB7;
                    font-family: 'Courier New', monospace;
                    border-radius: 8px;
                    border-left: 3px solid #9b5de5;
                    box-shadow: 0 0 8px rgba(155,93,229,0.5);
                    display: inline-block;
                    max-width: 95%;
                ">
                    {respuesta.strip()}
                </div>
            """, unsafe_allow_html=True)



#base="#48E58F"
# [theme]
# primaryColor="#8F48E5"
# backgroundColor="#B8F5D3"
# secondaryBackgroundColor="#49E48F"
# textColor="#8F48E5"
# font="sans serif"