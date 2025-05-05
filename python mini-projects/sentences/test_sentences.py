from sentences import get_determiner, get_noun, get_preposition, get_verb
import pytest

def test_get_determiner():
    # 1. Test the single determiners.

    single_determiners = ["the", "one"]

    # This loop will repeat the statements inside it 4 times.
    # If a loop's counting variable is not used inside the
    # body of the loop, many programmers will use underscore
    # (_) as the variable name for the counting variable.
    for _ in range(4):
        word = get_determiner(1)

        # Verify that the word returned from get_determiner is
        # one of the words in the single_determiners list.
        assert word in single_determiners

    # 2. Test the plural determiners.

    plural_determiners = ["some", "many"]

    # This loop will repeat the statements inside it 4 times.
    for _ in range(4):
        word = get_determiner(2)

        # Verify that the word returned from get_determiner
        # is one of the words in the plural_determiners list.
        assert word in plural_determiners

def test_get_noun():
    single_nouns = ["adult", "bird", "boy", "car", "cat",
        "child", "dog", "girl", "man", "woman"]

    for _ in range(4):
        noun = get_noun(1)
        assert noun in single_nouns

    plural_nouns = ["adults", "birds", "boys", "cars", "cats",
        "children", "dogs", "girls", "men", "women"]

    for _ in range(4):
        noun = get_noun(2)
        assert noun in plural_nouns

def test_get_verb():
    #Past Test
    past = ["drank", "ate", "grew", "laughed", "thought",
        "ran", "slept", "talked", "walked", "wrote"]

    for _ in range(4):
        verb = get_verb(1, "past")
        assert verb in past
    
    for _ in range(4):
        verb = get_verb(2, "past")
        assert verb in past

    #present test for singular
    present_1 = ["drinks", "eats", "grows", "laughs", "thinks",
        "runs", "sleeps", "talks", "walks", "writes"]

    for _ in range(4):
        verb = get_verb(1, "present")
        assert verb in present_1

    #Present test for Pural
    present_2 = ["drink", "eat", "grow", "laugh", "think",
        "run", "sleep", "talk", "walk", "write"]

    for _ in range(4):
        verb = get_verb(2, "present")
        assert verb in present_2
    
    #Future test
    future = ["will drink", "will eat", "will grow", "will laugh",
        "will think", "will run", "will sleep", "will talk",
        "will walk", "will write"]

    for _ in range(4):
        verb = get_verb(1, "future")
        assert verb in future
    
    for _ in range(4):
        verb = get_verb(2, "future")
        assert verb in future

def test_get_preposition():
    prepositions = ["about", "above", "across", "after", "along",
        "around", "at", "before", "behind", "below",
        "beyond", "by", "despite", "except", "for",
        "from", "in", "into", "near", "of",
        "off", "on", "onto", "out", "over",
        "past", "to", "under", "with", "without"]
    for _ in range(4):
        preposition = get_preposition()
        assert preposition in prepositions

def test_get_prepositional_phrase():
    
    prep = get_preposition()
    word = get_determiner(1)
    noun = get_noun(1)
    phrase = str(f'{prep} {word} {noun}.')
    word_list = phrase.split()
    number_of_words = len(word_list)
    assert number_of_words == 3

pytest.main(["-v", "--tb=line", "-rN", __file__])