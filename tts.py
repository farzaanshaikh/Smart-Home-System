#import weather
import os
import sys
from gtts import gTTS


def say(words):

    tts = gTTS(text=words, lang='en')
    tts.save("temp.mp3")
    os.system("mpg321 temp.mp3")
    os.system("rm temp.mp3")
def sayhindi(words):
    tts = gTTS(text=words, lang='hi')
    tts.save("temp2.mp3")
    os.system("mpg321 temp2.mp3")
    os.system("rm temp2.mp3")


#say(weather.d)
