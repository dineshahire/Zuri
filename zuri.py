import datetime
import os
import cv2
import pyautogui
import pyttsx3
import requests
import speech_recognition as sr
import wikipedia
from requests import get
import webbrowser
import pywhatkit as kit
import smtplib
import sys
import time
import pyjokes
import instaloader

engine = pyttsx3.init("sapi5")
voices = engine.getProperty('voices')
print(voices[1].id)
engine.setProperty('voices', voices[1].id)
engine.setProperty('rate',175)

#text to speech
def speak(audio):
    engine.say(audio)
    print(audio)
    engine.runAndWait()

#voice to text
def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
     print("listening...")
     r.pause_threshold = 1
     audio = r.listen(source,timeout=5,phrase_time_limit=8)

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
    tt = time.strftime("%I:%M %p")

    if hour>=0 and hour<=12:
        speak("good morning")
    elif hour>12 and hour<18:
        speak("good afternoon")
    else:
        speak("good evening")
    speak("i am zuri sir please tell me how can i  help you")

def sendEmail(to,content):
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('your user', 'youe pass')
    server.sendmail('your email id', to . content)
    server.close()

def news():
    main_url = 'https://newsapi.org/v2/everything?q=tesla&from=2023-06-21&sortBy=publishedAt&apiKey=563aa873b8324abf835a399efd5fc26a'

    main_page = requests.get(main_url).json()
    #print main page
    articles = main_page["articles"]
    #print(articles)
    head = []
    day=["first","second","third","fourth","fifth","sixth","seventh","eighth","nineth","tenth"]
    for ar in  articles:
        head.append(ar["title"])
    for i in range (len(day)):
        speak(f"today's {day[i]} news is: {head[i]}")

