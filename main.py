import tweepy
from json import load
import sys

dump_text = 1

with open('text.json', 'r') as text_file:
    text = load(text_file)
    categories = text.keys()
    intro_dict = text['intros']
    quality_dict = {key: ''.join(lines) for key, lines in text['qualities'].items()}
    animal_dict = {key: ''.join(lines) for key, lines in text['animals'].items()}
    buyer_dict = {key: ''.join(lines) for key, lines in text['buyers'].items()}
    extra_dict = {key: ''.join(lines) for key, lines in text['extras'].items()}
    metadata_dict = {key: ''.join(lines) for key, lines in text['metadata'].items()}

    master_dict = {'intro_' + key: tweet for key, tweet in intro_dict.items()}
    master_dict.update({'quality_' + key: tweet for key, tweet in quality_dict.items()})
    master_dict.update({'animal_' + key: tweet for key, tweet in animal_dict.items()})
    master_dict.update({'buyer_' + key: tweet for key, tweet in buyer_dict.items()})
    master_dict.update({'extra_' + key: tweet for key, tweet in extra_dict.items()})
    master_dict.update({'metadata_' + key: tweet for key, tweet in metadata_dict.items()})

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
    with open('twtcred.json', 'r') as cred_file:
        keys = load(cred_file)
        consumer_key = keys['KEY']
        consumer_secret = keys['KEY_SECRET']
        access_token = keys['TOKEN']
        access_secret = keys['TOKEN_SECRET']

    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_secret)
    api = tweepy.API(auth)
    try:
        api.verify_credentials()
        print("Authentication OK")
    except:
        print("Error during authentication")
    return api


def update(quality, animal, buyer):
    intro = create_intro(quality, animal, buyer)
    api = login()
    tweets = [intro, quality_dict[quality], extra_dict[quality], animal_dict[animal], buyer_dict[buyer]]
    # tweets = ['test 1', 'test 2', 'test 3', 'test 4']
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
            print(e)
            sys.exit('Status update failed')

        img_id = None

    print('Status update successful')


update_input = input("Enter the Quality/Animal/Buyer, separated by spaces: ")
fad_data = update_input.split(' ')
update(*fad_data)

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
