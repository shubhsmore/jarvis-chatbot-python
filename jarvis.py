import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import smtplib

engine = pyttsx3.init('sapi5') #microsoft speech api

voices = engine.getProperty('voices')

engine.setProperty('voices', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak('good morning')
    elif hour>=12 and hour<18:
        speak('good afternoon')
    else:
        speak('good evening')
    speak("I'm jarvis sir, please tell me how can i help you?")

def takeCommand():
    #it takes microphone input from the user and return string output
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening..')
        r.pause_threshold = 1 #seconds of non speaking audio before a phrase is considered complete
        audio = r.listen(source)

    try:
        print('Recognising')
        query=r.recognize_google(audio)
        print("You said:", query)
    except Exception as e:
        print(e) #cancel if you dont want to print exception
        print('Say that again please')
        return 'None'

    return query
def sendEmail(to,content):
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.ehlo()
    server.starttls()
    server.login('#youremailid', '#yourpassword')
    server.sendmail('#youremailid', to, content)
    server.close()

def greeting():
    print('Hi i am Jarvis, I am robot, ask me anything i will answer you')
    speak('Hi i am Jarvis, I am robot, ask me anything i will answer you')

if __name__ == "__main__":
    wishme()
    print('Say Bye to exit chatbot')
    while True:
        query = takeCommand().lower()
        # logic for executing task based on query


        if 'wikipedia' in query:
            speak('searching wikipedia..')
            query= query.replace('wikipedia',"")
            result= wikipedia.summary(query, sentences=1)
            speak('According to wikipedia')
            print(result)
            speak(result)

        elif 'open youtube' in query:
            webbrowser.open('youtube.com')

        elif 'open google' in query:
            webbrowser.open('google.com')

        elif 'open facebook' in query:
            webbrowser.open('facebook.com')

        elif 'play music' in query:
            music_dir = "C:\\Users\\shbhs\\Music"
            songs= os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[0]))

        elif 'time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f'sir current time is {strTime}')
            print(strTime)

        elif 'open spyder' in query:
            codepath1 = ""
            os.startfile(codepath)

        elif ('open jupiter' in query) or ('open jupyter' in query):
            codepath2 = ""
            os.startfile(codepath2)

        elif "send email" in query:
            try:
                speak('who should i mail?')
                #here i take written input
                to = input("")
                speak('what should i mail?')
                content = takeCommand()
                sendEmail(to,content)
                speak('Email has been sent')
            except Exception as e:
                print(e)
                speak('Sorry email address not found')

        elif "search" in query:
            q=query.split()[1:]
            speak('searching {}'.format(q))
            search = 'https://google.co.in/search?q={}'.format(q)
            webbrowser.open(search)

        elif 'bye' in query:
            speak('good bye, see you again')
            break
