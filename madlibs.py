# MadLibs Spec: https://docs.google.com/document/d/1suR3hzqfGSL9o99rNbDrcU0N1Z47EREubP38IY4Ptuc/edit#heading=h.i5zc39w8ruz2

# Story Template
# Dear Diary,
# I've been here for [LOW NUMBER] days.  Today I woke up with [LOW NUMBER] [INSECT] bites.  It's been [ADJECTIVE].  I love the [ADJECTIVE] weather here but the [NOUN] leaves much to be desired.  School is [ADVERB] ramping up.  I'm [ADJECTIVE]. My family is eager to visit soon.  I hope [VERB-ING] won't be too much of an issue! 
# Love, [NAME]

part_of_speech_dict = {
    "noun": "a person, place, or thing. Example: book",
    "verb": "used to describe an action, state, or occurence. Example: swim",
    "adjective": "used to describe or modify nouns or pronouns. Example: gorgeous",
    "adverb": "modifies or qualifies an adjective, verb or other adverb. Example: quickly"
}

word_dict = {
    'nouns': [], 'verbs': [], 'adjectives': [], 'adverbs': []}
# Adding words to lists
def add_noun():
    user_noun = input('Enter a noun: ')
    word_dict['nouns'].append(user_noun)
    # word_dict['nouns'][0] returns 'Book' | dict['key'][list_index]
    # word_dict.items() returns dict items

def init_prompt():
    start = input('Hello ' + player_name + '. Ready to play? ')
    if start == 'yes':
        print('OKAY')
    elif start == 'no':
        print('GOODBYE')
    else:
        print('please enter yes or no')
        init_prompt()

#def begin_game(): 

# def pos_help():

player_name = input('Hello there. What\'s your name? ')

init_prompt()