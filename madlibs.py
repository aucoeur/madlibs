# MadLibs Spec: https://docs.google.com/document/d/1suR3hzqfGSL9o99rNbDrcU0N1Z47EREubP38IY4Ptuc/edit#heading=h.i5zc39w8ruz2

# Story Template
# Dear Diary,
# I've been here for [LOW NUMBER] days.  Today I woke up with [LOW NUMBER] [INSECT] bites.  At least, it's not a [INSECT] bite.  It's been [ADJECTIVE].  I love the [ADJECTIVE] weather here but the [NOUN] leaves much to be desired.  School is [ADVERB] ramping up.  I'm [ADJECTIVE]. My [NOUN] is eager to [VERB] soon.  I hope [VERB-ING] won't be too much of an issue! 
# Love, [NAME]    

from string import Template

# input_words = {
#     'low_num': '3',
#     'num': '10',
#     'bug': 'mosquito',
#     'animal': 'cat',
#     'adj': 'frustrating',
#     'adj2': 'windy',
#     'adj3': 'stoked',
#     'noun': 'hills',
#     'noun2': 'family'
#     'adverb': 'quickly',
#     'verb': 'visit',
#     'verb2': 'driving'}

# List of keys
key_list = ["low_num", "num", "bug", "animal", "adj", "adj2", "adj3", "noun", "noun2", "adverb", "verb", "verb2"]

# Initialize dictionary
input_words = dict.fromkeys(key_list, None)

# Add words to dictionary
def add_word():
    for word_type, value in input_words.items():
        value = input('Enter a ' + word_type + ": ")
        input_words[word_type] = value
        
add_word()

story = Template('Dear Diary,\nI\'ve been here for $low_num days.  Today I woke up with $num $bug bites.  At least, it\'s not a $animal bite.  It\'s been $adj.  I love the $adj2 weather here but the $noun leaves much to be desired.  School is $adverb ramping up.  I\'m $adj3. My $noun2 is eager to $verb soon.  I hope $verb2 won\'t be too much of an issue!\nLove, [NAME]')

print(story.substitute(input_words))