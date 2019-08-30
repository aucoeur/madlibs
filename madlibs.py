# MadLibs Spec: https://docs.google.com/document/d/1suR3hzqfGSL9o99rNbDrcU0N1Z47EREubP38IY4Ptuc/edit#heading=h.i5zc39w8ruz2

# Story Template
# Dear Diary,
# I've been here for [LOW NUMBER] days.  Today I woke up with [LOW NUMBER] [INSECT] bites.  At least, it's not a [INSECT] bite.  It's been [ADJECTIVE].  I love the [ADJECTIVE] weather here but the [NOUN] leaves much to be desired.  School is [ADVERB] ramping up.  I'm [ADJECTIVE]. My [NOUN] is eager to [VERB] soon.  I hope [VERB-ING] won't be too much of an issue! 
# Love, [NAME]

num_list = list()

def create(var_list, item):
    var_list.append(item)

def list_all_items():
    index = 0
    for list_item in num_list:
        print("{} {}".format(index, list_item))
        index += 1

def req_prompt():
    required_dict = {
        'req_nouns' : 2,
        'req_adjs' : 3,
        'req_bugs' : 2,
        'req_verbs' : 2,
        'req_adverbs' : 1
    }

    for each in required_dict.values():
        index = int(each) - 1
        # print(each, index)
    
        if len(num_list) < index:
            prompt_user()
            index += 1

def prompt_user():
    prompt_dict = {
    'num_prompt': 'I need a number from 1-7: ',
    'noun_prompt': 'Give me a noun: ',
    'adj_prompt': 'Throw me an adjective: ',
    'adverb_prompt': 'How about an adverb?: ',
    'bug_prompt': 'Name an animal: '
    }

    low_num = input('OKAY. Let\'s go! ' + prompt_dict['num_prompt'])
    create(num_list, low_num)

def init_prompt():
    start = input('Hello ' + player_name + '. Ready to play? ')
    if start == 'yes':
        req_prompt()
        # list_all_items()
    elif start == 'no':
        print('GOODBYE')
    else:
        print('please enter yes or no')
        init_prompt()

player_name = input('Hello there. What\'s your name? ')

init_prompt()