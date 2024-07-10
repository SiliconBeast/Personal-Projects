# Jarvis in process :)
# Made with online help and previous knowledge
import speech_recognition as sr 
import webbrowser
import pyttsx3

recognizer = sr.Recognizer() #helps in speech recog. functionality
ttsx = pyttsx3.init()

# takes voice and outputs as text
def speak():
    engine.say(text)
    engine.runAndWait()
    
    
if __name__ == "__main__":
    speak("Initializing Jarvis...")
    while True:
    # listen for the wake phrase "JARVIS"
    # get audio from the microphone
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening!")
        audio = r.listen(source)
    command = r.recog
    # recognize the speech with the help of Sphinx
    try:
        print("Sphinx")
