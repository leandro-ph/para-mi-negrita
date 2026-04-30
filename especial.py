
import streamlit as st
import time

# 1. Configuración visual (Estilo Hello Kitty / Amor)
st.set_page_config(page_title="💖Para mi Vida💖", page_icon="💖")

st.markdown("""
    <style>
    .stApp {
        background-color: #FFB6C1;
        background-image: radial-gradient(#FF69B4 0.5px, transparent 0.5px);
        background-size: 20px 20px;
    }
    h1, h2, h3, p {
        color: #8B0000 !important;
        font-family: 'Comic Sans MS', cursive;
    }
    .stButton>button {
        background-color: #FF69B4;
        color: white;
        border-radius: 20px;
        border: 2px solid #FF1493;
    }
    </style>
    """, unsafe_allow_html=True)

# 2. Control de Acceso
if 'autenticado' not in st.session_state:
    st.session_state.autenticado = False

if not st.session_state.autenticado:
    st.subheader("🌸 Ingrese datos")
    user = st.text_input("Usuario")
    password = st.text_input("Contraseña", type="password")
    
    if st.button("Entrar 💖"):
        if user == "JulianCito" and password == "JulianCito":
            st.session_state.autenticado = True
            st.rerun()
        else:
            st.error("Datos incorrectos, mi amor. Inténtalo de nuevo.")
else:
    # 3. Música de fondo (Aquel Nap ZzZz)
    # El tag 'loop' asegura que se repita siempre
    st.audio("musica.mp3", format="audio/mp3", loop=True, autoplay=True)

    # 4. Animación de Entrada
    if 'paso' not in st.session_state:
        st.session_state.paso = 'animacion'

    if st.session_state.paso == 'animacion':
        st.balloons() # Simulación de mariposas/vuelo
        st.markdown("<h1 style='text-align: center;'>🦋 ❤️ 🦋</h1>", unsafe_allow_html=True)
        st.markdown("<h1 style='text-align: center; font-size: 50px;'>Te Amo mi Vida</h1>", unsafe_allow_html=True)
        
        # Imagen de Hello Kitty
        try:
            st.image("kitty.gif", use_container_width=True)
        except:
            st.write("✨ (Aquí va tu GIF de Hello Kitty) ✨")
            
        if st.button("Empezar Cuestionario ✨"):
            st.session_state.paso = 'cuestionario'
            st.rerun()

    # 5. El Cuestionario
    elif st.session_state.paso == 'cuestionario':
        st.title("💘 ¿Cuánto conoces a tu amor?")
        
        q1 = st.text_input("1. ¿En que año nacio el amor de tu vida?").strip().lower()
        q2 = st.text_input("2. ¿Qué edad tiene el amor de tu vida?")
        q3 = st.text_input("3. ¿Cómo se llama el amor de tu vida?").strip().capitalize()
        q4 = st.text_input("4. ¿Cuándo conociste al amor de tu vida?")
        q5 = st.radio("5. ¿Estarias con el amor de tu vida?", ("Selecciona", "si", "no"))

        if st.button("Enviar respuestas 💌"):
            puntos = 0
            if q1 == "2008": puntos += 1
            if q2 == "18": puntos += 1
            if q3 in ["Julian", "Leandro"]: puntos += 1
            if "2022" in q4: puntos += 1
            if q5 == "si": puntos += 1
            
            st.session_state.puntos = puntos
            st.session_state.paso = 'resultado'
            st.rerun()

    # 6. Pantallas de Resultado
    elif st.session_state.paso == 'resultado':
        p = st.session_state.puntos
        
        if p >= 4:
            st.header("🎊 FELICIDADES, TE GANASTE MI CORAZON")
            st.image("kitty.gif", use_container_width=True)
        
        elif p in [2, 3]:
            st.header("🧸 Muy Bien Niñita")
            if st.button("Volver a intentar"):
                st.session_state.paso = 'cuestionario'
                st.rerun()

        else:
            st.header("❌ Fallaste Amor")
            st.write("¿Deseas continuar?")
            col1, col2 = st.columns(2)
            with col1:
                if st.button("Sí"):
                    st.session_state.paso = 'cuestionario'
                    st.rerun()
            with col2:
                if st.button("No"):
                    st.write("Programa cerrado. Adiós, amor.")
                    st.stop()





































































































































































































