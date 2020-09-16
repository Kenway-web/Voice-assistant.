import pyttsx
import datetime
import speech_recognition as sr
import wikipedia
import wolframalpha
import webbrowser  
import os
import smtplib

engine=pyttsx.init('sapi5')
voices =engine.getProperty('voices')
engine.setProperty('rate', 140)
print(voices[1].id)
engine.setProperty('voice',voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()



def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")   

    else:
        speak("Good Evening!")  

    speak("I am allion  Sir. Please tell me how may I help you") 



def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source,duration=1)
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognising....")
        query=r.recognize_google(audio,language='en-in')
        print("User said::"+query )
        

            
    except Exception as e:
        #print(e)
       print("Say that again:")
       return "None"

    return query


def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('shoaibali26021999@gmail.com', 'Shoaib2602@')
    server.sendmail('shoaibali26021999@gmail.com', to, content)
    server.close()


if __name__ == "__main__":
    wishMe()
    while True:
    #if 1:
      query=takeCommand().lower()
      #building logic for excecuting task
    
      
      if 'who made you' in query or 'define your self ' in query:
          speak('i am Kenway an AI created by Shoaib ali ')
    
      elif 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)
            
      elif  'open youtube' in query:    
           webbrowser.open('youtube.com')
      
      elif  'open google' in query:    
           webbrowser.open('google.com')
      

      
      elif  'open stackoverflow'  in query:
             webbrowser.open('stackoverflow.com')
             
      elif 'play music' in query:
          music_dir='D:\\Non critical\songs\play'
          songs=os.listdir(music_dir)
          print(songs)
          os.startfile(os.path.join(music_dir, songs[0]))
          
      elif 'the time' in query:
          strTime = datetime.datetime.now().strftime("%H:%M:%S")    
          speak(f"Sir, the time is {strTime}")
      
      
      
      elif "calculate" in query: 
              
            # write your wolframalpha app_id here 
            app_id = "APER4E-58XJGHAVAK" 
            client = wolframalpha.Client(app_id) 
  
            indx = query.lower().split().index('calculate') 
            query = query.split()[indx + 1:] 
            res = client.query(' '.join(query)) 
            answer = next(res.results).text 
            speak("The answer is " + answer) 
            print("Answer is"+answer)
      
      
                
      elif 'open code' in query:
            codePath = "C:\\Users\SHOAIB ALI\AppData\Local\Programs\Microsoft VS Code\Code.exe"
            os.startfile(codePath) 
    
      elif 'open chrome' in query:
            codePath="C:\Program Files (x86)\Google\Chrome\Application\chrome.exe"
            os.startfile(codePath)
            
      
      elif 'open facebook' in query:
             webbrowser.open('facebook.com')
    
      
      elif 'send email' in query:
          try:
             speak('What should i say:')
             content = takeCommand()
             if 'sister' in query: 
                to = "nidaali26021999@gmail.com"    
                sendEmail(to, content)
             
             elif ' friend' in query:
                 to = "tijus7399@gmail.com"    
                 sendEmail(to, content)
                 
          
             else:
                  speak("provide mail that is before @gmail....")
                  x=takeCommand().lower()        
                  y=x+'@gmail.com'
                  sendEmail(y,content)
             speak("Email has been sent!")
          
          
          except Exception as e:
             print(e)
             speak("unable to reach please try again. I am not able to send this email") 
            
             
    
             
      elif 'email to' in query:
          try:
             speak('What should i say:')
             content = takeCommand()
             to = "nidaali26021999@gmail.com"    
             sendEmail(to, content)
             speak("Email has been sent!")
          except Exception as e:
             print(e)
             speak("unable to reach please try again. I am not able to send this email") 
          
          
          
          
      elif "exit" in query or "bye" in query or "sleep" in query: 
            speak("Ok bye,Shoaib") 
            break
            
      
      elif 'search' in query:
          
            speak("I can search the web for you, Do you want to continue?") 
            ans = takeCommand().lower()
            if 'yes' in ans or 'yeah' in ans: 
                
                webbrowser.open(query)           
            
      
 