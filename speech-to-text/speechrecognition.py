import speech_recognition as sr
import pyttsx3
#import PyAudio
r = sr.Recognizer() 

speak = [ "cancer", "diabetes", "Thyroid"]
speak = set(speak)
answer = []
  

def SpeechtoText(command):
     engine = pyttsx3.init()
     engine.say(command) 
     engine.runAndWait()
      
while(1):    
      
   
    try:
          
       
        with sr.Microphone() as source2:
               
            r.adjust_for_ambient_noise(source2, duration=0.2)
            audio2 = r.listen(source2)
              
            
            Text = r.recognize_google(audio2)
            Text = Text.lower()
  
            print("You said"+Text)
            Text=Text.split(" ")
            ans = [x for x in Text if x in speak]
            print(answer)
            answer.append(ans)
              
    except sr.RequestError as e:
        print("Could not request results; {0}".format(e))
          
    except sr.UnknownValueError:
        print("We could not catch that, please repeat")