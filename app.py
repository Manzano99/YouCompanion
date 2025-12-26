import streamlit as st
import os
from dotenv import load_dotenv
from groq import Groq
from youtube_helper import get_transcript_text

# 1. Configuración de la Página
st.set_page_config(page_title="YouTube Study Companion", page_icon="🎓", layout="centered")

# 2. Cargar entorno
load_dotenv()
api_key = os.getenv("GROQ_API_KEY")

if not api_key:
    st.error("No se encontró la API Key. Revisa tu archivo .env")
    st.stop()

client = Groq(api_key=api_key)

# 3. Función auxiliar para llamar al LLM
def generar_resumen(texto_entrada):
    prompt_sistema = """
    Eres un profesor experto. Genera un resumen estructurado en Markdown:
    1. Resumen Ejecutivo (2-3 frases)
    2. Conceptos Clave (Viñetas)
    3. Quiz de Repaso (3 preguntas cortas)
    """
    try:
        chat_completion = client.chat.completions.create(
            messages=[
                {"role": "system", "content": prompt_sistema},
                {"role": "user", "content": f"Texto a resumir: {texto_entrada}"}
            ],
            model="llama-3.3-70b-versatile",
            temperature=0.5,
        )
        return chat_completion.choices[0].message.content
    except Exception as e:
        return f"Error en la IA: {e}"

# 4. Interfaz Gráfica
st.title("YouTube Study Companion")
st.markdown("Convierte videos en apuntes. Si la carga automática falla, usa el modo manual.")

# --- PESTAÑAS (NUEVO) ---
tab1, tab2 = st.tabs(["Vía URL (Automático)", "Pegar Texto (Manual)"])

# Pestaña 1: Automática
with tab1:
    video_url = st.text_input("🔗 Link del Video:", placeholder="https://youtube.com/...")
    if st.button("Analizar Video"):
        if not video_url:
            st.warning("Introduce una URL.")
        else:
            with st.spinner("Conectando con YouTube..."):
                transcript_text = get_transcript_text(video_url)
                
                # DETECCIÓN INTELIGENTE DE FALLO
                if "Hola a todos, bienvenidos a este curso de Python" in transcript_text:
                    # En lugar de dar un resumen falso, avisamos y detenemos.
                    st.error("YouTube ha bloqueado la conexión automática desde esta red (Protección Anti-Bot).")
                    st.info("**Solución:** Por favor, usa la pestaña **'Pegar Texto (Manual)'**. Copia la transcripción del video y pégala ahí para un análisis 100% real.")
                else:
                    # Si funcionó de verdad (milagro), mostramos el resumen
                    st.success("Subtítulos descargados correctamente.")
                    respuesta = generar_resumen(transcript_text)
                    st.markdown("---")
                    st.markdown(respuesta)

# Pestaña 2: Manual (La solución robusta)
with tab2:
    st.info("Si YouTube bloquea la URL, copia la transcripción del video y pégala aquí.")
    texto_manual = st.text_area("Pega aquí el texto del video:", height=300)
    
    if st.button("Analizar Texto Manual"):
        if not texto_manual:
            st.warning("El campo de texto está vacío.")
        else:
            with st.spinner("Analizando tus notas..."):
                respuesta = generar_resumen(texto_manual)
                st.markdown("---")
                st.markdown(respuesta)

# Footer
st.markdown("---")
st.caption("Desarrollado usando Streamlit y Groq Llama 3")