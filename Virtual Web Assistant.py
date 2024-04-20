import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes
import webbrowser

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def talk(text):
    engine.say(text)
    engine.runAndWait()


def take_command():
    command = ''
    try:
        with sr.Microphone() as source:
            print('listening...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'lisa' in command:
                command = command.replace('lisa', '')
                print(command)
    except:
        pass
    return command


def run_lisa():
    while True:
        command = take_command()
        print(command)
        if 'play' in command:
            song = command.replace('play', '')
            talk('playing ' + song)
            pywhatkit.playonyt(song)
        elif 'open youtube' in command:
             youtube = webbrowser.open("youtube.com")
             talk('opening youtube')
        elif 'time' in command:
             time = datetime.datetime.now().strftime('%I:%M %p')
             talk('Current time is ' + time)
        elif 'open google' in command:
              google = webbrowser.open("google.com")
              talk('here you go!!')
        elif 'who is' in command:
              person = command.replace('who is', '')
              info = wikipedia.summary(person, 5)
              print(info)
              talk(info)
        elif 'ok bye' in command:
            talk('thanks for you time')
            exit()
        else:
            talk('Please say the command again.')

    while True:
        run_lisa()
