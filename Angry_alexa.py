import speech_recognition as sr
import pyttsx3
import pywhatkit

listener=sr.Recognizer()
engine=pyttsx3.init()
voices=engine.getProperty("voices")
engine.setProperty("voice",voices[1].id)

def talk(text):
   
   engine.say(text)

   engine.runAndWait()

def alexa_command():
  while True:
    command=False
    try:
        with sr.Microphone() as source:
            print("Listning...")
            voice=listener.listen(source)
            command=listener.recognize_google(voice)
            command=command.lower()
            if "alexa" in command:
               command=command.replace("alexa","")
               
               print(command)
               return command
    except:
        pass
    return command

def run_alexa():
    command=alexa_command()
    if command==False:
        return
    print(command)
    if "play" in command:
        song=command.replace("play","")
        talk("playing"+song)
        pywhatkit.playonyt(song)
    else:
        talk('please say the command again.')
while True:
    try:
    
       run_alexa()
    except UnboundLocalError:
        print("No command detected")
        talk("No command detected")
        break