import tweepy
import os
from json import load
from dotenv import load_dotenv
load_dotenv()

dump_text = 1

with open('text.json', 'r') as text_file:
    text = load(text_file)
    categories = text.keys()
    intro_dict = text['intros']
    quality_dict = {key: ''.join(list) for key, list in text['qualities'].items()}
    animal_dict = {key: ''.join(list) for key, list in text['animals'].items()}
    buyer_dict = {key: ''.join(list) for key, list in text['buyers'].items()}
    extra_dict = {key: ''.join(list) for key, list in text['extras'].items()}

    master_dict = {'intro_' + key: tweet for key, tweet in intro_dict.items()}
    master_dict.update({'quality_' + key: tweet for key, tweet in quality_dict.items()})
    master_dict.update({'animal_' + key: tweet for key, tweet in animal_dict.items()})
    master_dict.update({'buyer_' + key: tweet for key, tweet in buyer_dict.items()})
    master_dict.update({'extra_' + key: tweet for key, tweet in extra_dict.items()})

    if dump_text:
        with open('text_dump.txt', 'w') as dump_file:
            for tweet in master_dict.values():
                dump_file.write(tweet)
                dump_file.write('\n\n\n')


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

char_lim = 280


def update(quality, animal, buyer):
    intro = create_intro(quality, animal, buyer)
    api = login()
    tweets = [intro, quality_dict[quality], animal_dict[animal], buyer_dict[buyer]]
    reply_id = None
    for tweet in tweets:
        status = api.update_status(status=tweet,
                                 in_reply_to_status_id=reply_id,
                                 auto_populate_reply_metadata=True)
        reply_id = status.id


'''

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