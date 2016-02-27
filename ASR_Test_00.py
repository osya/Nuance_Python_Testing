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

    # write audio to a WAV file
    with open('microphone-results.wav', "wb") as f:
        f.write(audio.get_wav_data())

    # What file to open??
    with open('microphone-results.wav', 'rb') as asr_file:
        asr_file_content = asr_file.read()

        # Set a random ID via list comprehension, randomizing a-z, A-Z and digits 0-9
        randomID = ''.join([random.choice(string.ascii_letters + string.digits) for n in range(8)])

        # HTTP Request Headers
        headers = {
            "Content-Type": "audio/x-wav;codec=pcm;bit=16;rate=8000",
            "Content-Length": len(asr_file_content),
            "Accept": "text/plain",
            # "Transfer-Encoding": "chunked",
            "Accept-Topic": "Dictation",
            "Accept-Language": "en-US"
        }

        params = urllib.urlencode({'appId': args.app_id, 'appKey': args.app_key, 'id': randomID})
        url = '%s%s?%s' % (args.asr_uri, args.asr_endpoint, params)
        req = requests.post(url, data=asr_file_content, headers=headers)
    print(req.text)
