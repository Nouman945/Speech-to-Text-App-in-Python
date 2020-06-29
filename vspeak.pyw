from tkinter import *
from tkinter import ttk
import speech_recognition as sr
from pygame import mixer
import pyperclip
import threading


root = Tk()                              
root.title('Voice Input')
root.iconbitmap('mic.ico')
style = ttk.Style()
style.theme_use('winnative')

# The image that is used for the speak button

photo = PhotoImage(file='microphone.png').subsample(15,15)

# Creating a guiding 'label' widget

label1 = ttk.Label(root, text="Speak -> Paste (or CTRL+V)", font='Courier 11 bold')     
label1.grid(row=0, column=1)                


def buttonClick():


    mixer.init()
    mixer.music.load('chime1.mp3')
    mixer.music.play()


    r = sr.Recognizer()                                         
    r.pause_threshold = 0.7                                     
    r.energy_threshold = 400
    
    with sr.Microphone() as source:
        
        try:
            
            audio = r.listen(source, timeout=5)


            message = str(r.recognize_google(audio, key='your_google_api_key')) 


            mixer.music.load('chime2.mp3')
            mixer.music.play()

            # placing the recognized 'message' on the clipboard

            pyperclip.copy(message)

        except sr.UnknownValueError:
            print("Google Speech Recognition could not understand audio")
            
        except sr.RequestError as e:
            print("Could not request results from Google Speech Recognition service; {0}".format(e))

        else:
            pass


def thr():
    t1 = threading.Thread(target=buttonClick, daemon=True)
    t1.start()

# creating the Speak button, which calls 'thr' which invokes 'buttonClick()'

MyButton1 = Button(root, image=photo, width=150, command=thr, activebackground='#c1bfbf', bd=0)
MyButton1.grid(row=0, column=2)

# making sure the app stay on top of all windows (use this optionally)

root.wm_attributes('-topmost', 1)

# running the mainloop

root.mainloop()                             
