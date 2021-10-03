def count_words(sentence):
    s = sentence.lower()
    
    for punc in '.,;:!@#$%^&*()-_':
        s = s.replace(punc, ' ')
        
    list_words = [w.strip("'") for w in s.split()]
    word_counts = {}
    
    for word in set(list_words):
        word_counts.setdefault(word, list_words.count(word))
    return word_counts