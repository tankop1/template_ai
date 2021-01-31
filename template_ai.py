import warnings
import speech_recognition as sr
import pyttsx3 as p
import random

# ----------------------------- MAIN FUNCTIONALITY -------------------------

# Ignores warning messages
warnings.filterwarnings('ignore')

# Instantinizes pyttsx3 object
engine = p.init()

# Detirmines gender of voice
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

# Records audio and returns in form of string
def recordAudio():

    # Records audio
    r = sr.Recognizer() # Creates recognizer object

    # Opens the microphone to recording
    with sr.Microphone() as source:
        audio = r.listen(source)

    # Uses Google speech recognition to return string
    data = ''

    try:
        data = r.recognize_google(audio)
        print("You said: " + data)
    except sr.UnknownValueError: # Checks for unknown errors
        print('Google speech recognition encountered an unknown error.')
    except sr.RequestError as e:
        print('Request results from Google service error: ' + e)
    
    return data


# Controls wake words
def wakeWord(text):
    WAKE_WORDS = ['jarvis', 'jarvy']

    text = text.lower() # Converts text to lowercase
    for phrase in WAKE_WORDS:
        if phrase in text:
            return True
    
    # Only executes if wake word isn't found
    return False

# ------------------------- SKILL FUNCTIONS BELOW ---------------------------

# WHEN WRITING YOUR SKILL FUNCTION, PUT A COMMENT WITH YOUR NAME AND A DESCRIPTION OF THE SKILL ABOVE IT

# EXAMPLE SKILL FUNCTION
def randomGreeting(text):

    GREETING_INPUTS = ['hi', 'whassup', 'whats up', 'what\'s up', 'hello']

    GREETING_RESPONSES = ['Hey, what\'s up?', 'How\'s it going?', 'Good to hear your voice.', 'Hello!', 'What can I do for you today?']

    # Returns random greeting if user input is a greeting
    for word in text.split():
        if word.lower() in GREETING_INPUTS:
            return random.choice(GREETING_RESPONSES)

# ------------------------- MAIN LOOP ---------------------------------------

print('Say something...')

On = True

while On:

    # Records audio at all times
    text = recordAudio()
    response = ''

    if (wakeWord(text) == True):

        # WHEN CALLING YOUR SKILL, AGAIN PUT A COMMENT WITH YOUR NAME ABOVE IT

        # CALLING EXAMPLE SKILL
        if ('hi' in text or 'whassup' in text or 'whats up' in text or 'what\'s up' in text or 'hello' in text):
            response = randomGreeting(text)

        # CALL YOUR SKILLS BELOW:

        if ('shutdown' in text or 'shut down' in text):
            response = 'Shutting down...'
            On = False     


    engine.say(response)
    engine.runAndWait()