import string

# List of "unimportant" words (feel free to add more)
keywords = ["go", "take", "drop", "east", "west", "south", "north", "double",
            "down", "up", "talk", "inspect", "give", "usb", "room", "recorder",
            "ink", "lead", "mugs", "camera", "plate", "documents", "login",
            "mainframekey", "vaultkey", "gun", "vaultlog", "vaultpass", "tech",
            "samantha", "bruce", "jenifer", "debra", "bob", "stephen", "alexa",
            "leg", "chest"]


def filter_words(words, keywords):
    """This function takes a list of words and returns a copy of the list from
    which all words provided in the list skip_words have been removed.
    For example:

    >>> filter_words(["talk", "to", "harry"], ["talk"])
    ['talk']

    >>> filter_words(["go", "south"], keywords)
    ['go', 'south']

    >>> filter_words(["hello", "take", "in"], keywords)
    ['take']

    """
    stop = False
    pos = 0
    while not stop:
        try:
            if words[pos] in keywords:
                pos += 1
            else:
                words.pop(pos)
        except:
            stop = True

    return words


def remove_punct(text):
    """This function is used to remove all punctuation
    marks from a string. Spaces do not count as punctuation and should
    not be removed. The funcion takes a string and returns a new string
    which does not contain any puctuation. For example:

    >>> remove_punct("Hello, World!")
    'Hello World'
    >>> remove_punct("-- ...Hey! -- Yes?!...")
    ' Hey  Yes'
    >>> remove_punct(",go!So.?uTh")
    'goSouTh'
    """
    no_punct = ""
    for char in text:
        if not (char in string.punctuation):
            no_punct = no_punct + char

    return no_punct


def normalise_input(user_input):
    """This function removes all punctuation from the string and converts it to
    lower case. It then splits the string into a list of words (also removing
    any extra spaces between words) and further removes all "unimportant"
    words from the list of words using the filter_words() function. The
    resulting list of "important" words is returned. For example:

    >>> normalise_input("  Go   south! ")
    ['go', 'south']
    >>> normalise_input("!!!  tAkE,.    LAmp!?! ")
    ['take', 'lamp']
    >>> normalise_input("HELP!!!!!!!")
    ['help']
    >>> normalise_input("Now, drop the sword please.")
    ['drop', 'sword']
    >>> normalise_input("Kill ~ tHe :-  gObLiN,. wiTH my SWORD!!!")
    ['kill', 'goblin', 'sword']
    >>> normalise_input("I would like to drop my laptop here.")
    ['drop', 'laptop']
    >>> normalise_input("I wish to take this large gem now!")
    ['take', 'gem']
    >>> normalise_input("How about I go through that little passage to the south...")
    ['go', 'passage', 'south']

    """
    # Remove punctuation and convert to lower case
    no_punct = remove_punct(user_input).lower()
    list_no_punct = no_punct.split()

    return filter_words(list_no_punct, keywords)