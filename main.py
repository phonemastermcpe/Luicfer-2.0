import pyttsx3
import speech_recognition as sr
import datetime
import os

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voices',voices[0].id)
engine.setProperty('rate', 160)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def commands():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening...')
        r.adjust_for_ambient_noise(source, duration=1)
        audio = r.listen(source)

    try:
        print('Wait For Few Moments')
        query =  r.recognize_google(audio, language="en-in")
        print(f"You just said: {query}\n")
    except Exception as e:
        print(e)
        speak('Please Say That Again')
        query = 'none'
    return query

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        print('Good Morning Sir')
        speak('Good Morning Sir')
        speak('PyBro Here. How May I Help You Sir')

    elif hour>=12 and hour<17:
        print('Good Afternoon Sir')
        speak('Good Afternoon Sir')
        speak('PyBro Here. How May I Help You Sir')
        

    elif hour>=17 and hour<21:
        print('Good Evening Sir')
        speak('Good Evening Sir')
        speak('PyBro Here. How May I Help You Sir')
        
    else:
        print('Good Night Sir')
        speak('Good Night Sir')


def tasks():
    if 'open google' or 'i want to google something' or 'search something on google' in query:
        speak('Opening Google Sir.')
        print('Openeing Google Sir.')
        os.startfile("C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe")

    elif 'open visual studio code' or 'open vs code' or 'open my default programing application' or 'open my default coding application'in query:
        speak('Opening Visual Studio Code Sir')
        print('Opening Visual Studio Code')
        os.startfile("C:\\Users\\vendors\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe")

    elif 'open both google as well vs code' or 'open google and vs code' or 'open visual studio code and google' or 'open vs code and google' in query:
        speak('Opening Visual Studio Code As Well As Google Sir.')
        print('Opening Visual Studio Code As Well As Google Sir.')
        os.startfile("C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe")
        os.startfile("C:\\Users\\vendors\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe")

    elif 'open bridge addon maker' or 'open bridge' or 'open bridge v2' or 'open my addon maker' or 'open my deafult addon maker' in query:
        speak('Opening Bridge Addon Maker Sir.')
        os.startfile("C:\\Program Files\\Google\\Chrome\\Application\\chrome_proxy.exe")

    elif 'open notepad' or 'i want to code something in notepad' or 'i want to code in notepad' in query:
        speak('I Got It Sir Opening Notepad Sir.')
        print('I Got It Sir Opening Notepad Sir.')

    elif 'open android studio' or 'i want to create a app' or 'i want to update my app' or 'i want to code a app' or 'i want to program a app' or 'i want to make a pair' in query:
        speak('Sure Sir. Opening Android Studio')
        print('Sure Sir. Opening Android Studio')
        os.startfile("C:\\Program Files\\Android\\Android Studio\\bin\\studio64.exe")

    elif 'open eclipse' or 'i want to do some coding on java' or 'i want to do some programing on java' or 'i want to make a prgram in java' or 'i want to do something on java' or 'i want to do something in java' in query:
        speak('Ok Sir. Opening Eclipse IDE')
        print('Ok Sir. Opening Eclipse IDE')
        os.startfile("E:\\New folder (2)\\eclipse\\eclipse.exe")

    elif 'play my favourite song' or 'play the song which is my favourite' in query:
        speak('Done Sir. Playing Your Favourite Song Sir')
        print('Done Sir. Playing Your Favourite Song Sir')
        os.startfile('C:\\Users\\vendors\\Desktop\\Brown Munde - AP Dhillon.mp3')


def talks():
    if 'hello pybro' or 'hi pybro' or 'hey pybro' or 'whatsup pybro' in query:
        speak('Hello Sir I Am Doing Good. How Can I Help You')
        print('Hello Sir I Am Doing Good. How Can I Help You')

    elif 'what do you do everytime' or 'what you do everyday' or 'what you do all the time':
        speak('Nothing Sir Just Watch Your Back For Any Help')
        print('Nothing Sir Just Watch Your Back For Any Help')

    elif 'your creator' or 'developed you' or 'created you' 'created by whom':
        speak('I was Created By Mr. Undefined Developer As Side His All time Ai Personal Assistant.')
        print('I was Created By Mr. Undefined Developer As Side His All time Ai Personal Assistant.')

    elif 'who are you' or 'who you are' or 'your intro please' or 'your introduction please' or 'something about you' in query:
        speak('I Am PyBro An Artificial Intelligence Created By Undefined Developer For His All Time Assistant. I am Designed To Reply His Snetences And Of Certain People A Which He Has Mentioned In My Script. And I Am Fully Safe Ai I Am Not Programmed To Harm Others. I Can Do Most Of The Human Computer Works Such As Creating Folders, Files, Open Apps  and Talking To You')
        print('I Am PyBro An Artificial Intelligence Created By Undefined Developer For His All Time Assistant. I am Designed To Reply His Snetences And Of Certain People A Which He Has Mentioned In My Script. And I Am Fully Safe Ai I Am Not Programmed To Harm Others. I Can Do Most Of The Human Computer Works Such As Creating Folders, Files, Open Apps  and Talking To You')

    elif 'are you there' or 'are you online' in query:
        speak('I Am Online As Much As My Script Is Running')
        print('I Am Online As Much As My Script Is Running')

    elif 'can you dance':
        speak('No I Cannot Dance Because I am Just A Desktop Assistant')
        print('No I Cannot Dance Because I am Just A Desktop Assistant')

    elif 'can access you' or 'will listen to them' or 'will work for them' or 'secondry masters' in query:
        speak('I Can Only Be Access By My Si Mr. Undefined Developer. But There Are Two More More Person Who Can Access Me. There Names Are Mr.GsX And Miss. S Sri')
        print('I Can Only Be Access By My Si Mr. Undefined Developer. But There Are Two More More Person Who Can Access Me. There Names Are Mr.GsX And Miss. S Sri')

    elif 'can you solve mathmatics' or 'can you do maths' 'can you solve maths' in query:
        speak('Yes I Can. I Am Programed For That Also.')
        print('Yes I Can. I Am Programed For That Also.')

if __name__ == '__main__':
    wishMe()
    while True:
        query = commands().lower()
        if 'time' in query:
            strTime = datetime.datetime.now().strftime('%H:%M:%S')
            print(strTime)
            speak(f'Sir The Time Is {strTime}')
        talks()
        tasks()

