import os
import time
import playsound
import speech_recognition as sr
from gtts import gTTS
import random


words = ["fuck","what the hell","whatever","screw that","thats rough buddy","go stick your ass somewhere else"]

def voice(txt):
    tts = gTTS(text=txt, lang='en-us',slow=False)
    filename = "sound1.mp3"
    tts.save(filename)
    playsound.playsound(filename)
    os.remove(filename)


def audio():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        audio =r.listen(source)
        said = ""
        try:
            said = r.recognize_google(audio)
            print(said)
        except Exception as e:
            print("\n" + str(e))
    return said
print("speak\n")
text = audio()
voice(random.choice(list(words)))



