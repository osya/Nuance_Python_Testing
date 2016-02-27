import requests
import random
import string
import argparse
import speech_recognition as sr
import urllib

if __name__ == '__main__':
    p = argparse.ArgumentParser()
    p.add_argument('-a', dest='app_id')
    p.add_argument('-k', dest='app_key')
    p.add_argument('--asr_uri')
    p.add_argument('--asr_endpoint')
    args = p.parse_args()

    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        print("Say something!")
        audio = r.listen(source)

    # Set a random ID via list comprehension, randomizing a-z, A-Z and digits 0-9
    randomID = ''.join([random.choice(string.ascii_letters + string.digits) for _ in range(8)])

    # HTTP Request Headers
    headers = {
        "Content-Type": "audio/x-wav;codec=pcm;bit=16;rate=8000",
        "Content-Length": len(audio.get_wav_data()),
        "Accept": "text/plain",
        # "Transfer-Encoding": "chunked",
        "Accept-Topic": "Dictation",
        "Accept-Language": "en-US"
    }

    params = urllib.urlencode({'appId': args.app_id, 'appKey': args.app_key, 'id': randomID})
    url = '%s%s?%s' % (args.asr_uri, args.asr_endpoint, params)
    req = requests.post(url, data=audio.get_wav_data(), headers=headers)
    print(req.text)
