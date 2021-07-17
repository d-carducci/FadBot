import tweepy
import os
from json import load
from dotenv import load_dotenv
load_dotenv()

with open('text.json', 'r') as text_file:
    text = load(text_file)
    intro_dict = text['intros']
    quality_dict = text['qualities']
    animal_dict = text['animals']
    buyer_dict = text['buyers']


def create_intro(*args):
    intro = ''
    for arg in args:
        intro += intro_dict[arg]
    return intro

def login():

    consumer_key = os.environ.get('KEY')
    consumer_secret = os.environ.get('KEY_SECRET')
    access_token = os.environ.get('TOKEN')
    access_secret = os.environ.get('TOKEN_SECRET')

    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_secret)
    api = tweepy.API(auth)
    return api

api = login()
try:
    api.verify_credentials()
    print("Authentication OK")
except:
    print("Error during authentication")

char_lim = 280

for key, list in animal_dict.items():
    tweet = ''.join(list)
    print(tweet)
    print(-len(tweet) + char_lim)



'''
consumer_key = "2zsbF13GobWZpoLMJF3rPBQ4T"
consumer_secret = "xbvXWMumsj9BQFRlFVSIUYJrpc73WZbOAAUJV3YiQKCKeIIqlk"

access_token = "357633629-cZglWFyrjRE8sewL4Pb7Er4P4np0LYSm6dEOqLnz"
access_secret = "m6150haorpimbqM8truGkeYRO8PVMqiTjttkS3a8ppTic"



api = tweepy.API(auth)

first = api.update_status("[Apologies, doing some tests to automate updates]")
second = api.update_status(status="[Seeing if I can get it to do threads]",
                                 in_reply_to_status_id=first.id,
                                 auto_populate_reply_metadata=True)

media1 = api.media_upload("images\\Midnighter.png")
media2 = api.media_upload("images\\ZailorWPI.png")
media3 = api.media_upload("images\\Ambassador.png")

api.create_media_metadata(media1.media_id, "Dreary Midnighter")
print(media1.media_id)

third = api.update_status(status="[And seeing if I can get it to add pictures]",
                          media_ids=[1416339064991670273],
                                 in_reply_to_status_id=second.id,
                                 auto_populate_reply_metadata=True)
'''