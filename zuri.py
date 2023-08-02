import datetime
import os
from PIL import Image
import wolframalpha
import pywhatkit
from pywikihow import search_wikihow
import PyPDF2
from gtts import gTTS
import pyautogui
import pyttsx3
import requests
import webbrowser as web
from keyboard import press
from keyboard import press_and_release
from keyboard import write
from bs4 import BeautifulSoup
from googletrans import Translator
import speech_recognition as sr
import wikipedia
from requests import get
import datetime
from playsound import playsound
import webbrowser
import pywhatkit as kit
import sys
import time
import pyjokes
import instaloader
import whatsapp
from geopy.distance import great_circle
from geopy.geocoders import Nominatim
import geocoder
import mediapipe as mp
import cv2
import smtplib


#<--color recongnation (START)





engine = pyttsx3.init("sapi5")
voices = engine.getProperty('voices')
print(voices[0].id)
engine.setProperty('voice', voices[6].id)
engine.setProperty('rate', 176)


# text to speech
def speak(audio):
    engine.say(audio)
    print(audio)
    engine.runAndWait()

Api_key = "QZds4MWpWiEcQvJQwUVu8cuN2nNjdlMNdldA6aO3"

def NasaNews(Date):

    speak("Extracting data from nasa")

    Url = "https://api.nasa.gov/planetary/apod?api_key" + str(Api_key)

    Params = {'date':str(Date)}

    r = requests.get(Url,params = Params)

    Data = r.json()

    Info = Data['explanation']

    Title = Data['title']

    Image_Url = Data['url']

    Image_r = requests.get(Image_Url)


    FileName = str(Data) + '.jpg'

    with open(FileName,'wb') as  f:

        f.write(Image_r.content)

    path_1 = "C:\\Users\\91836\\OneDrive\\Desktop\\ZURI\\zuri\\" + str(FileName)

    path_2 = "C:\\Users\\91836\\OneDrive\\Desktop\\ZURI\\zuri\\nasadatabase\\" + str(FileName)

    os.rename(path_1,path_2)

    img = Image.open(path_2)

    img.show()

    speak(f"Title : {Title}")
    speak(f"According to nasa : {Info}")




# voice to text
def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("listening...")
        r.pause_threshold = 1
        audio = r.listen(source, timeout=5, phrase_time_limit=8)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"user said: {query}")


    except Exception as e:
        speak("Say that again please...")
        return "none"
    return query.lower()


def takecommand_Hindi():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("listening...")
        r.pause_threshold = 1
        audio = r.listen(source, timeout=5, phrase_time_limit=8)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='hi')
        print(f"user said: {query}")


    except Exception as e:
        speak("Say that again please...")
        return "none"
    return query.lower()



def TaskExe():
    speak("Hello, I am zuri")
    speak("How can i help you ?")

def GoogleMaps(Place):

    Url_Place = "https://www.google.com/maps/place/" + str(Place)

    geolocater = Nominatim(user_agent="myGeocoder")

    location = geolocater.geocode(Place , addressdetails= True)

    target_latlon = location.latitude , location.longitude

    web.open(url=Url_Place)

    location = location.raw['address']

    target = {'city' : location.get('city',''),
              'state' : location.get('state',''),
              'country' : location.get('country','')}

    current_loca = geocoder.ip('me')

    current_latlon = current_loca.latlng

    distance = str(great_circle(current_latlon,target_latlon))
    distance = str(distance.split(' ',1)[0])
    distance = round(float(distance),2)



    speak(target)
    speak(f"Sir, {Place} is {distance} kilometre away from your location.")


def MarsImage():

    name = 'curiosity'

    date = '2020-12-3'

    Api_ = str(Api_key)

    url  = f"https://api.nasa.gov/mars-photos/api/v1/rovers/{name}/photos?earth_date={date}&Api_key={Api_}"

    print(url)

    r = requests.get(url)

    Data = r.json()

    Photos = Data['photos'][:20]

    try:

        for index , photo in enumerate(Photos):

            camera = photo['camera']

            rover = photo['rover']

            rover_name = rover['name']

            camera_name = camera['name']

            full_camera_name = camera['full_name']

            date_of_photo = photo['earth_date']

            img_url = photo['img_src']

            p = requests.get(img_url)

            img = f'{index}.jpg'

            with open(img,'wb') as file:
                file.write(p.content)

            path_1 = "C:\\Users\\91836\\OneDrive\\Desktop\\ZURI\\zuri\\" + str(img)

            path_2 = "C:\\Users\\91836\\OneDrive\\Desktop\\ZURI\\zuri\\nasadatabase\\marsimages" + str(img)

            os.rename(path_1,path_2)

            os.startfile(path_2)

            speak(f"This image was captured with : {full_camera_name}")

            speak(f"This image was captured on : {date_of_photo}")

    except:
        speak("There is error!")

