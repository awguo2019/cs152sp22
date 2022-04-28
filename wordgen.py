import nltk
from nltk.corpus import wordnet as wn

try:
    nltk.data.find('wordnet')
except LookupError:
    nltk.download('wordnet')

try:
    nltk.data.find('omw-1.4')
except LookupError:
    nltk.download('omw-1.4')

list_of_nouns = [
    'time',
    'love',
    'day',
    'light',
    'night',
    'man',
    'world',
    'eyes',
    'life',
    'water',
    'hand',
    'white',
    'air',
    'body',
    'death',
    'face',
    'dead',
    'heart',
    'years',
    'rain',
    'sand',
    'fire',
    'God',
    'sky',
    'sun',
    'wind',
]

default_adjs = ["happy", "sad", "joyful", "angry", "confused",
                "nostalgic", "jealous", "good", "evil", "amazing", "heroic"]


# Generate a list of adjectivese for each noun and for each adjective, print out the adjective and the noun.
with open('poem_gen/prompt_words.txt', 'a+') as f:
    for noun in list_of_nouns:
        list_of_adjs = [word for synset in wn.synsets(
            noun, pos=wn.ADJ) for word in synset.lemma_names()]

        # Deduplicate list
        list_of_adjs = list(dict.fromkeys(list_of_adjs))

        if not list_of_adjs:
            list_of_adjs = default_adjs

        for adj in list_of_adjs:
            f.write(f"{adj}, {noun}\n")
'''
with open('poem_gen/prompt_words-love.txt', 'a+') as f:
    noun = "love"
    list_of_adjs = [word for synset in wn.synsets(
        noun, pos=wn.ADJ) for word in synset.lemma_names()]
    # Deduplicate list
    list_of_adjs = list(dict.fromkeys(list_of_adjs))
    if not list_of_adjs:
        list_of_adjs = default_adjs
    for adj in list_of_adjs:
        f.write(f"{adj}, {noun}\n")
'''