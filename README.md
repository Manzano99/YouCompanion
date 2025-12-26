# YouTube Study Companion

![Python](https://img.shields.io/badge/Python-3.10%2B-blue)
![Streamlit](https://img.shields.io/badge/Frontend-Streamlit-red)
![AI](https://img.shields.io/badge/AI-Llama_3.3-purple)

Una aplicación de **Inteligencia Artificial Generativa** diseñada para estudiantes. Transforma videos educativos de YouTube en apuntes de estudio estructurados, cuestionarios y resúmenes en segundos.

## Características Principales

- **Análisis con IA Avanzada:** Utiliza el modelo **Llama 3.3** (Groq) para entender contextos y extraer conceptos clave.
- **Sistema Robusto (Anti-Bloqueo):** Incluye un sistema de detección de fallos. Si YouTube bloquea la descarga automática de subtítulos, la app sugiere automáticamente el **Modo Manual**.
- **Salida Estructurada:** Genera automáticamente:
  - Resumen Ejecutivo.
  - Puntos Clave (Bullet points).
  - Quiz de Autoevaluación.
- **Rápida:** Gracias a la inferencia de Groq, procesa textos largos en milisegundos.

## Stack Tecnológico

- **Frontend:** Streamlit (Python)
- **Backend:** Python
- **Modelos AI:** Llama 3.3-70b-versatile (vía Groq API)
- **Ingesta de Datos:** `youtube-transcript-api`

## Instalación y Configuración

1.  **Clonar el repositorio:**

    ```bash
    git clone [https://github.com/TU_USUARIO/youtube-study-companion.git](https://github.com/TU_USUARIO/youtube-study-companion.git)
    cd youtube-study-companion
    ```

2.  **Crear entorno virtual:**

    ```bash
    # Windows
    py -m venv venv
    .\venv\Scripts\activate

    # Mac/Linux
    python3 -m venv venv
    source venv/bin/activate
    ```

3.  **Instalar dependencias:**

    ```bash
    pip install -r requirements.txt
    ```

4.  **Configurar Variables de Entorno:**
    Crea un archivo `.env` en la raíz y añade tu API Key de Groq (es gratis):

    ```
    GROQ_API_KEY=gsk_tu_clave_aqui...
    ```

5.  **Ejecutar la App:**
    ```bash
    streamlit run app.py
    ```

## Uso

1.  **Modo automático:** Pega la URL de un video de YouTube.
2.  **Modo manual (Recomendado):** Si el video tiene restricciones, copia la transcripción desde YouTube, ve a la pestaña "Pegar Texto" y deja que la IA haga su magia.