def SolarBodies(body):

    url = "https://api.le-systeme-solaire.net/rest/bodies/"

    r = requests.get(url)

    Data = r.json()

    bodies = Data['bodies']

    Number = len(bodies)

    for bodyyy in bodies:
        print(bodyyy['id'],end=',')

    url_2 = f"https://api.le-systeme-solaire.net/rest/bodies/{body}"

    rrr = requests.get(url_2)

    data_2 =rrr.json()

    mass = data_2['mass']['massValue']

    volume = data_2['vol']['volValue']

    density = data_2['density']

    gravity = data_2['gravity']

    escape = data_2['escape']

    speak(f"Number of bodies in solar system : {Number} ." )
    speak(f"Mass of {body} is {mass} .")
    speak(f"gravity of {body} is {gravity} .")
    speak(f"escape velocity of {body} is {escape} .")
    speak(f"Density of {body} is {density} .")



def Eyecontrolled():

  cam = cv2.VideoCapture(0)
  face_mesh = mp.solutions.face_mesh.FaceMesh(refine_landmarks=True)
  screen_w, screen_h = pyautogui.size()
  while True:
    _, frame = cam.read()
    frame = cv2.flip(frame, 1)
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGRA2RGB)
    output = face_mesh.process(rgb_frame)
    landmark_points = output.multi_face_landmarks
    frame_h, frame_w, _ = frame.shape
    if landmark_points:
        landmarks = landmark_points[0].landmark
        for id, landmark in enumerate(landmarks[474:478]):
            x = int(landmark.x * frame_w)
            y = int(landmark.y * frame_h)
            cv2.circle(frame, (x, y), 3, (0, 255, 0))
            if id == 1:
                screen_x = screen_w / frame_w * x
                screen_y = screen_h / frame_h * y
                pyautogui.moveTo(screen_x, screen_y)
        left = [landmarks[145], landmarks[159]]
        for landmark in left:
            x = int(landmark.x * frame_w)
            y = int(landmark.y * frame_h)
            cv2.circle(frame, (x, y), 3, (0, 255, 255))
        if (left[0].y - left[1].y) < 0.009:
            pyautogui.click()
            pyautogui.sleep(1)

    cv2.imshow('Eye controlled mouse', frame)
    cv2.waitKey(1)



def ColorRecongnation():
    cap = cv2.VideoCapture(0)
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1200)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)

    while True:
        _, frame = cap.read()
        hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        height, width, _ = frame.shape

        cx = int(width / 2)
        cy = int(height / 2)

        pixel_center = hsv_frame[cy, cx]
        hue_value = pixel_center[0]

        color = "Undefined"
        if hue_value < 5:
            color = "RED"
        elif hue_value < 22:
            color = "ORANGE"
        elif hue_value < 33:
            color = "YELLOW"
        elif hue_value < 78:
            color = "GREEN"
        elif hue_value < 131:
            color = "BLUE"
        elif hue_value < 170:
            color = "VIOLET"
        else:
            color = "RED"

        pixel_center_bgr = frame[cy, cx]
        b, g, r = int(pixel_center_bgr[0]), int(pixel_center_bgr[1]), int(pixel_center_bgr[2])

        cv2.putText(frame, color, (10, 78), 0, 1, (b, g, r), 2)
        cv2.circle(frame, (cx, cy), 5, (25, 25, 25), 3)

        cv2.imshow("Frame", frame)
        key = cv2.waitKey(1)
        if key == 27:
            break

    cap.release()
    cv2.destroyAllWindows()


#To wish
def wish():
    hour = int(datetime.datetime.now().hour)
    tt = time.strftime("%I:%M %p")

    if hour >= 0 and hour <= 12:
        speak("good morning")
    elif hour > 12 and hour < 18:
        speak("good afternoon")
    else:
        speak("good evening")
    speak("i am  zuri please tell me how may i  help you")


def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('your user', 'youe pass')
    server.sendmail('your email id', to.content)
    server.close()


