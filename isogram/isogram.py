def is_isogram(phrase):
    phrase=phrase.lower()
    phrase=[c for c in phrase if c.isalpha() ]
    return len(phrase) == len(set(phrase))
