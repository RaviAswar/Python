import pyttsx3
engine = pyttsx3.init()
engine.say('Hello sir ,i am jarvis How can i help you , room temperature is 27 degree celcious , the time is eleven hours 57 minutes 23 seconds , laptop aapko use kar ne ki anumati nahi hai , take permission from Ravi sir , sir please enter Number of total vehicles to be manufactured is')
engine.runAndWait()
v=int(input('Number of total vehicles to be manufactured is :'))
import pyttsx3
engine = pyttsx3.init()
engine.say('sir please enter Total number of wheels you want to used for manufacturing of vehicles is')
engine.runAndWait()
w=int(input('Total number of wheels you want to used for manufacturing of vehicles is :'))
b=(w-(v+v))/4
a=v-b
if w==1 or w<=v:
    import pyttsx3
    engine = pyttsx3.init()
    engine.say('sir Invalid input')
    engine.runAndWait()
    print('Invalid input')
else:
    import pyttsx3
    engine = pyttsx3.init()
    engine.say('Sir you entered {0} for total vehicle and {1} for total wheels used The number of four wheeler vehicles manufactured is {2}'.format(v,w,b))
    engine.runAndWait()
    print('The number of four wheeler vehicles manufactured is ',b)
import pyttsx3
engine = pyttsx3.init()
engine.say('Sir The number of two wheeler vehicles manufactured is {0}'.format(a))
engine.runAndWait()
print('The number of two wheeler vehicles manufactured is ',a)
