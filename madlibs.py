# MadLibs to go here

# Story Template
# Dear Diary,
# I've been here for [LOW NUMBER] days.  Today I woke up with [LOW NUMBER] [INSECT] bites.  It's been [ADJECTIVE].  I love the [ADJECTIVE] weather here but the [NOUN] leaves much to be desired.  School is [ADVERB] ramping up.  I'm [ADJECTIVE]. My family is eager to visit soon.  I hope [VERB-ING] won't be too much of an issue! 
# Love, [NAME]

def begin_game():
    start = input('Hello ' + player_name + '. Ready to play? ')
    if start == 'yes':
        print('OKAY')
    elif start == 'no':
        print('GOODBYE')
    else:
        print('please enter yes or no')
        begin_game()

player_name = input('Hello there. What\'s your name? ')

begin_game()