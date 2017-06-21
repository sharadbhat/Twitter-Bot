import tweepy
import requests
import datetime

consumerKey = "********"
consumerSecret = "**********"

accessKey = "*************"
accessSecret = "**************"

auth = tweepy.OAuthHandler(consumerKey, consumerSecret)
auth.set_access_token(accessKey, accessSecret)

twitterAPI = tweepy.API(auth)
count = 0



def downloadImage():
    while True:
        try:
            f = open('image.jpg','wb')
            f.write(requests.get('https://unsplash.it/1920/1080/?random').content)
            f.close()
            break
        except:
            print("Retrying downloading")
            time.sleep(2 * 60)



def uploadImage(count):
    try:
        now2 = datetime.datetime.now()
        twitterAPI.update_with_media("image.jpg", status=("Wallpaper #" + str(count)))
        print("Last image uploaded at " + str(now2.hour) + ":" + str(now2.minute))
        os.remove("image.jpg")
        time.sleep(120)
    except:
        print("Retrying uploading")
        time.sleep(2 * 60)


while True:
    count += 1
    downloadImage()
    now = datetime.datetime.now()
    while now.minute != 0:
        if now.minute < 57:
            time.sleep((60 - now.minute - 1) * 60)
        now = datetime.datetime.now()
        if now.minute == 0:
            uploadImage(count)
            break
