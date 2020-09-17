# -*- coding: utf-8 -*-
"""
Created on Wed Sep  9 19:07:28 2020

@author: Gurkirat
"""

import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import smtplib
import os, random
import webbrowser as wb
import pyautogui
import psutil
import pyjokes
import wolframalpha
from fpdf import FPDF

app_id = "4REUV2-EYRHP2KWLV"

def pdf():
    pdf=FPDF()
    pdf.add_page()
    pdf.set_font("Arial",size=12)
    pdf.cell(200,10,txt=takeCommand(),ln=1,align="C")
    pdf.output("1.pdf")
    
def wolframThisShit(search):
#	app_id = ""   #Put wolfram API here
	client = wolframalpha.Client(app_id)
	res = client.query(search)
	answer = next(res.results).text
	return answer

engine=pyttsx3.init()

def speak(audio):
    voices = engine.getProperty('voices')
    engine.setProperty('voice',voices[1].id)
    engine.say(audio)
    engine.runAndWait()
    
def time():
    Time = datetime.datetime.now().strftime("%I:%M:%S")
    speak("The current time is")
    speak(Time)
    
def date():
    year = int(datetime.datetime.now().year)
    month = int(datetime.datetime.now().month)
    date = int(datetime.datetime.now().day)
    speak("The Current date is")
    speak(date)
    speak(month)
    speak(year)
    
def wishme():
    speak("Welcome back Sir!")
    date()
    time()
    hour = datetime.datetime.now().hour
    if hour >= 4 and hour<12:
        speak("Good Morning Sir!")
    elif hour >=12 and hour<16:
        speak("Good afternoon Sir!")
    elif hour >= 16 and hour<21:
        speak("Good Evening Sir!")
    else:
        speak("Good Night Sir!")
    speak("Assistant at your service. How can I help you?")
    
def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshhold = 1
        r.adjust_for_ambient_noise(source, duration=1)
        audio = r.listen(source)
        
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(query)
        
    except Exception as e:
        print(e)
        speak("Please repeat again!")
        return "None"
        
    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('email@gmail.com','password')
    server.sendmail('email@gmail.com',to,content)
    server.close()
    
def screenshot():
    img = pyautogui.screenshot()
    img.save("C:\\Users\\Gurkirat\\Desktop\\New folder\\ss.png")
    
def cpu():
    usage = str(psutil.cpu_percent())
    speak('CPU is at'+usage)
    battery = psutil.sensors_battery()
    speak('Battery percentage is'+str(battery.percent))
    
def jokes():
    print(pyjokes.get_joke())
    speak(pyjokes.get_joke())
    
def fixText(text):
    this = ' '.join(str(e) for e in text)
    return this

def getGreeting():
	greetings = ["hello", "how can i help you", "how are you today", "what do you need assistance with", "how may i assist you", "did you need something", "hi sir how can i help", "ready to help"]
	return random.choice(greetings)


    
if __name__ == "__main__":
    wishme()
    while True:
        query = takeCommand().lower()
        if  'time' in query:
            time()
        elif 'date' in query:
            date()
        elif 'wikipedia' in query:
            speak("Searching...")
            query = query.replace("wikipedia","")
            result = wikipedia.summary(query, sentences=2)
            print(result)
            speak(result)
            
        elif 'send email' in query:
            try:
                speak("What is your message Sir?")
                content = takeCommand()
                to = 'gurkiratshere@gmail.com'
                sendEmail(to,content)
                speak("Email suceessfully sent Sir!")
            except Exception as e:
                print(e)
                speak("Unable to send Email")
                
                
        elif 'search in chrome' in query:
            speak("what should I search?")
            chromepath = "C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s"
            search = takeCommand().lower()
            wb.get(chromepath).open_new_tab(search+'.com')
            
        elif 'log out' in query:
            os.system("shutdown -l")
            
        elif 'shutdown' in query:
            os.system("shutdown /s /t l")
            
        elif 'restart' in query:
            os.system("shutdown /r /t l")
         
        elif 'play songs' in query:
            songs_dir = 'E:\\music\\G.O.A.T'
            songs = os.listdir(songs_dir)
            os.startfile(os.path.join(songs_dir, songs[0]))
            
        elif 'remember that' in query:
            speak("what should I remember?")
            data = takeCommand()
            speak("you said me to remember that"+data)
            remember = open('data.txt','w')
            remember.write(data)
            remember.close()
            
        elif 'do you know anything' in query:
            remember = open('data.txt','r')
            speak("you said me to remember that"+remember.read())
            
        elif 'screenshot' in query:
            screenshot()
            speak("Done!")
            
        elif 'cpu' in query:
            cpu()
            
        elif 'joke' in query:
            jokes()
            
        elif 'flip a coin' in query:
            ans = wolframThisShit("flip a coin")
            speak(ans)
            
        elif 'pdf' in query:
            pdf()
            
        elif 'offline' in query:
            quit()
            
        elif 'talk' in query:
            speak(getGreeting())
        
        elif 'what' in query:
                    
            ans = wolframThisShit(query)
            speak(ans)
            
