# KIVORT AI - Asistente de Voz con IA (Python)

Asistente de voz que escucha por micrófono, transcribe lo que dices, le pregunta a un modelo de OpenAI y responde en voz alta.
Construido en Python con `SpeechRecognition`, `pyttsx3` y la API de OpenAI (Chat Completions).

## Características

- 🎙️ Reconocimiento de voz en español (o el idioma que configures).
- 🤖 Respuestas generadas con un modelo de OpenAI (`gpt-4o-mini` por defecto).
- 🔊 Respuestas leídas en voz alta con texto a voz.
- 🔑 Manejo seguro de la API key mediante variables de entorno (`.env`).
- 🛑 Se detiene al decir "salir" o "exit".

## Requisitos

- Python 3.10, 3.11 o 3.12 (evitar versiones muy recientes por soporte de librerías de audio).
- Micrófono funcional.
- Cuenta de OpenAI con una API key y saldo cargado.

## Uso

Con el entorno virtual activo, ejecuta:

```bash
python asistente.py
```

Habla al micrófono cuando veas "Escuchando..." en la terminal. Di "salir" o "exit" para terminar la conversación.

## Estructura del proyecto

```
.
├── asistente.py       # Lógica principal del asistente
├── requirements.txt   # Dependencias del proyecto
├── .env                # API key (no se sube al repositorio)
├── .gitignore
└── README.md
```