if __name__ == "__main__":
  wish()
  while True:
   if 1:


      query = takecommand().lower()

      if "open notepad" in query:
          npath = "C:\\Windows\\notepad.exe"
          os.startfile(npath)

      if "open excel sheet" in query:
          apath = "C:\\Program Files\\Microsoft Office\\root\\Office16\\excel.exe"
          os.startfile(apath)

      if "open chrome" in query:
          bpath = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
          os.startfile(bpath)

      elif "open microsoft edge" in query:
          os.system("start microsoft edge")


      elif "open command prompt" in query:
          os.system("start cmd")

      elif "open camera" in query:
          cap = cv2.VideoCapture(0)
          while True:
              ret, img = cap.read()
              cv2.imshow('webcam', img)
              k = cv2.waitKey(50)
              if k==27:
                  break;
              cap.release()
              cv2.destroyWindow()

      elif "play music" in query:
          music_dir = "C:\\Users\\91836\\OneDrive\\Documents\\music"
          songs = os.listdir(music_dir)
          os.startfile(os.path.join(music_dir,songs[0]))

      elif "wikipedia" in query:
          speak("searching wikipedia...")
          query = query.replace("wikipedia","")
          results = wikipedia.summary(query,sentences=2)
          speak("according to wikipedia")
          speak(results)
          print(results)

      elif "address" in query:
          ip = get('https://api.ipify.org').text
          speak(f"your IP address is {ip}")

      elif "open youtube" in query:
          webbrowser.open("www.youtube.com")

      elif "open facebook" in query:
          webbrowser.open("www.facebook.com")

      elif "open instagram" in query:
          webbrowser.open("www.instagram.com")

      elif "open movie" in query:
          webbrowser.open("www.azmovies.com")

      elif "open linkedin" in query:
          webbrowser.open("www.linkedin.com")

      #programming courses
      elif "open coursera " in query:
          webbrowser.open("www.coursera.com")

      #normal languages
      elif "open udemy" in query:
          webbrowser.open("www.udemy.com")

      elif "asa" in query:
          webbrowser.open("https://replit.com/@SiddharthChakr4/Saarthi.com")

      #for github
      elif "369" in query:
          webbrowser.open("www.github.com")


      elif "google" in query:
          speak("sir, what should i search on google")
          danny = takecommand().lower()
          webbrowser.open(f"{danny}")

      elif "send message" in query:
          kit.sendwhatmsg("+919892752329", "this is testing protocol",2,25)#2,25 msg deilvered in 8 hours

      elif "play song on youtube" in query:
          kit.playonyt("see you again")

      elif "email to dinesh" in query:
          try:
              speak("what should i say")
              content = takecommand().lower()
              to = "type here person email"
              sendEmail(to,content)
              speak("Email has been send to dinesh")

          except Exception as e:
              print(e)
              speak("sorry sir, i am not able to sent this email to dinesh")

      elif "no thanks" in query:
          speak("thanks for using me sir,have a good day.")
          sys.exit()

  #to close any app
      elif "close notepad" in query:
          speak("okay sir,closing notepad")
          os.system("taskkill /f /im notepad.exe")

      elif "close command prompt" in query:
          speak("okay sir,closing command prompt")
          os.system("taskkill /f /im cmd.exe")


  #to set alaram
      elif "set alaram" in query:
          nn = int(datetime.datetime.now().hour)
          if nn==22:
              music_dir = 'C:\\Users\\91836\\OneDrive\\Documents\\music'
              songs = os.listdir(music_dir)
              os.startfile(os.path.join(music_dir, songs[0]))

   #to find a joke
      elif "tell me a joke" in query:
          joke = pyjokes.get_joke()
          speak(joke)

      elif "shut down the system" in query:
          os.system("shutdown /s /t 5")

      elif "restart the system" in query:
          os.system("shutdown /s /t 5")

      elif "sleep the system" in query:
          os.system("rundll32.exe powerprof.dll,SetSuspendState 0,1,0")

      elif 'switch window' in query:
          pyautogui.keyDown("alt")
          pyautogui.press("tab")
          time.sleep(1)
          pyautogui.keyUp("alt")

      elif "tell me news" in query:
          speak("please wait sir, fetching the latest news")
          news()

      #check location with the help of ip address
      elif "where i am" in query or "where we are" in query:
          speak("wait sir let me check")
          try:
              ipAdd = requests.get('https://api.ipify.org').text
              print(ipAdd)
              webbrowser.open("https://www.iplocation.net/myip")+ipAdd+'.json'


              speak(f"sir i am not sure, but i think we are in (city) city of (country) country")
          except Exception as e:
               speak("Yes sir, i found your location")
               pass

      elif "instagram profile" in query or "profile on instagram" in query:
          speak("sir please enter the user name correctly.")
          name = input("Enter username here: ")
          webbrowser.open(f"www.instagram.com/{name}")
          speak(f"sir here is the profile of the user {name}")
          time.sleep(5)
          speak("sir would you like to download profile picture of this account.")
          condition = takecommand().lower()
          if "yes" in condition:
              mod = instaloader.Instaloader()
              mod.download_profile(name, profile_pic_only=True)
              speak("i am done sir, profile picture is saved in our main folder. now i am ready for next command")
          else:
              pass


      elif "take scrrenshot" in query or "take a screenshot" in query:
          speak("sir, please tell me the name for this screenshot file")
          name = takecommand().lower()
          speak("please sir hold the screen for few seconds, i am taking screenshot")
          time.sleep(3)
          img = pyautogui.screenshot()
          img.save(f"{name}.png")
          speak("i am done sir, the screenshot is saved in our main folder. now i am ready for next command")

      elif "how are you" in query:
          speak("i am fine sir how about you")

      elif "zuri who made you" in query:
          speak("i have been made by Dinesh,Apurav and Shubham")

      elif "zuri do you have any girlfriend" in query:
          speak("yes sir, i have girlfriend...what about you do you have any girlfriend")

      elif "zuri what is your girlfriend name" in query:
          speak("i am shy but your my friend that's why i am telling you my girlfriend name is SIRI...")

      #speak("sir, do you have any other work")










