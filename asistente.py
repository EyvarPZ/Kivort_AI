import speech_recognition as sr
import pyttsx3
import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

engine = pyttsx3.init()
engine.setProperty("rate", 175)  # velocidad de habla


def speak(text: str):
    print(f"Asistente: {text}")
    engine.say(text)
    engine.runAndWait()


def listen() -> str:
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Escuchando...")
        recognizer.adjust_for_ambient_noise(source, duration=0.5)
        audio = recognizer.listen(source)
    try:
        query = recognizer.recognize_google(audio, language="es-MX")
        print(f"Dijiste: {query}")
        return query
    except sr.UnknownValueError:
        print("No entendí, ¿puedes repetir?")
        return ""
    except sr.RequestError:
        print("No hay conexión con el servicio de reconocimiento de voz.")
        return ""


def ask_openai(question: str) -> str:
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "Eres un asistente de voz breve y útil."},
            {"role": "user", "content": question},
        ],
        max_tokens=150,
    )
    return response.choices[0].message.content.strip()


def assistant():
    speak("Hola, ¿en qué puedo ayudarte?")
    while True:
        command = listen()
        if not command:
            continue
        if "salir" in command.lower() or "exit" in command.lower():
            speak("Hasta luego.")
            break
        respuesta = ask_openai(command)
        speak(respuesta)


if __name__ == "__main__":
    assistant()
