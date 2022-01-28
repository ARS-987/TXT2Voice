from cgitb import text
import imp


import pyttsx3
text = input("What to say ?")
sound = pyttsx3.init()
sound.setProperty('rate', 110)
sound.say(text)
sound.runAndWait()