import tweepy
import requests
from datetime import datetime
import time
import itertools
import functools

consumerKey = "********"
consumerSecret = "**********"

accessKey = "*************"
accessSecret = "**************"

auth = tweepy.OAuthHandler(consumerKey, consumerSecret)
auth.set_access_token(accessKey, accessSecret)

twitterAPI = tweepy.API(auth)

log = itertools.partial(print, end="\r")


def downloadImage():
    while True:
        try:
            image = requests.get('https://unsplash.it/1920/1080/?random').content
        except requests.RequestError:
            log("Retrying downloading")
            time.sleep(2 * 60)
        else:
            break
    with open('image.jpg', 'wb') as f:
        f.write(image)
    log("Download done.")


def uploadImage(count):
    while True
        try:
            twitterAPI.update_with_media("image.jpg", status="Wallpaper #{}".format(count))
        except tweepy.TweepError:
            log("Retrying uploading")
            time.sleep(2 * 60)
        else:
            break
    log("Image #{} uploaded at {:%H:%M}".format(count, datetime.now()))


for count in itertools.count(1):
    downloadImage()
    time.sleep((60 - datetime.now().minute) * 60)
    uploadImage(count)
