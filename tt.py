import speech_recognition as sr
r = sr.Recognizer()




while True:
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)

        try:
            print "Say"
            audio = r.listen(source, timeout=2)
        except sr.WaitTimeoutError:
            continue
        except KeyboardInterrupt:
            continue

    try:

        a =str(r.recognize_google(audio))
        print a
    except sr.UnknownValueError:
        continue
    except sr.RequestError as e:
        continue
