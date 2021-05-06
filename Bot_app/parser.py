

class Parser:
    def __init__(self):
        self.stop_word = 'stopword.json'

    def read_stop_word(self):
        with open(self.stop_word) as stopword:
            for words in stopword:
                for word in words:
                    word.strip("")
                    print(word)



parse = Parser()
parse.read_stop_word()
