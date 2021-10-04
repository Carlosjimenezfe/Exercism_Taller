def is_pangram(sentence):
    letters = set(filter(str.isalpha, sentence.lower()))
    return len(letters) == 26
