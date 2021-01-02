from gtts import gTTS


import os

run = True
while run is True:
    txt = input("enter whatever you want..\n")
    if txt == '':
        quit()
    else:
        Ln = 'en'
        say =gTTS(text=txt,lang=Ln,slow=False)
        say.save("shout.mp3")
        os.system("shout.mp3")
        print("to stop enter empty string")
    
