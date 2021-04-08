import numpy as np


def replace_vowels(word):
    replacement_map = {'a': 'u', 'e': 'i', 'i': 'a', 'o': 'e', 'u': 'o'}
    
    # Record positions of vowels and corresponding vowel
    modifications = {}
    for vw in replacement_map:
        if word.lower().find(vw) > -1:
            modifications[word.lower().find(vw)] = replacement_map[vw]

    for k, v in modifications.items():
        word = word[0:k] + v + word[k+1:]

    return word.lower()


def random_word_perturbation(word, single_char=False):

    if single_char:
        # Randomly change only one char in word
        pos = np.random.randint(0, len(word))
        char = np.random.randint(97, 123)
        word = word[0:pos] + chr(char) + word[pos+1:]
    else:
        # Randomly change 1/3 characters of the total word length
        size = len(word)//3
        for i in range(size):
            pos = np.random.randint(1, len(word))
            char = np.random.randint(97, 123)
            word = word[:pos] + chr(char) + word[pos+1:]
    return word


def create_en_non_words(word_list):
    "If len of the word is greater than 4 and less than 7, replace vowels with other vowels. Remove vowels. "

    non_words = []

    for w in word_list:
        w = w.lower()
        if len(w) > 4 and len(w) < 7:
            non_words.append(replace_vowels(w))
        elif len(w) <= 4:
            non_words.append(random_word_perturbation(w, single_char=True))
        else:
            non_words.append(random_word_perturbation(w))

    return non_words


if __name__ == "__main__":
    en_words = ['accept', 'actor', 'addition', 'africa', 'annoy', 'answer', 'arms', 'arrow', 'beard', 'beer', 'believe', 'bicycle', 'book', 'bored', 'broccoli', 'brother', 'builder', 'cancer', 'carpet', 'chalk', 'clay', 'cook', 'cop', 'crab', 'devil', 'atom', 'attic', 'average', 'ax', 'backpack', 'ballet', 'bar', 'base', 'beat', 'beautiful', 'begin', 'beginner', 'belt', 'bitch', 'blame', 'blanket', 'blow', 'blue', 'blush', 'REJECT', 'ACTRESS', 'SUBTRACTION', 'CONTINENT', 'FRUSTRATE', 'EXPLANATION', 'OCTOPUS', 'BOW', 'MUSTACHE', 'MUG', 'DISBELIEVE', 'TRICYCLE', 'MAGAZINE', 'BUSY', 'CAULIFLOWER', 'SISTER', 'CONTRACTOR', 'TUMOR', 'RUG', 'BLACKBOARD', 'POTTERY', 'KITCHEN', 'POLICEMAN', 'LOBSTER', 'VALUABLE', 'DISOWN', 'CAPABILITY', 'PERFORM', 'ACTOR', 'ADVERB', 'SUGGEST', 'CONTRACT', 'AWARENESS', 'DISALLOW', 'QUANTITY', 'ENTERTAIN', 'FURY', 'ANTEATER', 'SEEM', 'REGION', 'DISAGREEMENT', 'CRICKET', 'ASH', 'INQUIRE']
    en_non_words = create_en_non_words(en_words)

    with open("en_non_words.txt", "w") as f:
        for i in en_non_words:
            f.write(i + "\n")