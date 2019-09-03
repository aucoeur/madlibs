# MadLibs Spec: https://docs.google.com/document/d/1suR3hzqfGSL9o99rNbDrcU0N1Z47EREubP38IY4Ptuc/edit#heading=h.i5zc39w8ruz2

from string import Template

# List of keys
key_list = ["num1", "num2", "bug", "animal", "adj", "adj2", "adj3", "noun", "noun2", "adverb", "verb", "verb2"]

# Dictionary of keys and prompt phrasing
key_name = {
    'num1': 'a number',
    'num2': 'a number',
    'bug': 'a bug',
    'animal': 'an animal',
    'adj': 'an adjective',
    'adj2': 'an adjective',
    'adj3': 'an adjective',
    'noun': 'a noun',
    'noun2': 'a noun',
    'adverb': 'an adverb',
    'verb': 'a verb',
    'verb2': 'a verb ending in "-ing"'}

# Initialize word dictionary for input words
input_words = dict.fromkeys(key_list, None)

# Ask for user inputs
def add_words():
    for word_type, name in key_name.items():
        value = input('Enter ' + str(name) + ": ")
        if word_type == 'num1' or word_type == 'num2':
            check_int(word_type, value)    
        else:
            input_words[word_type] = text_format(value)

# Check if integer
def check_int(word_type, value):
    while True:
        if (value.isdigit()):
            input_words[word_type] = text_format(value)
            break
        else:
            key = input_words.get(word_type)
            input_words.pop(key, value)
            value = input('Input was string. Enter a number: ')

# Set input words to MAGENTA and BOLD
def text_format(value):
    bold_magenta = '\033[35m\033[1m'
    reset_color = '\033[0m'
    return bold_magenta + value + reset_color

# Start game prompt
def init_prompt():
    start = input('Hello ' + player_name + '. Ready to play? [Yes/No] ').lower()
    if start == 'yes' or start == 'y':
        print('\nOKAY! Let\'s play MAD LIBS!')
        print('-----------------------------')

        add_words()

        print('\n' + player_name.upper() + "\'S MAD LIB")
        print('-----------------------------')
        # Mad Lib story template
        story = Template('Dear Diary,\n\nIt\'s me, ' + player_name + '.  I\'ve been here for $num1 days.  Today I woke up with $num2 $bug bites.  At least, it\'s not $animal bites.\n\nIt\'s been $adj.  I love the $adj2 weather here but the $noun leaves much to be desired.  School is $adverb ramping up.\n\nI\'m $adj3. My $noun2 is eager to $verb soon.  I hope $verb2 won\'t be too much of an issue!\n\nLove, \n' + player_name)

        print(story.substitute(input_words))
    elif start == 'no' or start == 'n':
        print('GOODBYE')
    else:
        print('Please enter yes or no')
        init_prompt()

player_name = input('Hello there. What\'s your name? ')

init_prompt()