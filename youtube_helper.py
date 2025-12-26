import re
from youtube_transcript_api import YouTubeTranscriptApi, TranscriptsDisabled, NoTranscriptFound

MOCK_TRANSCRIPT = """
Hola a todos, bienvenidos a este curso de Python para principiantes. 
En este video vamos a aprender los conceptos básicos de la programación.
Python es un lenguaje muy popular porque su sintaxis es limpia y fácil de leer.
Primero, hablemos de las variables. Una variable es como una caja donde guardamos datos.
Por ejemplo, podemos guardar el número 5 en una variable llamada 'x'.
Luego tenemos las estructuras de control, como el 'if' y el 'else', que nos permiten tomar decisiones en el código.
También existen los bucles, como el 'for' y el 'while', para repetir tareas.
La inteligencia artificial usa mucho Python debido a librerías como TensorFlow y PyTorch.
En resumen, Python es ideal para empezar, pero también es muy potente para expertos.
Espero que disfruten este tutorial y se suscriban al canal.
"""

def extract_video_id(url):
    """Extrae el ID del video de la URL."""
    patterns = [r'(?:v=|\/)([0-9A-Za-z_-]{11}).*']
    for pattern in patterns:
        match = re.search(pattern, url)
        if match:
            return match.group(1)
    raise ValueError(" URL no válida")

def get_transcript_text(video_url):
    """
    Intenta bajar la transcripción real. 
    Si falla por bloqueo de YouTube, devuelve el texto de respaldo (MOCK).
    """
    video_id = "DESCONOCIDO"
    try:
        video_id = extract_video_id(video_url)
        print(f"ID detectado: {video_id}")
        
        transcript_list = YouTubeTranscriptApi.list_transcripts(video_id)
        transcript = transcript_list.find_transcript(['es', 'en'])
        transcript_data = transcript.fetch()
        
        full_text = " ".join([item['text'] for item in transcript_data])
        return full_text

    except Exception as e:
        print(f"AVISO: Falló la conexión con YouTube ({str(e)})")
        print("Activando MODO SIMULACIÓN con texto de respaldo...")
        return MOCK_TRANSCRIPT

if __name__ == "__main__":
    test_url = "https://www.youtube.com/watch?v=_uQrJ0TkZlc" 
    print("Probando extractor con Fail-safe...")
    resultado = get_transcript_text(test_url)
    
    print("\nRESULTADO FINAL (Para la IA):")
    print("-" * 50)
    print(resultado[:200] + "...") 
    print("-" * 50)