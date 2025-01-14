import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

wikipedia_mode = False  # Global flag for Wikipedia mode


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning!")

    elif hour >= 12 and hour < 18:
        speak("Good Afternoon!")

    else:
        speak("Good Evening!")

    speak("I am Jarvis Sir. Please tell me how may I help you")


def takeCommand():
    # Takes microphone input and returns string output
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        print("Say that again please...")
        return "None"
    return query.lower()


if __name__ == "__main__":
    wishMe()
    while True:
        query = takeCommand().lower()

        if "exit" in query or "quit" in query or "stop" in query:
            speak("Goodbye! Have a great day!")
            break

        # Turn on Wikipedia mode
        if "turn on wikipedia" in query:
            wikipedia_mode = True
            speak("Wikipedia is on")
            print("Wikipedia mode activated.")

        # Turn off Wikipedia mode
        elif "turn off wikipedia" in query:
            wikipedia_mode = False
            speak("Wikipedia mode is off")
            print("Wikipedia mode deactivated.")

        # Search in Wikipedia if mode is ON
        # Search in Wikipedia if mode is ON
        elif "search" in query:
            if wikipedia_mode:
                speak("Searching Wikipedia...")
                query = query.replace("search", "").strip()
                try:
                    results = wikipedia.summary(query, sentences=2)
                    speak("According to Wikipedia")
                    print(results)
                    speak(results)
                except wikipedia.exceptions.PageError:
                    speak("Sorry, I couldn't find a Wikipedia page for your query. Please try again with a different search term.")
                except wikipedia.exceptions.DisambiguationError as e:
                    speak("Your search term is ambiguous. Please specify further. Here are some suggestions:")
                    print(e.options)  # Print options to the console
                    speak(", ".join(e.options[:5]))  # Speak the first few options
                except Exception as e:
                    speak("An unexpected error occurred while searching Wikipedia.")
                    print(f"Error: {e}")
            else:
                speak("Wikipedia mode is off. Would you like to turn it on?")
                response = takeCommand()
                if "yes" in response or "turn on" in response:
                    wikipedia_mode = True
                    speak("Wikipedia mode is now on")
                else:
                    speak("Okay, not turning on Wikipedia mode.")


        # Example of adding other commands
        elif "open youtube" in query:
            webbrowser.open("youtube.com")

        elif "the time" in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")

        elif 'open code' in query:
           codePath = "C:\\Users\\nisha\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
           os.startfile(codePath)
        
        elif 'open studio' in query:
           codePath = "C:\\Program Files\\Android\\Android Studio\\bin\\studio64.exe"
           os.startfile(codePath)

        elif 'play music' in query:
            music_dir = 'D:\\Music_p'
            songs = os.listdir(music_dir)
            print(songs)    
            os.startfile(os.path.join(music_dir, songs[0]))
