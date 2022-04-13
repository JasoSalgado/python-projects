"""
Virtual assistant
"""
# Modules
from mimetypes import init
import pyttsx3
import speech_recognition as sr
import pywhatkit
import yfinance as yf
import pyjokes
import webbrowser
import datetime
import wikipedia

# Listen our microphone and returns audio as a text
def transform_audio_to_text():
    """
    Transform audio into text
    """
    # Store recognizer in a variable
    r = sr.Recognizer()

    # Config microphone
    with sr.Microphone() as origin:

        # Waiting time
        r.pause_threshold = 0.8

        # Report that starts the recording
        print('Ya puedes hablar.')

        # Save what microphone listens
        audio = r.listen(origin)

        try:
            # Look for at Google
            request = r.recognize_google(audio, language='es-mx')

            # Testing audio
            print('Dijiste: ' + request)

            # Return request
            return request
        
        # In case of audio is not readable
        except sr.UnknownValueError:
            # Test audio was not understood
            print('No entendí.')

            # Return error
            return 'Estoy esperando...'
        
        # If we cannot transform audio into text
        except sr.RequestError:
            print('Estoy esperando...')
        
        # Unexpected error
        except:
            print('Algo salió mal.')


# Assistant can be listening
def talk(message):
    # Turn on pyttsx3 on
    engine = pyttsx3.init()

    # Pronounce message
    engine.say(message)
    engine.runAndWait()


# What day is today
def ask_day():
    # Create variable with today data
    day = datetime.date.today()
    print(day)

    week_day = day.weekday()
    print(week_day)

    # Dict with days´ name
    calendar = {0: 'Lunes',
                1: 'Martes',
                2: 'Miércoles',
                3: 'Jueves',
                4: 'Viernes',
                5: 'Sábado',
                6: 'Domingo'}
    
    talk(f'Hoy es {calendar[week_day]}')


# What time is it?
def ask_time():
    # Time data
    hour = datetime.datetime.now()
    print(hour)
    hour = f'En este momento son las {hour.hour} horas con {hour.minute} minutos.'

    # Say hour
    talk(hour)


# Initial greeting
def init_greeting():
    # Variable with time data
    hour = datetime.datetime.now()
    if hour.hour < 6 or hour.hour > 20:
        momentum = 'Buenas noches'
    elif hour.hour >= 6 and hour.hour < 13:
        momentum = 'Buen día'
    else:
        momentum = 'Buenas tardes'
    
    # Say hi
    talk(f'{momentum} Hola, soy Python Asistente Personal. ¿En qué puedo ayudarte?')


# Assistant
def request_things():
    # Greeting
    init_greeting()

    # 
    start = True

    # Central loop
    while start:
        # Activate micro and save the request in a string
        request = transform_audio_to_text().lower()

        if 'abrir youtube' in request:
            talk('Estoy abriendo youtube')
            webbrowser.open('https://www.youtube.com')
            continue
        
        elif 'abrir navegador' in request:
            webbrowser.open('https://www.google.com')
            continue
        
        elif 'qué día es hoy' in request:
            ask_day()
            continue
        elif 'qué hora es' in request:
            ask_time()
            continue
        elif 'busca en wikipedia' in request:
            talk('Buscando en Wikipedia')
            request = request.replace('busca en wikipedia', '')
            wikipedia.set_lang('es')
            result = wikipedia.summary(request, sentences=1)
            talk('Wikipedia dice lo siguiente: ')
            talk(result)
        elif 'busca en internet' in request:
            talk('Estoy buscando...')
            request = request.replace('busca en internet', '')
            pywhatkit.search(request)
            talk('I found this')
            continue
        elif 'reproducir' in request:
            talk('Estoy reproduciendo...')
            pywhatkit.playonyt(request)
            continue
        elif 'broma' in request:
            talk(pyjokes.get_joke('es'))
            continue
        elif 'precio de criptomonedas' in request:
            cripto = request.split('de')[-1].strip()
            wallet = {'bitcoin': 'BTC',
                        'ethereum': 'ETH',
                        'solana': 'SOL'}
            try:
                looked_cripto = wallet(cripto)
                looked_cripto = yf.Ticker(looked_cripto)
                current_price = looked_cripto.info['regularMarketPrice']
                talk(f'Lo encontré. El precio de {cripto} es {current_price}')
                continue
            except:
                talk('No encontré nada')
                continue
        elif 'adiós' in request:
            talk('Hasta luego.')
            break