def news():
    main_url = 'https://newsapi.org/v2/everything?q=tesla&from=2023-06-21&sortBy=publishedAt&apiKey=563aa873b8324abf835a399efd5fc26a'

    main_page = requests.get(main_url).json()
    # print main page
    articles = main_page["articles"]
    # print(articles)
    head = []
    day = ["first", "second", "third", "fourth", "fifth", "sixth", "seventh", "eighth", "nineth", "tenth"]
    for ar in articles:
        head.append(ar["title"])
    for i in range(len(day)):
        speak(f"today's {day[i]} news is: {head[i]}")


def Temp():
    search = "temperature in mumbai"
    url = f"https://www.google.com/search?q={search}"
    r = requests.get(url)
    data = BeautifulSoup(r.text, "html.parser")
    temperature = data.find("div", class_="BNeawe").text
    speak(f"The Temperature Outside is {temperature} celcius")


def Takehindi():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("listening...")
        r.pause_threshold = 1
        audio = r.listen(source, timeout=5, phrase_time_limit=8)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='hi')
        print(f"user said: {query}")

    except Exception as e:
        speak("Say that again please...")
        return "none"
    return query.lower()


def Tran():
    speak("Tell me the line!")
    line = Takehindi()
    traslate = Translator()
    result = traslate.translate(line)
    Text = result.text
    speak(Text)

def DateConverter(Query):

    Date = Query.replace("and ","-")
    Date = Date.replace(" and ","-")
    Date = Date.replace("and ", "-")
    Date = Date.replace("and ", "-")
    Date = Date.replace(" ", " ")

    return str(Date)

def My_Location():

    op = "https://www.google.co.in/maps/place/Vidyavardhini's+College+of+Engineering+and+Technology/@19.3838696,72.8261587,17z/data=!3m1!4b1!4m6!3m5!1s0x3be7aec0a4b41bef:0xbd1a4ca919d6a613!8m2!3d19.3838696!4d72.8287336!16zL20vMGNscjgy?entry=ttu"

    speak("Checking...")

    web.open(op)

    ip_add = requests.get('https://api.ipify.org').text

    url = 'https://get.geojs.io/v1/ip/geo/' + ip_add + '.json'

    geo_q = requests.get(url)

    geo_d = geo_q.json()

    state = geo_d['city']

    country = geo_d['country']

    speak(f"Sir, you are now in {state, country}.")





def Speedtest():
    import speedtest
    speak("checking speed...")
    speed = speedtest.Speedtest()
    downlaoding = speed.download()
    correctDown = int(downlaoding / 800000)
    uploading = speed.upload()
    correctUpload = int(uploading / 800000)

    if "uploading" in query:
        speak(f"The uplaoding  speed is {correctUpload} mbp s")

    elif "downloading" in query:
        speak(f"The Downloading Speed is {correctDown} mbp s")

    else:
        speak(f"The Downlaoding is {correctDown} and the Uploading speed is {correctUpload} mbp s")


def Reader():
    speak("Tell me the name of the book!")

    name = takecommand()

    if "Mechanics" in name:

        os.startfile('file:///C:/Users/91836/Downloads/md3.pdf')
        book = open('file:///C:/Users/91836/Downloads/md3.pdf', 'rb')
        pdfreader = PyPDF2.PdfFileReader(book)
        pages = pdfreader.getNumPages()
        speak(f"Number of pages in this book are {pages}")
        speak("from which page i have to start reading ?")
        numPage = int(input("Enter the page number :"))
        page = pdfreader.getPage(numPage)
        text = page.extractText()
        speak("in which language , i have to read")
        lang = takecommand()

        if 'hindi' in lang:
            trans1 = Translator()
            textHin = trans1.translate(text, 'hi')
            textm = textHin.text
            speech = gTTS(text=textm)
            try:
                speech.save('book.mp3')
                playsound('book.mp3')
            except:
                playsound('book.mp3')

        else:
            speak(text)


def WolfRam(query):
    api_key = "7Y7G42-49XGR2LV73"

    requester = wolframalpha.Client(api_key)

    requested = requester.query(query)

    try:
        Answer = next(requested.results).text

        return Answer

    except:

        speak("No data found")



def Calculator(query):
    Term = str(query)

    Term = Term.replace("zuri", "")
    Term = Term.replace("multiply", "*")
    Term = Term.replace("plus", "+")
    Term = Term.replace("minus", "-")
    Term = Term.replace("into", "*")

    Final = str(Term)

    try:
        result = WolfRam(Final)
        speak(f"{result}")

    except:

        speak("No data found")


