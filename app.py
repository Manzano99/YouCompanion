import streamlit as st
import os
from dotenv import load_dotenv
from groq import Groq
from youtube_helper import get_transcript_text

# 1. Configuración de la página
st.set_page_config(page_title="YouTube Study Companion", page_icon="🎓")

# 2. Cargar entorno y cliente
load_dotenv()
api_key = os.getenv("GROQ_API_KEY")

if not api_key:
    st.error("No se encontró la API Key. Revisa tu archivo .env")
    st.stop()

client = Groq(api_key=api_key)

# 3. UI de Streamlit
st.title("YouTube Study Companion")
st.markdown("""
¡Convierte videos largos en apuntes de estudio en segundos!
*Pega la URL de un video educativo y la IA generará el resumen por ti.*
""")

# Input de URL
video_url = st.text_input("Link del Video de YouTube:", placeholder="https://www.youtube.com/watch?v=...")

if st.button("Generar Apuntes"):
    if not video_url:
        st.warning("Por favor, introduce una URL válida.")
    else:
        # Iniciamos el proceso
        with st.spinner("Escuchando el video y tomando notas..."):
            try:
                # PASO 1: Obtener transcripción
                transcript_text = get_transcript_text(video_url)
                
                # Mostramos un preview
                with st.expander("Ver transcripción cruda (Debug)"):
                    st.write(transcript_text[:500] + "...")

                # PASO 2: Preparar el Prompt para la IA
                prompt_sistema = """
                Eres un profesor experto y conciso. Tu tarea es ayudar a un estudiante a entender el siguiente texto extraído de un video.
                Debes generar una salida en formato Markdown con esta estructura exacta:
                
                # Resumen Ejecutivo
                (Un resumen de 2-3 frases de qué trata el video)
                
                # Conceptos Clave
                (Lista de viñetas con los 3-5 puntos más importantes)
                
                # Quiz de Repaso
                (3 preguntas cortas con sus respuestas ocultas o al final para autoevaluación)
                """

                # PASO 3: Llamar a Groq (Llama 3)
                chat_completion = client.chat.completions.create(
                    messages=[
                        {"role": "system", "content": prompt_sistema},
                        {"role": "user", "content": f"El texto del video es: {transcript_text}"}
                    ],
                    model="llama-3.3-70b-versatile",
                    temperature=0.5,
                )
                
                # PASO 4: Mostrar resultado
                respuesta = chat_completion.choices[0].message.content
                st.markdown("---")
                st.markdown(respuesta)
                st.success("¡Apuntes generados con éxito!")

            except Exception as e:
                st.error(f"Ocurrió un error: {e}")

# Footer
st.markdown("---")
st.caption("Desarrollado usando Streamlit y Groq Llama 3")