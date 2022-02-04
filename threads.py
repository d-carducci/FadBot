from math import sqrt

intro_dict={"antiquity": "The buyers of #FallenLondon look to the past! This week's fad quality is Antiquity.\n\n",
            "amalgamy": "#FallenLondon is just oozing with interest! This week's fad quality is Amalgamy.\n\n",
            "menace": "A taste for the macabre invests #FallenLondon! This week's fad quality is Menace.\n\n",
            "bird": "It seems everyone has been dreaming feathers! This week's zoological mania is for Birds.\n\n",
            "reptile": "The crowd at the Bone Market is simply roaring! This week's zoological mania is for Reptiles.\n\n",
            "amphibian": "The Bone Market croaks with activity! This week's zoological mania is for Amphibians.\n\n",
            "fish": "Zailors swarm the Bone Market! This week's zoological mania is for Fish.\n\n",
            "insect": "The Bone Market is crawling with buyers! This week's zoological mania is for Insects.\n\n",
            "arachnid": "Buyers are really eyeing the stalls! This week's zoological mania is for Arachnids. \n\n",
            "enthusiast": "An Enthusiast in Skulls is here, attracted by rumours of many-headed skeletons!",
            "midnighter": "A Dreary Midnighter has descended from the surface in search of realistic skeletons!",
            "phantasist": "A Colourful Phantasist would like to see your most unbelievable skeletons!",
            "malacologist": "An Ingenuous Malacologist wants molluscs, and squids, and anything with lots of tentacles!",
            "salesman": "An Enterprising Boots Salesman is on the lookout for many-legged skeletons to display!"}

quality_dict = {"antiquity":
                    ("*Fluctuations: Antiquity week*\n\n"
                     "- The Enthusiast will give one additional Unprovenanced Artifact;\n"
                     "- The Zailor and the Author will give additional secondary rewards equal to half " 
                     "the skeleton's Antiquity;\n"
                     "- The Ambassador will give Tailfeathers equal to 0.8*(Antiquity^2.1)."),
                "amalgamy":
                    ("*Fluctuations: Amalgamy week*\n\n"
                     "- The Servant will give 5 additional Ambiguous Eoliths;\n"
                     "- The Zailor and the Collector will give additional secondary rewards " 
                     "equal to half the skeleton's Amalgamy;\n"
                     "- The Entrepreneur will give Memories of Distant Shores equal to 4*(Amalgamy^2.1)."),
                "menace":
                    ("*Fluctuations: Menace week*\n\n"
                     "- Mrs Plenty will give one additional Basket of Rubbery Pies;\n"
                     "- The Author and the Collector will give additional secondary rewards "
                     "equal to half the skeleton's Menace;\n"
                     "- The Teller of Terrors will give Royal Blue Feathers equal to 4*(Menace^2.1).")
                }

animal_dict = {"bird": (
      "*Zoological Mania: Birds*\n"
      "\n"
      "Declaring a skeleton a Bird will increase its value by 10%!\n"
      "To do so you must have a Comprehensive Study of Avian Anatomies, Oneiric and Otherwise "
      "and your skeleton must have ANY # of skulls, EXACTLY 2 wings and 2 legs, NO arms/fins, and AT MOST 1 tail."),
    "reptile": (
      "*Zoological Mania: Reptiles*\n"
      "\n"
      "Declaring a skeleton a Reptile will increase its value by 10%!\n"
      "To do so you must have a Complete Account of Frogs, Toads, and Other Croaking Beasts "
      "and your skeleton must have EXACTLY 1 skull, AT MOST 4 legs, NO arms/fins/wings, and EXACTLY 1 tail."
    ),
    "amphibian": (
      "*Zoological Mania: Amphibians*\n"
      "\n"
      "Declaring a skeleton an Amphibian will increase its value by 10%!\n"
      "To do so you must have a Complete Account of Frogs, Toads, and Other Croaking Beasts "
      "and your skeleton must have EXACTLY 1 skull, EXACTLY 4 legs, NO arms/wings/fins, and NO tail."
    ),
    "fish": (
      "*Zoological Mania: Fish*\n"
      "\n"
      "Declaring a skeleton a Fish will increase its value by 15%!\n"
      "To do so you must have an Unexpurgated Accounting of the Anatomies of Aquatic Life-forms "
      "and your skeleton must have EXACTLY 1 skull, AT LEAST 2 fins, NO arms/legs/wings, and AT MOST 1 tail."
    ),
    "insect": (
      "*Zoological Mania: Insects*\n"
      "\n"
      "Declaring a skeleton an Insect will increase its value by 15%!\n"
      "To do so you must have a Survey of Arachnids and Insects Native to the Neath and Unterzee "
      "and your skeleton must have EXACTLY 1 skull and 6 legs, AT MOST 4 wings, and NO arms/fins/tails."
    ),
    "arachnid": (
      "*Zoological Mania: Arachnids*\n"
      "\n"
      "Declaring a skeleton an Arachnid will increase its value by 15%!\n"
      "To do so you must have a Survey of Arachnids and Insects Native to the Neath and Unterzee "
      "and your skeleton must have EXACTLY 8 legs, AT MOST 1 tail, and NO skulls/arms/fins/tails."
    )
  }

