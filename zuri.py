import  pyttsx3
import  speech_recognition as sr
import datetime
import os

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
print(voices[0].id)
engine.setProperty('voices', voices[0].id)

#text to speech
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

#voice to text
def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
     print("listening...")
     r.pause_threshold = 1
     audio = r.listen(source,timeout=1,phrase_time_limit=5)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio,language='en-in')
        print(f"user said: {query}")

    except Exception as e:
        speak("Say that again please...")
        return "none"
    return query

#To wish
def wish():
    hour = int(datetime.datetime.now().hour)

    if hour>=0 and hour<=12:
        speak("good morning")
    elif hour>12 and hour<18:
        speak("good afternoon")
    else:
        speak("good evening")
    speak("i am zuri sir please tell me how can i  help you")

if __name__ == "__main__":
  wish()
  while True:

      query = takecommand().lower()

      if "open notepad" in query:
          npath = "C:\\Windows\\notepad.exe"
          os.startfile(npath)