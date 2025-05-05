import random
from types import prepare_class
#This function determins, if the results will include prepositional phrases
def get_customization():
    prep = input('Do you want to have prepositions? (yes or no): ').lower()
    if prep == 'yes':
        preposition_validation = 0
    elif prep == 'no':
        preposition_validation = 3
    else:
        print('please restart the program. you entered the settings incorrectly')
    return preposition_validation

# This function determins if what the determiter is
def get_determiner(grammatical_number):
    if grammatical_number == 1:
        words = ["the", "one"]
    else:
        words = ["some", "many"]

    # Randomly choose and return a determiner.
    word = random.choice(words)
    return word

#This function selects a noun from a list
def get_noun(grammatical_number):
    if grammatical_number == 1:
        nouns = ["adult", "bird", "boy", "car", "cat",
        "child", "dog", "girl", "man", "woman"]
    else:
        nouns = ["adults", "birds", "boys", "cars", "cats",
        "children", "dogs", "girls", "men", "women"]

    # Randomly choose and return a determiner.
    noun = random.choice(nouns)
    return noun

#This function selects a verb from a list
def get_verb(grammatical_number, tense):
    if tense == "past":
        verbs = ["drank", "ate", "grew", "laughed", "thought",
        "ran", "slept", "talked", "walked", "wrote"]

    elif tense == "present" and grammatical_number == 1:
        verbs = ["drinks", "eats", "grows", "laughs", "thinks",
        "runs", "sleeps", "talks", "walks", "writes"]

    elif tense == "present" and grammatical_number != 1:
        verbs = ["drink", "eat", "grow", "laugh", "think",
        "run", "sleep", "talk", "walk", "write"]
    
    elif tense == "future":
        verbs = ["will drink", "will eat", "will grow", "will laugh",
        "will think", "will run", "will sleep", "will talk",
        "will walk", "will write"]

    # Randomly choose and return a determiner.
    verb = random.choice(verbs)
    return verb

#This function selects a preposition from a list
def get_preposition():
    prepositions = ["about", "above", "across", "after", "along",
        "around", "at", "before", "behind", "below",
        "beyond", "by", "despite", "except", "for",
        "from", "in", "into", "near", "of",
        "off", "on", "onto", "out", "over",
        "past", "to", "under", "with", "without"]
    preposition = random.choice(prepositions)
    return preposition

#This function generates sentences in the past tense
def get_past(preposition_validation):
    if preposition_validation == 0 or preposition_validation == 3:
        grammatical_number = 1
        for _ in range (2):
            tense = "past"
            word = get_determiner(grammatical_number)
            noun = get_noun(grammatical_number)
            verb = get_verb(grammatical_number, tense)
            print(f'{word} {noun} {verb}.')
            grammatical_number += 1

    elif preposition_validation == 1:
        grammatical_number = 1
        for _ in range (2):
            tense = "past"
            word = get_determiner(grammatical_number)
            noun = get_noun(grammatical_number)
            verb = get_verb(grammatical_number, tense)
            phrase = get_prepositional_phrase(grammatical_number)
            sentence = str(f'{word} {noun} {verb} ')
            output = sentence + phrase
            print(output)
            grammatical_number += 1

#This function generates sentences in the present tense
def get_present(preposition_validation):
    if preposition_validation == 0 or preposition_validation == 3:
        grammatical_number = 1    
        for _ in range (2):
            tense = "present"
            word = get_determiner(grammatical_number)
            noun = get_noun(grammatical_number)
            verb = get_verb(grammatical_number, tense)
            print(f'{word} {noun} {verb}.')
            grammatical_number += 1
    elif preposition_validation == 1:
        grammatical_number = 1
        for _ in range (2):
            tense = "present"
            word = get_determiner(grammatical_number)
            noun = get_noun(grammatical_number)
            verb = get_verb(grammatical_number, tense)
            phrase = get_prepositional_phrase(grammatical_number)
            sentence = str(f'{word} {noun} {verb} ')
            output = sentence + phrase
            print(output)
            grammatical_number += 1

#This function generates sentences in the future tense
def get_future(preposition_validation):
    if preposition_validation == 0 or preposition_validation == 3:
        grammatical_number = 1
        for _ in range (2):
            tense = "future"
            word = get_determiner(grammatical_number)
            noun = get_noun(grammatical_number)
            verb = get_verb(grammatical_number, tense)
            print(f'{word} {noun} {verb}.')
            grammatical_number += 1
    elif preposition_validation == 1:
        grammatical_number = 1
        for _ in range (2):
            tense = "future"
            word = get_determiner(grammatical_number)
            noun = get_noun(grammatical_number)
            verb = get_verb(grammatical_number, tense)
            phrase = get_prepositional_phrase(grammatical_number)
            sentence = str(f'{word} {noun} {verb} ')
            output = sentence + phrase
            print(output)
            grammatical_number += 1

#This function generates the prepositional phrase
def get_prepositional_phrase(grammatical_number):
    prep = get_preposition()
    word = get_determiner(grammatical_number)
    noun = get_noun(grammatical_number)
    phrase = str(f'{prep} {word} {noun}.')
    return phrase

#-----------Seperation of functions and main--------------------------

#This calls all the functions
def main(): 
    preposition_validation = int(get_customization())
    if preposition_validation == 3:
        for _ in range (2):
            get_past(preposition_validation)
            get_present(preposition_validation)
            get_future(preposition_validation)

    elif preposition_validation == 0:
        for _ in range (2):
            get_past(preposition_validation)
            get_present(preposition_validation)
            get_future(preposition_validation)
            preposition_validation += 1
main()