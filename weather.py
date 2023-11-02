def weather():
    import requests
    import pyttsx3
    import speech_recognition as sr
    def Weather():
        engine = pyttsx3.init()
        engine.setProperty('rate', 160)
        def talk(text):
            
            engine.say(text)
            engine.runAndWait()
        #Api_key = '6e6f9659fef62e5c5d1103979100d281'
        Api_key = 'bf11e639a23c6a159ae2e9709b1e3097'

        base_url = 'http://api.openweathermap.org/data/2.5/weather'

        listener = sr.Recognizer()
        city = talk('say city name ') 
        def weather_details():
            #while True:
                with sr.Microphone() as source:
                    print('listening...')
                        
                            #listener.adjust_for_ambient_noise(source, duration=1)
                    listener.adjust_for_ambient_noise(source)
                    voice = listener.listen(source)

                    try:
                        instructions = listener.recognize_google(voice)
                                    
                        instructions = instructions.lower()
                        print(instructions)

                        talk(instructions)
                    except:
                        instructions=''
                city = instructions      
                request_url = f"{base_url}?appid={Api_key}&q={city}"
                response = requests.get(request_url)
                if response.status_code==200:
                    data = response.json()
                    weather = data['weather'][0]['description']
                    temperature = round(data['main']['temp']- 273.15,2 ) # for celsius

                    w = ('Weather: ', weather)
                    t = ('Temperature: ', temperature)
                    
                    talk("weather details in")
                    talk(city)
                    talk(w)
                    talk(t) 
                else:
                    print("An error occured... ")    
        weather_details()
    Weather()
