import requests
import winsound
import time
import random
import string
import urllib
import argparse

# TODO: do not store parameters in file
# TDO: PEP-8
# TODO: commit & push

# Set your TTS Text here
ttsText = "Hello World..."

# Setting TTS end-point and app creds
appId = "NMDPTRIAL_emoshape20130902191817"
appKey = "d605c70d846155dfe7397bbfa56d4b785588df2473869074db6f6cf387328d5d37546bbbb5c09a9cf9165c9e83a716d82ff5fca27b8c1757fc834a83b5d7e0ec"
ttsUrl = "https://tts.nuancemobility.net:443/NMDPTTSCmdServlet"
ttsEndpoint = "/tts"

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
params = urllib.urlencode({'appId': appId, 'appKey': appKey, 'id': randomID, 'ttsLang': ttsLang, 'voice': voice})
url = '%s%s?%s' % (ttsUrl, ttsEndpoint, params)
req = requests.post(url, data=ttsText, headers=headers)

# Create wave file as Bytes (write binary mode is 'wb')
wav_file = open('tts_' + time.strftime("%H_%M_%S") + '.wav', 'wb')
wav_file.write(req.content)
wav_file.close()

# Play file using Windows
play_wav = winsound.PlaySound('tts_' + time.strftime("%H_%M_%S") +'.wav', winsound.SND_FILENAME)

# Play file using Linux
# https://pypi.python.org/pypi/pysox/0.3.6.alpha
# http://stackoverflow.com/questions/8195544/how-to-play-wav-data-right-from-memory

if __name__ == '__main__':
    p = argparse.ArgumentParser()
    p.add_argument('-m', dest='message', help='your message')
    p.add_argument('-s', dest='input_source', help='type or voice', default='type')
    p.add_argument('-i', dest='image_file', help='The image you\'d like to label.', default='image.jpg')
    p.add_argument("-k", dest='api_key', help='API key', required=True)
    p.add_argument('--max-results', default=1)
    args = p.parse_args()