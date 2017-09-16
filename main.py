import speech_recognition as sr
from process import command
import RPi.GPIO as GPIO
import random
from beep import beep

greet=["Hello","Hi","Hey"]
from tts import say
from tts import sayhindi


GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(18,GPIO.OUT)
GPIO.setup(17,GPIO.OUT)
GPIO.setup(27,GPIO.OUT)

r = sr.Recognizer()




def mic():
    while True:
        with sr.Microphone() as source:
            r.adjust_for_ambient_noise(source)

            try:
                GPIO.output(18,GPIO.HIGH)
                audio = r.listen(source, timeout=2)
                GPIO.output(18,GPIO.LOW)
            except sr.WaitTimeoutError:
                continue
            except KeyboardInterrupt:
                GPIO.output(18,GPIO.LOW)


        try:

            a =str(r.recognize_google(audio))
            c = int(len(a.split()))

            if (a.find('hello')>-1 or a.find('ok')>-1 or a.find('hey')>-1 or a.find('namaste')>-1)  and a.find('alpha')>-1:
                if c == 2 :
                    if (a.find('hello')>-1 or a.find('ok')>-1 or a.find('hey')>-1):
                        say(random.choice(greet)+" Sir! What can I do for you?")
                        beep()
                        mic2()

                    elif (a.find('namaste')>-1):
                        sayhindi("Namaste! Mai aapki kya madad kar sakti hu?")
                        beep()
                        mic2()

                else:
                    GPIO.output(17,GPIO.HIGH)
                    command(a)
                    GPIO.output(17,GPIO.LOW)



        except sr.UnknownValueError:
            continue
        except sr.RequestError as e:
            continue



def mic2():
    while True:

        with sr.Microphone() as source:
            r.adjust_for_ambient_noise(source)

            try:
                GPIO.output(27,GPIO.HIGH)
                audio = r.listen(source, timeout=2)
                GPIO.output(27,GPIO.LOW)
            except sr.WaitTimeoutError:
                continue
            except KeyboardInterrupt:
                GPIO.output(27,GPIO.LOW)


        try:

            a =str(r.recognize_google(audio))
            a=a.lower()
            if (a.find('no')>-1):
                mic()
            else:
                GPIO.output(17,GPIO.HIGH)
                command(a)
                GPIO.output(17,GPIO.LOW)
                say("Is there anything else I can do for you?")

        except sr.UnknownValueError:
            say("I do not understand what you said.")
            continue
        except sr.RequestError as e:
            continue


if __name__ == "__main__":
    mic()