buyer_dict = {
    "enthusiast": (
      "*Occasional Buyer: Enthusiast in Skulls*\n"
      "\n"
      "He wants skeletons with AT LEAST 2 skulls; "
      "he pays in Pieces of Rostygold equal to your skeleton's value in pennies and in "
      "Vital Intelligence equal to (Skulls - 1)^1.8; he gives 1 Exhaustion for every 4 Vital Intelligence."
    ),
    "midnighter": (
      "*Occasional Buyer: Dreary Midnighter*\n"
      "\n"
      "He wants NO chimeras or Curators and NO Amalgamy or Support for a Counter-Church Theology; "
      "he pays in Surface Currency equal to your skeleton's value/3 + 100 (3e bonus) and "
      "one Vienna Opening (2.5e bonus); he gives no exhaustion.\n"
    ),
    "phantasist": (
      "*Occasional Buyer: Colourful Phantasist\n"
      "\n"
      "She wants AT LEAST 2 Implausibility and AT LEAST 4 of either Antiquity/Amalgamy/Menace; "
      "she has several sale options which pay out in a variety of 0.5e and 2.5e items; "
      "she gives 1 Exhaustion for every 20 units of secondary payout."
    ),
    "malacologist": (
      "*Occasional Buyer: Ingenuous Malacologist\n"
      "\n"
      "He wants AT LEAST 4 tentacles; "
      "he pays in Preserved Surface Blooms equal to your skeleton's value/250 + 1 (2.5e bonus) and "
      "in Volumes of Collated Research equal to Tentacles^2.2/5; "
      "he gives Exhaustion equal to Tentacles^2.2/100."
    ),
    "salesman": (
      "*Occasional Buyer: Enterprising Boots Salesman\n"
      "\n"
      "He wants skeletons with NO Menace/Amalgamy and AT LEAST 4 legs; "
      "he pays Whisper-Satin equal to your skeleton's value in pennies/50 and "
      "Ostentatious Diamonds equal to Legs^2.2; "
      "he gives Exhaustion equal to Legs^2/100 (rounded down)."
    )
  }

extra_dict = {
    "phantasist": (
      "Each option pays 0.5e items equal to your skeleton's value/50 +2 (1e bonus) and 2.5e items "
      "equal to Implausibility*Quality. The options are:"
      "\n"
      "-Amalgamy: Hinterland Scrip and Bazaarine Poetry.\n"
      "-Menace: Solacefruit and Stygian Ivory.\n"
      "-Antiquity: Memories of Light and Scintillack."
    ),
    "antiquity": (
      "The Antiquity thresholds and secondary profit for the Ambassador this week are:\n"
      "\n"
      "- 4 Antiquity = 0 Exh. 37.5e\n"
      "- 7 Antiquity = 1 Exh. 120e\n"
      "- 8 Antiquity = 2 Exh. 157.5e\n"
      "- 9 Antiquity = 3 Exh. 202.5e\n"
      "- 11 Antiquity = 4 Exh. 307.5e\n"
      "- 14 Antiquity = 7 Exh. 510e"
    ),
    "amalgamy": (
      "The Amalgamy thresholds and secondary profit for the Entrepreneuer this week are:\n"
      "\n"
      "- 4 Amalgamy = 0 Exh. 37e\n"
      "- 7 Amalgamy = 1 Exh. 119e\n"
      "- 8 Amalgamy = 2 Exh. 157.5e\n"
      "- 9 Amalgamy = 3 Exh. 202e\n"
      "- 11 Amalgamy = 4 Exh. 307.5e\n"
      "- 14 Amalgamy = 7 Exh. 510.5e"
    ),
    "menace": (
      "The Menace thresholds and bonus profit for the Teller of Terrors this week are:\n"
      "\n"
      "- 4 Menace = 0 Exh. 37e\n"
      "- 7 Menace = 1 Exh. 119e\n"
      "- 8 Menace = 2 Exh. 157.5e\n"
      "- 9 Menace = 3 Exh. 202e\n"
      "- 11 Menace = 4 Exh. 307.5e\n"
      "- 14 Menace = 7 Exh. 510.5e\n"
    )
  }

