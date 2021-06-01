import speech_recognition as sr
import os
import pygame

r = sr.Recognizer()
with sr.Microphone() as source: 
        print("Say something!") 
        audio = r.listen(source) 
        dw = r.recognize_google(audio) 
        #st1=list(amt) 
        print(dw+"hi")
