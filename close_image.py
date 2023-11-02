def Closeimage():
    import pyttsx3 as tts
    speaker =tts.init()
    speaker.setProperty('rate',150)
    
    import os

    # Replace "C:\\Program Files\\MyApp\\myapp.exe" with the path to the app's executable file
    app_path = "C:\Program Files\WindowsApps\Microsoft.Windows.Photos"

   # Get the process ID of the app
    pid = os.getpid(app_path)

# Kill the process associated with the app
    os.kill(pid)
    print("image closed")
    speaker.say("image closed")
    speaker.runAndWait()