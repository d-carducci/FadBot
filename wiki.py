import requests
from re import search
import os

address_dict = {'quality': 'https://fallenlondon.wiki/wiki/Bone_Market_Fluctuations:',
                'animal': 'https://fallenlondon.wiki/wiki/Zoological_Mania:',
                'buyer': 'https://fallenlondon.wiki/wiki/Occasional_Buyer:'}

regex_string = r'Current value: ([\w\s]+)</p>'

headers = {
    'User-Agent': 'FadBot/1.1 (twitter.com/bonemarketfads) python requests',
    'From': os.environ.get('OWNER_MAIL')}

wiki_dict = {"Antiquity": "antiquity",
            "Amalgamy": "amalgamy",
            "Menace": "menace",
            "Birds": "bird",
            "Reptiles": "reptile",
            "Amphibians": "amphibian",
            "Fish": "fish",
            "Insects": "insect",
            "Arachnids": "arachnid",
            "An Enthusiast in Skulls": "enthusiast",
            "A Dreary Midnighter": "midnighter",
            "A Colourful Phantasist": "phantasist",
            "An Ingenuous Malacologist": "malacologist",
            "An Enterprising Boot Salesman": "salesman"}

def fetch_current_value(fad):
    trial = requests.get(address_dict[fad], headers=headers)
    page = trial.content.decode("utf-8")
    attempt = search(regex_string, page)

    return attempt.group(1)

def fetch_BM_values():

    wiki_values = []
    for quality in ('quality', 'animal', 'buyer'):
        value = fetch_current_value(quality)
        wiki_values.append(value)

    values = [wiki_dict[quality] for quality in wiki_values]
    return values

if __name__ == '__main__':

    for key in address_dict.keys():
        print(fetch_current_value(key))

    test1 = 'Current value: prova prova prova</p>'
    test2 = 'Current value: prova prova dio prova</p>'
    test3 = 'Current value: prova</p>'
    tests = (test1, test2, test3)
    reg = regex_dict['buyer']
    for test in tests:
        attempt = search(reg, test)
        print(attempt.group(1))
