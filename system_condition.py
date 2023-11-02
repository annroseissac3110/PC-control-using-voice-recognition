def Systemcondition():
     def check_resources(command):
                    import psutil
                    import pyttsx3 as tts
                    speaker =tts.init()
                    speaker.setProperty('rate',150)
                    
                    if "system charge" in command:
                        battery = psutil.sensors_battery()
                        percent = battery.percent
                        speaker.say(f"The battery is currently at {percent} percent")
                    elif "memory usage" in command:
                        memory = psutil.virtual_memory()
                        used = round(memory.used/1024/1024, 2)
                        total = round(memory.total/1024/1024, 2)
                        speaker.say(f"The system is currently using {used} megabytes of memory out of {total} megabytes")
                    elif "CPU usage" in command:
                        cpu = psutil.cpu_percent(interval=1)
                        speaker.say(f"The CPU usage is currently at {cpu} percent")
                    elif "hard disk usage" in command:
                        disk = psutil.disk_usage('/')
                        used = round(disk.used/1024/1024/1024, 2)
                        total = round(disk.total/1024/1024/1024, 2)
                        speaker.say(f"The disk usage is currently at {used} gigabytes out of {total} gigabytes")
                  
                    else:
                        speaker.say("I'm sorry, I didn't understand the command.")
                    
                    speaker.runAndWait()

                # Define a function to listen to voice commands and check the system resources
     def listen():
                    import speech_recognition as sr
                    with sr.Microphone() as source:
                        r=sr.Recognizer()
                        r.adjust_for_ambient_noise(source)
                        print("select:")
                        print("1.system charge")
                        print("2.memory usage")
                        print("3.CPU usage")
                        print("4.hard disk usage")
                        audio = r.listen(source)

                        try:
                            command = r.recognize_google(audio)
                            print(f"You said: {command}")
                            check_resources(command)
                        except sr.UnknownValueError:
                            print("Sorry, I couldn't understand what you said.")
                        except sr.RequestError as e:
                            print(f"Could not request results from Google Speech Recognition service; {e}")
                        
                # Call the listen function to start listening for voice commands
                
     listen()