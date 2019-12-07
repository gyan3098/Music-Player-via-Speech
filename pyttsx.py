
import pyttsx3
engine = pyttsx3.init()
engine.setProperty('rate', 100)

voices = engine.getProperty('voices')
for voice in voices:
    print ("Using voice:", repr(voice))
    engine.setProperty('voice', voice.id)
    engine.say("Hi i am somu")
    
engine.runAndWait()