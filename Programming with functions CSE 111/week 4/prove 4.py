import random

def get_determiner(quantity):
    """Return a randomly chosen determiner. A determiner is
    a word like "the", "a", "one", "some", "many".
    If quantity is 1, this function will return either "a",
    "one", or "the". Otherwise this function will return
    either "some", "many", or "the".

    Parameter
        quantity: an integer.
            If quantity is 1, this function will return a
            determiner for a single noun. Otherwise this
            function will return a determiner for a plural
            noun.
    Return: a randomly chosen determiner.
    """
    if quantity == 1:
        words = ["a", "one", "the"]
    else:
        words = ["some", "many", "the"]

    # Randomly choose and return a determiner.
    word_d = random.choice(words)
    return word_d

def get_noun(quantity):
    """Return a randomly chosen noun.
    If quantity is 1, this function will
    return one of these ten single nouns:
        "bird", "boy", "car", "cat", "child",
        "dog", "girl", "man", "rabbit", "woman"
    Otherwise, this function will return one of
    these ten plural nouns:
        "birds", "boys", "cars", "cats", "children",
        "dogs", "girls", "men", "rabbits", "women"

    Parameter
        quantity: an integer that determines if
            the returned noun is single or plural.
    Return: a randomly chosen noun.
    """
    if quantity == 1:
        words = ["bird", "boy", "car", "cat", "child",
        "dog", "girl", "man", "rabbit", "woman"]
    else:
        words = ["birds", "boys", "cars", "cats", "children",
        "dogs", "girls", "men", "rabbits", "women"]
    
    word_n = random.choice(words)
    return word_n

def get_verb(quantity, tense):
    """Return a randomly chosen verb. If tense is "past",
    this function will return one of these ten verbs:
        "drank", "ate", "grew", "laughed", "thought",
        "ran", "slept", "talked", "walked", "wrote"
    If tense is "present" and quantity is 1, this
    function will return one of these ten verbs:
        "drinks", "eats", "grows", "laughs", "thinks",
        "runs", "sleeps", "talks", "walks", "writes"
    If tense is "present" and quantity is NOT 1,
    this function will return one of these ten verbs:
        "drink", "eat", "grow", "laugh", "think",
        "run", "sleep", "talk", "walk", "write"
    If tense is "future", this function will return one of
    these ten verbs:
        "will drink", "will eat", "will grow", "will laugh",
        "will think", "will run", "will sleep", "will talk",
        "will walk", "will write"

    Parameters
        quantity: an integer that determines if the
            returned verb is single or plural.
        tense: a string that determines the verb conjugation,
            either "past", "present" or "future".
    Return: a randomly chosen verb.
    """



    if tense == "past":
        words = ["drank", "ate", "grew", "laughed", "thought",
        "ran", "slept", "talked", "walked", "wrote"]
    elif tense == "present":
        if quantity == 1:
            words = ["drinks", "eats", "grows", "laughs", "thinks",
        "runs", "sleeps", "talks", "walks", "writes"]
        else:
            words = ["drink", "eat", "grow", "laugh", "think",
        "run", "sleep", "talk", "walk", "write"]
    else:
        words = ["will drink", "will eat", "will grow", "will laugh",
        "will think", "will run", "will sleep", "will talk",
        "will walk", "will write"]
    
    word_v = random.choice(words)
    return word_v

def make_sentence(quantity, tense):
    """Build and return a sentence with three words:
    a determiner, a noun, and a verb. The grammatical
    quantity of the determiner and noun will match the
    number in the quantity parameter. The grammatical
    quantity and tense of the verb will match the number
    and tense in the quantity and tense parameters.
    """
    sentence = f" {get_determiner(quantity).capitalize()} {get_adjective()} {get_noun(quantity)} {get_prepositional_phrase(quantity)} {get_adverb()} {get_verb (quantity, tense)} {get_prepositional_phrase(quantity)}"
    return sentence

def get_preposition():
    """Return a randomly chosen preposition
    from this list of prepositions:
        "about", "above", "across", "after", "along",
        "around", "at", "before", "behind", "below",
        "beyond", "by", "despite", "except", "for",
        "from", "in", "into", "near", "of",
        "off", "on", "onto", "out", "over",
        "past", "to", "under", "with", "without"

    Return: a randomly chosen preposition.
    """
    words = ["about", "above", "across", "after", "along",
        "around", "at", "before", "behind", "below",
        "beyond", "by", "despite", "except", "for",
        "from", "in", "into", "near", "of",
        "off", "on", "onto", "out", "over",
        "past", "to", "under", "with", "without"]
    word_p = random.choice(words)
    return word_p


def get_prepositional_phrase(quantity):
    """Build and return a prepositional phrase composed
    of three words: a preposition, a determiner, and a
    noun by calling the get_preposition, get_determiner,
    and get_noun functions.

    Parameter
        quantity: an integer that determines if the
            determiner and noun in the prepositional
            phrase returned from this function should
            be single or pluaral.
    Return: a prepositional phrase.
    """
    if quantity == 1:
        determiner = get_determiner(1)
        noun = get_noun(1)
        preposition = get_preposition()
        adjective = get_adjective()
        phrase = (f"{preposition} {determiner} {adjective} {noun}")
        return phrase
    else:
        determiner = get_determiner(2)
        noun = get_noun(2)
        preposition = get_preposition()
        adjective = get_adjective()
        phrase = (f"{preposition} {determiner} {adjective} {noun}")
        return phrase

def get_adjective():
    """Return a randomly chosen adjective
    from this list of adjectives:
        "Beautiful", "Intelligent", "Courageous", "Creative", "Generous",
        "Compassionate", "Energetic", "Patient", "Joyful", "Loyal", "Reliable",
        "Humble", "Passionate", "Wise", "Resilient", "Honest", "Adventurous",
        "Gracious", "Determined", "Empathetic"

    Return: a randomly chosen adjective.
    """
    words = ["beautiful", "intelligent", "courageous", "creative", "generous",
        "compassionate", "energetic", "patient", "joyful", "loyal", "reliable",
        "humble", "passionate", "wise", "resilient", "honest", "adventurous",
        "gracious", "determined", "empathetic"]
    word_adj = random.choice(words)
    return word_adj

def get_adverb():
    """Return a randomly chosen adverb
    from this list of adverbs:
        "beautifully", "intelligently", "courageously", "creatively",
        "generously", "compassionately", "energetically", "patiently", "joyfully",
        "loyally", "reliably", "humbly", "passionately", "wisely","resiliently",
        "honestly", "adventurously", "graciously", "determinedly", "empathetically"

    Return: a randomly chosen adverb.
    """
    words = ["beautifully", "intelligently", "courageously", "creatively",
            "generously", "compassionately", "energetically", "patiently", "joyfully",
            "loyally", "reliably", "humbly", "passionately", "wisely","resiliently",
            "honestly", "adventurously", "graciously", "determinedly", "empathetically"]
    word_adv = random.choice(words)
    return word_adv




def main():
    sentence_a = make_sentence (1, "past")
    sentence_b = make_sentence (1, "present")
    sentence_c = make_sentence (1, "future")
    sentence_d = make_sentence (2, "past")
    sentence_e = make_sentence (2, "present")
    sentence_f = make_sentence (2, "future")

    print(f'sentence a: {sentence_a}.')
    print(f'sentence b: {sentence_b}.')
    print(f'sentence c: {sentence_c}.')
    print(f'sentence d: {sentence_d}.')
    print(f'sentence e: {sentence_e}.')
    print(f'sentence f: {sentence_f}.')


main()
