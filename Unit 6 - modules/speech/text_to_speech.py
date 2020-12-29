import pyttsx3

text = 'first time i\'m using a package in next.py course'
engine = pyttsx3.init()
engine.say(text)
engine.runAndWait()
