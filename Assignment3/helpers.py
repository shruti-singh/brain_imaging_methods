import numpy as np


def replace_vowels(word):
    replacement_map = {'a': 'u', 'e': 'i', 'i': 'a', 'o': 'e', 'u': 'o'}
    
    # Record positions of vowels and corresponding vowel
    modifications = {}
    for vw in replacement_map:
        if word.lower().find(vw) > -1:
            modifications[word.lower().find(vw)] = replacement_map[vw]

    for k, v in modifications:
        word[k] = v
    return word.lower()


def random_word_perturbation(word, single_char=False):
    non_word = ""

    if single_char:
        # Randomly change only one char in word
        pos = np.random.randint(0, len(word))
        char = np.random.randint(97, 123)
        word[pos] = char
    else:
        # Randomly change 1/3 characters of the total word length
        size = len(word)//3
        for i in size:
            pos = np.random.randint(0, len(word))
            char = np.random.randint(97, 123)
            word[pos] = char
    return word


def create_en_non_words(word_list):
    "If len of the word is greater than 4 and less than 7, replace vowels with other vowels. Remove vowels. "

    non_words = []

    for w in word_list:
        w = w.lower()
        if len(w) > 4 and len(w) < 7:
            non_words.append(replace_vowels(w))
        elif len(w) <= 4:
            random_word_perturbation(w, single_char=True)
        else:
            random_word_perturbation(w)

    return non_words