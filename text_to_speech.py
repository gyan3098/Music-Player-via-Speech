import speech_recognition as sr 
r = sr.Recognizer() 
with sr.Microphone() as source:
    print ("Say Something")
    #listens for the user's input 
    audio = r.listen(source) 

     
    try: 
        mytext = r.recognize_google(audio)
        print ("you said: " + mytext )
      
    #error occurs when google could not understand what was said 
      
    except sr.UnknownValueError: 
        print("Google Speech Recognition could not understand audio") 
      
    except sr.RequestError as e: 
        print("Could not request results from Google  ".format(e))
        
# Import the required module for text 
# to speech conversion 
from gtts import gTTS 
# This module is imported so that we can 
# play the converted audio 
import os 
mytext=mytext.split()
# The text that you want to convert to audio 
# Language in which you want to convert 
language = 'en'
# Passing the text and language to the engine, 
# here we have marked slow=False. Which tells 
# the module that the converted audio should 
# have a high speed 
myobj = gTTS(text=mytext, lang=language, slow=False) 

# Saving the converted audio in a mp3 file named 
# welcome 
myobj.save("gyan1.mp3") 

# Playing the converted file 
os.system("mpg321 gyan1.mp3") 

from pygame import mixer # Load the required library
from mutagen.mp3 import MP3
audio = MP3('C:/Users/Gyan Ranjan/Desktop/project/Abhi Abhi.mp3')
ad_len=audio.info.length
for i in range(len(mytext)):
    if(mytext[i]=='play'):
        mixer.init()
        mixer.music.load('C:/Users/Gyan Ranjan/Desktop/project/Abhi Abhi.mp3')
       
        mixer.music.play() 
        
