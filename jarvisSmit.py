import sys
import socket
import pyttsx3
import speech_recognition as sr
import datetime
import os
import cv2
import random
import requests, json
from requests import get
import wikipedia
import webbrowser
import pywhatkit as kit
import threading
import smtplib
import pyjokes
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
# import sys, bs4
# import weather1 as wea

# ----------Pre-Establishment----------

mobile1 = 'None'

new_socket = socket.socket()
host_name = socket.gethostname()
s_ip = socket.gethostbyname(host_name)

port = 8080

new_socket.bind((host_name, port))
print("Binding successful!")
print("This is your IP: ", s_ip)

print("Do you want to continue on this device?(press y/n)")
if input() in ['n','N']:
    print("Waiting for Clients to connect...")

    name = 'Server'
    new_socket.listen()
    try:
        new_socket.settimeout(60)
        conn, add = new_socket.accept()
        new_socket.settimeout(None)
        print(add)
        print("Received connection from ", add[0])
        print('Connection Established. Connected From: ', add[0])
        client = (conn.recv(1024)).decode()
        print(client + ' has connected.')
        conn.send(name.encode())
        mobile1 = 1
    except Exception as e:
        print("No client Found. Try Again!")
        sys.exit()

    except ConnectionResetError as cre:
        print("Client Disconnected!!!")
else:
    mobile1 = 0


engine = pyttsx3.init()

voices = engine.getProperty('voices')
# print(voices[0].id)
engine.setProperty('voices', voices[0].id)
engine. setProperty("rate", 165)
chrome_path = '"C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe" %s'

wb = webbrowser.get(chrome_path)

#-----------methods starts-----------

def mobile():
        message = conn.recv(1024)
        message = message.decode()
        return message

# text to speak
def speak(audio):
    print("Jarvis: " + audio)
    engine.say(audio)
    engine.runAndWait()



# voice to text
def takecommand():
    # client_req = mobile_req_func() #msg from mobile client
    # if (client_req):
    #   return client_req
    # else:

        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("listning.....")
            audio = r.listen(source,timeout=10,phrase_time_limit=5)
        try:
            print("Recognising.........")
            query = r.recognize_google(audio,language='en-in')
            print(f' user said: {query}')
        except Exception as e:
            speak("Please say that again sir")
            return "none"
        return query

def wish():
    hour = int(datetime.datetime.now().hour)
    # temp1, wether1 = wea.getweather()
    if hour>=7 and hour<=12:
        speak("good Morning sir")
    elif hour>12 and hour<18:
        speak("Good Afternoon Sir")
    else:
        speak("Good Evening sir")
    # speak(f"today's temperature is {temp1} and the climate will be approx {wether1}")
    speak("jarvis Here, how can i help you")


# contact = {
#     "pratik":"pratik.pawar@gmail.com",
#     "smith":"smit.btsr@gmail.com"
#            }

# def get_email(receiver):
    # if receiver in contact.keys():
    #     return receiver.value()


def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login("pawarbt2009@gmail.com","Pratik@123")
    server.sendmail('pawarbt2009@gmail.com',to,content)
    server.close()

def email_down(subject):
    fromaddr = "pawarbt2009@gmail.com"
    toaddr = "devloperp9@gmail.com"

    msg = MIMEMultipart()
    msg['From'] = fromaddr
    msg['To'] = toaddr
    msg['Subject']= subject
    body = "Body_of_the_mail"
    msg.attach(MIMEText(body, 'plain'))
    path = "C:/Users/Pratik/Downloads"
    list1 = os.listdir(path)
    conn.send(f"{list1}".encode())
    conn.send("Please enter Exact file name from above list: ".encode())
    filename = mobile()
    attachment = open(f"C:/Users/Pratik/Downloads/{filename}", "rb")
    p = MIMEBase('application', 'octet-stream')
    p.set_payload((attachment).read())
    encoders.encode_base64(p)
    p.add_header('Content-Disposition', "attachment; filename= %s" % filename)
    msg.attach(p)
    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.starttls()
    s.login(fromaddr, "Pratik@123")
    text = msg.as_string()
    s.sendmail(fromaddr, toaddr, text)
    s.close()

