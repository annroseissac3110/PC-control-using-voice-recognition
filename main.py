from neuralintents import GenericAssistant
import speech_recognition as sr

import sys
import datetime
import pyautogui
import psutil 
from news import News
from weather import weather

from wikipedia import wikisearch
from whatsapp import Whatsapp
from camera import Camera
from mail import Email
from show_image import Showimage
from negative import Negative
from system_condition import Systemcondition

import pyttsx3 as tts
speaker =tts.init()







def Time():
     time=datetime.datetime.now().strftime('%I:%M %p')
     print(time)
     speaker.say(time)
     speaker.runAndWait()
     
def Charge():
     battery = psutil.sensors_battery()
     percent = battery.percent
     speaker.say(f"The battery is currently at {percent} percent")
     
def Memory():
    memory = psutil.virtual_memory()
    used = round(memory.used/1024/1024, 2)
    total = round(memory.total/1024/1024, 2)
    speaker.say(f"The system is currently using {used} megabytes of memory out of {total} megabytes")
    
def Cpu():
     cpu = psutil.cpu_percent(interval=1)
     speaker.say(f"The CPU usage is currently at {cpu} percent")
     
def Disk():
    disk = psutil.disk_usage('/')
    used = round(disk.used/1024/1024/1024, 2)
    total = round(disk.total/1024/1024/1024, 2)
    speaker.say(f"The disk usage is currently at {used} gigabytes out of {total} gigabytes")
    
def volume_increase():
     pyautogui.press("volumeup")
     print("volume increased")
     speaker.say("volume increased")
     speaker.runAndWait()
     
def volume_decrease():
    pyautogui.press("volumedown")
    print("volume decreased")
    speaker.say("volume decreased")
    speaker.runAndWait()
    
def volume_muted():
    pyautogui.press("volumemute")
    print("volume muted")
    speaker.say("volume muted")
    speaker.runAndWait()
                
     

def youtube():
    import pyttsx3 as tts
    speaker =tts.init()
    speaker.setProperty('rate',150)
    
    
    import googleapiclient.discovery
    api_service_name = "youtube"
    api_version = "v3"
    DEVELOPER_KEY = "AIzaSyC0NrukLPSJ-KhzZ9Iw1xwiw4jXXEha-YE"  
    youtube = googleapiclient.discovery.build(api_service_name, api_version, developerKey=DEVELOPER_KEY)
    import speech_recognition as sr
    import webbrowser
    
    r = sr.Recognizer()


    def youtube_video():
        
                try:
                    video_name =  message
                    #inp.replace(" ","in youtube")
                    
                    print("The video is being played in youtube..")
                    speaker.say("the video is being played in youtube")
                    speaker.runAndWait()
            
                except sr.UnknownValueError:
                    print("Google Speech Recognition could not understand audio")
                    speaker.say("Google Speech Recognition could not understand audio")
                    speaker.runAndWait()
                except sr.RequestError as e:
                    print("Could not request results from Google Speech Recognition service; {0}".format(e))
                    speaker.say("Could not request results from Google Speech Recognition service; {0}".format(e))
                    speaker.runAndWait()

                # search for videos and extract the ID of the first result
                search_response = youtube.search().list(
                    q=video_name,
                    type='video',
                    part='id',
                    maxResults=1
                ).execute()

                video_id = search_response['items'][0]['id']['videoId']

                # construct the URL of the video and open it in the default browser
                video_url = "https://www.youtube.com/watch?v=" + video_id
                webbrowser.open(video_url)
            
          
                    
    youtube_video()  

def Google():
    import speech_recognition as sr
    import webbrowser
    # Perform the Google search and open the first result in a web browser
    url = f"https://www.google.com/search?q={message}"
    webbrowser.open_new_tab(url)


def Close():
     import speech_recognition as sr
     import pyttsx3 as tts
     speaker =tts.init()
     from AppOpener import close
     app_name = message.replace("close ","").strip()
     close(app_name, match_closest=True, output=False)
     print(""+app_name+" closed")
     speaker.say(""+app_name+" closed")
     speaker.runAndWait()
     
def Open():
    
    from AppOpener import open
    app_name = message.replace("open ","")
    open(app_name, match_closest=True)
     
def OpenPhotos():
   
    from AppOpener import open
    app_name = message.replace("open ","")
    open(app_name, match_closest=True)
    print(""+app_name+" opened")
    speaker.say(""+app_name+" opened")
    speaker.runAndWait()

def ClosePhotos():
    
    from AppOpener import close
    app_name = message.replace("close ","").strip()
    close(app_name, match_closest=True, output=False) 
    print(""+app_name+" closed")
        
     
    
    
   
mappings ={
    
    "news":News,
    "weather":weather,
    "youtube":youtube,
    "wikipedia":wikisearch,
    "time":Time,
    "charge":Charge,
    "memory":Memory,
    "cpu":Cpu,
    "disk":Disk,
    "volumeincrease":volume_increase,
    "volume decrease":volume_decrease,
    "mute volume":volume_muted,
    "whatsapp":Whatsapp,
    "camera":Camera,
    "email":Email,
    "showimage":Showimage,
    "negative":Negative,
    "open":Open,
    "close":Close,
    "open photos":OpenPhotos,
    "close photos":ClosePhotos,
    "google":Google,
    "system condition":Systemcondition
    
}


assistant = GenericAssistant('intents.json',intent_methods=mappings)
#assistant.train_model()
#assistant.save_model()
assistant.load_model()



print("Hey there, I am your voice assistant.")
print("say 'listen' for using me!")
speaker.say("Hey there, I am your voice assistant.")
speaker.runAndWait()
speaker.say("say 'listen' for using me!")
speaker.runAndWait()

while True:
    try:
        with sr.Microphone() as mic:
           
            recognizer=sr.Recognizer()
            recognizer.adjust_for_ambient_noise(mic,duration=0.2)
            audio=recognizer.listen(mic)
            
            global voice
            voice = recognizer.recognize_google(audio)
            voice = voice.lower()
            #print("You said:",voice)
            if "listen" in voice:
                import pyttsx3 as tts
                speaker =tts.init()
                print("listening...")
                speaker.say("listening..")
                speaker.runAndWait()
                
                try:
                    with sr.Microphone() as mic:
        
                        recognizer=sr.Recognizer()
                        recognizer.adjust_for_ambient_noise(mic,duration=0.2)
                        audio=recognizer.listen(mic)
                        global message
                        message = recognizer.recognize_google(audio)
                        message = message.lower()
                        print("You said:",message)
                        assistant.request(message)
                except sr.UnknownValueError:
                    recognizer = sr.Recognizer()
    except sr.UnknownValueError:
        recognizer = sr.Recognizer()
   


                
                