def temp(query):
    Term = str(query)

    Term = Term.replace("zuri", "")
    Term = Term.replace("in", "")
    Term = Term.replace("what is the", "")
    Term = Term.replace("temperature", "")

    Temp_query = str(Term)

    if "outside" in Temp_query:

        var1 = "Temperature in mumbai"

        answer = WolfRam(var1)

        speak(f"{var1} is{answer}")

    else:

        var2 = "Temperature in" + Temp_query

        answ = WolfRam(var2)

        speak(f"{var2} is {answ}")


def ChromeAuto(command): #start here (not working)


        query = str(command)

        if 'new tab' in query:

            press_and_release('ctrl + t')

        elif 'close tab' in query:

            press_and_release('ctrl + w')

        elif 'new window' in query:

            press_and_release('ctrl + n')

        elif 'history' in query:

            press_and_release('ctrl + h ')

        elif 'download' in query:

            press_and_release('ctrl + j')

        elif 'bookmark' in query:

            press_and_release('ctrl + d')

        elif 'incognito' in query:

            press_and_release('ctrl + shift + n')

        elif 'switch tab' in query:

            tab = query.replace("switch tab", "")
            Tab = tab.replace("to", "")

            num = Tab

            bb = f'ctrl + {num}'

            press_and_release(bb)

        elif 'open' in query:

            name = query.replace("open", "")

            NameA = str(name)



        if 'youtube' in NameA:
            web.open("https://www.youtube.com/")

        elif 'instagram' in NameA:
            web.open("https://www.instagram.com/")


        else:

                string = "https://www." + NameA + ".com"

                string_2 = string.replace(" ", "")

                web.open(string_2) #to end here (not working)




