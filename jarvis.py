import pyttsx3 #pip install pyttsx3
import speech_recognition as sr #pip install speechRecognition
import datetime
import time
import wikipedia #pip install wikipedia
from PIL import Image, ImageGrab
from covid import Covid
import webbrowser
import keyboard
import os
import smtplib
from pytube import YouTube
import random
import pyjokes
import akinator
import pyautogui

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        strdate1 = datetime.date.today()
        strTime1 = datetime.datetime.now().strftime("%H:%M:%S")
        speak("Good Morning Sir! I am Jarvis your personal assistant ")
        speak(f"today is {strdate1}")
        speak(f"and, time is{strTime1}")

    elif hour>=12 and hour<18:
        speak("Good AfternoonSir")   

    else:
        speak("Good EveningSir")  

    speak("how can I help you")

def Akinator():
    aki = akinator.Akinator()
    q = aki.start_game()
    while aki.progression <= 80:
        a = input(q +"\n\t")
        if a == 'b':
            try:
                q = aki.back()
            except akinator.CantGoBackAnyFurhter:
                pass
        else:
            q = aki.answer(a)
    aki.win()
    correct = input(f"Its {aki.first_guess['name']} ({aki.first_guess['description']})! Was i correct?\n{aki.first_guess['absolute_picture_path']}\n\t")
    if correct.lower() == 'yes' or correct.lower() == 'y':
        print("yes i got it\n")
    else:
        print("ohh just missed\n")       

def takeCommand():
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise
        print("Listening...")
        
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)    
        print("Say that again please...")  
        return "None"
    return query

def covid19():
    speak('here is the information, about covid 19')
    covid = Covid()
# printing data for the world
    print("Total active cases in world:", covid.get_total_active_cases())
    print("Total recovered cases in world:", covid.get_total_recovered())
    print("Total deaths in world:", covid.get_total_deaths())

    speak('here is the information, about covid19 in india.')
# getting data according to country name
# data will be stored as a dictionary
    cases = covid.get_status_by_country_name("india")
# printing country's data using for loop
    for x in cases:
        print(x, ":", cases[x])

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('your mail id', 'your password')
    server.sendmail('your mail id', to, content)
    server.close()

