def Email():
    import smtplib
    import speech_recognition as sr
    import pyttsx3
    from email.message import EmailMessage
    import ast
    import jellyfish
    import webbrowser
    

    listener = sr.Recognizer()
    engine = pyttsx3.init()
    

    def talk(text):
        engine.say(text)
        engine.runAndWait()


    def get_info():
        try:
            with sr.Microphone() as source:
                print('listening...')
                voice = listener.listen(source)
                info = listener.recognize_google(voice)
                return info.lower()
        except:
            pass
        
    def open_sent_email_in_gmail():
        url = f'https://mail.google.com/mail/u/0/#sent'
        webbrowser.open(url)



    def send_email(receiver, subject, message):
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()

        # Make sure to give app access in your Google account
        server.login('annroseissac2000@gmail.com', 'aenzmcwwajdermjl')
        email = EmailMessage()
        email['From'] = 'annroseissac2000@gmail.com'
        email['To'] = receiver
        email['Subject'] = subject
        email.set_content(message)
        server.send_message(email)


    try:
        with open('emailid.txt', 'r') as f:
            content = f.read()
            email_list = ast.literal_eval(content)
    except Exception as e:
        print("Error opening file:", e)
        talk("error opening file")


    def get_email_info():
        print('To whom do you want to send the email?')
        talk('To whom do you want to send the email?')
        name = get_info()
        print(name)

        # Find the closest match for the entered name based on soundex algorithm
        closest_match = max(email_list.keys(), key=lambda x: jellyfish.soundex(name) == jellyfish.soundex(x))
        if jellyfish.soundex(closest_match) == jellyfish.soundex(name):
            receiver = email_list[closest_match]
            print(f"Closest match: {closest_match}")
            print(f"Receiver: {receiver}")
            print('What is the subject of your email?')
            talk('What is the subject of your email?')
            subject = get_info()
            print(subject)
            print('Tell me the text in your email')
            talk('Tell me the text in your email')
            message = get_info()
            print(message)
            send_email(receiver, subject, message)
            print("Your email has been sent")
            talk('Your email has been sent')
            open_sent_email_in_gmail()
        else:
            print("No match found. Please try again.")


    get_email_info()

    