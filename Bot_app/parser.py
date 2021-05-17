
import re
from Bot_app.stopword import STOPWORDS


class Parser:

    def __init__(self, question):
        self.stop_word = STOPWORDS
        self.question = question
        self.delete_all_symbols()
        self.separate_word()
        self.remove_stop_word()

    def delete_all_symbols(self):
        self.question = re.sub('r/W', " ", self.question)

    def separate_word(self):
        self.question = self.question.split()

    def remove_stop_word(self):
        for words in self.stop_word:
            if words in self.question:
                self.question = self.question.remove(words)
