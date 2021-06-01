#!/usr/bin/env python3 

# -*- coding: utf-8 -*- 

from reportlab.pdfgen import canvas 
import datetime 
import tkinter 
from gtts import gTTS 
import os 
import speech_recognition as sr 
import time 
import pygame 

top = tkinter.Tk() 
r = sr.Recognizer() 
now = datetime.datetime.now() 
c=canvas.Canvas("Z_Output.pdf") 
time_now=now.strftime("%H:%M")
print(time_now)
def button_click(): 
	#for playing welcome
   	
	if time_now>'12':
		pygame.init() 
		pygame.mixer.music.load("afternoon.mp3") 
		pygame.mixer.music.play()
		time.sleep(1.5)
		dep_with()
	else:
		pygame.init() 
		pygame.mixer.music.load("morning.mp3") 
		pygame.mixer.music.play() 
		time.sleep(1.5)
		dep_with()
	


def dep_with(): 
    pygame.init() 
    pygame.mixer.music.load("dep_with.mp3") 
    pygame.mixer.music.play() 
    time.sleep(2) 

    #deposit or withdraw? 
    with sr.Microphone() as source: 
        print("Say deposit or withdrawl!") 
        audio = r.listen(source) 
        dw = r.recognize_google(audio) 
        #st1=list(amt) 
        print(dw)
        if dw=="deposit":
            c.drawString(230,600,"DEPOSIT FORM") 
            c.drawString(330,200,"Signature____________________") 
            pygame.init() 
            pygame.mixer.music.load("ask_acc.mp3") 
            pygame.mixer.music.play() 
            time.sleep(2) 
            read_acc() 
        elif dw=="withdrawal": 
            c.drawString(230,600,"WITHDRAWAL FORM")
            c.drawString(330,200,"Signature____________________")  
            pygame.init() 
            pygame.mixer.music.load("ask_acc.mp3") 
            pygame.mixer.music.play() 
            time.sleep(3) 
            read_acc()
        else: 
            pygame.init() 
            pygame.mixer.music.load("repeat.mp3") 
            pygame.mixer.music.play() 
            time.sleep(5) 
            button_click() 
        pygame.init() 
        pygame.mixer.music.load("wait.mp3") 
        pygame.mixer.music.play() 
        time.sleep(5)
        pygame.init() 
        pygame.mixer.music.load("thanku.mp3") 
        pygame.mixer.music.play() 

             

def read_acc():   #to read input 
   with sr.Microphone() as source: 
       print("Say account number!") 
       audio = r.listen(source) 
       global st 
       st = r.recognize_google(audio)
       st1=st 
       st=st1.replace(" ","")
       print(st) 
       s=list(st) 
       l=len(s) 

       #print(s) 
       p =','.join(s)
       

       #print(p) 
       tts = gTTS(text = p, lang='en', slow= True) 
       tts.save("acc_sav.mp3") 
       os.system("acc_sav.mp3")

       #for checking size of account number 
   while l != 5 or st.isdigit() == False: 
           pygame.init() 
           pygame.mixer.music.load("invalid_acc.mp3") 
           pygame.mixer.music.play() 
           time.sleep(5) 
           print ("Invalid, Try agin") 

           #to read input 
           with sr.Microphone() as source: 
               audio = r.listen(source) 
               st = r.recognize_google(audio) 
               s=list(st) 
               l=len(s) 
               print(st) 
               p =','.join(s) 

               #print(p) 
               tts = gTTS(text = p, lang='en', slow= True) 
               tts.save("acc_sav.mp3") 
               os.system("acc_sav.mp3") 
   verification("acc_ver.mp3","acc_sav.mp3","provide_valid_acc.mp3") 

        

         

def verification(ver,sav,valid):       

       #for asking verification 
       pygame.init() 
       pygame.mixer.music.load(ver) 
       pygame.mixer.music.play() 
       time.sleep(0) #While valid Time

       #for playing the acc nmbr 
       pygame.init() 
       pygame.mixer.music.load(sav) 
       pygame.mixer.music.play() 
       time.sleep(5) 

        

       #asking yes or no 
       pygame.init() 
       pygame.mixer.music.load("acc_yn.mp3") 
       pygame.mixer.music.play() 
       time.sleep(5) 
       with sr.Microphone() as source: 
           print("Say Yes Or No!!") 
           audio = r.listen(source) 
           yn = r.recognize_google(audio) 
           print(yn) 

       if ver == "acc_ver.mp3": 
           if yn=="yes": 
               read_amt()
           else: 
               pygame.init() 
               pygame.mixer.music.load(valid) 
               pygame.mixer.music.play() 
               time.sleep(5) 
               read_acc() 
       else:  
           if yn == "yes": 
               #c.drawImage('../SBI-logo.png', 100, 770, mask='auto', width=50, height=50) 
               c.drawString(350,700,"DATE & TIME:") 
               c.drawString(440,700,now.strftime("%d-%m-%Y %H:%M")) 

               #ACCOUNT DETAILS 

               c.drawString(50,500,"ACCOUNT NUMBER:") 
               c.drawString(180,490,"_____________________________________________________") 
               c.drawString(190,500,st) 

               c.drawString(110,400," AMOUNT:") 
               c.drawString(190,390,"_____________________________________________________") 
               c.drawString(200,400,amt)

               c.setFont("Helvetica", 30) 
               c.drawString(160,780,"STATE BANK OF INDIA")  
               c.setFont('Helvetica-Bold', 20) 
               c.save() 
           else: 
               read_amt() 

#asking for amount            
def read_amt(): 
           global amt 
           #PDF 
           #HEADING 
           pygame.init() 
           pygame.mixer.music.load("provide_amt.mp3") 
           pygame.mixer.music.play() 
           time.sleep(3) 
           #to read amount 
           with sr.Microphone() as source: 
               print("Say Amout!") 
               audio = r.listen(source) 
               amt = r.recognize_google(audio) 
               print(amt) 

               #storing the amount 
               tts = gTTS(text=amt, lang='en', slow= True) 
               tts.save("amt.mp3") 
               os.system("amt.mp3") 

               #checking whther digit or not 
               while amt.isdigit() == False: 
                   pygame.init() 
                   pygame.mixer.music.load("invalid_amt.mp3") 
                   pygame.mixer.music.play() 
                   time.sleep(2) 
                   print ("Say amount") 

                    #to read input 
                   with sr.Microphone() as source:
                       audio = r.listen(source) 
                       amt = r.recognize_google(audio) 
                       print(amt) 
                       tts = gTTS(text = amt, lang='en', slow= True) 
                       tts.save("amt.mp3") 
                       os.system("amt.mp3") 
               verification("amt_ver.mp3","amt.mp3","provide_valid_amt.mp3") 
                
top.title('GIF')
top.geometry("858x480+360+175")
bg = tkinter.PhotoImage(file = "F:/CdacProject/BankProject/imageone.png")
label = tkinter.Label(top, image = bg)
label.pack()
B = tkinter.Button(top, text ="HELP!", command = button_click, font=("Helvetica-Bold", 20), cursor="hand2")
B.place(x=380, y=360)
 
top.mainloop()