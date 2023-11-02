def Whatsapp():
    import datetime
    import speech_recognition as sr
    import pywhatkit
    import pyttsx3
    import ast
    from fuzzywuzzy import fuzz, process

    speaker = pyttsx3.init()
    voices = speaker.getProperty('voices')
    speaker.setProperty('voice', voices[0].id)

    try:
        with open('contacts.txt', 'r') as f:
            content = f.read()
            contacts = ast.literal_eval(content)

    except Exception as e:
        print("Error opening file:", e)
        speaker.say("Error opening file")
        speaker.runAndWait()


    # Initialize the recognizer
    r = sr.Recognizer()

    # Define the function to take voice commands and send a WhatsApp message
    def send_whatsapp():
        with sr.Microphone() as source:
            print("Hey there, whom should I send the message to?")
            speaker.say("Hey there, whom should I send the message to?")
            speaker.runAndWait()

            r.adjust_for_ambient_noise(source)
            audio = r.listen(source)
            try:
                contact_name = r.recognize_google(audio)
                name = contact_name.lower()
                print(name)

                # Find the closest match for the contact name based on string similarity
                closest_match = process.extractOne(name, contacts.keys())
                similarity = closest_match[1]
                if similarity >= 50:  # Minimum similarity threshold
                    closest_contact_name = closest_match[0]
                    phone_number = contacts[closest_contact_name]
                    print("Closest match:", closest_contact_name)
                else:
                    print("Sorry, I could not find a matching contact.")
                    speaker.say("Sorry, I could not find a matching contact.")
                    speaker.runAndWait()
                    return

                print("What should I send?")
                speaker.say("What should I send?")
                speaker.runAndWait()
                r.adjust_for_ambient_noise(source)
                audio = r.listen(source)
                message = r.recognize_google(audio)
                print(message)

                current_time = datetime.datetime.now()
                pywhatkit.sendwhatmsg(phone_number, message, current_time.hour, current_time.minute + 1)  # Send message after 1 minute
                print("Message sent successfully!")
                speaker.say("Message sent successfully")
                speaker.runAndWait()
            except sr.UnknownValueError:
                print("Sorry, I did not understand that.")
                speaker.say("Sorry, I did not understand that.")
                speaker.runAndWait()
            except sr.RequestError as e:
                print("Could not request results from Google Speech Recognition service; {0}".format(e))
                speaker.say("Could not request results from Google Speech Recognition service; {0}".format(e))
                speaker.runAndWait()

    # Call the function to send a WhatsApp message
    send_whatsapp()
