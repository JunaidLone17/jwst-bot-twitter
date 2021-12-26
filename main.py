from requests.sessions import session
import requests
import tweepy
from time import sleep
from requests_html import HTMLSession
import math
import os
import dotenv

dotenv.load_dotenv()
filename = 'totweet.jpg'
#Get Keys from Twitter Developer Portal
consumer_key = ""
consumer_secret = ""
key = ""
secret = ""
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(key, secret)
api = tweepy.API(auth)

while True:
    try:
        r = requests.get('http://3.141.6.183:8080')
        message = str(r.json()["Distance"]) + ". \n" + r.json(
        )["Deployment"] + "\n" + r.json()["eventtime"] + "\n Image: "
        picurl = r.json()["imglink"]
        request = requests.get(picurl, stream=True)
        if request.status_code == 200:
            with open(filename, 'wb') as image:
                for chunk in request:
                    image.write(chunk)
        api.update_status_with_media(message, filename)
    except:
        print("Anything Wrong")
    sleep(1800)