def email_doc(subject):
    fromaddr = "pawarbt2009@gmail.com"
    toaddr = "devloperp9@gmail.com"

    msg = MIMEMultipart()
    msg['From'] = fromaddr
    msg['To'] = toaddr
    msg['Subject'] = input("please insert the subject: ")
    body = "Body_of_the_mail"
    msg.attach(MIMEText(body, 'plain'))
    path = "C:/Users/Pratik/Downloads"
    list1 = os.listdir(path)
    conn.send(f"{list1}".encode())
    conn.send("Please enter Exact file name from above list: ".encode())
    filename = mobile()
    attachment = open(f"C:/Users/Pratik/Downloads/{filename}", "rb")
    p = MIMEBase('application', 'octet-stream')
    p.set_payload((attachment).read())
    encoders.encode_base64(p)
    p.add_header('Content-Disposition', "attachment; filename= %s" % filename)
    msg.attach(p)
    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.starttls()
    s.login(fromaddr, "Pratik@123")
    text = msg.as_string()
    s.sendmail(fromaddr, toaddr, text)
    s.close()

# ------------Jarvis Functionalities--------

def jarvisfunc():
    while True:
        query = takecommand().lower()
        # logic for tasks

        if "open notepad" in query:
            speak("Opening Notepad...")
            try:
                npath = "C:\\Windows\\system32\\notepad.exe"
                os.startfile(npath)
            except Exception as e:
                speak("Oh! There was some problem in opening Notepad!")
                # print("Please check configurations and try again!!!")
                speak("Oh! There was some problem in opening Notepad!")

        elif "close notepad" in query:
            speak("Notepad Closed.")
            os.system("taskkill /f /im notepad.exe")


        elif "open adobe reader" in query:
            try:
                speak("Opening Adobe reader...")
                apath = "C:\\Program Files\\Adobe\\Acrobat DC\\Acrobat\\Acrobat.exe"
                os.startfile(apath)
            except Exception as e:
                speak("Oh! There was some problem in opening Adobe Reader!")
                # print("Please check configurations and try again!!!")
                speak("Please check configurations and try again!!!")
            


        elif "open command prompt" in query:
            speak("Opening command prompt...")
            os.system("start cmd")


        elif "open camera" in query:
            try:
                speak("Opening Camera...")
                cap = cv2.VideoCapture(0)
                while True:
                    success, img = cap.read()
                    cv2.imshow("Video", img)
                    k = cv2.waitKey(50)
                    if k == 27:
                        cap.release()
                        cv2.destroyAllWindows()
            except Exception as e:
                speak("oh! Something went wrong, please try opening it manually!")
                

        elif "play music" in query:
            try: 
                speak("Playing Music...")
                music_dir = "E:\\Music"
                songs = os.listdir(music_dir)
                rd = random.choice(songs)
                os.startfile(os.path.join(music_dir, rd))
            except Exception as mus:
                speak("Looks like a problem in Music Directory, please check configurations...")    

        # elif "stop music" in query:


        elif "ip address" in query:
            ip = get("https://api.ipify.org").text
            speak(f"your ip address is {ip}")

        elif "temperature" in query:
            speak("current temperature is 24 degree Celsius ")

        elif "thank you" in query:
            speak("It's my pleasure")

        elif "wikipedia" in query:
            try:
                speak("searching wikipedia")
                # print(query)
                query = query.replace("wikipedia","")
                # print(query)
                results = wikipedia.summary(query, sentences=2)
                speak("according to wikipedia")
                # print(results)
                speak(results)
            except Exception as pgerr:
                speak("Looks like there is not much about the topic that i could find")
        
        elif "open youtube" in query:
            speak("Opening Youtube...")
            wb.open('youtubye.com')

            # webbrowser.open("youtube.com")

        elif "open facebook" in query:
            speak("Opening Facebook...")
            wb.open("facebook.com")

        elif "open stackoverflow" in query:
            speak("Opening Stackoverflow...")
            wb.open("stackoverflow.com")

        elif "google" in query:
            speak("sir, what should i search on google")
            cm = takecommand().lower()
            cm = cm.replace("search","")
            cm = cm.replace("about", "")
            speak("I found this on Google")
            url = "https://www.google.com.tr/search?q={}".format(cm)
            wb.open(url)
            

        # elif "whatsapp" in query:
        #     kit.sendwhatmsg("+919825018585","this msg is send by jarvis",2,25)
        #     speak("sorry sir currently i am unable to do so")

        elif "play song on youtube" in query:
            kit.playonyt("Despacito")

        elif "send mail" in query:
            try:
                speak("what should i say in mail")
                content = takecommand().lower()
                # function name for to
                speak("whom to send the mail")
                # receiver = takecommand().lower()
                # to = ""
                # if receiver in contact.keys():
                #     to = contact[receiver].value()
                # else:
                #     speak(f"email of {receiver} was not found.")
                to = "devloperp9@gmail.com"
                sendEmail(to,content)
                print(to)
                print(content)
                speak("Email has been sent sir")

            except Exception as e:
                speak("sorry sir i am unable to send the email currently due to Internet speed")

        elif "no thanks" in query:
            speak("Thanks for using me, See You!")
            sys.exit()

        # elif "set alarm" in query:
        #     nn = int(datetime.datetime.now().hour)
        #     if nn==22:
        #         music_dir = "E:\\Music"
        #         songs = os.listdir(music_dir)
        #         os.startfile(os.path.join(music_dir,songs[0]))


        elif "tell me a joke" in query:
            joke = pyjokes.get_joke()
            speak(joke)

        elif "python code" in query:
            try:
                path = 'C:\\Program Files\\JetBrains\\PyCharm Community Edition 2021.1.1\\bin\\pycharm64.exe'
                os.startfile(path)
            except Exception as e:
                speak('something looks wrong! Please check configurations and try again.')


        else:
            if query == 'none':
                pass
            else:
                speak("I found something related on web.")
                cm = query.replace("jarvis","")
                cm = cm.replace("search", "")
                cm = cm.replace("about", "")
                url = "https://www.google.com.tr/search?q={}".format(cm)
                wb.open(url)
            # results = wikipedia.summary(cm, sentences=3)
            # print(results)
            # speak(results)


        speak("anything else i can do for you?")

