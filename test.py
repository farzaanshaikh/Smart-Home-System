import speech_recognition as sr
from beep import beep
#import weather
#   from tts import say



# obtain audio from the microphone



r = sr.Recognizer()
while True:

    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        print "SAY"
        audio = r.listen(source, timeout=2)




    try:
    # for testing purposes, we're just using the default API key
    # to use another API key, use `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
    # instead of `r.recognize_google(audio)`
        a =str(r.recognize_google(audio))
        print a
    except sr.UnknownValueError:
        continue
    except sr.RequestError as e:
        continue
    if a.startswith("hello alpha") or a.startswith('Hello alpha'):
        print "OK"
