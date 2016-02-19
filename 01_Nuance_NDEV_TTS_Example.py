import requests
import winsound
import time
import random
import string

# Set your TTS Text here
ttsText = "Hello World..."

# Setting TTS end-point and app creds
appId = "NMDPTRIAL_ryan_bradon_8x8_com20150212225315"
appKey = "572d515114aa3e0e073a0eadf8c241b5da60dd7a2ad12169ddde47b2b869140f\
966560ab0f9eb916d8c7c4d1890586646564de8f3500f913de40c596aadaa540"
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
req = requests.post(ttsUrl + ttsEndpoint +
                    '?appId=' + appId +
                    '&appKey=' + appKey +
                    '&id=' + randomID +
                    '&ttsLang=' + ttsLang +
                    '&voice=' + voice,
                    data=ttsText,
                    headers=headers)

# Create wave file as Bytes (write binary mode is 'wb')
wav_file = open('tts_' + time.strftime("%H_%M_%S") + '.wav', 'wb')
wav_file.write(req.content)
wav_file.close()

# Play file using Windows
play_wav = winsound.PlaySound('tts_' + time.strftime("%H_%M_%S") +'.wav', winsound.SND_FILENAME)

# Play file using Linux
# https://pypi.python.org/pypi/pysox/0.3.6.alpha
# http://stackoverflow.com/questions/8195544/how-to-play-wav-data-right-from-memory