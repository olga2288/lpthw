
class ParserError(Exception):
    def describe_error(self, descr):




class Sentence(object):
    def __init__(self, subject, verb, obj):
        # remember we take ('noun','princess') tuples and convert them
        self.subject = subject[1]
        self.verb = verb[1]
        self.object = obj[1]

def peek(word_list):
    if word_list:
        word = word_list[0]
        return word[0]
    else:
        return None

def match(word_list, expecting):
    if word_list:
        word = word_list.pop(0)

        if word[0] == expecting:
            return word
        else:
            return None
    else:
        return None

def skip(word_list, word_type):
    while peek(word_list) == word_type:
        match(word_list, word_type)


class Parser(object):
    def __init__(self, word_list):
        self.word_list = word_list
        skip(self.word_list, 'stop')

    def parse_verb(self):
        if self.next_word == 'verb':
            return match(self.word_list, 'verb')
        else:
            raise ParserError('Expected a verb next.')

    def parse_object(self):
        if self.next_word == 'noun':
            return match(self.word_list, 'noun')
        elif self.next_word == 'direction':
            return match(self.word_list, 'direction')
        else:
            raise ParserError("Expected a noun or direction next.")

    def parse_subject(self, word_list):
        if self.next_word == 'noun':
            return match(word_list, 'noun')
        elif self.next_word == 'verb':
            return ('noun', 'player')
        else:
            raise ParserError("Expected a verb next.")

    def parse(self):
        skip(word_list, 'stop')




def parse_sentence(word_list):
    subj = ParseSubject.parse_subject(word_list)
    verb = ParseVerb.parse_verb(word_list)
    obj = ParseObject.parse_object(word_list)

    return Sentence(subj, verb, obj)