metadata_dict = {
    "antiquity": ("A collage of the in-game icons for the four buyers affected by the Antiquity fluctuations; "
                  "from left to right: the Enthusiast of the Ancient World, the Zailor with Particular Interests, "
                  "the Author of Gothic Tales, and the Investment-Minded Ambassador."),
    "amalgamy": ("A collage of the in-game icons for the four buyers affected by the Amalgamy fluctuations; "
                 "from left to right: the Tentacled Servant, the Zailor with Particular Interests, "
                 "the Rubbery Collector, and the Tentacled Entrepreneur."),
    "menace": ("A collage of the in-game icons for the four buyers affected by the Menace fluctuations;"
               "from left to right: Mrs Plenty, the Author of Gothic Tales, the Rubbery Collector, "
               "and the Teller of Terrors.")
  }

master_dict = {'intro ' + key: tweet for key, tweet in intro_dict.items()}
master_dict.update({'quality ' + key: tweet for key, tweet in quality_dict.items()})
master_dict.update({'animal ' + key: tweet for key, tweet in animal_dict.items()})
master_dict.update({'buyer ' + key: tweet for key, tweet in buyer_dict.items()})
master_dict.update({'extra ' + key: tweet for key, tweet in extra_dict.items()})
master_dict.update({'metadata ' + key: tweet for key, tweet in metadata_dict.items()})

char_limit = 280

def dump_text():
    with open('text_dump.txt', 'w') as dump_file:
        for tweet in master_dict.values():
            dump_file.write(tweet)
            dump_file.write('\n\n')

def check_format(*args):

    if len(args) == 3:
        conditions = [args[0] in quality_dict.keys(),
                      args[1] in animal_dict.keys(),
                      args[2] in buyer_dict.keys()]
        if all(conditions):
            return True

    return False

def create_intro(*args):
    if check_format(*args):
        intro = ''
        for arg in args:
            intro += intro_dict[arg]
        return intro
    else:
        return False

def check_length():
    for key, tweet in master_dict.items():
        if (len(tweet)) > char_limit:
            print("error: {} tweet too long ({} characters)".format(key, len(tweet)))

def check_intro():
    line_lengths = {key: len(line) for key, line in intro_dict.items()}
    max_quality = max(line_lengths[quality] for quality in quality_dict.keys())
    max_animal = max(line_lengths[animal] for animal in animal_dict.keys())
    max_buyer = max(line_lengths[buyer] for buyer in buyer_dict.keys())
    max_intro = max_quality + max_buyer + max_animal
    if max_intro > char_limit:
        print('error: intro tweet potentially too long')
        print('max quality line: {}'.format(max_quality))
        print('max animal line: {}'.format(max_animal))
        print('max buyer line: {}'.format(max_buyer))


def print_quadratic_thresholds():
    for i in range(8):
        max_qual = 5 * (sqrt(i + 1) - 0.001) // 1
        TE_pay = 0.5 * round(4 * max_qual ** 2.1)
        IMA_pay = 2.5 * round(0.8 * max_qual ** 2.1)
        print("{} exhaustion = {} quality = {} echoes (TE) = {} echoes (IMA)".format(i, max_qual, TE_pay, IMA_pay))

def print_occasional_thresholds():
    for i in range(8):
        max_qual = 10*(sqrt(i + 1) - 0.001) // 1
        BSM_pay = 0.5 * round(max_qual ** 2.2)
        IM_pay = 2.5 * round(0.2 * max_qual ** 2.2)
        print("{} exhaustion = {} quality = {} echoes (BSM) = {} echoes (IM)".format(i, max_qual, BSM_pay, IM_pay))

if __name__ == "__main__":
    dump_text()
    check_intro()
    check_length()
    print_occasional_thresholds()
    #print_thresholds()