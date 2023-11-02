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

      
     
    
    
   