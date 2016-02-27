import requests
import winsound
import time
import random
import string
import urllib
import argparse

if __name__ == '__main__':
    p = argparse.ArgumentParser()
    p.add_argument('-a', dest='app_id')
    p.add_argument('-k', dest='app_key')
    p.add_argument('--tts_url')
    p.add_argument('--tts_endpoint')
    args = p.parse_args()

    # Set your TTS Text here
    ttsText = "Hello World..."

    # Available Sources, http://dragonmobile.nuancemobiledeveloper.com/public/index.php?task=supportedLanguages
    ttsLang = "en_US"
    voice = "Susan"

    # Set a random ID via list comprehension, randomizing a-zA-Z and digits
    randomID = ''.join([random.choice(string.ascii_letters + string.digits) for n in range(8)])

    # HTTP Request Headers
    headers = {
        "Content-Type": "text/plain",
        "Accept": "audio/x-wav"
    }

    # Use Requests to send POST message with Query String
    params = urllib.urlencode({'appId': args.app_id, 'appKey': args.app_key, 'id': randomID, 'ttsLang': ttsLang,
                               'voice': voice})
    url = '%s%s?%s' % (args.tts_url, args.tts_endpoint, params)
    req = requests.post(url, data=ttsText, headers=headers)

    # Create wave file as Bytes (writ binary mode is 'wb')
    filename = 'tts_%s.wav' % time.strftime("%H_%M_%S")
    with open(filename, 'wb') as wav_file:
        wav_file.write(req.content)

    # Play file using Windows
    play_wav = winsound.PlaySound(filename, winsound.SND_FILENAME)

    # Play file using Linux
    # https://pypi.python.org/pypi/pysox/0.3.6.alpha
    # http://stackoverflow.com/questions/8195544/how-to-play-wav-data-right-from-memory
