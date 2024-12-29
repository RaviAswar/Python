import package_speech_recognizer as sr
import pyttsx3

from datetime import datetime
engine = pyttsx3.init()
engine.say("Hello SIR, How can i help you")
engine.runAndWait()

now = datetime.now()
current_time=now.strftime("%H:%M:%S")

def takecommand():
    command = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listning....")
        command.adjust_for_ambient_noise(source)
        command.pause_thresold = 1
        audio = command.listen(source)



        try:
            print("Recognizing....")
            query = command.recognize_google(audio,language="en-in")
            print("You said",query)
            if 'current time please' in query:
                engine = pyttsx3.init()
                engine.say(current_time)
                engine.runAndWait()
        except Exception as Error:
            returnNone
        return query
takecommand()
