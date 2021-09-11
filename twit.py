import tweepy
from threads import *
import sys
import os

owner_id = os.environ.get('OWNER_ID')

def login():

    consumer_key = os.environ.get('FB_KEY')
    consumer_secret = os.environ.get('FB_KEY_SECRET')
    access_token = os.environ.get('FB_TOKEN')
    access_secret = os.environ.get('FB_TOKEN_SECRET')

    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_secret)
    api = tweepy.API(auth)
    try:
        api.verify_credentials()
        print("Authentication OK")
    except:
        print("Error during authentication")
    return api


def update(api, quality, animal, buyer):
    intro = create_intro(quality, animal, buyer)
    if intro is False:
        sys.exit("Error: Invalid Fad Parameters")
    tweets = [intro, quality_dict[quality], extra_dict[quality], animal_dict[animal], buyer_dict[buyer]]
    structure = ["intro", "quality", "quality_extra", "animal", "buyer"]
    if buyer in extra_dict.keys():
        tweets.append(extra_dict[buyer])
        structure.append("buyer_extra")
    reply_id = None
    img_id = None
    for tweet, kind in zip(tweets, structure):
        if kind == 'quality':
            img = api.media_upload("images/{}.png".format(quality))
            api.create_media_metadata(img.media_id, metadata_dict[quality])
            img_id = [img.media_id]

        try:
            status = api.update_status(status=tweet, media_ids=img_id, in_reply_to_status_id=reply_id,
                                       auto_populate_reply_metadata=True)
            if status:
                print('posted {} tweet'.format(kind))
                reply_id = status.id
        except tweepy.error.TweepError as e:
            print('{} tweet failed'.format(kind))
            print(e)
            return kind


        img_id = None

    print('Status update successful')
    return -1

def contact_owner(api, text):
    api.send_direct_message(owner_id, text)

def fetch_reply(api, last_checked_id):
    latest_reply_fetched = False
    messages = api.list_direct_messages(50)
    response = {}
    for message in messages:
        if message.message_create["sender_id"] == owner_id:
            latest_reply_fetched = True
            break

    if latest_reply_fetched:
        update_input = message.message_create["message_data"]["text"]
        fad_data = update_input.split(' ')
        if check_format(*fad_data):
            response['success'] = 'valid input'
            response['data'] = fad_data
        else:
            response['success'] = 'invalid input'
    else:
        response['success'] = False

    return response

def TEST_fetch_reply(api):
    latest_reply_fetched = False
    messages = api.list_direct_messages(25)
    response = {}
    for message in messages:
        if message.message_create["sender_id"] == owner_id:
            latest_reply_fetched = True
            break

    if latest_reply_fetched:
        test_input = message.message_create["message_data"]["text"]

        if test_input == 'A':
            response['success'] = 'valid input'
        else:
            response['success'] = 'invalid input'
    else:
        response['success'] = False

    return response

if __name__ == "__main__":

    api = login()
    update_input = input("Enter the Quality/Animal/Buyer, separated by spaces: ")
    fad_data = update_input.split(' ')
    update(api, *fad_data)

