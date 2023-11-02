def wikisearch():
    import speech_recognition as sr
    import wikipediaapi
    import pyttsx3
    

    def wiki_search():
        # Initialize text-to-speech engine
        engine = pyttsx3.init()

        # Obtain audio from the microphone
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Say the topic to be searched in Wikipedia.")
            engine.say("Say the topic to be searched in Wikipedia.")
            engine.runAndWait()
            audio = r.listen(source)

        # Recognize speech using Google Speech Recognition
        query = r.recognize_google(audio)
        print(f"You said: {query}")
        engine.say(f"You said: {query}")
        engine.runAndWait()

        # Search for query in Wikipedia
        wiki = wikipediaapi.Wikipedia('en') # Set language to English (default is English)
        page = wiki.page(query)

        if page.exists():
            content = page.summary
            summary = '.'.join(content.split('.')[:5]) + '.' # Select the first 5 sentences
            print("Here is the search result:")
            engine.say("Here is the search result.")
            engine.runAndWait()
            print(summary)
            engine.say(summary)
            engine.runAndWait()

           

        else:
            print("No results found on Wikipedia.")
            engine.say("No results found on Wikipedia.")
            engine.runAndWait()
    wiki_search()
