
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


def create_en_non_words(word_list):
    "If len of the word is greater than 4 and less than 7, replace vowels with other vowels. Remove vowels. "

    non_words = []

    for w in word_list:
        if len(w) > 4 and len(w) < 7:
            non_words.append(replace_vowels(w))

    return non_words