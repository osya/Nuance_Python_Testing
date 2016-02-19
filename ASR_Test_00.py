import requests
import random
import string

# What file to open??
asr_file = open('file.wav', 'rb').read()

# Setting TTS end-point and app creds
appId = "NMDPTRIAL_ryan_bradon_8x8_com20150212225315"
appKey = "572d515114aa3e0e073a0eadf8c241b5da60dd7a2ad12169ddde47b2b869140f\
966560ab0f9eb916d8c7c4d1890586646564de8f3500f913de40c596aadaa540"
asrUrl = "https://dictation.nuancemobility.net/NMDPAsrCmdServlet"
asrEndpoint = "/dictation"

# Set a random ID via list comprehension, randomizing a-z, A-Z and digits 0-9
randomID = ''.join([random.choice(string.ascii_letters + string.digits) for n in range(8)])

# HTTP Request Headers
headers = {
    "Content-Type": "audio/x-wav;codec=pcm;bit=16;rate=8000",
    "Content-Length": len(asr_file),
    "Accept": "text/plain",
    # "Transfer-Encoding": "chunked",
    "Accept-Topic": "Dictation",
    "Accept-Language": "en-US"

}

req = requests.post(asrUrl + asrEndpoint +
                    '?appId=' + appId +
                    '&appKey=' + appKey +
                    '&id=' + randomID,
                    data=asr_file,
                    headers=headers)

print(req.text)