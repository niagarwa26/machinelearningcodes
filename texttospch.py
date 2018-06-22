#!/usr/bin/python3

import pyttsx3

write = pyttsx3.init()
text = input("enter the text")
write.say(text)
write.runAndWait()
