
words = {'verb' : ['go', 'kill','eat', 'eats'],
    'direction' : ['north', 'south', 'east'],
    'stop' : ['the', 'in', 'of'],
    'noun' : ["bear", "princess"]}

def scan(sentence):
    phrase_words = sentence.split()
    result = []
    for phrase_word in phrase_words:
        try:
            number = int(phrase_word)
            result.append(("number", number))
        except:
            phrase_word_type = None
            for word_type in words:
                if phrase_word in words[word_type]:
                    phrase_word_type = word_type
            if phrase_word_type is None:
                phrase_word_type = "error"
            result.append((phrase_word_type, phrase_word))
    return result
