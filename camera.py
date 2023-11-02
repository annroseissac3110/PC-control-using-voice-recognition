def Camera():
        import speech_recognition as sr
        import cv2
        import pyttsx3 as tts
        speaker =tts.init()
        speaker.setProperty('rate',150)
        import time
            
        # Create a function to capture a picture from the camera
        def capture_picture():
            # Create a VideoCapture object to access the camera
            
           
            cap = cv2.VideoCapture(0)
            

            # Check if camera is opened successfully
            if not cap.isOpened():
                print("Error opening camera")
                speaker.say("Error opening camera")
                speaker.runAndWait()
                return

            # Capture a frame from the camera
            ret, frame = cap.read()
            if ret:
                # Save the captured frame as an image
                cv2.imwrite("image.jpg", frame)

                # Release the VideoCapture object
                cap.release()
                cv2.destroyAllWindows()
            else:
                print("Error capturing frame")
                speaker.say("Error capturing frame")
                speaker.runAndWait()

       
        # Create a function to recognize voice commands and take action
        def recognize_voice():
            # Create a recognizer object
            r = sr.Recognizer()

            # Use the microphone as the audio source
            with sr.Microphone() as source:
                # Adjust for ambient noise
                r.adjust_for_ambient_noise(source)

                # Listen for the user's voice command
                print("To capture picture Say 'picture'")
                speaker.say("To capture picture say, 'picture'")
                speaker.runAndWait()
                audio = r.listen(source)

                try:
                    # Convert the user's speech to text
                    command = r.recognize_google(audio)
                    picture_command=command.lower()
                    print("You said:"+picture_command)

                    # Take action based on the user's command
                    if "picture" in picture_command:
                        
                        capture_picture()
                        print("Picture captured successfully")
                        speaker.say("Picture captured successfully")
                        speaker.runAndWait()
                   
                    else:
                        print("Invalid command")
                        speaker.say("Invalid command")
                        speaker.runAndWait()

                except sr.UnknownValueError:
                    print("Could not understand audio")
                    speaker.say("Could not understand audio")
                    speaker.runAndWait()
                except sr.RequestError as e:
                    print("Could not request results from Google Speech Recognition service; {0}".format(e))
                    speaker.say("Could not request results from Google Speech Recognition service; {0}".format(e))
                    speaker.runAndWait()

        # Call the recognize_voice function to start the voice recognition process
        recognize_voice()
