def Showimage():
                
                import pyttsx3 as tts
                speaker =tts.init()
                speaker.setProperty('rate',150)
    

                from PIL import Image

                # Open the image file
                print("opening image")
                speaker.say("opening image")
                speaker.runAndWait()
                img = Image.open("image.jpg")
                # Show the image
                img.show()
                print("Image opened")
                speaker.say("Image opened")
                speaker.runAndWait()
                
                
                

                    
                
                        
                        
                    
            
