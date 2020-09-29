import webbrowser as wb
import speech_recognition as sr
import pyttsx3
import os
print("=============================WELCOME TO MY TOOLS===============================")
print("=============following are some commands which i can run for you======================")
print("                              1.date                           ")
print("                              2.cal                            ")
print("==========================Applications available====================================")
print("                              1.notepad                        ")
print("                              2.paint                          ")
print("===============================================================================")
pyttsx3.speak("Tell me which app or command i can run for you ?")
while True:
    r=sr.Recognizer()
    with sr.Microphone() as source:
        pyttsx3.speak("start speaking...")
        print("start speaking..")
        audio=r.listen(source)
        print("Your requirement is captured.")
    select = r.recognize_google(audio)
    if "date" in select:
       wb.open("http://192.168.43.182/cgi-bin/f.py?c=date")
    elif "cal" in select:
        wb.open("http://192.168.43.182/cgi-bin/f.py?c=cal")
    elif "notepad" in select:
        os.system("notepad")
        pyttsx3.speak("notepad has closed.")
    elif "paint" in select:
        os.system("mspaint")
        pyttsx3.speak("paint has closed.")
    else:
        print("sorry ,I am not getting to you exactly...")