"""def Task_Gui():

     while True:

         query = takecommand()

         if "hello" in query:

         elif "whatsapp message" in query: <---one error here showing that's why msg is not send on whatsapp.             query = query.replace("zuri", "")
             query = query.replace("send", "")
             query = query.replace("whatsapp message", "")
             query = query.replace("to", "")
             name = query

             if "dinesh" in name:
                 numb = "9321770167"
                 speak(f"what's the message for {name}")
                 mess = takecommand()
                 whatsapp.whatsapp(numb, mess)

         elif "shubham" in name:
             numb = "123456789"
             speak(f"what's the message for {name}")
             mess = takecommand()
             whatsapp.whatsapp(numb, mess)

         elif "now" in name:
             gro = 'https://chat.whatsapp.com/G7WqT2xusUl41hYn6QoPiC'
             speak(f"what's the message for {name}")
             mess = takecommand()
             whatsapp.whatsapp_Grp(gro, mess)"""

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
                    if k == 27:
                        break;
                    cap.release()
                    cv2.destroyWindow()

            elif "temperature in" in query:
                temp(query)



            elif "play music" in query:
                music_dir = "C:\\Users\\91836\\OneDrive\\Documents\\music"
                songs = os.listdir(music_dir)
                os.startfile(os.path.join(music_dir, songs[0]))

            elif "wikipedia" in query:
                speak("searching wikipedia...")
                query = query.replace("wikipedia", "")
                results = wikipedia.summary(query, sentences=2)
                speak("according to wikipedia")
                speak(results)
                print(results)

            elif "address" in query:
                ip = get('https://api.ipify.org').text
                speak(f"your IP address is {ip}")

            elif "what is the" in query:
                WolfRam(query)

            elif "calculate" in query:
                Calculator(query)

            elif 'Chrome' in query:
                ChromeAuto(query)

            elif "open youtube" in query:
                webbrowser.open("www.youtube.com")

            elif "open facebook" in query:
                webbrowser.open("www.facebook.com")

            elif"space news" in query:

                speak("tell me the date for news extracting process")

                Date = takecommand()

                Value = DateConverter(Date)

                NasaNews(Value)









            elif "open instagram" in query:
                webbrowser.open("www.instagram.com")

            elif "open movie" in query:
                webbrowser.open("www.azmovies.com")

            elif "open linkedin" in query:
                webbrowser.open("www.linkedin.com")

            # programming courses
            elif "open coursera " in query:
                webbrowser.open("www.coursera.com")

            # normal languages
            elif "open udemy" in query:
                webbrowser.open("www.udemy.com")

            elif "asa" in query:
                webbrowser.open("https://replit.com/@SiddharthChakr4/Saarthi.com")

            # for github
            elif "369" in query:
                webbrowser.open("www.github.com")


            elif "google" in query:
                speak("sir, what should i search on google")
                danny = takecommand().lower()
                webbrowser.open(f"{danny}")

            elif "send message" in query:
                kit.sendwhatmsg("+919892752329", "this is testing protocol", 2, 25)  # 2,25 msg deilvered in 8 hours

            elif "play song on youtube" in query:
                kit.playonyt("see you again")

            elif "email to dinesh" in query:
                try:
                    speak("what should i say")
                    content = takecommand().lower()
                    to = "type here person email"
                    sendEmail(to, content)
                    speak("Email has been send to dinesh")

                except Exception as e:
                    print(e)
                    speak("sorry sir, i am not able to sent this email to dinesh")

            elif "no thanks" in query:
                speak("thanks for using me sir,have a good day.")
                sys.exit()

            elif "you need a break" in query:
                speak("ok sir , you can call me anytime")
                speak("just say wakeup zuri!")
                break

            # to close any app
            elif "close notepad" in query:
                speak("okay sir,closing notepad")
                os.system("taskkill /f /im notepad.exe")

            elif "close command prompt" in query:
                speak("okay sir,closing command prompt")
                os.system("taskkill /f /im cmd.exe")





            # to set alaram
            elif "alarm" in query:
                speak(": enter the time")
                time = input(": enter the time:")

                while True:
                    Time_Ac = datetime.datetime.now()
                    now = Time_Ac.strftime("%H:%M:%S")

                    if now == time:
                        speak("Time to wake up sir!")
                        playsound('chandra.mp3')
                        speak("alaram closed")
                    elif now > time:
                        break


            # to find a joke
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

            elif "tell me a news" in query:
                speak("please wait sir, fetching the latest news")
                news()


            elif "thank you" in query:
                speak("welcome sir,have good day")

            elif "temperature in mumbai" in query:
                Temp()

            elif "translator " in query:
                Tran()

            elif "downloading speed" in query:
                Speedtest()

            elif "uploading speed" in query:
                Speedtest()

            elif "internet speed" in query:
                Speedtest()

            elif "remember that" in query:
                remeberMsg = query.replace("remember that", "")
                remeberMsg = remeberMsg.replace("zuri", "")
                speak("you tell me to remind you that :" + remeberMsg)
                remeber = open('data.txt', 'w')
                remeber.write(remeberMsg)
                remeber.close()

            elif "what do you remember" in query:
                remeber = open('data.txt', 'r')
                speak("you tell me that" + remeber.read())

            elif "you understand" in query:
                speak("yes sir i understand")

            elif "ok bye" in query:
                speak("bye sir...have a good day")

            elif 'search on youtube' in query:
                Query = query.replace("zuri", "")
                query = Query.replace("zuri", "")
                from whatsapp import YouTubeSearch

                YouTubeSearch(query)


            # check location with the help of ip address
            elif "where i am" in query or "where we are" in query:
                speak("wait sir let me check")
                try:
                    ipAdd = requests.get('https://api.ipify.org').text
                    print(ipAdd)
                    webbrowser.open("https://www.iplocation.net/myip") + ipAdd + '.json'

                    speak(f"sir i am not sure, but i think we are in (city) city of (country) country")
                except Exception as e:
                    speak("Yes sir, i found your location")
                    pass



            elif "zuri who made you" in query:
                speak("i have been made by Dinesh,Apurav and Shubham")

            elif "no I am single" in query:
                speak("Ooo that's so sad to hear...would you like to be my boyfriend?")

            elif "do you have any girlfriend" in query:
                speak("no sir, i don't have any girlfriend...what about you do you have any girlfriend")


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

            elif "how to" in query:
                speak("Getting Data from the internet!!!")
                op = query.replace("zuri", "")
                max_result = 1
                how_to_func = search_wikihow(op, max_result)
                assert len(how_to_func) == 1
                how_to_func[0].print()
                speak(how_to_func[0].summary)

            elif 'mars images' in query:
                MarsImage()

            elif 'solar system' in query:
                speak("Tell me the name of the body")
                bod = takecommand()
                body = bod.replace(" ","")
                body = body.replace(" ","")
                Body = str(body)
                SolarBodies(body=Body)

            elif 'my location' in query:
                My_Location()

            elif 'where is' in query:

                Place = query.replace("Where is", "")
                Place = Place.replace("Zuri", "")
                GoogleMaps(Place)

            elif 'mouse' in query:
                Eyecontrolled()

            elif 'colour recognition' in query:
                ColorRecongnation()

            else:
                from Database.chatbot.chatbot import ChatterBot

                reply = ChatterBot(query)

                speak(reply)

            if 'bye' in query:
                break

            elif 'exit' in query:
                break

            elif 'go' in query:
                break


            elif 'Chatbot' in query:
                from  chatbot import ChatterBot
                ChatterBot(query)













            # speak("sir, do you have any other work")

