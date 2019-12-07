import time
from pygame import mixer # Load the required library
x= input().split()

from mutagen.mp3 import MP3

audio = MP3('C:/Users/Gyan Ranjan/Desktop/project/Abhi Abhi.mp3')
ad_len=audio.info.length
for i in range(len(x)):
    if(x[i]=='play'):
        mixer.init()
        mixer.music.load('C:/Users/Gyan Ranjan/Desktop/project/Abhi Abhi.mp3')
        t=(time.localtime().tm_min)*60+time.localtime().tm_sec
        length_stop=t+ad_len
        print(length_stop)
        print(t)
        mixer.music.play() 
        





t2=(time.localtime().tm_min)*60+time.localtime().tm_sec
print(t2)

if (length_stop-320-t2)>=0:
    mixer.music.stop()
    
import time
then = time.time()
now = time.time()
diff = now - then
print(diff)

import os
os.startfile('C:\Program Files\WinRAR\WinRaR.exe')