if __name__ == "__main__":
    wishMe()
    while True:
    # if 1:
        query = takeCommand().lower()

        # Logic for executing tasks based on query
        if 'wikipedia' in query:
            try:
                speak('Searching Wikipedia...')
                query = query.replace("wikipedia", "")
                results = wikipedia.summary(query, sentences=2)
                speak("According to Wikipedia")
                print(results)
                speak(results)
            except Exception as b:
                speak("sorry Sir, I can't found it!")

        if 'download' in query:
            # asking user to enter link
            speak("Ok, please enter the link of the video")
            link = input("Enter the link: ")
            print("Downloding...")
            YouTube(link).streams.first().download()
            print("Video downloaded successfully")

        #keyboard modual 
        elif 'team' in query:
            speak("ok, opening teams")
            keyboard.press_and_release('ctrl + alt + t')

        elif 'close' in query:
            speak("ok")
            keyboard.press_and_release('alt + F4')

        elif 'enter' in query:
            keyboard.press_and_release('enter')

        elif 'incognito' in query:
            speak("ok")
            webbrowser.open("https://www.google.com/")
            time.sleep(3)
            keyboard.press_and_release('ctrl + shift + n')

        elif 'pause' in query:
            speak("ok")
            keyboard.press_and_release('space')

        elif 'type' in query:
            speak("what should I type sir?")
            try:
                lol = takeCommand()
                speak("ok")
                keyboard.write(lol)
            except Exception as f:
                speak("sorry sir, I can't recognise it!")

        elif 'open youtube music' in query:
            speak("ok, opening youtube music"),webbrowser.open('https://www.music.youtube.com/')

        elif 'open youtube' in query:
            speak("ok, opening youtube"),webbrowser.open("https://www.youtube.com/")

        elif 'google' in query:
            speak("opening google"),webbrowser.open("https://www.google.com/")

        elif 'isro' in query:
            speak("ok, here it is"),webbrowser.open("https://www.isro.gov.in/")

        elif 'facebook' in query:
            speak("ok, opening facebook"),webbrowser.open("https://www.facebook.com/")

        elif 'livejournal' in query:
            speak("ok, opening livejournal"),webbrowser.open("https://www.livejournal.com/")

        elif 'classroom' in query:
            speak("ok, opening google classroom"), webbrowser.open("http://classroom.google.com/")

        elif 'gmail' in query:
            speak("ok, opening gmail"),webbrowser.open("https://mail.google.com/mail/u/0/#inbox") 

        elif 'instagram' in query:
            speak("ok, opening instagram"),webbrowser.open("https://www.instagram.com/")

        elif 'flip a coin' in query:
            speak("OK"),webbrowser.open("https://www.google.com/search?sxsrf=ALeKk01MnPEhwuvmwfrY_2FMjPiWykcM5A%3A1603858975577&source=hp&ei=H_KYX_uYIZOfmges56rICg&q=flip+a+coin&oq=flip+&gs_lcp=CgZwc3ktYWIQAxgAMgcIIxDJAxAnMgQIIxAnMgQIABBDMgQIABBDMgUIABCxAzIHCAAQsQMQCjIFCAAQsQMyAggAMgUIABCxAzIFCAAQsQM6CAgAELEDEIMBOgIILjoKCC4QsQMQgwEQClCGMliyN2C6PmgAcAB4AIABgAGIAd8EkgEDMC41mAEAoAEBqgEHZ3dzLXdpeg&sclient=psy-ab")

        elif 'satellite' in query:
            speak("ok"),webbrowser.open('https://maps.esri.com/rc/sat2/index.html')

        elif 'radar' in query:
            speak("ok sir"),webbrowser.open("https://www.flightradar24.com/28.59,77.38/13")

        elif 'whatsapp' in query:
            speak("opening whatshapp"),webbrowser.open("https://web.whatsapp.com/")

        elif 'play funny song' in query:
            speak("ok, I hope you will enjoy this song"),webbrowser.open("https://www.youtube.com/watch?v=Ct6BUPvE2sM")

        elif 'play motivational song' in query:
            speak("ok, playing Jeete chal song by Neerja Bhanot"),webbrowser.open("https://www.youtube.com/watch?v=Jlj_VvjwhFg")

        elif 'translator' in query:
            speak("ok, opening google translator"),webbrowser.open("https://translate.google.co.in/")

        elif 'news' in query:
            speak("Ok, here is your today's news"),webbrowser.open("https://news.google.com/topstories?tab=rn&hl=en-IN&gl=IN&ceid=IN:en")

        elif 'map' in query:
            speak("Ok, opening Google Maps"),webbrowser.open("https://maps.google.com/")

        elif 'movie' in query:
            speak("ok, playing Network Solution on amazon prime"),webbrowser.open("https://www.primevideo.com/detail/0GUQ6R689SN81SSJYLIRAFLD5T/ref=atv_hm_hom_c_8pZiqd_2_1")

        elif 'hungry' in query:
            speak("Ok, I found some restaurants nearby us"),webbrowser.open("https://www.google.com/search?#q=restaurants near by me")

        elif 'weather' in query:
            speak("Ok"),webbrowser.open("https://www.google.com/search?q=weather&rlz=1C1EJFC_enIN915IN915&oq=we&aqs=chrome.3.69i60j69i59l2j0i67i131i433j69i60l4.4068j0j7&sourceid=chrome&ie=UTF-8")
            
        elif 'youtube' in query:
            query = query.replace("youtube","")
            webbrowser.open('https://www.youtube.com/results?search_query='+query)

        elif 'direction' in query:
            speak("from  where  to  where?")
            nav = takeCommand()
            queryl = nav.replace("to","/")
            speak("ok, here it is")
            webbrowser.open('https://www.google.com/maps/dir/'+queryl)

        elif 'search' in query:
            speak("ok, here it is")
            query2 = query.replace("search","")
            webbrowser.open('https://www.google.com/search?q='+query2)


        elif 'i am bored' in query:
            speak("ohh, don't worry"),speak("Do you want to play akinator")
            x = takeCommand()
            if 'yes' in x:
                print("😉")
                speak("Got it!  Let's play Akinator")
                Akinator()
            else:
                speak("Can I play song?")
                x1 = takeCommand()
                if 'yes' in x1:
                    print("😉")
                    speak("Got it!")
                    webbrowser.open('https://www.youtube.com/watch?v=gBq9Zcs_5D8')
                else:
                    speak("So what can I do for you?")


        elif 'covid' in query:
            covid19()

        elif 'volume up' in query:
            pyautogui.press('volumeup')
            speak('okay!')

        elif 'volume down' in query:
            pyautogui.press('volumedown')
            speak('okay!')

        elif 'mute' in query:
            pyautogui.press('volumemute')

        elif 'shut' in query:
            speak('ok, shuting down the computer, goodbye and have a nice day!')
            os.system('shutdown /s /t 1')

        elif 'restart' in query:
            speak('ok, restarting the computer!')
            os.system('shutdown /r /t 1')

        elif 'set timer' in query:
            try:
                speak("ok, for how many seconds?")
                timer = int(takeCommand())
                speak(f"ok timer is set for{timer}seconds")
                time.sleep(timer)
                speak("time over, time over, time over")
            except Exception as l:
                speak("sorry! I can't recognise it")

        elif 'time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            print(f"The Time is {strTime}")    
            speak(f"Sir, the time is {strTime}")

        elif 'joke' in query:
            jokes = pyjokes.get_joke
            speak('ok, Here it is.....')
            print(jokes)
            speak(jokes)

        elif 'akinator' in query:
            speak("ok, let's play akinator")
            Akinator()

        elif 'date' in query:
            strdate = datetime.date.today()
            speak(f"Sir, today's date is {strdate}")
            print("Today's date is", strdate)

        elif 'screenshot' in query:
            speak("ok sir")
            def takeScreenshot():
                image = ImageGrab.grab()
                image.show()
            if __name__ == "__main__":
                takeScreenshot()

        elif 'mail' in query:
            try:
                speak("ok, please write email id to whom you want to send")
                to1 = input("write email id here =  ")
                speak("What should I say?")
                content1 = takeCommand()  
                sendEmail(to1, content1)
                speak("Email has been sent!")
            except Exception as e:
                print("Opps! :(")
                speak("Opps! Sorry sir, I am not able to send this email")
                print("Do you want see what error caused during sending the mail\nYes or No")
                speak("Do you want see what error caused during sending the mail")
                while True:
                    fs = takeCommand()
                    if 'yes' in fs:
                        print(e)
                        speak("ok, here it is! ")
                        break
                    elif 'no' in fs:
                        speak("Ok!")
                        break
                    else:
                        speak("sorry I can't recognise it, please speak it again")

        elif 'set alarm' in query:
            speak("ok, at what hour")
            alarmHour1 = int(takeCommand())
            speak("at what minute")
            alarmMinute1 = int(takeCommand())
            speak("am or pm")
            amPm1 = str(input("write here = "))

            if(amPm1 == "pm"):
                alarmHour1 = alarmHour1 + 12

            while(1 == 1):
                if(alarmHour1 == datetime.datetime.now().hour and
                   alarmMinute1 == datetime.datetime.now().minute):
                   speak("wake up, wake up, wake up")
                   break

        elif 'instant kill' in query:
            speak("activating instant kill")
            d1 = takeCommand()
            if 'deactivate' in d1:
                speak("instant kill deactivated")
        
        elif 'hello' in query: 
            speak("hello sir, how are you")

        elif 'hey' in query:
            speak("hello sir!")

        elif 'hai' in query:
            print("👋 Hi")
            speak("Hi sir")

        elif 'how are you' in query:
            speak("I am always fine sir")

        elif 'kill humans' in query:
            speak("ok, I will kill humans")

        elif 'sleep' in query:
            print("🥱")
            speak("ok, I am going to take rest for 5 minutes!")
            print("😴")
            time.sleep(300)
            print("🤗")
            speak("ok I wake up, Now I am feeling better")
            speak("Please tellme howcan I help you?")

        elif 'fine' in query:
            speak("ooh, that's great!")

        elif 'i am very ' in query:
            print("😃")
            speak("that's great!, today I am also very happy! ")

        elif 'happy' in query:
            print("🤗🤩")
            speak("Same to you sir!") 

        elif 'great' in query:
            print("😉")
            speak("Yeah, I know, that I am great!")

        elif 'nothing' in query:
            speak("Ok Sir")

        elif "it's ok" in query:
            speak("Thank you Sir, you are Really a great man")

        elif 'sorry' in query:
            print("👍😉")
            speak("it's ok!")

        elif 'who are you' in query:
            print("😘")
            speak("I am jarvis!, an artificial intelligence, or your personal assistant")

        elif 'what can you do' in query:
            speak("I can do many things like, I can send emails, play music, set alarms, open apps, entertain you and, many more things")
            speak("what can I do for you?")


        elif 'stop' in query:
            speak("ok sir, good bye and have a nice day")
            break

        elif 'bye' in query:
            hourzz = int(datetime.datetime.now().hour)
            print("goodbye 😊👋")
            if hourzz>=21 and hourzz<3:
                speak("good bye sir, and goodnight or sweet dreams")
            elif hourzz>=3 and hourzz<19:
                speak("good bye sir, and have a nice day")
            else:
                speak("good bye sir!")
            break


        elif 'well done' in query:
            speak("thank you sir")

        elif 'good'in query:
            speak("thank you sir")

        elif 'thank you' in query:
            speak("ooh, most welcome sir")

        elif 'what is my name' in query:
            speak("your name is Aaryan Kumar Singh")

        elif 'fantastic' in query:
            speak("Ohh, thank you sir ")

        elif 'excellent' in query:
            speak("Thank you Sir")

        elif 'father' in query:
            speak("I have no father, because I am a machine not a human!")


        elif 'what is your name' in query:
            speak("My name is jarvis and I am an artifitial intelligence or your persnol assistant")

        elif 'jarvis' in query:
            speak("yes sir")