def jarvisfuncmobile():
    while True:
        query = mobile()
        # logic for tasks

        if "open notepad" in query:
            try:
                npath = "C:\\Windows\\system32\\notepad.exe"
                os.startfile(npath)
                value = 'Notepad Opened.'
            except Exception as e:
                value = 'Oh! There was some problem in opening Notepad! Oh! There was some problem in opening Notepad!'
            conn.send(value.encode())

        elif "close notepad" in query:
            os.system("taskkill /f /im notepad.exe")
            value = 'Notepad Closed.'
            conn.send(value.encode())


        elif "open adobe reader" in query:
            try:
                apath = "C:\\Program Files\\Adobe\\Acrobat DC\\Acrobat\\Acrobat.exe"
                os.startfile(apath)
                value = 'Adobe Reader Opened.'
            except Exception as e:        
                value = 'Oh! There was some problem in opening Notepad! Oh! There was some problem in opening Notepad!'            
            conn.send(value.encode())


        elif "open command prompt" in query:
            os.system("start cmd")
            value = 'Command Prompt opened.'
            conn.send(value.encode())


        elif "open camera" in query:
            try:
                cap = cv2.VideoCapture(0)
                while True:
                    success, img = cap.read()
                    cv2.imshow("Video", img)
                    k = cv2.waitKey(50)
                    if k == 27:
                        cap.release()
                        cv2.destroyAllWindows()
                        value = 'Camera Opened.'
            except Exception as e:
                value = "oh! Something went wrong, please try opening it manually!"
            conn.send(value.encode())

        elif "play music" in query:
            try:
                music_dir = "E:\\Music"
                songs = os.listdir(music_dir)
                rd = random.choice(songs)
                os.startfile(os.path.join(music_dir, rd))
                value = 'task is completed sir'
            except Exception as e:
                value = "Looks like a problem in Music Directory, please check configurations..."
            conn.send(value.encode())


        elif "ip address" in query:
            ip = get("https://api.ipify.org").text
            speak(f"your ip address is {ip}")
            value = 'task is completed sir'
            conn.send(value.encode())


        elif "wikipedia" in query:
            try:
                speak("searching wikipedia")
                # print(query)
                query = query.replace("wikipedia","")
                # print(query)
                results = wikipedia.summary(query, sentences=2)
                results1 = "according to wikipedia"
                results = results1 + results
                # print(results)
                # speak(results)
                conn.send(results.encode())
            except Exception as e:
                emsg = "Looks like there is not much about the topic that i could find"
                conn.send(emsg.encode())

        elif "open youtube" in query:
            wb.open('youtube.com')
            value = 'Opened Youtube.'
            conn.send(value.encode())

            # webbrowser.open("youtube.com")

        elif "open facebook" in query:
            wb.open("facebook.com")
            value = 'opened Facebook.'
            conn.send(value.encode())

        elif "open stackoverflow" in query:
            wb.open("stackoverflow.com")
            value = 'Opened stackoverflow.'
            conn.send(value.encode())

        elif "google" in query:
            val = "sir, what should i search on google"
            conn.send(val.encode())
            cm = mobile().lower()
            cm = cm.replace("search","")
            # cm = cm.replace("about", "")
            value = 'I found this on Google...'
            conn.send(value.encode())
            url = "https://www.google.com.tr/search?q={}".format(cm)
            wb.open(url)

        # elif "whatsapp" in query:
        #     kit.sendwhatmsg("+919825018585","this msg is send by jarvis",2,25)
        #     speak("sorry sir currently i am unable to do so")

        elif"play songs on youtube" in query:
            kit.playonyt("Despacito")
            value = 'Playing Song...'
            conn.send(value.encode())

        # elif "send mail" in query:
        #     try:
        #         value = "what should i say in mail?"
        #         conn.send(value.encode())
        #         content = input().lower()
        #         # function name for to
        #         value = "whom to send the mail"
        #         conn.send(value.encode())
        #         receiver = input().lower()
        #         # to = ""
        #         # if receiver in contact.keys():
        #         #     to = contact[receiver].value()
        #         # else:
        #         #     speak(f"email of {receiver} was not found.")
        #         # to = "devloperp9@gmail.com"
        #         sendEmail(receiver,content)
        #         # print(to)
        #         # print(content)
        #         value = "Email has been sent sir!"
        #         conn.send(value.encode())
        #
        #     except Exception as e:
        #         value = "sorry sir i am unable to send the email currently due to Internet speed"
        #         conn.send(value.encode())

        elif "send mail" in query:
            try:
                conn.send("Please enter your subject: ".encode())
                subject = mobile().lower()
                conn.send("sir is file in download folder (y/n)".encode())
                x = mobile().lower()
                print(x)
                if(x=='y'):
                    email_down(subject)
                else:
                    pass
                conn.send("sir is file in document folder (y/n)".encode())
                z = mobile().lower()
                print(z)
                if(z == 'y'):
                    email_doc(subject)
                else:
                    pass
            except Exception as e:
                print(e)
                conn.send("sorry sir i am unable to send the email currently due to Internet speed".encode())


        elif "no thanks" in query:
            value = "Thanks for using me, See You!"
            conn.send(value.encode())
            sys.exit()

        # elif "set alarm" in query:
        #     nn = int(datetime.datetime.now().hour)
        #     if nn==22:
        #         music_dir = "E:\\Music"
        #         songs = os.listdir(music_dir)
        #         os.startfile(os.path.join(music_dir,songs[0]))


        elif "tell me a joke" in query:
            joke = pyjokes.get_joke()
            speak(joke)
            value = "Joke Over!"
            conn.send(value.encode())


        else:
            if query == 'none':
                pass
            else:
                speak("I found something related on web.")
                cm = query.replace("jarvis","")
                cm = cm.replace("search", "")
                cm = cm.replace("about", "")
                url = "https://www.google.com.tr/search?q={}".format(cm)
                value = "Searching..."
                conn.send(value.encode())
                wb.open(url)
                value = "Done!"
                conn.send(value.encode())
            # results = wikipedia.summary(cm, sentences=3)
            # print(results)
            # speak(results)

# ----------Main Method--------

if __name__ == "__main__":
    wish()
    if(mobile1 == 0):
        jarvisfunc()
    else:
        jarvisfuncmobile()